from auth import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time, random

browser = None

def login_chrome(login, password):
    global browser
    #Запуск Chrome и заход на сайт "https://www.instagram.com/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')

    # Ввод логина
    time.sleep(random.randrange(1, 3))
    _login = browser.find_element(By.NAME, "username")
    _login.clear()
    _login.send_keys(login)

    # Ввод пароля
    _password = browser.find_element(By.NAME, "password")
    _password.clear()
    time.sleep(random.randrange(1, 3))
    _password.send_keys(password)

    # Нажатие на кнопку через ENTER
    time.sleep(random.randrange(1, 3))
    _password.send_keys(Keys.ENTER)

    ####################################
    # Как нажимать на кнопку с помощью CCS
    # time.sleep(random.randrange(1, 3))
    # _login_button = browser.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    # _login_button.click()
    ####################################

    # Нажатие на кнопку "Не сейчас" после входа
    time.sleep(random.randrange(4, 6))
    _button = browser.find_element(By.CSS_SELECTOR, 'button[class="aOOlW   HoLwm "]')
    _button.click()

def close_browser():
    global browser
    browser.close()
    browser.quit()

def search_by_hashtag(hashtag):
    global browser
    # Запускает сайт с указанным в конце тэгом
    browser.get(f'https://www.instagram.com/explore/tags/{hashtag}')

    # Скролл страницы
    for i in range(1, 4):
        browser.execute_script("window.scroll(0, document.body.scrollHeight);")
        time.sleep(random.randrange(2, 5))

    # Ищет по тегу 'a'
    hrefs = browser.find_elements(By.TAG_NAME, 'a')

    # Находит и выводит ссылку у которых есть элемент /p в сылке
    urls = [item.get_attribute('href') for item in hrefs if "/p" in item.get_attribute('href')]
    print(urls)

    # Условия для нажатия лайка по очередно найденных ссылках которые выводятся на консоль
    for url in urls:
        browser.get(url)
        time.sleep(random.randrange(3, 5))
        time.sleep(3)
        like = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]')
        like.click()
        time.sleep(random.randrange(85, 105))


login_chrome(login, password)
time.sleep(5)
search_by_hashtag("dog")
time.sleep(200)
close_browser()