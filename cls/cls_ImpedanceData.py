class ImpedanceData:
    raw_data_dict_list = []
    norm_data_dict_list = []

    def __init__(self, folder_path:str, file_name: str):
        self.file_name = file_name
        self.folder_path = folder_path
        with open(f'{folder_path}{self.file_name}', 'r') as d_file:
            self.data_list = d_file.readlines()

        self.make_data_dict()
        self.normalize_data()

    def make_data_dict(self):
        for line in self.data_list:
            d_list = line.split(',')
            d = {
                'frequency': d_list[0],
                'z':  float(d_list[1]),
                'zz': float(d_list[2])*-1,
            }

            self.raw_data_dict_list.append(d)

    def normalize_data(self):

        null_idx = 0
        for i, line in enumerate(self.raw_data_dict_list):
            if line['zz'] >= 0.0:
                null_idx = i
                print(f'null_idx: {null_idx}')
                break

        for line in self.raw_data_dict_list[null_idx:]:
            d = {
                'frequency': line['frequency'],
                'z': float(line['z']) - self.raw_data_dict_list[null_idx]['z'],
                'zz': float(line['zz']),
            }
            self.norm_data_dict_list.append(d)

    def record_norm_data(self):
        new_name = f'{self.folder_path}normalized_{self.file_name}'
        with open(new_name, 'w') as f:
            for line in self.norm_data_dict_list:
                f.writelines(f"{line['frequency']},{line['z']},{line['zz']}")


