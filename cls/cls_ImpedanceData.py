import os


class ImpedanceData:
    data_list = []
    raw_data_dict_list = []
    norm_data_dict_list = []

    def __init__(self, folder_path: str, file_name: str):
        self.file_name = file_name
        self.folder_path = folder_path
        with open(f'{folder_path}{self.file_name}', 'r') as d_file:
            self.data_list = d_file.readlines()

        print(f'self.data_list len: {len(self.data_list)}')

        self.make_data_dict()
        self.normalize_data()
        self.record_norm_data()

    def make_data_dict(self):
        self.raw_data_dict_list.clear()
        print(f'self.raw_data_dict_list len: {len(self.raw_data_dict_list)}')
        for line in self.data_list:
            d_list = line.split(',')
            d = {
                'frequency': d_list[0],
                'z': float(d_list[1]),
                'zz': float(d_list[2]),
                'a': float(d_list[3]),
                'b': float(d_list[4]),
            }

            self.raw_data_dict_list.append(d)

        print(f'self.raw_data_dict_list len: {len(self.raw_data_dict_list)}')

    def normalize_data(self):
        self.norm_data_dict_list.clear()
        null_idx = 0
        for i, line in enumerate(self.raw_data_dict_list):
            if line['zz'] <= 0.0:
                null_idx = i
                print(f'null_idx: {null_idx}')
                break

        for line in self.raw_data_dict_list[null_idx:]:
            d = {
                'frequency': line['frequency'],
                'z': float(line['z']) - self.raw_data_dict_list[null_idx]['z'],
                'zz': float(line['zz']),
                'a': float(line['a']),
                'b': float(line['b']),
            }
            self.norm_data_dict_list.append(d)

    def record_norm_data(self):

        path = f'{self.folder_path}normalized'
        if not os.path.isdir(path):
            print('Create directory "normalized" in you data folder.')
            os.mkdir(path)
        else:
            print('The directory "normalized" is present in you data folder.')

        new_name = f'{self.folder_path}\\normalized\\normalized_{self.file_name}'

        with open(new_name, 'w') as f:
            for line in self.norm_data_dict_list:
                f.writelines(f"{line['frequency']},{line['z']},{line['zz']},{line['a']},{line['b']}\n")
