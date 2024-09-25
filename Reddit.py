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


class Reddit:
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def getPostReactions(self, link, scroll_down_times) -> dict:
        emotions = dict()
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

            try:
                load_comments_button = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//button[.//span[contains(text(), 'View more comments')]]"))
                )
                load_comments_button.click()
                time.sleep(2)
            except:
                pass
            
            comments = self.driver.find_elements(By.CSS_SELECTOR, "div#-post-rtjson-content p")

            for comment in comments:
                comment_text = comment.text.strip()
                if comment_text and comment_text not in processed_comments:
                    #print('---------------- Komentar ----------------')
                    #print(comment_text)
                    #print('------------------------------------------')
                    #print()
                    translated = translator.translate(comment_text)
                    if translated is None:
                        continue
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
        return emotions