from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from X import X
from Youtube import Youtube
from Reddit import Reddit
import matplotlib.pyplot as plt
import time
from urllib.parse import urlparse
import requests

def check_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    if "reddit.com" in domain:
        return 1
    elif "youtube.com" in domain:
        return 2
    elif "x.com" in domain:
        return 3
    else:
        return -1
    
def is_valid_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False


def main():

    username = None
    email = None
    password = None
    x_profile = None

    print('Do you want to use X for getting data (YES/NO)?')
    answer = input()
    answer = answer.strip().upper()
    if (answer == 'YES'):
        print('Please enter your X username:')
        username  = input()
        print('Please enter your X email:')
        email = input()
        print('Please enter your X password:')
        password = input()

    posts = []
    scroll_down_times = []
    #print("Enter URLs of posts you want to analyze (press CTRL + D or CTRL + Z to finish):")
    while True:
        try:
            print("Enter URL of post you want to analyze (press CTRL + D or CTRL + Z to finish):")
            url = input()
            if is_valid_url(url) and check_domain(url) != -1:
                print('How deep do you want to analyze this posts reactions? (1-10)')
                depth = input()
                while not (depth.isdigit() and int(depth) >= 1 and int(depth) <= 10):
                    print('Enter valid depth:')
                    depth = input()
                posts.append(url)
                scroll_down_times.append(int(depth) * 7)
            else:
                print('Enter valid URL')
        except EOFError:
            break

    chrome_options = Options()
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    reddit_profile = Reddit(driver)
    youtube_profile = Youtube(driver)
    if password != None:
        x_profile = X(driver, username, email, password)

    if (password != None):
        result = x_profile.login()
        if result != 1:
            print('Error: ' + '\n' + result)
    emotions = dict()
    time.sleep(5)
    for i in range(len(posts)):

        val = check_domain(posts[i])
        if val == 1:
            post_emotions = reddit_profile.getPostReactions(posts[i], scroll_down_times[i])
        elif val == 2:
            post_emotions = youtube_profile.getPostReactions(posts[i], scroll_down_times[i])
        elif val == 3:        
            post_emotions = x_profile.getPostReactions(posts[i], scroll_down_times[i])

        for key, value in post_emotions.items():
            if key in emotions:
                emotions[key] += value
            else:
                emotions[key] = value
    
    labels = list(emotions.keys())
    values = list(emotions.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.title('Users reaction')

    plt.show()



if __name__ == '__main__':
    main()