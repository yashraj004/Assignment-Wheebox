from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# login with correct creds
usernameInput = driver.find_element(By.ID , "username")
usernameInput.send_keys("student")
passwordInput = driver.find_element(By.ID , "password")
passwordInput.send_keys("Password123")
submitbtn = driver.find_element(By.ID, "submit")
submitbtn.click()

url = "https://practicetestautomation.com/logged-in-successfully/"
redirected_url = driver.current_url
if url == redirected_url:
   print("redirected url is correct")
else:
   print("redirected url is not correct")

successfullText = driver.find_element(By.XPATH , "//strong").text
assert successfullText == "Congratulations student. You successfully logged in!"
logout_button = driver.find_element(By.XPATH, "//a[text()='Log out']")
if logout_button.is_displayed():
   print("logout button is displayed")
else:
   print("logout button is not displayed")

logout_button.click()



# login with incorrect username
usernameInput = driver.find_element(By.ID , "username")
usernameInput.send_keys("student123")
passwordInput = driver.find_element(By.ID , "password")
passwordInput.send_keys("Password123")
submitbtn = driver.find_element(By.ID, "submit")
submitbtn.click()
error_msg = driver.find_element(By.XPATH , "//div[text()='Your username is invalid!']").text
assert error_msg == "Your username is invalid!"

sleep(3)

#login with incorrect password

usernameInput = driver.find_element(By.ID , "username")
usernameInput.send_keys("student")
passwordInput = driver.find_element(By.ID , "password")
passwordInput.send_keys("Password")
submitbtn = driver.find_element(By.ID, "submit")
submitbtn.click()
error_msg = driver.find_element(By.XPATH , "//div[text()='Your password is invalid!']").text
assert error_msg == "Your password is invalid!"


sleep(3)



driver.quit()


