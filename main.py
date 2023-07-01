from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
email = "your email"
password = "your password"
path = "Your chromedriver location"
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
url = "https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0&trk=public_jobs_nav-header-signin"#https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(url)
driver.maximize_window()
email = driver.find_element(by=By.ID, value="username")
email.send_keys(email)
password = driver.find_element(by=By.ID, value="password")
password.send_keys(password)
sign_btn = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
sign_btn.click()
time.sleep(2)

first_listing = driver.find_element(By.LINK_TEXT, "Python Developer")


first_listing.click()
try:
        job_apply = driver.find_element(By.CSS_SELECTOR, value='.jobs-unified-top-card__company-name a') # //*[@id="ember916"] //*[@id="ember297"] #//*[@id="ember298"]
        job_apply.click()

        time.sleep(5)
        follow = driver.find_element(By.CLASS_NAME, "follow")
        follow.click()
        time.sleep(5)
        confirm = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
        confirm.click()

        print("done")
except NoSuchElementException:
        print("nothing happened")


