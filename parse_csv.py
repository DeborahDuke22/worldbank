import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('world_bank_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS country')
conn.execute('DROP TABLE IF EXISTS deployments')
conn.execute('DROP TABLE IF EXISTS indicators')
conn.execute('DROP TABLE IF EXISTS years')
print("tables dropped successfully");

# create tables again
conn.execute('CREATE TABLE country (count_id INTEGER PRIMARY KEY AUTOINCREMENT, Country_name TEXT, Series_name TEXT)')
conn.execute('CREATE TABLE deployments (country_name_id INTEGER, Series_code TEXT, Yr2013 REAL, Yr2016 REAL, Yr2019 REAL, FOREIGN KEY(country_name_id) REFERENCES country(count_id))')
print("tables created successfully");
conn.execute('CREATE TABLE indicators (count_ID INTEGER PRIMARY KEY AUTOINCREMENT, country_name TEXT, series_name TEXT)')
conn.execute('CREATE TABLE years (count_name_id INTEGER, series_code TEXT, yr2013 REAL, yr2016 REAL, yr2019 REAL, FOREIGN KEY(count_name_id) REFERENCES indicators(count_ID))')

# open the file to read it into the database
with open('Data_Extract_From_World_Development_Indicators/a05b3cef-b5cb-4ea4-879b-b418bb9d2faa_Data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)#skip the header line
    for row in reader:
        print(row)
        
        count_id = int(row[0])
        Country_name = row[1]
        Series_name = row[3]
        Series_code = row[4]
        Yr2013 = float(row[5])
        Yr2016 = float(row[6])
        Yr2019 = float(row[7])
        cur.execute('INSERT INTO country VALUES (?,?,?)', (count_id, Country_name, Series_name))
        cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?)', (count_id, Series_code, Yr2013, Yr2016, Yr2019))
        conn.commit()      
print("data parsed successfully");

# open the file to read it into the database
with open('Data_Extract_From_World_Development_Indicators/20b642f1-19a3-4262-a734-d19c67074bd1_Data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)#skip the header line
    for row in reader:
        print(row)
        
        count_ID = int(row[0])
        country_name = row[1]
        series_name = row[3]
        series_code = row[4]
        yr2013 = float(row[5])
        yr2016 = float(row[6])
        yr2019 = float(row[7])
        cur.execute('INSERT INTO indicators VALUES (?,?,?)', (count_ID, country_name, series_name))
        cur.execute('INSERT INTO years VALUES (?,?,?,?,?)', (count_ID, series_code, yr2013, yr2016, yr2019))
        conn.commit()      
print("data parsed successfully");



conn.close()


