import os
import glob
import subprocess 

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(migrations)
current_directory = os.getcwd()

def search_line_in_all_files(line_entered, file_list):
    file_list_1 = list(file_list)
    line_for_check = ''.join(line_entered.split())
    count = 0
    res_list = list()
    # print(type(file_list_1))
    i = 0
    print(len(file_list_1))
    while i < len(file_list_1) - 1:
        with open(file_list_1[i]) as f:
            for line in f:
                line_1 = ''.join(f.read().split())
                if line_for_check in line_1:
                    res_list.append(filename)
                    count += 1
        i += 1
    print(res_list)
    print('Кол-во файлов: {}'.format(count))
    return res_list

if __name__ == "__main__":
       
    migrations_list = list()
    for filename in glob.glob('*.sql'):
        migrations_list.append(filename)

    while True:
        result_list = search_line_in_all_files(input('Введите строку для поиска: '), migrations_list)
        # print(type(result_list))
        migrations_list = list(result_list)
        
        if not(len(migrations_list)):
            break

