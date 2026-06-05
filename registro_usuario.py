from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Abrir página
driver.get("https://automationexercise.com")
driver.maximize_window()

time.sleep(2)

# Ir a Signup/Login
driver.find_element(By.XPATH, '//a[contains(@href,"/login")]').click()

time.sleep(2)

# Registro nuevo usuario
driver.find_element(By.NAME, "name").send_keys("Brian")

driver.find_element(
    By.XPATH,
    '//input[@data-qa="signup-email"]'
).send_keys("brian999999@test.com")

driver.find_element(
    By.XPATH,
    '//button[@data-qa="signup-button"]'
).click()

time.sleep(2)

# Título
driver.find_element(By.ID, "id_gender1").click()

# Password
driver.find_element(By.ID, "password").send_keys("123456")

# Fecha nacimiento
driver.find_element(By.ID, "days").send_keys("10")
driver.find_element(By.ID, "months").send_keys("May")
driver.find_element(By.ID, "years").send_keys("2000")

# Datos personales
driver.find_element(By.ID, "first_name").send_keys("Brian")
driver.find_element(By.ID, "last_name").send_keys("Rivas")
driver.find_element(By.ID, "address1").send_keys("La Paz Bolivia")
driver.find_element(By.ID, "state").send_keys("La Paz")
driver.find_element(By.ID, "city").send_keys("La Paz")
driver.find_element(By.ID, "zipcode").send_keys("1234")
driver.find_element(By.ID, "mobile_number").send_keys("77777777")

# Crear cuenta
driver.find_element(
    By.XPATH,
    '//button[@data-qa="create-account"]'
).click()

time.sleep(3)

# Captura de pantalla
driver.save_screenshot("registro_usuario.png")

# ASSERT 1
mensaje = driver.find_element(
    By.XPATH,
    '//h2[@data-qa="account-created"]'
).text

assert "ACCOUNT CREATED!" in mensaje

# ASSERT 2
assert "ACCOUNT CREATED!" in driver.page_source

print("Registro exitoso - Validaciones correctas")

time.sleep(5)

driver.quit()