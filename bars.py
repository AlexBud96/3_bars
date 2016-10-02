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
    
def print_bar(bar_name, how_big):
     if how_big is None:
            print ('Заведение %s находится на кратчайшем расстоянии от вас' % (bar_name))
     else:
            print ('В заведении %s имеется %d свободных мест' % (bar_name, how_big))

def get_big_and_small_bars(data):
    bar_name1 = data[1]['Cells']['Name']
    bar_name2 = data[1]['Cells']['Name']
    biggest = data[1]['Cells']['SeatsCount']
    smallest = data[1]['Cells']['SeatsCount']
    for bar in data:
        if biggest < bar['Cells']['SeatsCount']:
            biggest = bar['Cells']['SeatsCount']
            bar_name1 = bar['Cells']['Name']
        if smallest > bar['Cells']['SeatsCount']:
            smallest = bar['Cells']['SeatsCount']
            bar_name2 = bar['Cells']['Name']
    Bars = [bar_name1, biggest, bar_name2, smallest]
    return Bars

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
    Bars = get_big_and_small_bars(load_data(data_dir))
    print_bar(Bars[0], Bars[1])
    print_bar(Bars[2], Bars[3])
    longitude = input('Широта: ')
    latitude = input('Долгота: ')
    get_closest_bar(load_data(data_dir), longitude, latitude)
