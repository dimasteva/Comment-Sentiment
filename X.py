from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from transformers import pipeline
import matplotlib.pyplot as plt
from googletrans import Translator
from deep_translator import GoogleTranslator

class X:
    def __init__(self, driver, username, email, password) -> None:
        self.driver = driver
        self.name = username
        self.email = email
        self.password = password
    
    def login(self):
        try:
            self.driver.get('https://x.com/i/flow/login')

            entry = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7'))
            )
            if self.name != None:
                entry.send_keys(self.name)
            elif self.email != None:
                entry.send_keys(self.email)

            time.sleep(3)
            button = WebDriverWait(self.driver, 20).until (
                EC.presence_of_element_located((By.XPATH, '//button[./div/span/span[text()="Next"]]'))
            )
            button.click()
            email_input = None
            time.sleep(3)
            try:
                email_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.NAME, "text"))
                )
            except:
                #print('No email verification needed')
                pass
            if email_input != None:
                email_input.send_keys(self.email)
                verify_button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="ocfEnterTextNextButton"]'))
                )
                verify_button.click()
            time.sleep(3)
            password_entry = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7'))
            )
            password_entry.send_keys(self.password)
            time.sleep(3)
            login_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-testid="LoginForm_Login_Button" and .//span[text()="Log in"]]'))
            )
            login_button.click()
        except Exception as e:
            return str(e)
        return 1

    def getPostReactions(self, link, scroll_down_times) -> dict:
        emotions = dict()
        try:
            self.driver.get(link)
            time.sleep(5)
            emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
            processed_comments = set()
            translator = GoogleTranslator(source='auto', target='en')
            
            for _ in range(scroll_down_times):
                body = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'body'))
                )
                body.send_keys(Keys.PAGE_DOWN)

                time.sleep(2)
                
                comments = self.driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

                for comment in comments:
                    comment_text = comment.text.strip()
                    if comment_text and comment_text not in processed_comments:
                        #print('---------------- Komentar ----------------')
                        #print(comment_text)
                        #print('------------------------------------------')
                        #print()
                        translated = translator.translate(comment_text)
                        result = emotion_classifier(translated)
                        for r in result:
                            if r['score'] >= 0.7:
                                label = r['label']
                                if label not in emotions:
                                    emotions[label] = 0
                                emotions[label] += 1
                        #print(result)
                        #print()

                        processed_comments.add(comment_text)
            #print("LEN JE" + str(len(processed_comments)))
        except Exception as e:
            print(e)
        return emotions
        
