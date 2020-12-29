# Essencial to open browser
from selenium import webdriver
# Helps to find element
from selenium.webdriver.common.by import By
# Set wait rules
from selenium.webdriver.support.ui import WebDriverWait
# Set conditional rules
from selenium.webdriver.support import expected_conditions as EC
# Essencial to close terminal
import os
import signal
import time
import glob
# Essencial to control mouse and keyboard
from pynput.mouse import Button
from pynput.mouse import Controller

# Variables
URL = 'https://servicosonline.cpfl.com.br/agencia-webapp/#/login'
# Marcos
Email = 
Senha = 

# Set mouse automation
mouse = Controller()

# Load browser WebDriver ( Chrome or Firefox)
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

# Set usable wait time
wait = WebDriverWait(driver, 10)


# Open browser on page
driver.get(URL)

# Complete "E-mail" information
# Select the "E-mail" box
Email_box = wait.until(EC.presence_of_element_located((By.ID, 'documentoEmail')))
# Fill the box
Email_box.send_keys(Email)

# Complete "Senha" information
# Select the "Senha" box
Senha_box = wait.until(EC.presence_of_element_located((By.ID, 'password')))
# Fill the box
Senha_box.send_keys(Senha)

# Select "Entrar" button
Entrar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@translate = '@APP-LOGIN-BTN-ENTRAR']")))
# Click button
Entrar_button.click()

time.sleep(5)
driver.get('https://servicosonline.cpfl.com.br/agencia-webapp/#/historico-contas')

# Select "Selecionar Todas" checkbox
Todos_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@translate = '@APP-HISTORICO-CONTAS-CHECKBOX-SELECIONAR-TODAS']")))
# Confirm selection
Todos_checkbox.click()

# Select "Salvar Conta" button
Salvar_button = wait.until(EC.element_to_be_clickable((By.ID, 'btnSalvarContasPDF')))
# clic button
Salvar_button.click()