import os
import csv
from pathlib import Path
from string import Template
import shlex

def newSplit(value):
    lex = shlex.shlex(value)
    lex.quotes = '"'
    lex.whitespace_split = True
    lex.commenters = '#'
    return list(lex)


input_file_name = "E:/development/gitp/quran.co.com/assets/data/quran.v1.0.csv" #name/path of csv file
template_file_name = "E:/development/gitp/quran.co.com/themes/interface-hugo/archetypes/iaQuranAudio.md" #name/path of template file
output_file_name = "E:/development/gitp/quran.co.com/content/{}/audio-recitation/{}.md" #name/path of output file

language_list = ['en', 'fr', 'ar']

with open(template_file_name,"r", encoding="utf-8") as template_file:
    template = template_file.read()

for index, language in enumerate(language_list):
    recitor = "en_recitor"
    if(language == 'ar'):
        recitor = "ar_recitor"
    with open(input_file_name, encoding="utf8") as dataFile:
        reader = csv.DictReader(dataFile,delimiter=",")
        for row in reader:
            if(row["meaning_translation"] == "FALSE"):
                with open(output_file_name.format(language, row["identifier"].replace("_", "-")),"w", encoding="utf-8", newline='\n') as current_out:
                    current_out.write(template.format(title=row["{}_title".format(language)], keywords=newSplit(row["keywords"]), description=row["{}_title".format(language)], author=row[recitor], identifier=row["identifier"], playlist=row["identifier"],slug=row["{}_slug".format(language)]))