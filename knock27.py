import gzip
import json
import re

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
    pattern=re.compile(r'''(\'{2,5})(.*?)(\1)''',re.MULTILINE)
    target = pattern.sub(r'\2',target)
    pattern=re.compile(r'''\[\[(?:[^\|]*?\|)??([^\|]*?)\]\]''',re.MULTILINE)
    return pattern.sub(r'\1',target)

dict = {}
for line in result:
    dict[line[0]] = remove_markup(line[1])

for item in dict.items():
    print(item)