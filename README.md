# Customer-Segmentation
## Project Overview
The goal of this project is to segment the customers into distinct groups of individuals that have similar characteristics

This repository contains  online_transactional_cleaned data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

## Project Content

### Part 1 : Query the Cleaned data
- Explore online_transaction_cleaned data
- ata extraction
- Connecting to Redshift
### Part 2 : Showcase SQL skills & Data Viz
- Exploratory analysis using SQL query
### Part 3 : RFM analysis
- RFM analysis
- Derviation of RFM score
- Customer Segementation using RFM score
- Value segment & Viz
- Describe RFM customer segment
### Part 4 : RFM value analysis Data Visualization
- Data Visualization using barplot
- Plotly treemap RFM segment analysis
- Heatmap
- Pie chart
- Co-relation matrix
- Plotly go bar chart comparison customer segment with RFM score

# Build with
This repository contains below python files and jupyter notebook showcasing customer segmentation project.
* src/extract.py -a python script that contains instructions to connect to Amazon Redshift data warehouse and to extract online transactions cleaned data with transformation tasks performed using SQl
* .env file-a text document that contains list of enviornment variables used
* .gitignore- a text document that specifies intentionally untracked files that Git should ignore.
* main.py - a python script that contains all instructions to execute all the steps to extract, transform and load the transformed data using the functions from extract.py.

## How to Run the customer segmentation project
A. To run the customer segmentation on local terminal:

## Requirements
* Python 3+
* Python IDE or a text editor to edit files
* 

## Steps to follow 

1. Copy the .env.example file to .env and fill out the environment vars.
2. Install all the libraries needed to execute main.py
3. Run the main.py script

