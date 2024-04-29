from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random

def PrettyPrint(all_text):
    for t in all_text.split('\n'):
        if 'Песни из этого же альбома или этого автора:' in t:
            break
        print(t)
options = webdriver.EdgeOptions()

options.add_argument("--headless=new")
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#chrome_driver_path  = r'C:\Python311\Scripts\chromedriver.exe'
#service = Service(chrome_driver_path)
driver = webdriver.Edge(options=options)
driver.get("https://www.gr-oborona.ru/texts/")
elements = driver.find_elements(by='xpath', value=r'//*[@id="abc_list"]/li[2]/a')
songLinks = []
for elem in elements:
    songLinks.append(elem.get_attribute('href'))

r_song = random.choice(songLinks)
driver.get(r_song)
elements = driver.find_elements(by='xpath',value=r'//*[@id="cont"]')
songname = driver.find_element(by='xpath', value=r'//*[@id="headers"]/h3')
print(songname.text)
print()
for elem in elements:
    PrettyPrint(elem.text)

driver.quit()
