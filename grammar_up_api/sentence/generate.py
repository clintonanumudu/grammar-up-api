from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def generateSentence():
  chrome_options = Options()
  chrome_options.headless = True
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(chrome_options=chrome_options)
  driver.get("https://randomwordgenerator.com/sentence.php")
  sentenceElement = driver.find_element(By.CLASS_NAME, "support-sentence")
  WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CLASS_NAME, "support-sentence").get_attribute("innerHTML"))
  sentence = sentenceElement.get_attribute("innerHTML")
  driver.quit()
  return sentence
