import csv
import datetime

import matplotlib
import matplotlib.pyplot as plt

from meteostat_api import FILE

matplotlib.style.use('ggplot')


def create_graphic():
    temp = read_file(FILE)
    interval = 1
    x = []
    y = []

    for i in temp[::interval]:
        x.append(datetime.datetime.strptime(i['Date'], "%Y-%m-%d").date())
        y.append(i['Temp'])

    plt.figure(figsize=(15, 7))
    plt.plot(x, y, label='Day temperature')
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)
    plt.title("Temperature in New Philadelphia")
    plt.legend()
    plt.show()


def read_file(path):
    with open(path, 'r', newline='') as file:
        temp = []
        reader = csv.DictReader(file, delimiter=';')
        for line in reader:
            temp.append({
                'Date': line['Date'],
                'Temp': float(line['Temp'])
            })
    return temp


if __name__ == '__main__':
    create_graphic()
