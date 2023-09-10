import os
import numpy as np
from datetime import datetime

from src.extract import extract_transactional_data
from src.extract import extract_customer_data
from src.transform import calculate_rfm_and_segment

from dotenv import load_dotenv
load_dotenv() #only for local testing

# import variables from .env file
dbname = os.getenv('dbname')
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')


#this creates a variable that tracks the time we executed the script
start_time=datetime.now()


customer_data_df =extract_customer_data(dbname, host, port, user, password)
print(customer_data_df.info())


customer_data_df = calculate_rfm_and_segment(customer_data_df)
print(customer_data_df.head())



#this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")

