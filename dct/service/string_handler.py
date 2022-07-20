import re

from dct.service.parser_yandex_api import getEngTranslate


def get_unic_words(text: str) -> list:
    clean_text = re.sub('[^a-zA-Z]', ' ', text).lower()
    return sorted(set(clean_text.split()))

def get_test_text() -> list:
    # with open('E:\YandexDisk\Python\projects\learn_eng\dct\service\text.txt', 'r') as infile:
    #     text = infile.read()
    text = '''
    Bootstrap 5 is evolving with each release to better utilize CSS variables for global theme styles, individual components, and even utilities. 
    We provide dozens of variables for colors, font styles, and more at a :root level for use anywhere. 
    On components and utilities, CSS variables are scoped to the relevant class and can easily be modified.
    '''

    return {word : getEngTranslate(word) for word in get_unic_words(text)}


