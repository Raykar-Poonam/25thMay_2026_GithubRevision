from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    Input_Email_ID = "email"
    Input_Password_ID = "password"
    Click_LoginButton_XPATH = "//button[normalize-space()='Login']"
    Validate_LoginStatus_XPATH = "//h2[normalize-space()='Login Successful']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, self.Input_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.Input_Password_ID).send_keys(password)

    def Click_LoginButton(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Click_LoginButton_XPATH)))
        self.driver.execute_script(
            "arguments[0].click();", button
        )
        # self.driver.find_element(By.XPATH,self.Click_LoginButton_XPATH).click()

    def Validate_LoginStatus(self):

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.Validate_LoginStatus_XPATH)))
            # self.driver.find_element(By.XPATH, self.Validate_LoginStatus_XPATH)
            return "Pass"
        except:
            return "Fail"

    # def Click_LoginButton(self):
    #
    #     button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(
    #             (By.XPATH, self.Click_LoginButton_XPATH)
    #         )
    #     )
    #
    #     self.driver.execute_script(
    #         "arguments[0].click();", button
    #     )
