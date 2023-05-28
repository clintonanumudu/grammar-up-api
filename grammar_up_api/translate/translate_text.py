from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def translateText(toTranslate):
  chrome_options = Options()
  chrome_options.headless = True
  driver = webdriver.Chrome(chrome_options=chrome_options)
  driver.get("https://www.google.com/search?q=translate+to+german")
  driver.execute_script("document.getElementById('L2AGLb').click()")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "goog-textarea")))
  toTranslateElement = driver.find_element(By.CLASS_NAME, "goog-textarea")
  complete = "**djfnskdnskdjnfjddcn**"
  toTranslateElement.send_keys(toTranslate + complete)
  translationElement = driver.find_elements(By.CLASS_NAME, "Y2IQFc")[2]
  WebDriverWait(driver, 10).until(lambda driver: driver.find_elements(By.CLASS_NAME, "Y2IQFc")[2].get_attribute("innerHTML").endswith(complete))
  translation = translationElement.get_attribute('innerHTML')
  translation = translation.replace(complete, "")
  driver.quit()
  return translation
