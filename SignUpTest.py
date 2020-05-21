import unittest
import HtmlTestRunner
import time
from selenium import webdriver
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/loginpage")    #run through cmd and to generate report we need this or else no need
from PageObjects.SignUpPage import SignUpPage

class LoginTest(unittest.TestCase):

    baseURL="https://testauth.digicollect.com/"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Vandana Mallaiah\\PycharmProjects\\loginpage\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_Login(self):
        sp=SignUpPage(self.driver)
        sp.click_signUp()
        time.sleep(3)
        self.driver.save_screenshot("C:\\Users\\Vandana Mallaiah\\PycharmProjects\\loginpage\\Screenshots\\signuppage.png")
        self.assertEqual("DigiCollect CRM", self.driver.title, "web pae title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))






