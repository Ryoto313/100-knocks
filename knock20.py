import gzip
import json
fname = 'jawiki-country.json.gz'

with gzip.open(fname, 'rt',encoding="utf-8") as data_file, open("UK.txt",mode="w",encoding="utf-8") as UK_file:
    for line in data_file:
        data_json = json.loads(line)
        if data_json['title'] == 'イギリス':
            print(data_json['text'])
            UK_file.write(str(data_json["text"]))
            break