from selenium import webdriver
from selenium.webdriver.common.by import By
import json

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
    user_name = data['user_name']
    pw = data['pw']

except FileNotFoundError:
    user_name = input('user_name :')
    pw = input('pass:')
    n_data = {"user_name": user_name, "pw": pw}
    j = input('Θέλετε να αποθηκεύσετε σε ένα αρχείο το username και password (y/N) : ')
    list_j = ['Y', 'y', 'υ', 'Υ']
    if j in  list_j:
        with open("data.json", "w") as outfile:
            json.dump(n_data, outfile)


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# specify the path to chromedriver.exe https://chromedriver.chromium.org/ (download and save on your computer)
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get("https://mail.google.com/mail/u/0/?zx=u9eg2rc583jf#inbox")
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(user_name)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[2]').click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pw)
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]').click()
driver.implicitly_wait(20)
driver.stop_client()


