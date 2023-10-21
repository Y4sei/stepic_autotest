'''
<Задание: работа с выпадающим списком>
Для этой задачи мы придумали еще один вариант капчи для роботов.
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

1. Открыть страницу https://suninjuly.github.io/selects1.html
2. Посчитать сумму заданных чисел
3. Выбрать в выпадающем списке значение равное расчитанной сумме
4. Нажать кнопку "Submit"
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, z):
    return str(int(x) + int(z))


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    z_element = browser.find_element(By.ID, "num2")
    z = z_element.text
    y = calc(x, z)

    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    print(y)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
