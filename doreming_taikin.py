# Generated by Selenium IDE
import sys
sys.dont_write_bytecode = True
import pytest
import time
import json
from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDoreming():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_doreming(self):
    self.driver.get("https://d.doreming.com/entrance/")
    self.driver.set_window_size(1050, 716)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("2004184281")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("nextgen111")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(7)").click()
    time.sleep(2)
    #スタッフ専用というボタンが無くなったのでコメント化。2022/12/13
    #self.driver.find_element(By.LINK_TEXT, "スタッフ専用").click()
    #time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".float-left > .icon-time_recorder").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
    time.sleep(5)
    #確認ボタンが無くなったのでコメント化。(2024/03/20)
    #self.driver.find_element(By.CSS_SELECTOR, ".btn-confirm-ok").click()
  
