import numpy as np
import pandas as pd


def calculate_rfm_and_segment(df):
    """Calculation of recency, frequency , monetary score"""
    if 'recent_purchase_made' in df.columns:
     """Calculate recency : To Check recent purchase made by customer"""
    df["recency"] = round((df['recent_purchase_made'].max() - df['recent_purchase_made']) / np.timedelta64(1, 'D'),0)

    if 'stock_code' in df.columns:
     """Calculate frequency: how often a customer has bought products """
    frequency_data = df.groupby('customer_id')['stock_code'].count().reset_index()
    """Rename stock_code column as frequency"""
    frequency_data.rename(columns={'stock_code': 'frequency'}, inplace=True)
    """Merge left join using customer_id common column"""
    customer_freq_data = df.merge(frequency_data, on='customer_id', how='left')

    if 'avg_order_value' in df.columns:
     """Calculate monetary_value : how much on average customer spends"""
    monetary_data = df.groupby('customer_id')['avg_order_value'].sum().reset_index()
    """ Rename Average_order_value column as monetary_value"""
    monetary_data.rename(columns={'avg_order_value': 'monetary_value'}, inplace=True)
    """ Merge left join customer_freq_data using customer_id common column"""
    df = customer_freq_data.merge(monetary_data, on='customer_id', how='left')

    """ Using pd.qcut function assigning 4 bins calculate rfm score"""
    """ Calculate rec_score"""
    df['rec_score'] = pd.qcut(df['recency'], 4, ['4', '3', '2', '1']).astype(int)
    """ Calculate freq_score"""
    df['freq_score'] = pd.qcut(df['frequency'], 4, ['4', '3', '2', '1']).astype(int)
    """Calculate mone_score"""
    df['mone_score'] = pd.qcut(df['monetary_value'], 4,['4', '3', '2', '1']).astype(int)
    """Add rec_score,freq_score,mone_score to form rfm_score"""
    df['rfm_score'] = df['rec_score'] + df['freq_score'] + df['mone_score']

    """Create Segment _labels as low_value,mid_value & high_value"""
    segment_labels = ['low-value', 'mid-value', 'high-value']
    """Using pd.qcut function assigned 3 bins to create value_segments"""
    df['value_segment'] = pd.qcut(df['rfm_score'], q=3, labels=segment_labels)

    """Create new column rfm_customer_segments"""
    df['rfm_customer_segments'] = ''
    """Assigned rfm_customer_segments by distribution of rfm_score"""
    df.loc[(df['rfm_score'] >= 9) & (df['rfm_score'] < 13), 'rfm_customer_segments'] = 'Champions'
    df.loc[(df['rfm_score'] >= 7) & (df['rfm_score'] < 9), 'rfm_customer_segments'] = 'Loyal'
    df.loc[(df['rfm_score'] >= 5) & (df['rfm_score'] < 7), 'rfm_customer_segments'] = 'Speculative'
    df.loc[(df['rfm_score'] >= 3) & (df['rfm_score'] < 5), 'rfm_customer_segments'] = 'Churned'

    return df