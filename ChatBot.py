from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from random import randint


texto = str(input("Qual a mensagem que deseja enviar a lista de contatos:"))
texto = urllib.parse.quote(texto)

url_whatsapp = 'https://web.whatsapp.com/'

driver_service = Service(executable_path="C:/Users/lucas/OneDrive/Desktop/Whatsappchatbot/chromedriver.exe")
options = Options() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")



driver = webdriver.Chrome(service=driver_service, options=options)

driver.get(url_whatsapp)
sleep(1)

contatos = ['+5511992885569', '+5511976489740']

lista = []

while len(lista) < 1:
    try:
        lista.append(driver.find_element(By.ID, 'side'))

    except:
        sleep(1)



for contato in contatos:
    lista = []

    link = f'https://web.whatsapp.com/send?phone={contato}&text={texto}'
    driver.get(link)
    
    while len(lista) < 1:
        try:
            lista.append(driver.find_element(By.ID, 'side'))

        except:
            sleep(1)

    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
    sleep(randint(0, 7))