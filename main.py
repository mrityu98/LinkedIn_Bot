from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
#from webdriver_manager.chrome import ChromeDriverManager 

def launchBrowser():
    chrome_driver_path="C:/Users/mrmkc/Downloads/chromedriver-win64/chromedriver-win64/chromedriver"
    options = webdriver.ChromeOptions()
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3663654269&f_AL=true&geoId=111795395&keywords=ms%20excel&location=Kolkata%2C%20West%20Bengal%2C%20India&refresh=true") 
    return driver

driver = launchBrowser()
sign_in_button=driver.find_element("link text","Sign in")
sign_in_button.click()
email = driver.find_element(By.ID,"username")
email.send_keys("mkcgmeet98@gmail.com")
password = driver.find_element(By.ID,"password")
password.send_keys("mkc@ugAsrp98")
password.send_keys(Keys.ENTER)
all_listings=driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
for listing in all_listings:
    print("Called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR,".job-s-apply button")
        apply_button.click()
        time.sleep(2)
        phone_number = driver.find_element(By.CSS_SELECTOR,"fb-single-line-text__input")
        phone_number.send_keys("1234567890")
        next_button  = driver.find_element(By.CSS_SELECTOR,"footer button")
        
        if next_button.get_attribute("data-control-name") == "continue _unify":
            next_button.click()
        else:
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.XPATH,"//button[contains(@class,'artdeco-button')]//*[contains(.,'Discard')]/..")
            discard_button.click()
            continue
        time.sleep(2)
        review_button = driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
        if review_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.XPATH,"//button[contains(@class,'artdeco-button')]//*[contains(.,'Discard')]/..")
            discard_button.click()
            continue
        else:
            review_button.click()
            time.sleep(2)
            submit_button = driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
            if submit_button.get_attribute("data-control-name") =="submit_unify":
                submit_button.click()
                time.sleep(2)
                close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                close_button.click()
            else:
                
                close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element(By.XPATH,"//button[contains(@class,'artdeco-button')]//*[contains(.,'Discard')]/..")
                discard_button.click()
                continue
                                            
    except NoSuchElementException:
        continue



                                           
while(True):
    pass


   