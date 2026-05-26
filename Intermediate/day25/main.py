# with open('./weather_data.csv') as data_file:
#    data = data_file.readlines()
#    print(data)

# import csv
#
# with open('./weather_data.csv') as data_file:
#    data = csv.reader(data_file)
#    temperatures = set()
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.add(int(row[1]))
#    print(temperatures)


import pandas

data = pandas.read_csv('weather_data.csv')

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

# Average
print(int(data['temp'].mean()))

# Max Number to temp column
print(data['temp'].max())

# Get Data in Columns
print(data['condition'])
print(data.condition)

# Get Data in Row
print(data[data.day == 'Monday'])
