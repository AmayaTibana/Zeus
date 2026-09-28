import pandas as pd

database = []

with open("database", "a") as juanito:
    for item in database:
        juanito.write(f"{item}\n")