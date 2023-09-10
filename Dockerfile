# Deriving the python image
FROM python:3.8

# Create a working directory in Docker, makes life easier when running instructions
WORKDIR /app

# Copies all the source code into our directory to the Docker image
COPY . /app

# installs all the libraries we will need to execute the code
RUN pip3 install psycopg2-binary pandas boto3

# tell Docker the command to run inside the container
CMD ["python", "./main.py"]
