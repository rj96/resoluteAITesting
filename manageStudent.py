from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def manageStudent_test(driver, url):
    while(True):
        try:#click on Manage Student from the menu
            driver.find_element(By.CSS_SELECTOR, "[data-testid=\"GroupIcon\"]").click()
            break
        except Exception as e:
            pass
    print("In ManageStudent Menu")
    driver.implicitly_wait(20)
    addStudentByForm = driver.find_element(By.CLASS_NAME, "MuiButton-root")
    addStudentByForm.click()
    driver.implicitly_wait(40)
    admissionNo_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-invalid="false"][name="admissionNo"]')
    admissionNo_input.send_keys("102-2023")
    driver.implicitly_wait(30)
    firstName_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-invalid="false"][name="firstName"]')
    firstName_input.send_keys("Jonathan")
    driver.implicitly_wait(50)
    lastName_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-invalid="false"][name="lastName"]')
    lastName_input.send_keys("Mishra")
    driver.implicitly_wait(60)
    fatherName_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-invalid="false"][name="fathersName"]')
    fatherName_input.send_keys("Jhonny")
    driver.implicitly_wait(50)
    mobile_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-invalid="false"][name="mobileNo"]')
    mobile_input.send_keys("3652147896")
    dob_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-invalid="false"][name="dateOfBirth"]')
    dob_input.send_keys("25-08-2000")
    while(True):
        try:
            allDropdownMenu = driver.find_elements(By.CSS_SELECTOR, ".MuiFormControl-root.MuiFormControl-fullWidth.css-1mejovb")
            allDropdownMenu[0].click()
            driver.implicitly_wait(50)
            # class_selection
            driver.find_element(By.XPATH, "//li[@data-value='CLASS 12']").click()
            allDropdownMenu[1].click()
            driver.implicitly_wait(50)
            # divison_selection
            driver.find_element(By.XPATH, "//li[@data-value='B']").click()
            allDropdownMenu[2].click()
            driver.implicitly_wait(50)
            # geneder_selection
            driver.find_element(By.XPATH, "//li[@data-value='M']").click() 
            allDropdownMenu[3].click()
            driver.implicitly_wait(50)
            # bus selection
            driver.find_element(By.XPATH, "//li[@data-value='01']").click()
            allDropdownMenu[4].click()
            driver.implicitly_wait(50)
            # payment status selection
            driver.find_element(By.XPATH, "//li[@data-value='Yes']").click()
            allDropdownMenu[5].click()
            driver.implicitly_wait(50)
            # registered selection
            driver.find_element(By.XPATH, "//li[@data-value='Yes']").click()
            allDropdownMenu[7].click()
            driver.implicitly_wait(50)
            # admission status selection
            driver.find_element(By.XPATH, "//li[@data-value='Studying']").click()
            allDropdownMenu[8].click()
            driver.implicitly_wait(50)
            # hostel selection
            driver.find_element(By.XPATH, "//li[@data-value='Hostel']").click()
            # allDropdownMenu[6].click()
            # # area selection
            # driver.find_element(By.XPATH, "//li[@data-value='None']").click()
            break
        except Exception as e:
            pass
    addStudentDetails = driver.find_element(By.CSS_SELECTOR, ".MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-fullWidth.MuiButtonBase-root")
    addStudentDetails.click()
    confirm_Student_details = driver.find_elements(By.CSS_SELECTOR, ".MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-fullWidth.MuiButtonBase-root") 
    confirm_Student_details_button = confirm_Student_details[1]
    driver.execute_script("arguments[0].scrollIntoView();", confirm_Student_details_button)
    confirm_Student_details_button.click()

    # check student details
    confirm_elements = driver.find_elements(By.CSS_SELECTOR, ".MuiOutlinedInput-input.MuiInputBase-input.Mui-disabled.css-1x5jdmq")
    print("Full Name: ",confirm_elements[0].get_attribute("value"))
    print("Admission No: ",confirm_elements[1].get_attribute("value"))
    print("Class: ",confirm_elements[2].get_attribute("value"))
    print("Division: ",confirm_elements[3].get_attribute("value"))
    print("Gender: ",confirm_elements[4].get_attribute("value"))
    print("Area: ",confirm_elements[5].get_attribute("value"))
    print("Address: ",confirm_elements[6].get_attribute("value"))
    print("Mobile No: ",confirm_elements[7].get_attribute("value"))
    print("Bus ID: ",confirm_elements[8].get_attribute("value"))
    print("Payment Status: ",confirm_elements[9].get_attribute("value"))
    print("Registered: ",confirm_elements[10].get_attribute("value"))