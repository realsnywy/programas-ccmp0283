# tests/test_pytestSelenium.py

import pytest
import selenium
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_lambdatest_todo_app():

    servico = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=servico)

    chrome_driver.get("https://lambdatest.github.io/sample-todo-app")
    chrome_driver.maximize_window()

    chrome_driver.find_element("name", "li1").click()
    chrome_driver.find_element("name", "li2").click()

    title = "Sample page - Lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element("id", "sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)

    chrome_driver.find_element("id", "addbutton").click()
    sleep(5)

    output_str = chrome_driver.find_element("name", "li6").text
    sys.stderr.write(output_str)

    sleep(2)
    chrome_driver.close()
