from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.flipkart.com/search?q=smartphone+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&cmpid=content_21655629291_gmc_pla&gad_source=1&gclid=CjwKCAiAl4a6BhBqEiwAqvrquqAY6AbRF3jzbDkjyu5TdaUTsZadv_eWtKISDpaOau2cuZaYoj5c2RoCNwQQAvD_BwE&page=1")

phonename = []
romram = []
frontcamera = []
phonebattery = []
phonedisplay = []
phoneprice = []
Processor = []

for page in range(1, 60):
    driver.get(f"https://www.flipkart.com/search?q=smartphone+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&cmpid=content_21655629291_gmc_pla&gad_source=1&gclid=CjwKCAiAl4a6BhBqEiwAqvrquqAY6AbRF3jzbDkjyu5TdaUTsZadv_eWtKISDpaOau2cuZaYoj5c2RoCNwQQAvD_BwE&page={page}")
    time.sleep(3)

    for i in range(1, 25):
        try:
            phone_name_element = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[1]')
            phonename.append(phone_name_element.text)
        except:
            phonename.append("NAN")

        try:
            phone_rom_element = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[1]')
            romram.append(phone_rom_element.text)
        except:
            romram.append('NAN')

        try:
            phone_front_camera = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[3]')
            frontcamera.append(phone_front_camera.text)
        except:
            frontcamera.append("NAN")

        try:
            phone_price = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
            phoneprice.append(phone_price.text)
        except:
            phoneprice.append("NAN")

        try:
            phone_battery = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[4]')
            phonebattery.append(phone_battery.text)
        except:
            phonebattery.append('NAN')

        try:
            phone_processor = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[5]')
            Processor.append(phone_processor.text)
        except:
            Processor.append("NAN")

        try:
            phone_display = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[2]')
            phonedisplay.append(phone_display.text)
        except:
            phonedisplay.append("NAN")

data = {
    'Phone Name': phonename,
    'ROM/RAM': romram,
    'Front Camera': frontcamera,
    'Battery': phonebattery,
    'Display': phonedisplay,
    'Price': phoneprice,
    'Processor': Processor
}

df = pd.DataFrame(data)

df.to_csv('smartphones_prices.csv', index=False)

driver.quit()

print("Scraping complete! Data has been saved to 'smartphones_under_30000_page_1_to_250.csv'.")
