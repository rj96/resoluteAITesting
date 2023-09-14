from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def logout_test(driver, url):
    wait = WebDriverWait(driver, 20)
    while(True):
        try:
            driver.find_element(By.CSS_SELECTOR, "[data-testid=\"LogoutIcon\"]").click()
            break
        except Exception as e:
            pass
    ok_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")
    driver.implicitly_wait(20)
    ok_button.click()
    if(driver.current_url == url):
        print("Logout Successful")