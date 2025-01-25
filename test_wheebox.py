from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://uat.wheebox.com/LOGIN-2/sales.jsp")
driver.maximize_window()
driver.implicitly_wait(2)

click_register = driver.find_element(By.XPATH , "//b[text()='Register']")
click_register.click()

registration_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Registration Form']"))
    )

loginId = driver.find_element(By.ID , "temp_login_id")
loginId.send_keys("yash2@yopmail.com")

confirm_loginId = driver.find_element(By.ID , "login_id")
confirm_loginId.send_keys("yash2@yopmail.com")

Password = driver.find_element(By.ID , "tempPassword")
Password.send_keys("Yash@1234")

confirm_Password = driver.find_element(By.ID , "password")
confirm_Password.send_keys("Yash@1234")

first_name = driver.find_element(By.ID , "first_name")
first_name.send_keys("Yash")

last_name = driver.find_element(By.ID , "last_name")
last_name.send_keys("Raj")

click_dropdown_gender = driver.find_element(By.ID , "sex")
click_dropdown_gender.click()
select = Select(click_dropdown_gender)
select.select_by_value("66f426f62f0944700d67639791981d63")

click_dropdown_year = driver.find_element(By.ID , "years")
click_dropdown_year.click()
select = Select(click_dropdown_year)
select.select_by_value("fc2395e1c126994839101d1d1d1b633c")

click_dropdown_month = driver.find_element(By.ID , "months")
click_dropdown_month.click()
select = Select(click_dropdown_month)
select.select_by_value("d62155c7a3080a0ced7fffabdad33184")

click_dropdown_day = driver.find_element(By.ID , "days")
click_dropdown_year.click()
select = Select(click_dropdown_day)
select.select_by_value("f17d6f8aff92a5331abc0c345001a054")


input_email = driver.find_element(By.ID , "email_id")
input_email.send_keys("yash2@yopmail.com")



state_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "centerState"))
    )


driver.execute_script("window.scrollTo(0, 600);")
sleep(3)
click_dropdown_state = driver.find_element(By.ID , "centerState")
click_dropdown_state.click()
select = Select(click_dropdown_state)
select.select_by_value("11565372da70d70b659665a446bf7b7c")

click_dropdown_district = driver.find_element(By.ID , "centreDistrict")
click_dropdown_district.click()
select = Select(click_dropdown_district)
select.select_by_value("e37c37263600581a3816e1b47a34baf9")

click_dropdown_city = driver.find_element(By.ID , "test_city")
click_dropdown_city.click()
select = Select(click_dropdown_city)
select.select_by_value("916b8f62bd917054644cd6dc0047b707")

click_start_date = driver.find_element(By.ID , "testValidityStart")
click_start_date.click()

driver.execute_script("window.scrollTo(0, 900);")
click_validity_month = driver.find_element(By.XPATH , "(//div[@class='xdsoft_label xdsoft_month'])[1]")
click_validity_month.click()

opt = driver.find_element(By.XPATH, "(//div[text()='December'])[1]")
driver.execute_script("arguments[0].scrollIntoView(true);", opt)
opt.click()


click_validity_year = driver.find_element(By.XPATH , "(//div[@class='xdsoft_label xdsoft_year'])[1]")
click_validity_year.click()
opt1 = driver.find_element(By.XPATH, "(//div[text()='2026'])[1]")
opt1.click()

click_validity_Date = driver.find_element(By.XPATH , "(//td[@data-date='19'])[1]")
click_validity_Date.click()

#click_validity_time = driver.find_element(By.XPATH , "(//div[@class='xdsoft_time_variant'])[1]")
#click_validity_time.click()
#opt3 = driver.find_element(By.XPATH, "")




click_end_date = driver.find_element(By.ID , "testValidity")
click_end_date.click()


click_validity_month2 = driver.find_element(By.XPATH , "(//div[@class='xdsoft_label xdsoft_month'])[2]")
click_validity_month2.click()

opt = driver.find_element(By.XPATH, "(//div[text()='January'])[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", opt)
opt.click()

click_validity_year2 = driver.find_element(By.XPATH , "(//div[@class='xdsoft_label xdsoft_year'])[2]")
click_validity_year2.click()
opt1 = driver.find_element(By.XPATH, "(//div[text()='2027'])[2]")
opt1.click()

click_validity_Date2 = driver.find_element(By.XPATH , "(//td[@data-date='19'])[2]")
click_validity_Date2.click()

click_select_text = driver.find_element(By.XPATH , "(//button[@type='button'])[1]")
click_select_text.click()


click_select_text_option = driver.find_element(By.XPATH , "(//span[normalize-space()='11 MAY 9 ATTEMP'])[1]")

click_select_text_option.click()

click_checkbox_option = driver.find_element(By.XPATH , "(//input[@type='checkbox'])[1]")
click_checkbox_option.click()

click_submit = driver.find_element(By.XPATH , "(//button[@type='submit'])[1]")
click_submit.click()

click_to_login = driver.find_element(By.XPATH , "//a[text()='Click To Login']")
click_to_login.click()

driver.get("https://uat.wheebox.com/LOGIN-2/sales.jsp")

Email = driver.find_element(By.ID , "login")
Email.send_keys("yash1@yopmail.com")

Password1 = driver.find_element(By.ID , "password")
Password1.send_keys("Yash@1234")

lognbtn = driver.find_element(By.ID , "submitButton")
lognbtn.click()

driver.quit()