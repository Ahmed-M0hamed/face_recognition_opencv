from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import os 
import uuid

htmldata = urlopen('https://unsplash.com/s/photos/blank-background')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')
urls = [image['src'] for image in images] 

for url in urls[:10] :
    urllib.request.urlretrieve(url ,os.path.join('scrabed_data' , 'images' , f'{str(uuid.uuid1())}.jpg') ) 
    