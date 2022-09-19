class ImpedanceData:

    def __int__(self, file_name: str):
        print(f'ImpedanceData file_name:{file_name}')
        with open(file_name, 'r') as d_file:
            # self.data_list.append(t_file.read().readline())
            self.data_list = d_file.readlines()
