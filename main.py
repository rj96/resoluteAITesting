from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import login
import logout
import dashboard
import manageStudent

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://facegenie-ams-school.web.app/"
driver.get(url)
wait = WebDriverWait(driver,10)
login.login_test(driver)
dashboard.dashboard_test(driver, driver.current_url)
manageStudent.manageStudent_test(driver, driver.current_url)
logout.logout_test(driver,url)
input("Press Enter to close the browser...")
driver.quit()