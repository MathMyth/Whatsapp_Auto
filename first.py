from selenium import webdriver
import time,sys
from selenium.common.exceptions import NoSuchElementException

def new_chat(user_name):
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="rRAIq"]')
    new_chat.click()

    new_user = chrome_browser.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(2)

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as ne:
        print('Given user "{}" is not found in contact list..'.format(user_name))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()

if __name__=='__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:/Users/a/AppData/Local/Google/Chrome/User Data/Default')
    options.add_argument('--profile-directory=Default')
    chrome_browser = webdriver.Chrome(executable_path="C:/Users/a/Desktop/chromedriver",
                                      options=options)
    chrome_browser.get(url="https://web.whatsapp.com/")

    time.sleep(17)

    print("QR Scanned successfully")

    user_name_list = ["Maulik CE"]

    for user_name in user_name_list:
        try:
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException as ne:
            new_chat(user_name)

        message_box = chrome_browser.find_element_by_xpath('//div[@class="_1Plpp"]')
        message_box.send_keys("Don't worry...This is Testing Bot..")

        send_button = chrome_browser.find_element_by_xpath('//button[@class="_35EW6"]')
        send_button.click()

    print("Messages sent successfully..")
