import os
from pprint import pprint

from cls.cls_ImpedanceData import ImpedanceData

if __name__ == '__main__':
    # folder_path = input("Input all folder path:\t")

    folder_path = "B:\WorkInLab\Ba5Y2Al2Zr1-xCexO13\data_SM\Station_4_13.09.22_163836"

    print(f"Your folder_path is: {folder_path}")

    files_list = [files for root, dirs, files in os.walk(folder_path)][0]
    data_lst = list(filter(lambda file_name: "Impedarce.txt" in file_name, files_list))

    print('All files in your data folder:')
    pprint(files_list)
    print('\nImpedance data files:')
    pprint(data_lst)

    folder_path = folder_path + "\\"
    # file = "pump_Air_Cycle#_10_1_T_349C_Auto_start_Impedarce.txt"

    for file in data_lst:
        print(f'file: {file}')
        d_file = ImpedanceData(folder_path, file)
        print(f'raw_data_dict_list len: {len(d_file.raw_data_dict_list)}')
        print(f'raw_data_dict_list len: {len(d_file.norm_data_dict_list)}')
