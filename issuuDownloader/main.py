import os
import re
import string
import random
import subprocess
from email.message import Message

import requests 
from bs4 import BeautifulSoup as bs

def generate_random_string(string_length: int = 10) -> str: 
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(alphabet) for _ in range(string_length))

# You can use proxies to avoid blocking.
#proxies = {
#    'http': 'socks5|http://host(IP|domain):port',
#    'https': 'socks5|https://host(IP|domain):port'
#}
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
docUri = input('Enter a document URI (URL) like https://issuu.com/europan/docs/doc-on-a-topic: ')
response = requests.get(docUri, proxies=proxies, headers=headers)
print(f'Response: {response.status_code} {response.reason}')
assert response.status_code == requests.codes.ok
soup = bs(response.content, 'lxml')
docUuid = re.search(r'/([-\w\d]+)/', soup.find('meta', attrs={'name': 'twitter:image'})['content']).group(1)
docTitle = soup.find('link', attrs={'rel': 'alternate', 'media': 'application/json+oembed'})['title']
numberOfPages = int(re.search(r'\\"pageCount\\":(\d+),', response.content.decode(encoding='utf-8')).group(1))
tempStorage = f'{os.getcwd()}/{generate_random_string()}'
if not os.path.exists(tempStorage):
    os.makedirs(tempStorage)

print(f'\nDocument title: {docTitle}')
print(f'Pages: {numberOfPages}')
print('Start the task')
for pageNumber in range(1, numberOfPages+1):
    print(f'\nURI: https://svg.issuu.com/{docUuid}/page_{pageNumber}.svg\nNumber of page: {pageNumber}/{numberOfPages}')
    print('Downloading')
    subprocess.run(['chromium',
                    '--headless',
                    '--disable-gpu',
                    '--no-margins',
                    #f'--proxy-server={proxies['https']}',
                    '--no-pdf-header-footer',
                    f'--print-to-pdf={tempStorage}/{pageNumber}.pdf',
                    f'https://svg.issuu.com/{docUuid}/page_{pageNumber}.svg'])
    print('Downloaded')
subprocess.run(['pdfunite']+[f'{tempStorage}/{pageNumber}.pdf' for pageNumber in range(1, numberOfPages+1)]+[f'{os.getcwd()}/{docTitle}.pdf'])

for pageNumber in range(1, numberOfPages+1):
    os.remove(f'{tempStorage}/{pageNumber}.pdf')
os.rmdir(tempStorage)
print('\nThe task is done')
