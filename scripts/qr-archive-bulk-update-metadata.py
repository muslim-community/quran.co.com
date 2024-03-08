import os
import csv
from pathlib import Path
from internetarchive import modify_metadata

id_list = ['yasser_alqorashi_mp3_quran', 'Abdulbaset_abdulsamad_with_naeem_sultan_pickthallTranslation_mp3_quran', 'Abdullah_Basfar_with_Ibrahim_Walk_Saheeh_Intl_English_Translation', 'Al-tablawi_MP3_Quran', 'Mishari_al-Afasy_with_Saabir_Muhsin_Khan_English_Translation', 'Muhammad_ayyub_with_mikaal_waters_muhsinKhan_english_translation', 'OifyHfPiyfOug', 'Saud_al-shuraim_with_abdulrahman_alsudaesurduTranslation_mp3_quran', 'Shakir_Qasami_with_Aslam_Athar_Pickthall_Translation', 'SudaisAndShuraymWithAslamAtharpickthallTranslation', 'Sudais_and_Shuraym_with_Naeem_Sultan_Pickthall_English_Translation', 'la_traduction_des_sens_du_coran_en_francais']

with open( 'E:/development/gitp/qurand.com/data-ext/archive-audio.csv', encoding="utf8") as dataFile:
    reader = csv.DictReader(dataFile,delimiter=";")
    for line in reader:
        if line['identifier'] in id_list:
            r = modify_metadata(line['identifier'], metadata=dict(description=line['description']))
            print('Status code for : ' + line['identifier'] + ' : ' + str(r.status_code))
        
