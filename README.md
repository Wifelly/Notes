# Notes

REST API сервис для хранения заметок

## Требования

* Python **версии 3.7 и выше**
* Flask **версии 1.1.1 и выше**

## Установка и запуск

### Используя Docker

1. Склонировать репозиторий:  
   `git clone https://github.com/Wifelly/Notes.git`

2. Перейти в рабочую дирректорию:
   `cd Notes`

3. Запустить сервис
   `docker-compose up`

### Без использования Docker

1. Склонировать репозиторий:  
   `git clone https://github.com/Wifelly/Notes.git`

2. Перейти в рабочую дирректорию:
   `cd Notes`

3. Установить необх. библиотеки:
   `python3 -m pip install -r requirements.txt`

4. Запустить сервис
   `flask run`

## P.S.
Т.к. Docker не поддерживает мою версию ubuntu (19.04), пришлось проектировать его "на коленке"  ¯\_(ツ)_/¯ 