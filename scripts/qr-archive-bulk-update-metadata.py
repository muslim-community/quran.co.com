import os
import csv
from pathlib import Path
from internetarchive import modify_metadata

input_file_name = "E:/development/gitp/quran.co.com/assets/data/quran.v1.0.csv"  # name/path of csv file

id_list = [
    "Mishary_Alafasy_Quran"
]

with open(input_file_name, encoding="utf8") as dataFile:
    reader = csv.DictReader(dataFile, delimiter=",")
    for line in reader:
        if line["identifier"] in id_list:
            r = modify_metadata(
                line["identifier"],
                metadata=dict(
                    title=line["title"],
                    description=line["description"],
                    subject=line["keywords"],
                    creator=line["ar_reciter"],
                    reciter_english=line["en_reciter"],
                    source=line["source"],
                    uploaded_by=line["uploaded_by"],
                    recitation=line["en_recitation"],
                    method=line["en_method"],
                    arabic_recitation=line["ar_recitation"],
                    arabic_method=line["ar_method"],
                    translation_language_english=line["translation_language_english"],
                    translation_language=line["translation_language"],
                    translation_version=line["translation_version"],
                    translation_reciter=line["translation_reciter"],
                    meaning_translation=line["meaning_translation"],
                    Title_amharic=line["am_title"],
                    Title_arabic=line["ar_title"],
                    Title_bengali=line["bn_title"],
                    Title_chinese=line["zh_title"],
                    Title_english=line["en_title"],
                    Title_french=line["fr_title"],
                    Title_indonesian=line["id_title"],
                    Title_pashto=line["ps_title"],
                    Title_persian=line["fa_title"],
                    Title_russian=line["ru_title"],
                    Title_turkish=line["tr_title"],
                    Title_urdu=line["ur_title"],
                    Title_uyghur=line["ug_title"],
                ),
            )
            print("Status code for : " + line["identifier"] + " : " + str(r.status_code) + " : " + str(r.reason))
