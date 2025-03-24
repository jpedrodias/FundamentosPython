'''
Exercício 3 - FAV Enunciado WebScraping - Selenium
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DEBUG = True

def teste_eight_components():
    
    driver = webdriver.Firefox()

    driver.get('https://www.selenium.dev/selenium/web/web-form.html')

    title = driver.title
    if DEBUG: print(title)
    assert title == 'Web form'

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value='my-text')
    text_box.send_keys("Selenium") 

    #submit_button = driver.find_element(by=By.XPATH, value="/html/body/main/div/form/div/div[2]/button")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message") 
    value = message.text 
    assert value == "Received!" 

    driver.quit()

if __name__ == '__main__':
    teste_eight_components()