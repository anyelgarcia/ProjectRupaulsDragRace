import selenium
from selenium import webdriver
import pandas as pd
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.instagram.com/kimkardashian/?hl=en')

#NUMBER OF POSTS
Posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[1]/a/span').text
#NUMBER OF FOLLOWERS
Followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[2]/a/span').text
#NUMBER FOLLOWING
Following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[3]/a/span').text



#PRINTS OUT THE DATA PULLED FROM ABOVE
print(Posts)
print(Followers)
print(Following)

#CREATES A EMPTY DATAFRAME
data1 = {'Posts':[], 'Followers':[], 'Following':[],}
fulldf = pd.DataFrame(data1)

#APPENDING THE DATA PULLED FROM ABOVE INTO THE EXISTING DATAFRAME
row = [Posts, Followers, Following]
fulldf.loc[len(fulldf)] = row