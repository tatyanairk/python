# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def script1():

	for i in range(1, 10):
	path = os.path.join(os.getcwd(), "dir_" + str(i))

	try:
		return os.mkdir(path)
		print("успех!")

	except FileExistsError:
    print("имя занято :(")

def script2():

    try:
    for i in range(1, 10):
        return os.rmdir("dir_" + str(i)
        print("успех!")

    except:
    	print("уже удалили :)")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def script3():
	
	lst = os.listdir()

	for i in lst:
		lst.append(i)
	print(lst)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def script4():

	return shutil.copy(r'easy.py')