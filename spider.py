import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

try:
    driver.get('https://dapic.webpic.com.br/')

    time.sleep(3)

    company_input = driver.find_element('xpath', '//input[@placeholder="Identificador da empresa"]')
    username_input = driver.find_element('xpath', '//input[@placeholder="Usuário"]')
    password_input = driver.find_element('xpath', '//input[@placeholder="Senha"]')
    submit_button = driver.find_element('xpath', '//button[@type="submit"]')

    company_input.send_keys('urbanzone')
    username_input.send_keys('urbanpe')
    password_input.send_keys('Urban#2022')

    time.sleep(2)


    submit_button.click()

    time.sleep(2)

    search_input = driver.find_element('xpath', '//input[@placeholder="Pesquisar (F1)"]')
    search_input.send_keys('Gestão de estoque')

    time.sleep(2)

    search_input.send_keys(Keys.ENTER)

    time.sleep(5)

    consultar_button = driver.find_element(By.XPATH, '//button[contains(text(), "Consultar")]')
    consultar_button.click()

    time.sleep(8)

    consultar_a= driver.find_element(By.XPATH, '//a[contains(text(), "Exportar")]')
    consultar_a.click()

finally:
    driver.quit()