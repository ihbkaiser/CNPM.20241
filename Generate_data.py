from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

fees = ['water', 'electricity', 'service', 'parking']
apartment_codes = [f'APT{str(i).zfill(4)}' for i in range(1, 21)]

def last_day_of_month(year, month):
    next_month = month % 12 + 1
    next_month_year = year + month // 12
    return (datetime(next_month_year, next_month, 1) - timedelta(days=1)).date()

# Generate SQL queries for the 'fees' table
fees_queries = []
fee_names = []
for _ in range(100):
    fee = random.choice(fees)
    month_year = fake.date_between_dates(date_start=datetime(2023, 1, 1), date_end=datetime(2024, 12, 31)).strftime("%m/%Y")
    fee_name = f"{fee} {month_year}"
    fee_names.append(fee_name)
    month, year = map(int, month_year.split('/'))
    deadline = last_day_of_month(year, month)
    total = random.randint(1000, 10000)
    paid = random.randint(0, total)
    remain = total - paid
    query = f"INSERT INTO fees (fee_name, deadline, total, paid, remain) VALUES ('{fee_name}', '{deadline}', {total}, {paid}, {remain});"
    fees_queries.append(query)

# Generate SQL queries for the 'userfee' table
userfee_queries = []
for _ in range(100):
    apartment_code = random.choice(apartment_codes)
    fee_name = random.choice(fee_names)
    total = random.randint(1000, 10000)
    paid = random.randint(0, total)
    remain = total - paid
    residual = random.randint(0, 1000)
    query = f"INSERT INTO userfee (apartment_code, fee_name, total, paid, remain, residual) VALUES ('{apartment_code}', '{fee_name}', {total}, {paid}, {remain}, {residual});"
    userfee_queries.append(query)

# Print the queries
for query in fees_queries + userfee_queries:
    print(query)