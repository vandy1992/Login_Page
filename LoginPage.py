class LoginPage():
    #Locators of all the web element
    email_id="emailaddress"
    password_name="password"
    signin_xpath="//button[@class='btn btn-block btn-gradient fuse-ripple-ready']"
    forgot_password_xpath="//small[contains(text(),'Forgot your password?')]"
    signUp_xpth="//b[contains(text(),'Sign Up')]"

    #constructor

    def __init__(self,driver):
        self.driver=driver

    #action method

    def setUserEmail(self,email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_name(self.password_name).send_keys(password)

    def clickSignin(self):
        self.driver.find_element_by_xpath(self.signin_xpath).click()








