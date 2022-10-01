import re
from datetime import datetime

import requests

from config import yandexDictonaryKey

def get_unic_words(text: str) -> list:
    clean_text = re.sub('[^a-zA-Z]', ' ', text).lower()
    return sorted(set(clean_text.split()))

def _get_examples(response):
    res_dct = {}
    for pos in response['def']:
        if 'pos' in pos:
            key, values = pos['pos'], []
            for item in pos['tr']:
                if 'ex' in item:
                    for example in item['ex']:
                        values.append(f"{example['text']} – {example['tr'][0]['text']}")
                if values: res_dct[key] = values

    return res_dct


def _get_synonyms(response):
    res_dct = {}
    for pos in response['def']:
        if 'pos' in pos:
            key, values = pos['pos'], []
            values.append(pos['tr'][0]['text'])
            if 'syn' in pos['tr'][0]:
                for syn in pos['tr'][0]['syn']:
                    values.append(syn['text'])
            if values: res_dct[key] = values
    return res_dct


def _get_transcriprion(response):
    return response['def'][0].get('ts', '') if response['def'] else ''


def getEngTranslate(findWord) -> dict:
    URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=" + yandexDictonaryKey + \
          "&lang=en-ru&text=" + findWord + "&ui=ru"
    res = requests.get(URL).json()

    return {'text' : findWord,
            'ts' : _get_transcriprion(res),
            'tr' : _get_synonyms(res),
            'ex' : _get_examples(res)}


def sec_to_datetime(sec: int) -> str:
    return datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M')


def get_dct_words(pagination):
    words = pagination.items
    res = [
        { 'id' : wrd.id,
            'text' : wrd.eng_word,
            'ts' : wrd.ts,
            'tr' : [{pos.pos : [tr.rus_word for tr in wrd.translated_words if pos == tr.pos]} for pos in set(tr.pos for tr in wrd.translated_words)],
            'ex' : [{pos.pos : [ex.example for ex in wrd.examples if pos == ex.pos] } for pos in set(ex.pos for ex in wrd.examples)]}
        for wrd in words]
    return res
