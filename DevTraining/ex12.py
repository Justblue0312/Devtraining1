from selenium import webdriver
from selenium.webdriver.edge.service import Service

DRIVER_PATH = Service(
    r'C:\Users\Admin\Downloads\Programs\New folder\chromedriver.exe')
url = "http://45.79.43.178/source_carts/wordpress/wp-admin/"
username = "admin"
password = "123456aA"


driver = webdriver.Chrome(service=DRIVER_PATH)
driver.maximize_window()
driver.get(url)

username_field = driver.find_element_by_id("user_login")
username_field.send_keys(username)

password_field = driver.find_element_by_id("user_pass")
password_field.send_keys(password)

summit_field = driver.find_element_by_id("wp-submit")
summit_field.submit()

getusername = driver.find_element_by_class_name("display-name").text

print(getusername)
