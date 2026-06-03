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


# import pandas

# data = pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # Average
# print(int(data['temp'].mean()))
#
# # Max Number to temp column
# print(data['temp'].max())
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9 / 5 + 32

# print('Fahrenheit Temp: %s °F' % (monday_temp_F))

# Create a dataframe form scratch
# data_dict = {'students': ['Amy', 'James', 'Angela'], 'scores': [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

result = {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': []}
for i in result['Fur Color']:
    result['Count'].append(len(data[data['Primary Fur Color'] == i]))

df = pandas.DataFrame(result)
df.to_csv('squirrel_count.csv')
