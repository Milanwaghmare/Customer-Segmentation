import os
import numpy as np
from datetime import datetime

from src.extract import extract_transactional_data
from src.extract import extract_customer_data
from src.extract import calculate_recency
from src.extract import calculate_customer_frequency
from src.extract import calculate_monetary_value
from dotenv import load_dotenv
load_dotenv() #only for local testing

#import variables from .env file
dbname= os.getenv('dbname')
host=os.getenv('host')
port=os.getenv('port')
user=os.getenv('user')
password=os.getenv('password')


#this creates a variable that tracks the time we executed the script
start_time=datetime.now()


customer_data =extract_customer_data(dbname, host, port, user, password)
print(customer_data.info())

customer_data["recency"] = round((customer_data['recent_purchase_made'].max() - customer_data['recent_purchase_made']) / np.timedelta64(1, 'D'),0)
print("recency:", customer_data["recency"])

# Calculate frequency: how often a customer has bought products
frequency_data = customer_data.groupby('customer_id')['stock_code'].count().reset_index()
# Rename the column 'stock_code' as 'frequency'
frequency_data.rename(columns={'stock_code': 'frequency'}, inplace=True)
customer_freq_data = customer_data.merge(frequency_data, on='customer_id', how='left')


# Calculate Monetary Value: sum of avg_order_value for each customer
monetary_data = customer_data.groupby('customer_id')['avg_order_value'].sum().reset_index()
# Rename the column 'avg_order_value' as 'monetary_value'
monetary_data.rename(columns={'avg_order_value': 'monetary_value'}, inplace=True)
# merge with customer_data using a left join
customer_final_data = customer_data.merge(monetary_data, on='customer_id', how='left')
indexer =customer_final_data.columns.get_loc(monetary_data)
print(customer_final_data.info())



 #this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")

