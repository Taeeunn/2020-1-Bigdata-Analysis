from urllib.request import urlopen, Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import warnings
import time
warnings.filterwarnings(action='ignore')

baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)
driver.get(url)

time.sleep(3)

# automatic login
login_section = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
driver.find_element_by_xpath(login_section).click()
time.sleep(3)

id_blank = driver.find_element_by_name("username")
id_blank.clear()
id_blank.send_keys('')  # my instagram ID

passwd_blank = driver.find_element_by_name('password')
passwd_blank.clear()
passwd_blank.send_keys('')  # my instagram password

time.sleep(3)

login_button = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button'
driver.find_element_by_xpath(login_button).click()

time.sleep(5)

save_button = '//*[@id="react-root"]/section/main/div/div/div/section/div/button'
driver.find_element_by_xpath(save_button).click()

time.sleep(10)
SCROLL_PAUSE_TIME = 3.0
reallink = []
stop=0

while True:
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')

    for link1 in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
        for i in range(3):
            title = link1.select('a')[i]
            real = title.attrs['href']
            reallink.append(real)
            if len(reallink) == 999:
                stop=1
                break
        if stop==1: break
    if stop==1: break


    last_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)


num_of_data=len(reallink)

result = []

for i in tqdm(range(num_of_data)):

    result.append([])
    req = Request("https://www.instagram.com/p"+reallink[i], headers={'User-Agent': 'Mozila/5.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8')

    for element in soup.find_all('meta', attrs={'property':"instapp:hashtags"}):
        hashtags = element['content'].rstrip(',')
        result[i].append(hashtags)

    data = pd.DataFrame(result)
    data.to_csv(plusUrl+'.txt', encoding='utf-8')

driver.close()