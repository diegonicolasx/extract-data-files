import glob
import os

def list_excel_files():
    dir = '/mnt/c/OENERGY Dropbox/1160-COMPARTIDO-AM/BEE/Cóndor/O&M Reports/2024/Monthly/01 January'
    excel_files_pattern = os.path.join(dir, '*.xlsx')
    excel_files = glob.glob(excel_files_pattern)        
    for excel_file in excel_files:
        print(excel_file)


