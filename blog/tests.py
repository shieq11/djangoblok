from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element(By.XPATH, '//*[@id="id_username"]' ).send_keys("shieq") # wpisywanie loginu
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("Brzezinki77B") #wpisywanie hasła
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click() # klikniecie
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="user-tools"]/a[1]').click()
    driver.find_element(By.XPATH, '/html/body/nav/div/a/span').click()

#element_is_clickable()

def response_check(w,file):
    height = 768
    driver.set_window_size(w,height)
    driver.save_screenshot(file)

response_check(900, "test900.png")
response_check(1200, "test1200.png")
response_check(1800, "test1800.png")
response_check(600, "test600.png")