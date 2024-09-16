# WhatsApp Bot - Atividade Somativa 1 
# Agentes Conversacionais - Inteligência Artificial Aplicada - PUCPR
# Aluno: Alan Gonçalves

# Arquivo main para executar o bot de WhatsApp.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from whatsapp_bot import WhatsAppBot

def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()

    bot = WhatsAppBot(driver)
    bot.start()

if __name__ == "__main__":
    main()

# Separei o código em quatro arquivos: 
# main.py, whatsapp_bot.py, message_processing.py e config.py.
# e adicionei um arquivo intents.json para armazenar as intenções do bot.

# Adicionei também um print pra evidenciar que o bot está respondendo as mensagens.

