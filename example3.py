# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from urllib.parse import quote

options = Options()
#options.add_argument("user-data-dir=/Users/vaibhavchopra/Library/Application Support/Google/Chrome/Default")

message = '''Hi, ik that fats are coming near but the board wants to continue the medium articles and so, yogi didi needs u to write a tech article. plz try to submit it by 31st so that, next week there wont be any pressure on u.'''

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
f.close()
# numbers.reverse()
TRIES = 30

driver = webdriver.Chrome("drivers/chromedriver", options=options)
# driver.get('https://web.whatsapp.com')
# input()
for number in numbers:
	if number == "":
		continue
	print('Number: ' + number)
	try:
		url = 'https://web.whatsapp.com/send?phone=91' + number + '&text=' + message
		driver.get(url)
		sleep(5)
		# click_btn = driver.find_elements(By.CSS_SELECTOR,"footer > div.copyable-area  div:nth-child(3) > button").get(0)
		click_btn = WebDriverWait(driver, TRIES).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'footer > div.copyable-area  div:nth-child(3) > button')))
		click_btn.click()
		sleep(10)
		print('Message sent to: ' + number)
	except Exception:
		print('Failed to send message to ' + number)
driver.quit()