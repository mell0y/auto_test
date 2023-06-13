# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver = webdriver.Chrome()
    driver.get('https://sbis.ru/')
    driver.maximize_window()
    time.sleep(2)
    contacts_button = driver.find_element(By.CSS_SELECTOR, '[class=sbisru-Header] [href="/contacts"]')
    contacts_button.click()
    info_tensor_banner = driver.find_element(By.CSS_SELECTOR, '[id="contacts_clients"] [href="https://tensor.ru/"]')
    time.sleep(2)
    info_tensor_banner.click()
    time.sleep(2)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    banner_strong_in_human = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-bg"]')
    driver.execute_script("arguments[0].scrollIntoView();", banner_strong_in_human)
    time.sleep(2)
    banner_name = driver.find_element(By.XPATH, '//p[text()="Сила в людях"]')
    assert banner_strong_in_human.is_displayed(), 'Новость "Сила в Людях", не найдена'
    assert banner_name.text == 'Сила в людях'
    link_about = driver.find_element(By.CSS_SELECTOR, '[href="/about"][class="tensor_ru-Header__menu-link"]')
    link_about.click()
    time.sleep(3)
    about_page = driver.current_url
    assert about_page == 'https://tensor.ru/about'
finally:
    driver.quit()
