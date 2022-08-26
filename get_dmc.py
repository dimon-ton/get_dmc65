from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

path = r'C:\Users\saich\Documents\get_dmc\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get('https://portal.bopp-obec.info/obec65/auth/login')

username = '1103100275320'
password = '12345678'

username_inpurt = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[1]/div/input').send_keys(username)
password_input = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[2]/div/input').send_keys(password)

login_submit = driver.find_element(By.ID,'btnSubmit').click()

dashbaord = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div/ul[2]/li[1]/a/button').click()

row = []
row_dict = {}

for i in range(4):
    data = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/table[1]/tbody/tr[1]/td[{}+1]'.format(i)).text
    row.append(data)



row_dict[row[0]] = {'boy':row[1], 'girl':row[2], 'total':row[3]}

print(row_dict)

driver.close()