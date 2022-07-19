import requests

from  dct.service.config_yandex_dct import yandexDictonaryKey

def print_examples(res):
    for item1 in res['def']:
        print()
        print(item1['pos'] + ':')
        for item2 in item1['tr']:
            if 'ex' in item2:
                for item3 in item2['ex']:
                    print(f'{item3["text"]} – {item3["tr"][0]["text"]}')

def print_syn(res):
    lst = []
    for item1 in res['def']:
        print()
        print(item1['pos'] + ':')
        print(item1['tr'][0]['text'])
        if 'syn' in item1['tr'][0]:
            for item2 in item1['tr'][0]['syn']:
                print(item2['text'])


def getEngTranslate(findWord):
    URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=" + yandexDictonaryKey + "&lang=en-ru&text=" + findWord + "&ui=ru"
    res = requests.get(URL).json()

    print(res)
    # examples
    print_examples(res)
    # syn
    print_syn(res)



getEngTranslate('walk')