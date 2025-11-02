from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    def setup_method(self):
        self.driver=webdriver.Chrome()

#Login Success
    def test_login_positive(self):
        driver=self.driver
        driver.get("https://practicetestautomation.com/practice-test-login/")

#HTTPS Check
        assert driver.current_url.startswith("https://"),"Insecure protocol detected(not https)"

        username=driver.find_element(By.ID,"username")
        username.send_keys("student")

        password=driver.find_element(By.ID,"password")
        password.send_keys("Password123")

        submit=driver.find_element(By.ID,"submit")
        submit.click()

        expected_text="Logged In Successfully"
        actual_text=driver.find_element(By.TAG_NAME,"h1").text
        assert actual_text in expected_text,"Login ought to be successful but is not"

#Checking for cookies 
        cookies=driver.get_cookies()
        if not cookies:
            print("No cookies provided by the site hence skip cookie checking")
        else:
            for c in cookies:
                name=c["name"]
                assert c.get("secure", False),"Missing 'Secure' flag"
                assert c.get("httpOnly", False),"Missing 'HttpOnly' flag"
                same_site=c.get("samesite","")
                assert same_site.lower() in ["lax", "strict"],"Missing 'SameSite' flag"

#Login Failure 
       
    def test_login_negative(self):
        driver=self.driver
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username=driver.find_element(By.ID,"username")
        username.send_keys("student")

        password=driver.find_element(By.ID,"password")
        password.send_keys("Password1234")

        submit=driver.find_element(By.ID,"submit")
        submit.click()

        expected_text="Your password is invalid!"
        actual_text=driver.find_element(By.ID,"error").text
        assert actual_text in expected_text,"Login ought to be failed but is not"

    def teardown_method(self):
        self.driver.quit()
            