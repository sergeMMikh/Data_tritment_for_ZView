import os
from cls.cls_ImpedanceData import ImpedanceData
from pprint import pprint


if __name__ == '__main__':
    # folder_path = input("Pleasu input all folder path:\t")

    folder_path = "B:\WorkInLab\Ba5Y2Al2Zr1-xCexO13\data_SM\Station_4_13.09.22_163836"

    print(f"Your folder_path is: {folder_path}")

    files_list = [files for root, dirs, files in os.walk(folder_path)][0]
    data_lst = list(filter(lambda file_name: "Impedarce.txt" in file_name, files_list))

    print(files_list)
    print(data_lst)

    file = f'{folder_path}\pump_Air_Cycle#_10_1_T_349C_Auto_start_Impedarce.txt'
    print(f'file: {file}')

    d_file = ImpedanceData()
    pprint(d_file.data_list)

