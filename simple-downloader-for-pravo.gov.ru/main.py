import os
from email.message import Message

import requests 

def create_calendar(from_date: list|tuple, to_date: list|tuple):
    calendar = dict()
    for year in range(from_date[2], to_date[2]+1):
        calendar[str(year)] = dict()
        for month in range(1, 13):
            match month:
                case 1: # January
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 2: # February
                    if (year % 4 == 0 or year % 400 == 0) and not (year % 100 == 0):
                        calendar[str(year)][str(month)] = []
                        for day in range(1, 30):
                            if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                                   calendar[str(year)][str(month)].append(day)
                                   calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                                   return calendar
                            else:
                                calendar[str(year)][str(month)].append(day)
                        calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                    else:
                        calendar[str(year)][str(month)] = []
                        for day in range(1, 29):
                            if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                                   calendar[str(year)][str(month)].append(day)
                                   calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                                   return calendar
                            else:
                                calendar[str(year)][str(month)].append(day)
                        calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 3: # March
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 4: # April
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 31):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 5: # May
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 6: # June
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 31):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 7: # July
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 8: # August
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 9: # September
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 31):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 10: # October
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 11: # November
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 31):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                case 12: # December
                    calendar[str(year)][str(month)] = []
                    for day in range(1, 32):
                        if day == to_date[0] and month == to_date[1] and year == to_date[2]:
                               calendar[str(year)][str(month)].append(day)
                               calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])
                               return calendar
                        else:
                            calendar[str(year)][str(month)].append(day)
                    calendar[str(year)][str(month)] = tuple(calendar[str(year)][str(month)])

def get_file_name_from_content_disposition(server_response: requests.Response):
    message = Message()
    message['content-disposition'] = server_response.headers['Content-Disposition']
    return message.get_filename()

def get_file_format_by_mime(server_response: requests.Response):
    return server_response.headers['content-type'][server_response.headers['content-type'].find('/')+1:]

def download_file_by_uri(uri: str, save_path: str = './'):
    response = requests.get(uri)
    print(f'\nURI: {uri}')
    print(f'Response code: {response.status_code} ({response.reason})')
    assert response.status_code == requests.codes.ok
    file_name = get_file_name_from_content_disposition(response)
    file_size = float(response.headers['Content-Length']) / 10**3
    print(f'File to download: {file_name}\nFile size: {file_size} KB\nDownloading...')
    with open(save_path+file_name, 'wb') as file:
        file.write(response.content)
    print('The file has been downloaded\n')

def download_documents_for_period(from_date: list|tuple, to_date: list|tuple, save_path: str = './'):
    print(f'\nDocuments will be downloaded for a period from {from_date[0]}-{from_date[1]}-{from_date[2]} to {to_date[0]}-{to_date[1]}-{to_date[2]}.')
    print(f'Path to save documents is {save_path}.')
    period = create_calendar(from_date, to_date)
    downloaded_files = 0
    for year in period:
        for month in period[year]:
            for day in period[year][month]:
                for num in range(1, 10_000):
                    zeros = '0' * (4-len(str(num)))
                
                    if len(str(day)) == 1 and not len(str(month)) == 1:
                        uri = f'http://publication.pravo.gov.ru/file/pdf?eoNumber=0001{year}{month}0{day}{zeros}{num}'
                    elif len(str(month)) == 1 and not len(str(day)) == 1:
                        uri = f'http://publication.pravo.gov.ru/file/pdf?eoNumber=0001{year}0{month}{day}{zeros}{num}'
                    elif len(str(day)) == 1 and len(str(month)) == 1:
                        uri = f'http://publication.pravo.gov.ru/file/pdf?eoNumber=0001{year}0{month}0{day}{zeros}{num}'
                    else:
                        uri = f'http://publication.pravo.gov.ru/file/pdf?eoNumber=0001{year}{month}{day}{zeros}{num}'

                    try:
                        download_file_by_uri(uri, save_path)
                        downloaded_files += 1
                    except AssertionError:
                        break
    print(f'\nNumber of downloaded files is {downloaded_files}')
