import os
import numpy as np
import pandas as pd
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


customer_data_df = customer_data_df.groupby(['customer_id']).agg(value_segment=('value_segment', 'first'),rfm_customer_segments=('rfm_customer_segments', 'first'),rfm_score = ('rfm_score','first')).reset_index()
print(customer_data_df.head())

#Connection to local folder
print("loading data to csv")


#this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")

