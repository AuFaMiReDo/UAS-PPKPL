import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://localhost:8000/login") 

try:
    print("Mulai Regression Test: Alur Pembuatan Pesanan BBM...")
    
    driver.find_element(By.NAME, "email").send_keys("staf@perusahaanA.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    buat_pesanan_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Buat Pesanan')]"))
    )
    buat_pesanan_btn.click()

    fuel_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "fuel_type"))
    ))
    fuel_select.select_by_visible_text("Solar Industri")

    volume_input = driver.find_element(By.NAME, "volume_liters")
    volume_input.send_keys("15000") 
    
    price_input = driver.find_element(By.NAME, "unit_price")
    price_input.send_keys("12500")

    driver.find_element(By.NAME, "delivery_location").send_keys("Depot TBBM Pertamina Banjarmasin")
    
    driver.find_element(By.NAME, "scheduled_at").send_keys("2026-07-15T08:00")

    driver.find_element(By.XPATH, "//button[contains(text(), 'Ajukan Pesanan')]").click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "session-success-alert")) 
    )
    
    print("✅ REGRESSION TEST PASSED: Fungsionalitas pembuatan order tidak terpengaruh oleh penambahan fitur logistik baru.")

except Exception as e:
    print(f"❌ REGRESSION TEST FAILED: Terdapat masalah pada UI/API lama. Error: {e}")

finally:
    time.sleep(3)
    driver.quit()