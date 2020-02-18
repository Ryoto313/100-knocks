import gzip
import json
import re
import requests

fname = 'jawiki-country.json.gz'
def get_UK():
    with gzip.open(fname, 'rt',encoding="utf-8") as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return(data_json['text'])

    raise ValueError("イギリスの記事が見つからない")

pattern = re.compile(r'''^\|([^ =]*) = (.*)$''',re.MULTILINE)
result = pattern.findall(get_UK())
def remove_markup(target):
    #強調markup
    pattern = re.compile(r'''(\'{2,5})(.*?)(\1)''',re.MULTILINE)
    target = pattern.sub(r'\2',target)
    #内部リンクとファイル
    pattern = re.compile(r'''\[\[(?:[^\|]*?\|)*?([^\|]*?)\]\]''',re.MULTILINE)
    target = pattern.sub(r'\1',target)
    #lang
    pattern = re.compile(r'''\{\{(?:[^\|]*\|)*?([^\|]*)\}\}''', re.MULTILINE)
    target = pattern.sub(r'\1',target)
    pattern = re.compile(r'''<[^>]*>''', re.MULTILINE)
    target = pattern.sub('', target)
    pattern = re.compile(r'''\[.*\]''', re.MULTILINE)
    target = pattern.sub('',target)
    return target


dict = {}
for line in result:
    dict[line[0]] = remove_markup(line[1])

fname = dict["国旗画像"]

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:" + fname
}
proxy_dict = {
    "http": "http://W436647_nttdiomc:Takeuti0313@proxy.igs.nttdata.co.jp:8080",
    "https": "http://W436647_nttdiomc:Takeuti0313@proxy.igs.nttdata.co.jp:8080"
}

R = S.get(url=URL, params=PARAMS,proxies=proxy_dict)
DATA = R.json()
PAGES = DATA["query"]["pages"]
for k, v in PAGES.items():
    for kk, vv in v.items():
        if kk == 'imageinfo':
            print(vv[0]['url'])