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

pattern = re.compile(r'''^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$''',re.MULTILINE)
result = pattern.findall(get_UK())
for line in result:
    print(line)