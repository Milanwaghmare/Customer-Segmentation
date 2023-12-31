# Customer-Segmentation
## Project Overview
The goal of this project is to segment the customers into distinct groups of individuals that have similar characteristics.To understand purchasing behavior pattern of customer  in terms how recently they have made purchases,how frequently and how much average monetary_value customers are spending to do purchases.

This repository contains  online_transactional_cleaned data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

## Project Structure

#### Part 1 : Query the Cleaned data 
- Import libraries
- Explore online_transaction_cleaned data
- Data extraction 
- Connecting to Redshift
#### Part 2 : Exploratory analysis & Visualization
- Using SQL query
- Bar plot Top 10 countries
- Bar plot Top 10 customers as per average spending value
#### Part 3 : Transforming Data
- RFM analysis
- Derivation of RFM score
- Customer Segmentation using RFM score
- Value segment & Viz
- Describe RFM customer segment
#### Part 4 : Data Visualization
- Bar plot value segments
- Plotly treemap RFM segment analysis
- Heatmap
- Pie chart
- Co-relation matrix
- Plotly go bar chart comparison customer segment with RFM score

This repository contains below python files and jupyter notebook showcasing customer segmentation project.
* src/extract.py :-a python script that contains instructions to connect to Amazon Redshift data warehouse and to extract online transactions cleaned data with transformation tasks performed using SQl
* src/transform.py :- a python script that contains instructions to calculate rfm score and customer segments
* .env file: -a text document that contains list of environment variables used
* main.py - a python script that contains all instructions to execute all the steps to extract and transform data using the functions from extract.py and transform.py
* .gitignore:- a text document that specifies intentionally untracked files that Git should ignore.
* requirements.txt - a text document that contains all the libraries required to execute the code
* Dockerfile - a text document that contains all the instructions a user could call on the command line to assemble an image
* .dockerignore - a text document that contains files or directories to be excluded when docker CLI sends the context to docker daemon.This helps to avoid unnecessarily sending large or sensitive files and directories to the daemon and potentially adding them to images using ADD or copy



# How to Run the customer segmentation project
- A. Running the customer segmentation on the local terminal
- B. Executing customer segmentation via Docker'

# A. Running the customer segmentation on the local terminal :

## Requirement
* Python 3+
* Python IDE or a text editor to edit files


## Steps to follow 

1. Copy the .env.example file to .env and fill out the environment vars.
2. Install all the libraries needed to execute main.py
3. Run the main.py script

## Usage
- .env file adds variable for connecting from DBeaver

```bash
 pip3 install -r requirements.txt
```
```bash
 python main .py
```

# B. To run customer-segmentation using Docker :

## Requirements
- Docker for  Mac :
Installation: Install Docker Desktop on Mac 
- Docker for Windows:
- Installation: install Docker Desktop on Windows using WSL-2


## Instructions
- Ensure Docker is running locally
- Comment out the code from dotenv import load_dotenv and load_dotenv() in the main.py script before executing the following codes
- Copy the .env.example file to .env and fill out the environment vars.
- Make sure you are executing the code from the customer-segmentation folder, and you have Docker Desktop running.

## Dependencies

The following Python libraries are used in this project. You can install them using the provided `requirements.txt` file.

- **psycopg2-binary**: This library is used for connecting to a PostgreSQL database. It provides a PostgreSQL adapter for Python.

- **pandas**: Pandas is a powerful data manipulation and analysis library. It is used extensively for data preprocessing and analysis tasks in this project.



#### Build an Image

* To run it locally first build the image.

```bash
  docker image build -t customer-segmentation-pipeline:0.1 .
```

- Then run the etl job using docker:
```bash
  docker run --env-file .env customer-segmentation:0.1
```


## References

- [RFM Analysis Using Python](https://thecleverprogrammer.com/2023/06/12/rfm-analysis-using-python/) - The Clever Programmer (June 12, 2023)

  This source was consulted for guidance and inspiration in implementing RFM analysis as part of this project. It provides a detailed tutorial on RFM analysis using Python and served as a valuable reference.

## Author
**Milan Waghmare**


