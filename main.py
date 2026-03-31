from config import CODICE_PERSONA, PASSWORD, FAVOURITE_SLOTS

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

POLIMI_LINK = 'https://www.sport.polimi.it/'

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver))
driver.maximize_window()
driver.get(POLIMI_LINK)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "offerta"))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(., "Accedi al tuo account")]'))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login"))
).send_keys(CODICE_PERSONA)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password"))
).send_keys(PASSWORD)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "RESTA_CONNESSO"))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(., "Accedi")]'))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(., "Continua")]'))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Rifiuta")]'))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "home_btt_booking"))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(., " Nuova Prenotazione")]'))
).click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(., "Giuriati - Fit Center")]'))
).click()


sleep(5)
available_slots = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//div[contains(@class, "slot-available")]')
    )
)
searched_slots = available_slots.find_elements(By.XPATH, './/[contains(., "16:30")]')
print(searched_slots.text)

for time in FAVOURITE_SLOTS:
    for slot in available_slots:
        if time in slot.text:
            driver.execute_script("arguments[0].click();", slot)
            
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Conferma Prenotazione")]'))
            )
            print(confirm_button, confirm_button.text)
            driver.execute_script("arguments[0].click();", confirm_button)
            print("slot clickato!")

            sleep(3)
            print(time, slot.text)
    


for slot in available_slots:
    print("miao")
    print(slot.text)
print(len(available_slots))


sleep(5)
elem = driver.find_elements(By.XPATH, '//div[contains(@class, "event-slot") and contains(@class, "slot-available")]')
print(len(elem))
for time in FAVOURITE_SLOTS:
    elements = driver.find_elements(By.XPATH, '//div[contains(@class, "slot-available") and .//span[contains(@class, "time-start") and normalize-space()="{time}"]]')
    print(time)
    print(elements)
    if elements:
        print(elements)
        #elements[0].click()

        break

# print("URL:", driver.current_url)
# times = driver.find_elements(By.XPATH, '//span[contains(@class, "time-start")]')
# print("Times:", len(times))

# slots = driver.find_elements(By.XPATH, '//div[contains(@class, "slot-available")]')
# print("Slots:", len(slots))


# times = driver.find_elements(By.XPATH, '//span[contains(@class, "time-start")]')
# print("Times trovati:", len(times))

# for t in times:
#     print("TESTO:", repr(t.text))
#     print("HTML:", t.get_attribute("outerHTML"))




input("Premi invio per chiudere...")
driver.quit()


# from selenium import webdriver

# driver = webdriver.Chrome()

# #driver.maximize_window()
# driver.get("https://www.google.com")

# input("Premi invio per chiudere...")
# driver.quit()

#driver.find_element(By.CLASS_NAME, "offerta").click()
#driver.find_element(By.XPATH, '//button[@type="submit" and contains(., "Accedi al tuo account")]')
