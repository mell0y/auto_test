# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()
try:
    user_login, user_password = 'жма', 'Балонка1'
    my_name = 'Жмышенко Валерий'
    auth_page = 'https://fix-sso.sbis.ru/auth-online/'
    driver.get(auth_page)
    driver.maximize_window()
    time.sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    time.sleep(5)
    registry_contact = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    registry_contact.click()
    time.sleep(1)
    button_contact = driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-SubMenu__head"]')
    button_contact.click()
    time.sleep(1)
    add_mail = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_mail.click()
    time.sleep(1)
    field_search = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    field_search.send_keys(my_name, Keys.ENTER)
    time.sleep(2)
    mail_sender = driver.find_element(By.CSS_SELECTOR, '[class="msg-addressee-selector__addressee"]')
    time.sleep(2)
    mail_sender.click()
    time.sleep(2)
    text_window = driver.find_element(By.CSS_SELECTOR, '[role="textbox"][data-qa="textEditor_slate_Field"]')
    text_window.send_keys("Hello autotest", Keys.ENTER)
    time.sleep(2)
    up_mail = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    up_mail.click()
    time.sleep(2)
    mail_in_registry = driver.find_element(By.XPATH, '//p[contains(text(), "Hello autotest")]')
    time.sleep(2)
    assert mail_in_registry.text == "Hello autotest", 'Письмо не найденно в реестре'
    mail_in_registry.click()
    time.sleep(2)
    mail_del = driver.find_element(By.CSS_SELECTOR, '[data-qa="remove"]')
    mail_del.click()
    time.sleep(2)
finally:
    driver.quit()
