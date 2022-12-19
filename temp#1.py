# Calista Adler and Brandon Zhao

import pandas as pd
import csv 

# opening and reading data from records.csv file 
data = pd.read_csv(r'/Users/calistaadler/Downloads/records.csv')

# writing into new csv file 
f = open('/Users/calistaadler/Downloads/tempout.csv', 'w')
writer = csv.writer(f)

# creates column titles 
header = ['Timestamp', 'ModA Temp', 'ModB Temp', 'ModC Temp', 'Gate Driver Board Temp']
writer.writerow(header)

# used to parse through each row 
i = 0
n = 1

# id for temperature #1
temp1_id = '00A0'

# replaces square brackets and single quotes for correct formatting and type conversions
def replace(var):
    var = var.replace("]","")
    var = var.replace("[","")
    var = var.replace("'","")

# iterates through each row in original records file
for index, row in data.iterrows():
    
    year = data['year'][i:n].tolist()
    year = str(year)
    replace(year)
    
    month = data['month'][i:n].tolist()
    month = str(month)
    replace(month)

    day = data['day'][i:n].tolist()
    day = str(day)
    replace(day)
    
    hour = data['hour'][i:n].tolist()
    hour = str(hour)
    replace(hour)
    
    minute = data['minutes'][i:n].tolist()
    minute=str(minute)
    replace(minute)

    second = data['seconds'][i:n].tolist()
    second = str(second)
    replace(second)
    
    new_row = [''.join([month, '/', day, '/', year, " ",hour, ':', minute, ':', second])]
   
    id = data['id'][i:n].tolist()
    id = str(id)
    replace(id)

    # converts each byte from hex to decimal if correct id for temperature #1
    if temp1_id in data['id'][i:n].tolist():
        byte0 = data['data0'][i:n].tolist()
        byte0 = str(byte0)
        replace(byte0)
        byte0 = int(byte0, 16)
        byte0 = str(byte0)

        byte1 = data['data1'][i:n].tolist()
        byte1 = str(byte1)
        replace(byte1)
        byte1 = int(byte1, 16)
        byte1 = str(byte1)

        byte2 = data['data2'][i:n].tolist()
        byte2 = str(byte2)
        replace(byte2)
        byte2 = int(byte2, 16)
        byte2 = str(byte2)

        byte3 = data['data3'][i:n].tolist()
        byte3 = str(byte3)
        replace(byte3)
        byte3 = int(byte3, 16)
        byte3 = str(byte3)

        byte4 = data['data4'][i:n].tolist()
        byte4 = str(byte4)
        replace(byte4)
        byte4 = int(byte4, 16)
        byte4 = str(byte4)
        
        byte5 = data['data5'][i:n].tolist()
        byte5 = str(byte5)
        replace(byte5)
        byte5 = int(byte5, 16)
        byte5 = str(byte5)

        byte6 = data['data6'][i:n].tolist()
        byte6 = str(byte6)
        replace(byte6)
        byte6 = int(byte6, 16)
        byte6 = str(byte6)

        byte7 = data['data7'][i:n].tolist()
        byte7 = str(byte7)
        replace(byte7)
        byte7 = int(byte7, 16)
        byte7 = str(byte7)
        
        new_row = str(new_row)
        replace(new_row)

        # calculates temperature for each type using 2 bytes
        modA = int(byte0) + 256*int(byte1)
        modB = int(byte2) + 256*int(byte3)
        modC = int(byte4) + 256*int(byte5)
        gate_driver = int(byte6) + 256*int(byte7)

        # writes all data into new csv file
        writer.writerow([new_row, modA, modB, modC, gate_driver])
     
    i = i + 1
    n = n + 1
    
output = pd.read_csv(r'/Users/calistaadler/Downloads/tempout.csv')

f.close()

