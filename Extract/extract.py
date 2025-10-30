#extract data
import pandas as pd

try:
    df = pd.read_csv(r"C:\Users\indur\Downloads\zomato_messy_to_messy_20000.csv")
    print(df.to_string)
except Exception:
    print('error whilw loading dataset')

finally:
    print('👍👍 sucessfully we extract data set')