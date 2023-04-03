# from msilib.schema import tables

# from google.cloud.sql.connector import connector

# from pandas import pd

from google.cloud import bigquery     #pip install google-cloud-bigquery

# 
client = bigquery.client()  #client object created

data_ref = client.dataset("hacker_news", project = "bigquery-public-data")   #create a reference

dataset = client.get_dataset(data_ref)   #getting dataset

tables = list(client.list_tables(dataset))  #list tables

for table in tables:
    print(table.table_id)    #names of the tables

table_ref = data_ref.table("full")   # reference for table full

table = client.get_table(table_ref)  #getting the table

table.schema   #print informatinon in the columns on the table full


'''
    Each SchemaField tells us about a specific information about each column
    the fields provide sthe name, fiel_type, mode, and the description of each
    column

'''


client.list_rows(table, max_results = 5).to_dataframe()    #see the first five lines of the table

#to_dataframe() converts the bigquery produced RowIterator object to pandas framework

#And also checks the databases fi there is any false informatin soemtimes the data may be outdated


client.list_rows(table, selected_fields = table.schema[:1], max_results=5).to_dataframe()

#list_rows allows to fidn the entries in the specific column and can be accessed by list operations





# from google.cloud import bigquery

# client = bigquery.Client()

# # Perform a query.
# QUERY = (
#     'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
#     'WHERE state = "TX" '
#     'LIMIT 100')
# query_job = client.query(QUERY)  # API request
# rows = query_job.result()  # Waits for query to finish

# for row in rows:
#     print(row.name)