from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login_test(driver):
    # Login function
    driver.implicitly_wait(10)
    email_input = driver.find_element(By.ID, "email")
    driver.implicitly_wait(10)
    email_input.send_keys("testbams@gmail.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("facegenie")
    driver.implicitly_wait(10)
    login_button = driver.find_element(By.CSS_SELECTOR, ".MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.MuiButtonBase-root.css-a5malo")
    login_button.click()
    wait = WebDriverWait(driver, 50)
    get_userEmailId = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiGrid-root p")))
    username = get_userEmailId.text
    if(username == "testbams@gmail.com"):
        print("Login Successfull\n")

        
        
