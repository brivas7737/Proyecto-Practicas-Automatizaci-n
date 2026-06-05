from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Abrir página
driver.get("https://automationexercise.com")
driver.maximize_window()

time.sleep(2)

# Bajar al final de la página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)

# Correo de suscripción
correo = driver.find_element(By.ID, "susbscribe_email")
correo.send_keys("brian@test.com")

# Botón suscribirse
driver.find_element(By.ID, "subscribe").click()

time.sleep(3)

# Captura
driver.save_screenshot("suscripcion.png")

# ASSERT 1
mensaje = driver.find_element(
    By.CSS_SELECTOR,
    ".alert-success.alert"
).text

assert "successfully subscribed" in mensaje.lower()

# ASSERT 2
assert correo.is_displayed()

print("Suscripción correcta")

time.sleep(5)

driver.quit()