# Load the cleaned CSV files from data/processed and write each one to a Postgres table.

# pandas reads CSV files into DataFrames; os builds file paths that work on any computer.
import pandas as pd
import os
from sqlalchemy import create_engine

# The processed files this script loads. Each name is also the source for the table name.
file_names=['accounts_clean.csv','invoices_clean.csv','payments_clean.csv','plans_clean.csv','subscriptions_clean.csv']

# __file__ is this script's path (src/data_ingestion.py).
# The first dirname gives the src folder, the second gives the project folder that contains data/.
file_path=((os.path.dirname(os.path.dirname(__file__))))

# Dictionary that will hold table name -> DataFrame.
tables={}

# Read each processed CSV into a DataFrame and store it under its name without ".csv".
for file in file_names:
    # Build the full path, e.g. <project>/data/processed/accounts_clean.csv.
    data_file_path=os.path.join(file_path,'data','processed',file)
    df=pd.read_csv(data_file_path)
    # splitext splits "accounts_clean.csv" into ("accounts_clean", ".csv"); keep the name only.
    name,extension=os.path.splitext(file)
    tables[name]=df



# Connection to the Postgres container: user root, password root, database saas_production_grade, port 5432.
# The host comes from the DB_HOST environment variable. It defaults to localhost when running on your computer.
# Inside Docker Compose, DB_HOST is set to "postgres", the name of the database service.
db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ['POSTGRES_USER']
db_password = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']
engine = create_engine(f'postgresql+psycopg://{db_user}:{db_password}@{db_host}:5432/{db_name}')

# Write each DataFrame to a table of the same name. 'replace' drops and recreates the table on every run.
for single_table in tables.items() :
    # single_table is (table name, DataFrame); index 0 is the name, index 1 is the DataFrame.
    single_table[1].to_sql(name=single_table[0],con=engine,if_exists='replace')
    print(f"table created:{single_table[0]} ")
