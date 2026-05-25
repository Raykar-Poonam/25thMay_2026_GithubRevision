import pytest
import allure
from allure_commons.types import AttachmentType

from pageobjects.LoginPage_QABrains import LoginPage
from utilities.readconfigFile import readconfig
from utilities.Logger import loggen


@pytest.mark.usefixtures("setup")
class Test_Login_QABrains:
    log = loggen.gen_logger()

    @pytest.mark.ddtparams
    def test_login_QAbrains_TC01(self, setup, dataForlogin):

        self.log.info("Test Case test_login_QAbrains_TC01 Started")

        email = dataForlogin[0]
        password = dataForlogin[1]

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

        Actual_Result = lp.Validate_LoginStatus()
        Expected_Result = dataForlogin[2]

        TestCase_Status_List = []
        if Expected_Result == "Pass" and Actual_Result == "Pass":
            self.log.info("Expected Result & Actual Result both are Pass")
            TestCase_Status_List.append("PASS")
            self.log.info("Updated TestCase_Status_List as " + str(TestCase_Status_List))
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_PASS.png")
            self.log.info("Taking Allure Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_QAbrains_TC01_PASS",
                          attachment_type=AttachmentType.PNG)


        elif Expected_Result == "Fail" and Actual_Result == "Fail":
            self.log.info("Expected Result & Actual Result both are Fail")
            TestCase_Status_List.append("PASS")
            self.log.info("Updated TestCase_Status_List as " + str(TestCase_Status_List))
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_Fail.png")
            self.log.info("Taking Allure Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_QAbrains_TC01_Fail",
                          attachment_type=AttachmentType.PNG)

        else:
            self.log.info("Expected Result: " + str(Expected_Result) + "  " + "Actual Result: " + str(
                Actual_Result) + " Not Same")
            TestCase_Status_List.append("FAIL")
            self.log.info("Updated TestCase_Status_List as " + str(TestCase_Status_List))
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_FAIL.png")
            self.log.info("Taking Allure Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_QAbrains_TC01_FAIL",
                          attachment_type=AttachmentType.PNG)

        assert "FAIL" not in TestCase_Status_List
        self.log.info("TestCase_Status_List --> " + str(TestCase_Status_List))

        self.log.info("Test Case test_login_QAbrains_TC01 is Completed ")
















    # if lp.Validate_LoginStatus() == "Pass":
    #     self.log.info("Login Validating status Pass ")
    #     self.log.info("Test Case test_login_QAbrains_TC01 Passed ")
    #     self.log.info("Taking Screenshot for Pass  ")
    #     self.driver.save_screenshot("C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_PASS.png")
    #     assert True
    # else:
    #     self.log.info("Login Validating status Pass ")
    #     self.log.info("Test Case test_login_QAbrains_TC01 Failed ")
    #     self.log.info("Taking Screenshot for Fail ")
    #     self.driver.save_screenshot("C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Screenshots\\test_login_QAbrains_TC01_FAIL.png")
    #     assert False
    #
    # self.log.info("Test Case test_login_QAbrains_TC01 is Completed ")
