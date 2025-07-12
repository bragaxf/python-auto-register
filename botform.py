# -*- coding: utf-8 -*-
# Selenium Auto Register - Main Script
# This script automates filling out a registration form on a website.
# You can change the HTML selectors and URL according to the site being automated.
# ⚠️ If a field is not going to be used, you should comment out or remove that section.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
import time
import multiprocessing

# Functions to generate random values

def generate_random_username():
    prefix = ''.join(random.choices(string.ascii_lowercase, k=5))
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}{suffix}"

def generate_random_nome():
    return ''.join(random.choices(string.ascii_lowercase, k=7))

def generate_random_sobremone():
    return ''.join(random.choices(string.ascii_lowercase, k=9))

def generate_random_email():
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}@gmail.com"

def generate_random_zipcode():
    return f"3030-{''.join(random.choices(string.digits, k=3))}"

def generate_random_nRUA():
    return ''.join(random.choices(string.digits, k=3))

def generate_random_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

# Main browser automation function

def automate_browser_instance():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
        """
    })

    # 🔧 Change the URL to match the target registration form
    url = 'https://example.com/?modal=registration'
    driver.get(url)

    try:
        time.sleep(10)  # Wait for page to fully load

        # 🧾 FIELD: First Name
        name_field = driver.find_element(By.ID, 'name')
        name_field.send_keys(generate_random_nome())

        # 🧾 FIELD: Last Name
        surname_field = driver.find_element(By.ID, 'surname')
        surname_field.send_keys(generate_random_sobremone())

        # 📅 FIELD: Date Picker
        calendar_icon = driver.find_element(By.CSS_SELECTOR, ".ng-datepicker-calendar-icon")
        calendar_icon.click()

        wait = WebDriverWait(driver, 10)
        year_2006 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='2006']")))
        year_2006.click()

        selected_year = random.choice(['2003', '2004', '2005'])
        selected_year_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{selected_year}']")))
        selected_year_element.click()

        month_november = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Nov']")))
        month_november.click()

        month_prefixes = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Dec"]
        selected_month_prefix = random.choice(month_prefixes)
        selected_month_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{selected_month_prefix}']")))
        selected_month_element.click()

        # 🧾 FIELD: Day
        day = random.randint(1, 28)
        day_option = driver.find_element(By.XPATH, f"//*[text()='{day}']")
        day_option.click()

        # 🧾 FIELD: Confirm date selection
        select_birthday = driver.find_element(By.XPATH, f"//*[text()='Select']")
        select_birthday.click()

        # 🧾 FIELD: Email
        email_field = driver.find_element(By.ID, 'email')
        email_field.send_keys(generate_random_email())

        # 🧾 FIELD: City
        city_names = ["Condeixa", "Coimbra", "Lousa", "Soure", "Penacova", "Cernache", "Antanhol"]
        selected_city_names = random.choice(city_names)
        city_field = driver.find_element(By.ID, 'city')
        city_field.send_keys(selected_city_names)

        # 🧾 FIELD: Address
        address_field = driver.find_element(By.ID, 'address')
        address_field.send_keys('Rua , ' + generate_random_nRUA())

        # 🧾 FIELD: Zip Code
        zip_code_field = driver.find_element(By.ID, 'zip_code')
        zip_code_field.send_keys(generate_random_zipcode())

        # 🧾 FIELD: Currency (dropdown)
        currency_dropdown = driver.find_element(By.CSS_SELECTOR, '.ng-select__center')
        currency_dropdown.click()
        time.sleep(1)
        euro_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Euro') or contains(text(), 'EUR')]")
        euro_option.click()

        # 🧾 FIELD: Country (scroll dropdown)
        country_selector = driver.find_element(By.CSS_SELECTOR, '.ng-select__value')
        country_selector.click()
        time.sleep(2)
        for _ in range(13):
            zip_code_field.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.1)

        # 🧾 FIELD: Phone number
        phone_input = driver.find_element(By.CSS_SELECTOR, "input.tw-bg-transparent.tw-outline-none.tw-block")
        phone_input.clear()
        random_phone_number = '3519' + ''.join(str(random.randint(0, 9)) for _ in range(8))
        phone_input.send_keys(random_phone_number)

        # 🧾 FIELD: Username
        username_field = driver.find_element(By.ID, 'username')
        username_field.send_keys(generate_random_username())

        # 🧾 FIELD: Password
        password = generate_random_password()
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

        # 🧾 FIELD: Password confirmation
        password_confirm_field = driver.find_element(By.ID, 'password_confirmation')
        password_confirm_field.send_keys(password)

        # ✅ FIELD: Age policy checkbox
        privacy_policy_element = driver.find_element(By.XPATH, "//div[contains(text(), 'I confirm that I am at least 18 years old')]")
        privacy_policy_element.click()

        # 🔽 Scroll down to ensure visibility of the submit button
        actions = ActionChains(driver)
        for _ in range(5):
            actions.send_keys("\ue015")
        actions.perform()

        # 🧾 FIELD: Submit button
        sign_up_button = driver.find_element(By.XPATH, "//button[contains(@class, 'ng-btn-primary') and text()='Sign Up']")
        sign_up_button.click()

        print("'Sign Up' button clicked successfully.")

        while True:
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        while True:
            time.sleep(1)

# Run multiple browser instances in parallel
if __name__ == "__main__":
    multiprocessing.freeze_support()
    try:
        num_windows = int(input("How many windows do you want to open? "))
        processes = []

        for _ in range(num_windows):
            process = multiprocessing.Process(target=automate_browser_instance)
            process.start()
            processes.append(process)

        for process in processes:
            process.join()

    except ValueError:
        print("Please enter a valid number of windows.")
