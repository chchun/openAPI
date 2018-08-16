import requests
from bs4 import BeautifulSoup
from urllib.parse import  urlparse

class PokoParser:
    def __init__(self, func=None):
        if func:
            self.parse_url = func
    def parse_url (self, url):
        print ('parse_url 구현이 안되었어요')
        print (url)

def okky_parser(url):
    #html을 요청
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #li 들의 리스트를 가져옴
    list = soup.select('li.list-group-item')

    data = ''
    # 필요한 내용을 파싱
    for li in list:
        a = li.find('h5').find('a')
        id = li.find('span').text[1:]
        link = a['href']
        title = a.text.strip() # 타이틀
        print(id, link, title)

def todayhumor_parser(url):
    print('구현이 안되었어요')

def iamprogrammer_parser(url):
    print('구현이 안되었어요')


if __name__ == "__main__":
    urls = [
        'https://okky.kr/articles/questions',
        'https://okky.kr/articles/tech',
        'https://okky.kr/articles/blockchain-qna',
        'http://www.todayhumor.co.kr/board/list.php?table=programmer',
        'http://www.todayhumor.co.kr/board/list.php?table=it',

    ]

    parser_select_dict = {
        'okky.kr': okky_parser,
        'www.todayhumor.co.kr': todayhumor_parser,
        'qna.iamprogrammer.io': iamprogrammer_parser
    }

    for url in urls:
        parse_url = urlparse(url)
        print(parse_url[1] + parse_url[2])

        func = parser_select_dict[parse_url[1]]
        parser = PokoParser(func)
        print(parser.parse_url(url))
