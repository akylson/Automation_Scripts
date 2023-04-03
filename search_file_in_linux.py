# Assignment:
# Write a simple script to find a file in the filesystem. , let say you are searching for file /etc/hosts in your system.
# BONUS

# Try to make your script user-friendly so that it will accept arguments like the path to search(e.g.,/etc.) and then filename(, hosts) on the command line.
# Hint: You need to use argparse module for that

# I am looking forward to you guys joining the amazing journey.


import os

# получаем путь к домашней директории текущего пользователя
home_dir = os.path.expanduser("~")
print("Find files in Linux system:")

# запрашиваем у пользователя имя файла
filename = input("filename: ")

# запрашиваем у пользователя тип поиска
filetype = input("select one of two search types: exact name (exact) or similar (similar): ")

# выполняем поиск файла
for root, dirs, files in os.walk("/"):
    for f in files:
        if f == filename and os.path.isfile(os.path.join(root, f)):
            print(os.path.join(root, f))
        elif filetype == "similar" and filename in f and os.path.isfile(os.path.join(root, f)):
            print(os.path.join(root, f))
        elif filetype != "exact" and filetype != "similar":
            print("select one of two search types: exact name (exact) or similar (similar)")