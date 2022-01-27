import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time, urllib.request
import requests
import pandas as pd

TIMEOUT = 15

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.instagram.com/')

print("[Info] - Clearing cookies")
time.sleep(0.5)

cookies_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, "//button[contains(text(), 'Aceptar todas')]")))
cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Aceptar todas')]").click()

print("[Info] - Logging in")
time.sleep(2)

user_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "input[name='username']")))
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username.clear()
username.send_keys("lavanetobuenorra")

pass_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "input[name='password']")))
password=driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password.clear()
password.send_keys("naranjin")

login_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "button[type='submit']")))
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(10)
notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Ahora no')]").click()
time.sleep(10)
notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Ahora no')]").click(
)
time.sleep(5)

print("[Info] - Buscando los datos")


reinas =[]
reinas.append("https://www.instagram.com/pythia.queen/")
driver.get(reinas[0])

wait = WebDriverWait(driver, 20)
number_of_follower = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href$='/pythia.queen/followers/'] span"))).get_attribute('title')
print(number_of_follower)


#CREATES A EMPTY DATAFRAME
data1 = {'Posts':[], 'Followers':[], 'Following':[],}
fulldf = pd.DataFrame(data1)

#APPENDING THE DATA PULLED FROM ABOVE INTO THE EXISTING DATAFRAME
row = [Posts, Followers, Following]
fulldf.loc[len(fulldf)] = row

