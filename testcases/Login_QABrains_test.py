import pytest

from pageobjects.LoginPage_QABrains import LoginPage

@pytest.mark.usefixtures("setup")
class Test_Login_QABrains:

    @pytest.mark.general
    def test_login_QAbrains_TC01(self,setup):

        self.driver = setup
        lp = LoginPage(self.driver)
        lp.Enter_Email("qa_testers@qabrains.com")
        lp.Enter_Password("Password123")
        lp.Click_LoginButton()
        if lp.Validate_LoginStatus() == "Pass":
            assert True
        else:
            assert False

