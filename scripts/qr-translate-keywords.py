import os
from pathlib import Path
from googletrans import Translator

language_list = ['fr', 'ha', 'id', 'xxx', 'en', 'tr', 'ur', 'xxx', 'vi', 'ta', 'zh', 'te', 'ml', 'pt', 'uk', 'mg', 'it', 'hu', 'xxx', 'fa', 'hi', 'ku', 'az', 'xxx', 'ki', 'ln', 'ru', 'sd', 'sv']

translator = Translator()

text = 'Islam;Translation;Quran;Meanings'

for index, language in enumerate(language_list):
    if language != 'xxx':
        translator.translate(text , dest =language).text

