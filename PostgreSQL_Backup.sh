#!/bin/bash

# Указываем параметры для подключения к базе данных
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="acweb"
DB_USER="yourusername"
DB_PASSWORD="yourpassword"

# Создаем директорию для хранения бэкапов
BACKUP_DIR="/path/to/backup/directory"
mkdir -p ${BACKUP_DIR}

# Определяем имя бэкапа
BACKUP_NAME="acweb_$(date +%Y%m%d%H%M%S).backup"

# Создаем резервную копию базы данных
pg_dump -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER} -F c -b -v -f ${BACKUP_DIR}/${BACKUP_NAME} ${DB_NAME}

# Удаляем старые бэкапы (оставляем только последние 7)
cd ${BACKUP_DIR}
ls -t | grep acweb | tail -n +8 | xargs rm -f




#### CRONTAB 0 3 * * 5 /path/to/backup/script.sh
