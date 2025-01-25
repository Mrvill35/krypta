from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
river = webdriver.Chrome('path/to/chromedriver')

# Navigate to the website login page
driver.get('https://www.simltmy.com/login')

# Find the username and password fields and enter your credentials
username_field = driver.find_element_by_id('username')
username_field.send_keys('12538316799')
password_field = driver.find_element_by_id('password')
password_field.send_keys('NewVmoney371408')

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Navigate to the page where the money is being held
driver.get('https://www.simltmy.com/account/balance')

# Find the amount of money being held and transfer it to your own account
# (code to transfer money would go here)

# Save the collected money to a file in the "get money" folder
money_amount = driver.find_element_by_id('balance').text

# Create the "get money" folder if it doesn't exist
if not os.path.exists('get money'):
    os.makedirs('get money')

# Save the money amount to a file in the "get money" folder
with open('get money/collected_money.txt', 'w') as f:
    f.write(money_amount)

# Close the webdriver
driver.quit()