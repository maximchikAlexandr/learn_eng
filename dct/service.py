import re
from datetime import datetime

import requests

from config import yandexDictonaryKey


def get_unic_words(text: str) -> list:
    clean_text = re.sub('[^a-zA-Z]', ' ', text).lower()
    return sorted(set(clean_text.split()))


def sec_to_datetime(sec: int) -> str:
    return datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M')


def _get_response(findWord):
    URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=" + yandexDictonaryKey + \
          "&lang=en-ru&text=" + findWord + "&ui=ru"
    return requests.get(URL).json()


class Traslation:

    def __init__(self, word):
        self.__word = word
        self.__response = _get_response(word)

    def parsing_response(self):
        return {'text': self.__word,
                'ts': self._get_transcription(),
                'tr': self._get_synonyms(),
                'ex': self._get_examples()}

    def _get_examples(self):
        res_dct = {}
        for pos in self.__response['def']:
            if 'pos' in pos:
                key, values = pos['pos'], []
                for item in pos['tr']:
                    if 'ex' in item:
                        for example in item['ex']:
                            values.append(f"{example['text']} – {example['tr'][0]['text']}")
                    if values: res_dct[key] = values
        return res_dct

    def _get_synonyms(self):
        res_dct = {}
        for pos in self.__response['def']:
            if 'pos' in pos:
                key, values = pos['pos'], []
                values.append(pos['tr'][0]['text'])
                if 'syn' in pos['tr'][0]:
                    for syn in pos['tr'][0]['syn']:
                        values.append(syn['text'])
                if values: res_dct[key] = values
        return res_dct

    def _get_transcription(self):
        return self.__response['def'][0].get('ts', '') if self.__response['def'] else ''
