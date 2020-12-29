# Essencial to open browser
from selenium import webdriver
# Helps to find element
from selenium.webdriver.common.by import By
# Set wait rules
from selenium.webdriver.support.ui import WebDriverWait
# Set conditional rules
from selenium.webdriver.support import expected_conditions as EC
# Essencial to terminate script, close terminal and make dir
import os
import signal
# Essencial to move and rename file
import os.path
import shutil
from datetime import date
# Set wait times on the program
import time
# Essencial to control mouse and keyboard
from pynput import keyboard
from pynput.keyboard import Key

# Variables
URL = 'https://agenciaweb.celesc.com.br/AgenciaWeb/autenticar/loginCliente.do'

#Cliente = 
#Site = 
#Unidade_Consumidora = 
#Documento = 
#Senha = 

# Set input automation
keyboard = keyboard.Controller()

# Load browser WebDriver (Chrome or Firefox)
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

# Set usable wait time
wait = WebDriverWait(driver, 10)

# Open browser on page
driver.get(URL)

# Fill on the "Unidade Consumidora" box
wait.until(EC.presence_of_element_located(\
    (By.NAME, 'sqUnidadeConsumidora'))).send_keys(Unidade_Consumidora)

# Select "CPF" or "CNPJ" and complete "Documento" information
if len(Documento) == 12 - 1: # If "Documento" is a "CPF"
    # Select "CPF" radio
    wait.until(EC.presence_of_element_located(\
        (By.ID, 'CPF'))).click()
    
    # Fill the "Documento" box
    wait.until(EC.presence_of_element_located(\
        (By.NAME, 'numeroDocumentoCPF'))).send_keys(Documento)

else: #If "Documento" is a "CNPJ"
    # Select "CNPJ" radio
    wait.until(EC.element_to_be_clickable(\
        (By.ID, 'CPJ'))).click()

    # Fill the "Documento" box
    wait.until(EC.presence_of_element_located(\
        (By.NAME, 'numeroDocumentoCNPJ'))).send_keys(Documento)


# Click "Entrar" button
wait.until(EC.element_to_be_clickable(\
    (By.XPATH, "//input[@value = 'Entrar']"))).click()

# Fill "Senha" box
wait.until(EC.presence_of_element_located(\
    (By.NAME, 'senha'))).send_keys(Senha)

# Click "Entrar" button
wait.until(EC.element_to_be_clickable(\
    (By.XPATH, "//input[@value = 'Entrar']"))).click()

try:
    # Check existence of bill
    wait.until(EC.presence_of_element_located(\
    (By.XPATH, "//a[text() = 'Imprimir	2ª Via']"))).click()
except:
    #Close browser windows
    driver.quit()
    os.kill(os.getppid(), signal.SIGHUP)

# Save file
with keyboard.pressed(Key.ctrl):
    keyboard.press('s')
    keyboard.release('s')
time.sleep(2)

# Rename file
keyboard.type(os.getcwd() + "/.temp/" + Cliente + " " + Site + " "\
    + date.today().strftime("%m-%y"))
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# Wait finish download
while not os.path.exists(os.getcwd() + "/.temp/" + Cliente + " " + Site + " "\
    + date.today().strftime("%m-%y") + ".pdf"):
    time.sleep(1)

# Confirm existante of file
if os.path.isfile(os.getcwd() + "/.temp/"  + Cliente + " " + Site+ " "\
    + date.today().strftime("%m-%y") + ".pdf"):
    # Check existance of dir "Cliente"
    if not os.path.exists(os.getcwd() + "/Clientes/" + Cliente):
        # Make dir if not exist
        os.makedirs(os.getcwd() + "/Clientes/" + Cliente)
    # Check existance of dir "Ano" in dir "Cliente"
    if not os.path.exists(os.getcwd() + "/Clientes/" + Cliente + "/"\
        + date.today().strftime("%Y")):
        # Make dir if not exist
        os.makedirs(os.getcwd() + "/Clientes/" + Cliente + "/"\
            + date.today().strftime("%Y"))
    # Move file from "Download" to "Clientes/cliente/Ano"
    shutil.move(os.getcwd() + "/.temp/" + Cliente + " " + Site + " "\
        + date.today().strftime("%m-%y") + ".pdf", os.getcwd() + "/Clientes/"\
            + Cliente + "/" + date.today().strftime("%Y") + "/"+ Cliente + " "\
                + Site + " " + date.today().strftime("%m-%y") + ".pdf")

#Close browser windows
driver.quit()
os.kill(os.getppid(), signal.SIGHUP)