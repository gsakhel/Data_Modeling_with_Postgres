# Summary
This project creates relational database extacting information from supplied songfiles and log files. The database allows us to quickly view which artists and songs are getting the most plays as well as other useful analytics.

Song and log files are extracted, transformed, and loaded into postgres using the etl.py which uses sql_queries for its SQL statements. 

# Instructions
1. requirements.txt - use to install python packages: `pip install -r requirements.txt`
2. intialize_student.sql - use to create a studentdb database and student user which we will use for connecting to postgres
3. create_tables.py - this will create or recreate an empty sparkifydb database using the parameters from sql_queries.py
4. etl.py - fill in the tables in the sparkifydb using statements from sql_queries.py
5. test.ipnb - use to test that our tables were created as expected
6. analytics.ipnb - to to see relevant data extracted from our database

* etl.ipnb - Used for interactively creating the ETL pipeline
* sql_queries.py - stores our CREATE, INSERT, and SELECT SQL queries
* README.md - basic instructions and useful links.



# QUESTIONS
In etl.ipnb under "Process log_data" #3 there are multiple ways to create the timed_df. Enumerating is fast with zip-dict a close second. Is there a prefered way to do this step?

Why are only certain fields for the tables constrained to NOT NULL? For example, why shouldn't artist_id be NOT NULL in the songs table While user_id is NOT NULL for songplays table.

When using test.py, why am I getting the error: "[WARNING] Type 'double precision' may not be an appropriate data type for column 'start_time' in the 'songplays' table."? My SQL query designates the start_time column as a timestamp.

For "Insert data using the COPY command to bulk insert log files instead of using INSERT on one row at a time", how do I read the log .json files and copy them into a table? Do I need to convert to .csv as mentioned here? https://stackoverflow.com/questions/66930940/how-do-i-copy-import-a-json-file-into-postgres



# Useful Links:

Install Psycopg2
https://www.psycopg.org/docs/install.html

Psycopg2 Usage
https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries

Passing tuples vs lists to psycopg2
https://stackoverflow.com/questions/18345825/typeerror-int-object-does-not-support-indexing

PSQL Cheatsheet
https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546

Implementing Primary Keys
https://www.w3schools.com/sql/sql_primarykey.asp

UPSERT
https://www.geeksforgeeks.org/postgresql-upsert/
https://www.postgresqltutorial.com/postgresql-upsert/

Running local .sql file in postgres
https://kb.objectrocket.com/postgresql/how-to-run-an-sql-file-in-postgres-846

Installing SQL magic for jupyter notebooks 
https://www.geeksforgeeks.org/how-to-install-ipython-sql-package-in-jupyter-notebook/

COPY json to postgres
https://www.postgresql.org/docs/9.1/sql-copy.html
https://stackoverflow.com/questions/66930940/how-do-i-copy-import-a-json-file-into-postgres

Set NA/NaNs to None for Postgres to correctly interpret NULL values
https://stackoverflow.com/questions/46283312/how-to-proceed-with-none-value-in-pandas-fillna

Pandas Iterrows
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html

Datetime References
https://docs.python.org/3/library/datetime.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html
https://www.geeksforgeeks.org/how-to-insert-current_timestamp-into-postgres-via-python/
https://www.programiz.com/python-programming/datetime/timestamp-datetime

Docstrings
https://www.geeksforgeeks.org/python-docstrings/

Eventplot
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html

Geopandas
https://datascientyst.com/plot-latitude-longitude-pandas-dataframe-python/