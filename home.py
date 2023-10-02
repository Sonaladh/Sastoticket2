import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Baseclass:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sastotickets.com/")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


class TestLogin(Baseclass):
    def test_clickLogin(self):
        self.driver.find_element(By.XPATH, "//*[@data-target='#login-modal']").click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//*[@id='login_username']").send_keys("sonal")
        # self.driver.find_element(By.XPATH, "//*[@id='login_password']").send_keys("sonal")

        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login_username")))
        pass_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login_password")))
        username_input.send_keys("sonal")
        pass_input.send_keys("sonal")

        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "btnLogin")))
        login_click.click()




        time.sleep(10)
