import os
from pprint import pprint

from cls.cls_ImpedanceData import ImpedanceData

if __name__ == '__main__':

    folder_path = input("Input all folder path:\t")

    files_list = [files for root, dirs, files in os.walk(folder_path)][0]
    print('\nAll files in your data folder:')
    pprint(files_list)

    suffix = input("""\nInput a keyword for data file filtration or """
                   """use 'd' to use default 'Impedarce.txt' or """
                   """use 'n' to use all files: \t""")

    if suffix == 'd':
        suffix = "Impedarce.txt"
    elif suffix == 'n':
        suffix = ".txt"
    else:
        pass

    # Find impedance text data."
    data_lst = list(filter(lambda file_name: suffix in file_name, files_list))

    print('\nImpedance data files:')
    pprint(data_lst)

    folder_path = folder_path + "\\"

    if not len(data_lst):
        print('No impedance data files found.')
    else:
        print('Impedance data files will be recorded to folder "Impedance"')

        print('new data files will be recorded to folder "normalized"')

        # Take data from folder according impedance data list and normalize it.
        for file in data_lst:
            print(f'file: {file}')
            d_file = ImpedanceData(folder_path, file)
            print(f'raw_data_dict_list len: {d_file.make_data_dict()}')
            print(f'norm_data_dict_list len: {d_file.normalize_data()}')
            print()
            d_file.record_raw_data()
            d_file.record_norm_data()

