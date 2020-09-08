import requests
import json
from datetime import datetime
import csv


API_URL_BASE = 'https://api.meteostat.net/v1/history/daily'
API_KEY = 'key=QAKRxwZD'
ID_REGION = 'station=KPHD0'  # New Philadelphia / Schoenbrunn Estates (US)
END_DATE = f'end={datetime.today().date().strftime("%Y-%m-%d")}'

FILE = 'meteostat.csv'


def get_api():
    START_DATE = set_period()
    response = requests.get(
        f'{API_URL_BASE}' + '?' + f'{ID_REGION}' + f'&{START_DATE}' + f'&{END_DATE}' + f'&{API_KEY}')
    text = response.text
    dict_text = dict(json.loads(text))
    li = list(dict_text.get("data"))
    result = []
    for i in li:
        temp = i.get('temperature')
        # print(datetime.datetime.strptime(i.get('date'), '%Y-%m-%d').date(), temp)
        date = datetime.strptime(i.get('date'), '%Y-%m-%d').date()
        result.append({"Date": date,
                       "Temp": i.get('temperature')})
        # print(type(temp))
    save_file(result, FILE)


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Date', 'Temp'])
        for item in items:
            date = item['Date']
            temp = item['Temp']
            if temp is None:
                continue
            if __name__ == '__main__':
                print(date, temp)
            writer.writerow([date, temp])


def set_period():
    print("Введите период (в годах), за которое хотите вести наблюдение: ")
    period = int(input())
    START_DATE = f'start={datetime.today().date().replace(year=datetime.today().date().year - period).strftime("%Y-%m-%d")}'
    return START_DATE


if __name__ == '__main__':
    get_api()
