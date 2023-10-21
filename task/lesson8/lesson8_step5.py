'''
<Задание на execute_script>
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
который дизайнер всё никак не успевает переделать. 
Вам потребуется написать код, чтобы:

1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "I'm the robot".
7. Переключить radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
'''

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
