
#python parser for data
import re
non_decimal = re.compile(r'[^\d.]+')

f = open('static/po_water.txt', 'r')
year_labels =[]
cost = []
water = []

for line in f:
    line = line.strip()
    columns = line.split()
    cost.append(non_decimal.sub('',columns[3]))
    year_labels.append(columns[0])
    
    water_value = non_decimal.sub('',columns[1])
    water.append(water_value)


