from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from transformers import pipeline
import matplotlib.pyplot as plt

name = 'Dimitri60581694'
password = 'IdeGas692007!'
email = 'buckappnoreply@gmail.com'

chrome_options = Options()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://x.com/i/flow/login')

    time.sleep(5)

    entry = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7'))
    )
    entry.send_keys(name)

    button = WebDriverWait(driver, 20).until (
        EC.presence_of_element_located((By.XPATH, '//button[./div/span/span[text()="Next"]]'))
    )
    button.click()
    time.sleep(5)
    email_input = None
    try:
        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
    except:
        print('Nema potvrde')
    if email_input != None:
        email_input.send_keys(email)
        verify_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="ocfEnterTextNextButton"]'))
        )
        verify_button.click()
        time.sleep(5)

    password_entry = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7'))
    )
    password_entry.send_keys(password)

    login_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-testid="LoginForm_Login_Button" and .//span[text()="Log in"]]'))
    )
    login_button.click()
    time.sleep(5)

    driver.get('https://x.com/DonaldJTrumpJr/status/1835391015181545831')

    time.sleep(5)
    emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
    processed_comments = set()
    emotions = dict()
    
    for _ in range(100):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        comments = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

        for comment in comments:
            comment_text = comment.text.strip()
            if comment_text and comment_text not in processed_comments:
                print('---------------- Komentar ----------------')
                print(comment_text)
                print('------------------------------------------')
                print()
                
                # Analiziraj emocije koristeći transformers
                result = emotion_classifier(comment_text)
                for r in result:
                    if r['score'] >= 0.7:
                        label = r['label']
                        if label not in emotions:
                            emotions[label] = 0
                        emotions[label] += 1
                print(result)
                print()

                processed_comments.add(comment_text)
    print("LEN JE" + str(len(processed_comments)))

    labels = list(emotions.keys())
    values = list(emotions.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.title('Users reaction')

    plt.show()

finally:
    driver.quit()