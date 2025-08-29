from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Altere para a mensagem desejada"
        self.contato = ["coloque o nome do contato que enviar a mensagem"]

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        service = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 60)
    
    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        print("Escaneie o QR Code no WhatsApp Web...")
        time.sleep(20)

        for contato in self.contato:
            contato_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//span[@title='{contato}']"))
            )
            contato_element.click()

            chat_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//footer//div[@contenteditable='true']"))
            )
            chat_box.click()
            chat_box.send_keys(self.mensagem + Keys.ENTER) 
            time.sleep(20)

bot = WhatsappBot()
bot.EnviarMensagens()
