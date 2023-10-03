import numpy as np
import pandas as pd


def calculate_rfm_and_segment(customer_rfm):
    """Calculation of recency, frequency , monetary score"""

    # Calculate recency : To Check recent purchase made by customer
    if 'recent_purchase_made' in customer_rfm.columns:
        customer_rfm["recency"] = round((customer_rfm['recent_purchase_made'].max() - customer_rfm['recent_purchase_made']) / np.timedelta64(1, 'D'),0)

    # Calculate frequency: how often a customer has bought products
    if 'stock_code' in customer_rfm.columns:
        frequency_data = customer_rfm.groupby('customer_id')['stock_code'].count().reset_index()
    # Rename stock_code column as frequency
        frequency_data.rename(columns={'stock_code': 'frequency'}, inplace=True)
    # Merge left join using customer_id common column"""
        customer_freq_data = customer_rfm.merge(frequency_data, on='customer_id', how='left')
    # Calculate monetary_value : how much on average customer spends
    if 'avg_order_value' in customer_rfm.columns:
        monetary_data = customer_rfm.groupby('customer_id')['avg_order_value'].sum().reset_index()
    # Rename Average_order_value column as monetary_value
        monetary_data.rename(columns={'avg_order_value': 'monetary_value'}, inplace=True)
    # Merge left join customer_freq_data using customer_id common column"""
        customer_rfm = customer_freq_data.merge(monetary_data, on='customer_id', how='left')

    """Using pd.qcut function assigning 4 bins calculate rfm score"""

    # Calculate rec_score
    customer_rfm['rec_score'] = pd.qcut(customer_rfm['recency'], 4, ['4', '3', '2', '1']).astype(int)
    # Calculate freq_score"""
    customer_rfm['freq_score'] = pd.qcut(customer_rfm['frequency'], 4, ['4', '3', '2', '1']).astype(int)
    # Calculate mone_score"""
    customer_rfm['mone_score'] = pd.qcut(customer_rfm['monetary_value'], 4,['4', '3', '2', '1']).astype(int)
    # Add rec_score,freq_score,mone_score to form rfm_score"""
    customer_rfm['rfm_score'] = customer_rfm['rec_score'] + customer_rfm['freq_score'] + customer_rfm['mone_score']

    # Create Segment _labels as low_value,mid_value & high_value
    segment_labels = ['low-value', 'mid-value', 'high-value']

    """Using pd.qcut function assigned 3 bins to create value_segments"""

    customer_rfm['value_segment'] = pd.qcut(customer_rfm['rfm_score'], q=3, labels=segment_labels)

    # Create new column rfm_customer_segments
    customer_rfm['rfm_customer_segments'] = ''
    # Assigned rfm_customer_segments by distribution of rfm_score"""
    customer_rfm.loc[(customer_rfm['rfm_score'] >= 9) & (customer_rfm['rfm_score'] < 13), 'rfm_customer_segments'] = 'Champions'
    customer_rfm.loc[(customer_rfm['rfm_score'] >= 7) & (customer_rfm['rfm_score'] < 9), 'rfm_customer_segments'] = 'Loyal'
    customer_rfm.loc[(customer_rfm['rfm_score'] >= 5) & (customer_rfm['rfm_score'] < 7), 'rfm_customer_segments'] = 'Speculative'
    customer_rfm.loc[(customer_rfm['rfm_score'] >= 3) & (customer_rfm['rfm_score'] < 5), 'rfm_customer_segments'] = 'Churned'

    return customer_rfm