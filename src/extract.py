import psycopg2
import pandas as pd
import numpy as np

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    print("connection to redshift made")

    return connect



def extract_transactional_data(dbname,host,port,user,password):
    """Extracts data from redshift"""
    # Querying the table online_transactions_cleaned from bootcamp data warehouse
    
    connect = connect_to_redshift(dbname, host, port, user, password)

    query = """
    select *
    from bootcamp.online_transactions_cleaned 
    """
    online_trans_cleaned =pd.read_sql(query,connect)
   

    return online_trans_cleaned

def extract_customer_data(dbname,host,port,user,password):

    """
    Extracts data from redshift
    1. Querying the table online_transactions_cleaned from bootcamp data warehouse
    2.  Create variable as transactions_count from distinct invoices
    3.  Create variable as product_count from distinct stock code
    4.  Extract max invoice date as recent purchase made
    5. Average total order value rounded to 2
    6. Extract year from invoice_date as 2011
    7.  Having order value greater than 0 to remove cancellation invoices
    """

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

