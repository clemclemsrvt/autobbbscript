from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
import time

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


if connect() == True:
    print("connection [OK]")
    strURL = "https://bbb.ensicaen.fr/b/por-y3e-4tq" # Replace with the url of the bbb room
    username = "Clément" # Your name
    print(f"opening url {strURL} with safari and using {username} as username")
    driver = webdriver.Safari() # Can use Chrome or Mozilla : search on google for selenium + your browser
    driver.get(strURL)
    delay = 999
    try:
        wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "_b_por-y3e-4tq_join_name")))
        print ("Page loaded")
        driver.find_element_by_id("_b_por-y3e-4tq_join_name").send_keys(username) # Enter username in the form
        time.sleep(2)
        driver.find_element_by_id("_b_por-y3e-4tq_join_name").submit() # Confirm the name / join
        try:
            wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]")))
            print ("Page loaded")
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]").click() # click on audio only 
            try:
                wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "message-input")))
                print ("Page loaded")
                driver.find_element_by_id("message-input").send_keys("Bonjour") # write "bonjour" in the chat form
                time.sleep(2)
                driver.find_element_by_id("message-input").submit() # send the message
            except TimeoutException:
                print ("Timeout")
        except TimeoutException:
            print ("Timeout")
    except TimeoutException:
        print ("Timeout")   
else:
    print("Connection timedout, impossible to reach 8.8.8.8")


   


# driver.find_element_by_id("_b_por-y3e-4tq_join_name").send_keys(username)
# time.sleep(1)
# driver.find_element_by_id("_b_por-y3e-4tq_join_name").submit()
# time.sleep(10)
# driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]").click()
# time.sleep(2)
# driver.find_element_by_id("message-input").send_keys("Bonjour")
# time.sleep(2)
# driver.find_element_by_id("message-input").submit()