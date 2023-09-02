from typing import Iterator

import psycopg2
import pandas as pd

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    print("connection to redshift made")

    return connect



def extract_transactional_data(dbname,host,port,user,password):
    # extracts data from redshift
    # querying the table online_transactions_cleaned from bootcamp data warehouse
    
    connect = connect_to_redshift(dbname, host, port, user, password)

    query = """
    select *
    from bootcamp.online_transactions_cleaned 
    """
    online_trans_cleaned =pd.read_sql(query,connect)
   

    return online_trans_cleaned

def extract_customer_data(dbname,host,port,user,password):

    # extracts data from redshift
    # querying the table online_transactions_cleaned from bootcamp data warehouse
    # create variable as transactions_count from distinct invoices
    # create variable as product_count from distinct stock code
    # extract max invoice date as recent purchase made
    # average  total order value rounded to 2
    # extract year from invoice_date as 2011
    # having order value greater than 0 to remove cancellation invoices

    connect = connect_to_redshift(dbname, host, port, user, password)

    query = """
       select customer_id, 
              country,
              description,
              stock_code,
              count(distinct invoice) as transaction_count,
              count(distinct stock_code) as product_count,
              max(invoice_date) as recent_purchase_made,
              round(avg(total_order_value),2) as avg_order_value
       from bootcamp.online_transactions_cleaned 
       where extract(year from invoice_date) = '2011' 
       group by customer_id,country,description,stock_code
       having avg_order_value > 0
       order by avg_order_value desc;
       """
    online_trans_cleaned = pd.read_sql(query, connect)

    return online_trans_cleaned

def calculate_recency(customer_data):
    customer_data["recency"] = round((customer_data['recent_purchase_made'].max() - customer_data['recent_purchase_made']) / np.timedelta64(1, 'D'),0)
    print("Recency:", customer_data["recency"])


def calculate_customer_frequency(customer_data):
    # Calculate frequency: how often a customer has bought products
    frequency_data = customer_data.groupby('customer_id')['stock_code'].count().reset_index()

    # Rename the column 'stock_code' as 'frequency'
    frequency_data.rename(columns={'stock_code': 'frequency'}, inplace=True)

    # Merge with customer_data using a left join
    customer_freq_data = customer_data.merge(frequency_data, on='customer_id', how='left')

    return customer_freq_data

def calculate_monetary_value(customer_data):
    # Calculate Monetary Value: sum of avg_order_value for each customer
    monetary_data = customer_data.groupby('customer_id')['avg_order_value'].sum().reset_index()

    # Rename the columns
    monetary_data.rename(columns={'avg_order_value': 'monetary_value'}, inplace=True)

    # Merge with customer_data using a left join
    customer_final_data = customer_data.merge(monetary_data, on='customer_id', how='left')

    return customer_final_data


def calculate_scores(customer_final_data):
    # Binning and scoring for recency
    customer_final_data['rec_score'] = pd.qcut(customer_final_data['recency'], 4, ['4', '3', '2', '1'])
    # Binning and scoring for frequency
    customer_final_data['freq_score'] = pd.qcut(customer_final_data['frequency'], 4, ['4', '3', '2', '1'])
    # Binning and scoring for monetary value
    customer_final_data['mone_score'] = pd.qcut(customer_final_data['monetary_value'], 4, ['4', '3', '2', '1'])


# Calculate RFM Score
customer_final_data['rfm_score'] = customer_final_data.rec_score + customer_final_data.freq_score + customer_final_data.mone_score

# Assigned variable name as segment_labels
segment_labels = ['low-value', 'mid-value', 'high-value']
# Using pd.qcut created new column name value_segment
customer_final_data['value_segment'] = pd.qcut(customer_final_data['rfm_score'], q=3, labels=segment_labels)