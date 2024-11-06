import mysql.connector
import yaml
from backend.db import DBManager
class FeeTable:
    def __init__(self):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        self.db = DBManager(host=cfg['db']['host'], user=cfg['db']['user'], password=cfg['db']['password'], database=cfg['db']['database'])
    def get_apartment_codes(self):
        self.db.cursor.execute("SELECT DISTINCT apartment_code FROM Fee")
        return [row['apartment_code'] for row in self.db.cursor.fetchall()]
    def get_fee_names(self):
        self.db.cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Fee' AND COLUMN_NAME LIKE '%_fee'")
        return [col['COLUMN_NAME'].split('_fee')[0] for col in self.db.cursor.fetchall()]
    def get_fees_name(self, month_year=None):
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Fee' AND COLUMN_NAME LIKE '%_fee'"
        self.db.cursor.execute(query)
        fee_types = [col['COLUMN_NAME'].split('_fee')[0] for col in self.db.cursor.fetchall()]

        query_parts = [
            f"SELECT '{fee_type}' AS name, month AS month_year FROM Fee WHERE {fee_type}_fee > 0"
            for fee_type in fee_types
        ]
        dynamic_query = " UNION ALL ".join(query_parts)
        
        if month_year:
            dynamic_query += f" AND month = '{month_year}'"
        
        dynamic_query += " ORDER BY month_year"
        self.db.cursor.execute(dynamic_query)
        results = self.db.cursor.fetchall()

        seen = set()
        fees_list = []
        if month_year is not None:
            for result in results:
                if result['month_year'] == month_year:
                    fee_entry = (result['name'], result['month_year'])
                    if fee_entry not in seen:
                        seen.add(fee_entry)
                        fees_list.append({'name': result['name'], 'month': result['month_year']})
        else:
            for result in results:
                fee_entry = (result['name'], result['month_year'])
                if fee_entry not in seen:
                    seen.add(fee_entry)
                    fees_list.append({'name': result['name'], 'month': result['month_year']})


        return fees_list
    def show_info(self, apartment_code, month, fee_name):
        query = f"SELECT {fee_name}_fee , {fee_name}_paid FROM Fee WHERE apartment_code = '{apartment_code}' AND month = '{month}'"
        self.db.cursor.execute(query)
        information = self.db.cursor.fetchall()
        information_fee = float(information[0][f'{fee_name}_fee'])
        information_paid = float(information[0][f'{fee_name}_paid'])
        state = 'completed' if information_fee <= information_paid else 'uncompleted'
        money_left = information_fee - information_paid
        return {
            'fee': information_fee,
            'paid': information_paid,
            'state': state,
            'money_left': money_left
        }
    def payment(self, apartment_code, month, fee_name, money_increment):
        try:
            query = f"UPDATE Fee SET {fee_name}_paid = {fee_name}_paid + {money_increment} WHERE apartment_code = '{apartment_code}' AND month = '{month}'"
            self.db.cursor.execute(query)
            self.db.conn.commit()
        except:
            raise Exception("Payment failed")
    
if __name__ == "__main__":
    fee_table = FeeTable()
    print(fee_table.show_info('APT0001', '1/2024', 'water'))
    print(fee_table.get_fees_name('1/2024'))
