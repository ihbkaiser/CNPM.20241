import yaml

def generate_sql_file():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)

    db_config = config['db']
    sql_filename = 'setup.sql'

    try:
        # Create SQL file and write queries to it
        with open(sql_filename, 'w') as sql_file:
            # Create the user
            create_user_query = f"""
            CREATE USER IF NOT EXISTS '{db_config['user']}'@'{db_config['host']}'
            IDENTIFIED BY '{db_config['password']}';
            """
            sql_file.write(create_user_query + '\n')

            # Grant privileges
            grant_privileges_query = f"""
            GRANT ALL PRIVILEGES ON {db_config['database']}.* TO '{db_config['user']}'@'{db_config['host']}';
            """
            sql_file.write(grant_privileges_query + '\n')

            # Create the database if it does not exist
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_config['database']};"
            sql_file.write(create_db_query + '\n')

            sql_file.write("FLUSH PRIVILEGES;\n")

        print(f"SQL file '{sql_filename}' generated successfully!")

    except Exception as e:
        print(f"Error: {e}")

generate_sql_file()
