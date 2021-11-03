# main.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


USERNAME = "ACCOUNT_USER"
PASSWORD = "ACCOUNT_PASS"
URL = "https://www.netflix.com/browse/my-list"
REGEX = r"https://www.netflix.com/watch/(.*?)\?tctx"


def login(browser):
    print(browser.current_url)
    try:
        username_field = browser.find_element(By.ID, 'id_userLoginId')
        username_field.send_keys(USERNAME)
        password_field = browser.find_element(By.ID, "id_password")
        password_field.send_keys(PASSWORD)
    except:
        username_field = browser.find_element(By.ID, 'email')
        username_field.send_keys(USERNAME)
        password_field = browser.find_element(By.ID, "password")
        password_field.send_keys(PASSWORD)
    login_button = browser.find_element(By.CLASS_NAME, 'login-button')
    login_button.click()


def profileselect(browser):
    print(browser.current_url)
    try:
        profiles = browser.find_elements(By.CLASS_NAME, "profile-icon")
        profiles[0].click()
    except:
        print("Error al seleccionar un perfil.")


def get_value(S, j):
    try:
        return S[j]
    except IndexError:
        return 0


def pin_numbers(browser):
    print(browser.current_url)
    try:
        numbers = browser.find_elements(By.CLASS_NAME, "pin-number-input")

        for i in range(300, 10000):
            n = list(map(int, str(i)))

            time.sleep(0.1)
            numbers[0].send_keys(get_value(n, 0))
            time.sleep(0.1)
            numbers[1].send_keys(get_value(n, 1))
            time.sleep(0.1)
            numbers[2].send_keys(get_value(n, 2))
            time.sleep(0.1)
            numbers[3].send_keys(get_value(n, 3))
            time.sleep(0.1)

            print("\n", n, "\n")
    except:
        print("Error al ingresar el PIN.")


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(options=options)

    print("Running Netflix Selenium")
    browser.get(URL)

    time.sleep(1)
    login(browser)
    time.sleep(1)
    profileselect(browser)
    time.sleep(1)
    pin_numbers(browser)


if __name__ == "__main__":
    main()
    # browser.quit()
