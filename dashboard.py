from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def dashboard_test(driver, url):
    print("In Dashboard")
    wait = WebDriverWait(driver, 20)
    driver.implicitly_wait(10)
    while(True):
        try:
            calendar_date_element = driver.find_element(By.XPATH, "//button[contains(text(), '12')]")
            calendar_date_element.click()
            break
        except Exception as e:
            pass
    
    while(True):
        try:
            driver.find_element(By.ID, "demo-simple-select-helper").click()
            element_to_click = driver.find_element(By.XPATH, "//li[@data-value='01']").click()
            break
        except Exception as e:
            pass

    #Get parent element and then search for texts
    parent_element = driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root.css-1mxkoj8")
    text_elements = parent_element.find_elements(By.XPATH, ".//h6 | .//h2/b")
    text_values = [element.text for element in text_elements]
    for text in text_values:
        print("*",text)

    parent_element = driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root.css-609us4")
    text_elements = parent_element.find_elements(By.XPATH, ".//h6 | .//h2/b")
    text_values = [element.text for element in text_elements]
    for text in text_values:
        print("*",text)
    
    driver.implicitly_wait(30)

