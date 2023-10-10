import pandas as pd

def connect_to_local_folder(customer_data_df, data):
    try:
        # Save the DataFrame to a CSV file
        customer_data_df.to_csv(data, index=False)
        print(f"Data saved to {data}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    # Create or load your 'segment_data' DataFrame (replace this with your actual data)

    # Specify the path where you want to save the CSV file
    csv_file_path = "../data/customer_segmentation_data.csv"

    # Call the function to save the DataFrame to the specified path
    connect_to_local_folder(segment_data, csv_file_path)

