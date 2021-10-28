from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    #Считываем х, подставляем в функцию calc
    x = browser.find_element_by_id('input_value').text
    result = calc(int(x))

    browser.execute_script("window.scrollBy(0, 150);")

    #Вводим результат в поле ответа
    browser.find_element_by_id('answer').send_keys(result)

    #Кликаем чекбокс и радиокнопку
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    #Кликаем кнопку
    browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(10)
    browser.quit()
