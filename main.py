import pandas as pd
import matplotlib as pyplot


new_stock = pd.read_csv(r'C:\Users\DELL\Documents\GOOGLE-stock.csv')
new_stock.head(30)
# new_stock.info()
# new_stock.describe()

new_stock.to_csv('GOOGLE-stock1.csv')
print(new_stock)

