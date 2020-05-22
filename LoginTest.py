import unittest
import HtmlTestRunner
import time
from selenium import webdriver
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/loginpage")    #run through cmd and to generate report we need this or else no need
from PageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):

    baseURL="https://testauth.digicollect.com/"
    email ="mandar.asp5@gmail.com"
    password ="123456789"
    driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_Login(self):
        lp=LoginPage(self.driver)
        lp.setUserEmail(self.email)
        lp.setPassword(self.password)
        lp.clickSignin()
        time.sleep(3)
        self.driver.save_screenshot("C:..\\Screenshots\\homepage.png")
        self.assertEqual("DigiCollect CRM", self.driver.title, "web page title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))






