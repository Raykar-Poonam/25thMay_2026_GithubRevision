import pytest

from pageobjects.LoginPage_QABrains import LoginPage
from utilities.readconfigFile import readconfig
from utilities.Logger import loggen

@pytest.mark.usefixtures("setup")
class Test_Login_QABrains:

    log = loggen.gen_logger()

    @pytest.mark.config
    def test_login_QAbrains_TC01(self,setup):

        self.log.info("Test Case test_login_QAbrains_TC01 Started")

        email = readconfig.getEmail()
        password = readconfig.getPassword()

        self.log.info("Opening browser & navigating to QABrain Website ")
        self.driver = setup
        lp = LoginPage(self.driver)

        self.log.info("Entering Email")
        lp.Enter_Email(email)
        self.log.info("Entering Password")
        lp.Enter_Password(password)
        self.log.info("Clicking Login Button")
        lp.Click_LoginButton()
        self.log.info("Validating Login Status")
        if lp.Validate_LoginStatus() == "Pass":
            self.log.info("Login Validating status Pass ")
            self.log.info("Test Case test_login_QAbrains_TC01 Passed ")
            self.log.info("Taking Screenshot for Pass  ")
            self.driver.save_screenshot("C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_PASS.png")
            assert True
        else:
            self.log.info("Login Validating status Pass ")
            self.log.info("Test Case test_login_QAbrains_TC01 Failed ")
            self.log.info("Taking Screenshot for Fail ")
            self.driver.save_screenshot("C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_FAIL.png")
            assert False

        self.log.info("Test Case test_login_QAbrains_TC01 is Completed ")