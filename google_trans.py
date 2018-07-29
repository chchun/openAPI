import requests


def read_file (file_name):
    txt_lines = []
    try:
        f = open(file_name,'r')
        txt_lines = f.readlines()
        f.close()
    except:
        print(file_name + "File Not Found")

    return txt_lines

def translate(en_lines):
    ko_lines = []
    api_key = 'AIzaSyDkkOFihPG6JlmCToD8LxhjuZUcTrW-UAs'
    url = 'https://www.googleapis.com/language/translate/v2?'

    text = ""
    for line in en_lines:
        text  += str(line)

    payload = {
        'q': text,
        'source': 'en',
        'target': 'ko',
        'key': api_key
    }

    ko_lines = text.split('\n')

    response = requests.get(url, params=payload)

    res_json = response.json()['data']['translations'][0]['translatedText']

    print(res_json)

    ko_lines = res_json.split('.')

    return ko_lines


def make_file(trans_file_name, en_lines, ko_lines):

    f = open(trans_file_name, 'w', encoding='UTF-8')

    for en_str, ko_str in zip(en_lines, ko_lines):
        print(en_str.replace('\n', ''))
        f.write(en_str)
        print(ko_str)
        f.write(ko_str + '\n')
    f.close()


def main():
    file_name = 'yesterday.txt'
    trans_file_name = 'yesterday_translated.txt'

    en_lines = read_file(file_name)  # 파일을 읽어서, 영문 text list를 만든다.

    # OPEN API 통해서 한글 text list를 만든다.
    ko_lines = translate(en_lines)

    make_file(trans_file_name, en_lines, ko_lines)  # 번역된 가사 파일을 저장한다.


if __name__ == '__main__':
    main()
