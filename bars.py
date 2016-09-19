import json
import os
import sys
import math


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        data = json.load(file_handler)
    return data

def get_biggest_bar(data):
    bar_name = data[1]['Cells']['Name']
    biggest = data[1]['Cells']['SeatsCount']
    for bar in data:
        if biggest < bar['Cells']['SeatsCount']:
            biggest = bar['Cells']['SeatsCount']
            bar_name = bar['Cells']['Name']
    print ('В заведении ' + bar_name + ' имеется ' + str(biggest) + ' свободных мест')


def get_smallest_bar(data):
    bar_name = data[1]['Cells']['Name']
    biggest = data[1]['Cells']['SeatsCount']
    for bar in data:
        if biggest > bar['Cells']['SeatsCount']:
            biggest = bar['Cells']['SeatsCount']
            bar_name = bar['Cells']['Name']
    print ('В заведении ' + bar_name + ' имеется ' + str(biggest) + ' свободных мест')


def get_closest_bar(data, longitude, latitude):
    bar_name = data[1]['Cells']['Name']
    length = math.sqrt((int(data[0]['Cells']['geoData']['coordinates'][0]) ** 2 - int(longitude) ** 2) + (int(data[0]['Cells']['geoData']['coordinates'][1]) ** 2 - int(latitude) ** 2))
    for bar in data:
         path = math.sqrt((int(bar['Cells']['geoData']['coordinates'][0]) ** 2 - int(longitude) ** 2) + (int(bar['Cells']['geoData']['coordinates'][1]) ** 2 - int(latitude) ** 2))
         if path < length:
            length = path
            bar_name = bar['Cells']['Name']
    print ('Заведение ' + bar_name + ' находится на кратчайшем расстоянии от вас')

if __name__ == '__main__':
    get_biggest_bar(load_data("/projects/3_bars/Bars.json"))
    get_smallest_bar(load_data("/projects/3_bars/Bars.json"))
    get_closest_bar(load_data("/projects/3_bars/Bars.json"), sys.argv[1], sys.argv[2])
