from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.first
def test_first(driver):
    category_cards = driver.find_elements(By.CLASS_NAME, 'card')
    WebDriverWait(driver, 5).until(EC.visibility_of(category_cards[1]))
    category_cards[1].click()
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'element-group'))
    )#==
    left_panel_elements = driver.find_elements(By.CLASS_NAME, 'element-group')
    WebDriverWait(driver, 5).until(EC.visibility_of(left_panel_elements[1]))
    left_panel_elements[1].click()
    pass