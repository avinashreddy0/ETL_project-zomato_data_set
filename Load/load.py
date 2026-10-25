import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

try:
 
    df = pd.read_csv(r"C:\Users\indur\OneDrive\Desktop\depolyment projects\zomato_project\zomato_clean_data_set.csv")
    print("✅ CSV file loaded successfully")


    user = 'root'
    password = quote_plus('induri@05')  
    host = 'localhost'
    database = 'zomato_db'

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    df.to_sql('zomato_clean_data_set', con=engine, if_exists='replace', index=False)
    print("✅ Data successfully loaded into MySQL table: zomato_clean_data_set")

except Exception as e:
    print("❌ Error while loading data:", e)

finally:
    print("👍 ETL process completed.")
