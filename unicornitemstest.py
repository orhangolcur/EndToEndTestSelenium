import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class EndToEndTestSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_unicornitems(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys("abcd")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("1234")

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.NAME, "login")))
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))
        alert_message = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")

        self.assertIn("ERROR: INCORRECT USERNAME OR PASSWORD", alert_message.text)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
