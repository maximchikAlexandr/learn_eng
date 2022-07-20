import requests, pprint

from  dct.service.config_yandex_dct import yandexDictonaryKey

def get_examples(response):
    res_dct = {}
    for pos in response['def']:
        key, values = pos['pos'], []
        for item in pos['tr']:
            if 'ex' in item:
                for example in item['ex']:
                    values.append(f"{example['text']} – {example['tr'][0]['text']}")
            if values: res_dct[key] = values

    return res_dct


def get_synonyms(response):
    res_dct = {}
    for pos in response['def']:
        key, values = pos['pos'], []
        values.append(pos['tr'][0]['text'])
        if 'syn' in pos['tr'][0]:
            for syn in pos['tr'][0]['syn']:
                values.append(syn['text'])
        if values: res_dct[key] = values
    return res_dct


def get_transcriprion(response):
    return response['def'][0].get('ts', '') if response['def'] else ''


def getEngTranslate(findWord):
    URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=" + yandexDictonaryKey + \
          "&lang=en-ru&text=" + findWord + "&ui=ru"
    res = requests.get(URL).json()

    return {'ts' : get_transcriprion(res),
            'tr' : get_synonyms(res),
            'ex' : get_examples(res)}
