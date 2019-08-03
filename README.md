# udacity-logs-analysis-project

## Overview

this is a python application to automatically generate a report from a news database.

The news database is a PostgreSQL database used for a fictional news website, created for the purpose of this project.

Running the python script wil generate an automated report including:
* Top 3 most viewd articles.
* Most popular authors of all time and total views.
* Days which had over 1% request errors

## Setup and instructions

1. Download the database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. unzip the file into the vagrant directory, which is shrard with your virtual machine
3. enter the faollowing command:
    psql -d news -f newsdata.sql
4. finally, from the directory run the program with 
    python log_analysis.py

## Outcome

you should get somthing similar to what is seen on result example.txt