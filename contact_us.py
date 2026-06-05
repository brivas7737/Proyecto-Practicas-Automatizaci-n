from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

driver.get("https://automationexercise.com")
driver.maximize_window()

time.sleep(2)

# Ir a Contact Us
driver.find_element(By.XPATH, '//a[contains(@href,"/contact_us")]').click()

time.sleep(2)

# Formulario
driver.find_element(By.NAME, "name").send_keys("Brian")
driver.find_element(By.NAME, "email").send_keys("brian@test.com")
driver.find_element(By.NAME, "subject").send_keys("Prueba Selenium")
driver.find_element(By.ID, "message").send_keys("Mensaje de prueba automatizado")

# Adjuntar archivo
ruta_archivo = os.path.abspath("archivo_prueba.txt")

driver.find_element(By.NAME, "upload_file").send_keys(ruta_archivo)

# Enviar
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="submit-button"]').click()

time.sleep(2)

# Aceptar alerta
driver.switch_to.alert.accept()

time.sleep(3)

# Captura
driver.save_screenshot("contact_us.png")

# ASSERT 1
assert "Success!" in driver.page_source

# ASSERT 2
mensaje = driver.find_element(
    By.CSS_SELECTOR,
    ".status.alert.alert-success"
).text

assert "successfully" in mensaje.lower()

print("Formulario enviado correctamente")

time.sleep(5)

driver.quit()