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
    
def print_bar(barName, howBig):
     if not howBig:
            print ('Заведение %s находится на кратчайшем расстоянии от вас' % (barName))
     else:
            print ('В заведении %s имеется %d свободных мест' % (barName, howBig))

def get_biggest_bar(data):
    barName = data[1]['Cells']['Name']
    biggest = data[1]['Cells']['SeatsCount']
    for bar in data:
        if biggest < bar['Cells']['SeatsCount']:
            biggest = bar['Cells']['SeatsCount']
            barName = bar['Cells']['Name']
    print_bar(barName, biggest)


def get_smallest_bar(data):
    barName = data[1]['Cells']['Name']
    smallest = data[1]['Cells']['SeatsCount']
    for bar in data:
        if smallest > bar['Cells']['SeatsCount']:
            smallest = bar['Cells']['SeatsCount']
            barName = bar['Cells']['Name']
    print_bar(barName, smallest)

def length_of_path(coordinates, longitude, latitude):
    length = math.sqrt((int(coordinates[0]) ** 2 - int(longitude) ** 2) + (int(coordinates[1]) ** 2 - int(latitude) ** 2))
    return length
    
def get_closest_bar(data, longitude, latitude):
    bar_name = data[1]['Cells']['Name']
    length = length_of_path(data[0]['Cells']['geoData']['coordinates'], longitude, latitude)
    for bar in data:
         path = length_of_path(bar['Cells']['geoData']['coordinates'], longitude, latitude)
         if path > length:
            length = path
            bar_name = bar['Cells']['Name']
    print_bar(bar_name, None)
            

if __name__ == '__main__':
    data_dir = input('Укажите путь до файла: ')
    get_biggest_bar(load_data(data_dir))
    get_smallest_bar(load_data(data_dir))
    longitude = input('Широта: ')
    latitude = input('Долгота: ')
    get_closest_bar(load_data(data_dir), longitude, latitude)
