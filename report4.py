from requests import Request, Session

def read_file (file_name):
    txt_lines = []
    try:
        f = open(file_name,'r')
        txt_lines = f.readlines()
        f.close()
    except:
        print(file_name + "File Not Found")

    return txt_lines

def translate(en_lines, type = 'NMT'):
    ko_lines = []
    NAVER_CLIENT_ID = 'lhmShHu6t3rRvTT92aUi'
    NAVER_CLIENT_SECRET = 'kFVG1uxDco'

    headers = {
        'X-Naver-Client-Id': NAVER_CLIENT_ID,
        'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
    }
    if type  == 'SMT':
        url = 'https://openapi.naver.com/v1/language/translate'
    else:
        url = 'https://openapi.naver.com/v1/papago/n2mt'

    s = Session()

    text = ""
    for line in en_lines:
        text  += str(line)
    payload = {
        'source': 'en',
        'target': 'ko',
        'text': text,
    }

    ko_lines = text.split('\n')

    req = Request('POST', url, data=payload, headers=headers)
    prepped = req.prepare()

    res = s.send(prepped)

    res_json = res.json()

    ko_lines = res_json['message']['result']['translatedText'].split('\n')

    return ko_lines


def make_file(trans_file_name, en_lines, ko_lines):

    f = open(trans_file_name, 'w', encoding='UTF-8')

    for en_str, ko_str in zip(en_lines, ko_lines):
        print(en_str.replace('\n', ''))
        f.write(en_str)
        if ko_str not in ['','\n']:
            print(ko_str)
            f.write(ko_str + '\n')
    f.close()


def main():
    file_name = 'yesterday.txt'
    trans_file_name = 'yesterday_translated.txt'

    en_lines = read_file(file_name)  # 파일을 읽어서, 영문 text list를 만든다.

    # OPEN API 통해서 한글 text list를 만든다.
    # default = SMT, 머신러닝기반 = 'MNT'
    ko_lines = translate(en_lines,'SMT')

    make_file(trans_file_name, en_lines, ko_lines)  # 번역된 가사 파일을 저장한다.


if __name__ == '__main__':
    main()
