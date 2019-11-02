from json import loads
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString,re
from ssl import SSLContext
import requests
from time import time,sleep
import requests
from bs4 import BeautifulSoup
from lxml import html
from urllib.request import urlopen
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui 
from functions import *
from data import *



#span#uitk-type-300 uitk-type-bold all-r-padding-one '''review rating'''
#div#uitk-grid all-grid-align-middle all-grid-align-end '''prices conter'''.a    if found   .get_text()
#span#uitk-cell uitk-type-600 uitk-type-bold all-cell-shrink '''after off price'''



################################''' user inputs '''#################################
print('pleas make sure ')
print('1- created an new google sheet on your google drive .')
print('2- shared the google sheet with service email \' resorts@reliable-plasma-257117.iam.gserviceaccount.com \' .')
print('3- no other google sheet shared before with the same name of current sheet .')
print('4- copy the name of sheet and be ready to enter the sheet name .')
print('5- copy the full url of the search page of travelocity.com from your browser to enter it as input .')
print('6- you will enter the number what you want of resorts to collect the data about .')
print('7- google chrome installed on your machine .')

print('\n\n\n')
search_link ='https://www.travelocity.com/Hotel-Search?adults=2&destination=Northern%20California%2C%20United%20States%20of%20America&endDate=2019-11-30&localDateFormat=M%2Fd%2Fyyyy&regionId=6229628&rfrrid=TG.LP.Hotels.Hotel&sort=RECOMMENDED&star=40&star=50&startDate=2019-11-29&useRewards=true'#input('%50s: '%('search link'))
sheet_name  ='testSheet'#input('%50s: '%('sheet name'))
num_resorts =10#input('%50s: '%('number of resorts to scrape'))
close_driver=False# True if input('%50s (y/n): '%('number of resorts to scrape'))=='y' else False
image       =True# True if input('%50s (y/n): '%('number of resorts to scrape'))=='y' else False

###################################################################################



################################''' inputs preproccessing '''#################################
showmore=round(num_resorts/20)-1

##############################################################################################

################################''' inputs preproccessing '''#################################
driver=webdriver.Chrome('chromedriver')
driver.get(search_link)
sleep(1)
current_position=pyautogui.position()
maxx,maxy=pyautogui.size()
pyautogui.moveTo(x=maxx-10,y=maxy-10)
sleep(0.2)
pyautogui.moveTo(current_position)

while(True):#close the popup 
    sleep(0.2)
    try:
        driver.find_element_by_class_name('uitk-button uitk-button-small uitk-toolbar-button uitk-flex-shrink-0'.replace(' ','.')).click()
        break
sleep(0.5)
while(showmore):#clicks acertain
    ActionChains(driver).move_to_element(driver.find_element_by_class_name('uitk-button uitk-button-small uitk-button-secondary'.replace(' ','.')).perform()
    driver.find_element_by_class_name('uitk-button uitk-button-small uitk-button-secondary'.replace(' ','.')).click()
    showmore=showmore-1
    sleep(0.5)

page=driver.page_source
page=BeautifulSoup(page,'lxml')
resorts=[h.get_text for h in page.findAll('h3',{'class':'pwa-theme--grey-900 truncate all-b-padding-half uitk-type-heading-500','aria-hidden':'true'})]
resorts=resorts[:num_resorts]
ratings=page.findAll('span',{'class':'uitk-type-300 uitk-type-bold all-r-padding-one'},limit=num_resorts)
ratings=ratings[:num_resorts]
ratings=[tag.get_text().strip.replace('/5','') for tag in ratings]
price_without_off=page.findAll('div',{'class':'uitk-grid all-grid-align-middle all-grid-align-end'},limit=num_resorts)
price_without_off=[ tag.findChild('span',{'class':'content-hotel-strikeout-price--a11y'}).get_text().replace('$','') if tag.a else 'not available' for tag in price]
price_with_off   =page.findaAll('span',{'class':'uitk-cell uitk-type-600 uitk-type-bold all-cell-shrink'},limit=num_resorts)
price_with_off   =[tag.get_text().replace('$','') for tag in price_with_off]

#span#uitk-type-300 uitk-type-bold all-r-padding-one '''review rating'''
#div#uitk-grid all-grid-align-middle all-grid-align-end '''prices conter'''.a    if found   .get_text()
#span#uitk-cell uitk-type-600 uitk-type-bold all-cell-shrink '''after off price'''

#### finding the site for each resort




##############################################################################################

creds = ServiceAccountCredentials.from_json_keyfile_name("resorts_creds", scope)
client = gspread.authorize(creds)
sheet = client.open("testSheet").sheet1  # Open the spreadhseet
data =[]
data.append(data_header)
sheet.append_row(insertRow,value_input_option='RAW')  # Insert the list as a row at index 4

numRows = sheet.row_count  #



################################''' functions '''#################################

################################################################################
