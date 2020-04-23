import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary
import time
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#%%

driver = webdriver.Firefox(executable_path=r"C:\fdriver\geckodriver.exe")
driver.get("http://www.frisco.pl")

driver.find_element_by_xpath('/html/body/div[1]/div/div/div[8]/div/div/a[2]').click()

sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/a[1]').click()

sleep(5)

driver.find_element_by_name('username').send_keys('mymail@gmail.com')

sleep(5)

driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('mypass')

sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/form/section/input').click()

sleep(5)

# banner po logowaniu
# driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/a[2]').click()

sleep(5)

del_date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[4]/div/div[2]')
delivery = del_date.text

while '12 cze' in delivery:
    print('Nearest delivery date '+delivery)
    sleep(30)
    driver.refresh()
    sleep(5)
    del_date = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[4]/div/div[2]')
    delivery = del_date.text
else:
    print('Wcześniejszy termin! '+delivery)

#Clicking
    sleep(2)

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[4]').click()

    sleep(2)

    driver.find_element_by_xpath('/html/body/div[1]/div/div/span/div/div/div/div[2]/div[2]/div[2]').click()

    sleep(5)
    #driver.find_element_by_css_selector("div[class='calendar_column-day available']").click()
    #wait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='calendar_column-day available']"))).click()
    try:
        element = driver.find_element_by_css_selector("div[class='calendar_column-day available']")
    except:
        element = driver.find_element_by_css_selector("div[class='calendar_column-day last available']")
# scroll to the element
    sleep(5)
    element.location_once_scrolled_into_view
    element.click()

    driver.execute_script("window.scrollTo(0, 100)")

    sleep(5)
    confirm = wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='button higher cta']")))

    confirm.click()

    
    print('Delivery reserved on '+delivery)

#%%

type(element)

