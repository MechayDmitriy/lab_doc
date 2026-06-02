import os
import sys
import hashlib

#функция получения хеш-кода файла
def get_hash(file_path):
    hash_func = hashlib.new('sha1')
    with open(file_path,'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

try:
    main_dir_name = sys.argv[1]
    #Изменение рабочей директории
    os.chdir(main_dir_name)
except:
    print("Ошибка: Нет каталога или каталог указан неверно!")
    exit()

all_files = []

#Получение всех файлов из всех подкаталогов
for root, dirs, files in os.walk("."):
    for file in files:
        all_files.append(os.path.join(root,file))

dict_files = {}

#Получение словаря, ключ = уникальный хеш, значение = список файлов этого хеша
for file in all_files:
    file_hash = get_hash(file)
    if file_hash in dict_files:
        dict_files[file_hash].append(file)
    else:
        dict_files[file_hash] = [file]

#Основной цикл, перебор словаря
for key in dict_files:
    if len(dict_files[key]) > 1:

        print("> Найдены одинаковые файлы:")

        files = (dict_files[key])
        files.sort()

        for i in range(len(files)):
            print(f"{i+1}) {files[i]}")

        print("> Выберите номер файла, который хотите сохранить или 0, если хотите пропустить")
        while True:
            try:
                number = int(input(">>> "))
            except:
                print("> Неизвестный номер!")
                continue
            print("")

            if number == 0:
                break
            elif number < 0 or number > (len(files)):
                print("> Неизвестный номер!")
                continue
            else:
                number -= 1
                print(f"> Файл {files[number]} сохранён")
                
                for i in range(len(files)):
                    if i != number:
                        os.remove(files[i])
                print("> Остальные файлы удалены\n")
                break

print("Программа завершает работу")
            