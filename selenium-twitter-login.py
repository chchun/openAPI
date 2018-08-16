from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time

def login_twitter(driver, username, password):
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)
    
    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()
    #driver.implicitly_wait(5)
    time.sleep(15)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    savefiles = []
    all_imgs = soup.select('div.AdaptiveMedia-photoContainer > img')
    for img in all_imgs:
        print(img.get('src'))
        savefiles.append(img.get('src'))

    return savefiles

def download_file(urls):

    # url : https://pbs.twimg.com/media/Dkusz91W4AA4Z7O.jpg
    file_path = 'd:\\temp\\'

    for savefile in urls:
        print(savefile.split('/')[4], savefile)
        urllib.request.urlretrieve(savefile, file_path + savefile.split('/')[4])
        time.sleep(1)


if __name__ == "__main__":
  #  username = input("user name : ")
  #  password = input("password  : ")
  username = 'chchun88@gmail.com'
  password = open("mypass.txt").read().strip()
  driver = webdriver.Chrome()
  # twitter에 로그인 하여서,  사진 url을 가지고 옴
  savefiles = login_twitter(driver, username, password)
  # 저장함.
  download_file(savefiles)