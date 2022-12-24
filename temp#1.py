# Calista Adler and Brandon Zhao

import pandas as pd
import csv 

# opening and reading data from records.csv file 
data = pd.read_csv(r'/Users/calistaadler/Downloads/DFR/records.csv')

# creating new data frame 
output = pd.DataFrame(columns=['Timestamp','ModA Temp', 'ModB Temp', 'ModC Temp', 'Gate Driver Board Temp'])

# id for temperature #1
temp1_id = '00A0'

# iterates through each row in original records file
for index, row in data.iterrows():
    

    year = row['year']
    month = row['month']
    day = row['day']
    hour = row['hour']
    minute = row['minutes']
    second = row['seconds']

    new_row = [''.join([str(month), '/', str(day), '/', str(year), " ", str(hour), ':', str(minute), ':', str(second)])]

    curr_id = row['id']
    
    # converts each byte from hex to decimal if correct id for temperature #1
    if temp1_id == curr_id:
        byte0 = row['data0']
        byte0 = int(byte0, 16)

        byte1 = row['data1']
        byte1 = int(byte1, 16)
        
        byte2 = row['data2']
        byte2 = int(byte2, 16)
       
        byte3 = row['data3']
        byte3 = int(byte3, 16)

        byte4 = row['data4']
        byte4 = int(byte4, 16)
        
        byte5 = row['data5']
        byte5 = int(byte5, 16)

        byte6 = row['data6']
        byte6 = int(byte6, 16)

        byte7 = row['data7']
        byte7 = int(byte7, 16)
        
        new_row = str(new_row)
        new_row = new_row.replace("'","")
        new_row = new_row.replace("[","")
        new_row = new_row.replace("]","")

        # calculates temperature for each type using 2 bytes
        modA = int(byte0) + 256*int(byte1)
        modB = int(byte2) + 256*int(byte3)
        modC = int(byte4) + 256*int(byte5)
        gate_driver = int(byte6) + 256*int(byte7)

        # appends items to dataframe
        output.loc[len(output.index)] = [new_row, modA/10, modB/10, modC/10, gate_driver/10]

        
# stores final data frame in csv file 
output.to_csv(r'/Users/calistaadler/Downloads/DFR/tempout.csv')


