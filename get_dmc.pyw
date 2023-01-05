from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests
import urllib.parse
import sys
import datetime

from chromedriver_autoinstaller.utils import get_chromedriver_path
from chromedriver_autoinstaller.utils import get_chrome_version
from chromedriver_autoinstaller import install

# install chromedriver if it is outdated.
install()

def send_line(msg, pic):
    LINE_ACCESS_TOKEN="chlq8dq9PMYatKECbIy2jM07xI58ttFVLZDhUokM4uI"
    url = "https://notify-api.line.me/api/notify"
    file = {'imageFile':open(pic,'rb')}
    data = ({
            'message':msg
        })
    LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    r=session.post(url, headers=LINE_HEADERS, files=file, data=data)


path = '{}/{}/chromedriver.exe'.format(get_chromedriver_path(), get_chrome_version()[:3])
print(path)
print('test',get_chromedriver_path)
service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get('https://portal.bopp-obec.info/obec65/auth/login')


# open file for authen
with open('auth.txt', 'r') as file:
    username = file.readline().strip()
    password = file.readline().strip()


username_inpurt = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[1]/div/input').send_keys(username)
password_input = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[2]/div/input').send_keys(password)

login_submit = driver.find_element(By.ID,'btnSubmit').click()

dashbaord = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div/ul[2]/li[1]/a/button').click()


# row_dict = {}
# for r in range(10):
#     row = []
#     for i in range(4):
#         data = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/table[1]/tbody/tr[{}+1]/td[{}+1]'.format(r, i)).text
#         row.append(data)

#     row_dict[row[0]] = [row[1], row[2], row[3]]


# print(row_dict)

total = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/table[1]/tbody/tr[24]/td[4]').text

print(total)

now = datetime.datetime.now()
str_now = now.strftime('%d-%m-%Y %H:%M:%S')
msg = 'รายงานข้อมูลนักเรียนจาก dmc ข้อมูล ณ วันที่ ' + str_now + '\nจำนวนนักเรียนทั้งหมด: ' + total


driver.execute_script('window.scrollTo(0, 220)')
driver.save_screenshot('pic.png')

image_path = 'pic.png'

driver.quit()


send_line(msg, image_path)