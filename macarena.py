import pandas as pd
import os
import sqlite3
import json
import csv
import openpyxl
import pyarrow
import fastparquet

database = []

def write_csv():
with open("database", "w") as db:
    for item in database:
        db.write(f"{item}\n")

def read_csv():
with open("database", "r") as db:
    for item in database:
        content = database.read()
        print(content)

def write_sqlite():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS database (item TEXT)''')
    for item in database:
        c.execute("INSERT INTO database (item) VALUES (?)", (item,))
    conn.commit()
    conn.close()

def read_sqlite():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database")
    rows = c.fetchall()
    for row in rows:
        print(row[0])
    conn.close()

def write_excel():
    df = pd.DataFrame(database, columns=["item"])
    df.to_excel("database.xlsx", index=False)
    df.to_csv("database.csv", index=False)
    df.to_json("database.json", orient="records")
    df.to_html("database.html", index=False)
    df.to_parquet("database.parquet", index=False)
    df.to_feather("database.feather", index=False)
    df.to_stata("database.dta", index=False)
    df.to_sas("database.sas7bdat", index=False)
    df.to_msgpack("database.msgpack", index=False)
    df.to_pickle("database.pkl", index=False)
    df.to_hdf("database.h5", key="df", mode="w", index=False)
    df.to_sql("database", "sqlite:///database.db", if_exists="replace", index=False)
    df.to_gbq("database", project_id="your_project_id", if_exists="replace", index=False)
    df.to_orc("database.orc", index=False)
    df.to_xml("database.xml", index=False)
    df.to_parquet("database.parquet", index=False, engine="pyarrow")
#all possible reading and writing methods for pandas dataframe, including csv, excel, json, html, parquet, feather, stata, sas, msgpack, pickle, hdf, sql, gbq, orc, xml    
