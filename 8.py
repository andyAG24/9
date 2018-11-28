
import os
import glob
import subprocess 

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

# __name__ = input('Введите строку: ')


os.chdir(migrations)
current_directory = os.getcwd()

def search_line_in_all_files(line_entered):
    line_for_check = ''.join(line_entered.split())
    res_list = list()
    count = 0
    file_list = list()
    for filename in glob.glob('*.sql'):
        file_list.append(filename)
    print(len(file_list))
    i = 0
    while i < len(file_list) - 1:
        with open(file_list[i]) as f:
            for line in f:
                line_1 = ''.join(f.read().split())
                if line_for_check in line_1:
                    res_list.append(filename)
                    count += 1
        i += 1
    print(res_list)
    print('Кол-во файлов: {}'.format(count))

while True:
    command = str(input('Введите значение для поиска: '))
    search_line_in_all_files(command)