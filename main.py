from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from io import BytesIO




''' ask user to input the instagram post url '''
link = input("Enter Instagram Image URL: ")

''' 
create a webdriver chrome object by passing the path of "chromedriver.exe" file.(do not include .exe in the path).
'''
cService = webdriver.ChromeService(executable_path='')
driver = webdriver.Chrome(service = cService)

''' Open the instagram post on your chrome browser'''
driver.get(link)

''' Fetch the source file of the html page using BeautifulSoup'''
soup = BeautifulSoup(driver.page_source, 'lxml')

''' Extract the url of the image from the source code''' 
img = soup.find('img', class_='FFVAD')
images = soup.find_all('img')

# Extract and print the URLs of the images
for img in images:
    img_url = img.get('src')
    if img_url:  # Check if the 'src' attribute exists
        print(img_url)
    else:
        print("Image tag without 'src' attribute found.")


'''Download the image via the url using the requests library'''
r = requests.get(img_url)

with open("instagram"+str(time.time())+".png",'wb') as f: 
    f.write(r.content)

print('success')
