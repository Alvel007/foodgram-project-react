# Cервис Foodgram - продуктовый помощник

## Описание 

Проект «Фудграм» — дипломный проект Яндекс Практикума. Сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов.

Проект доступен по [адресу](http://fooodgrams.duckdns.org/)

Данные для входа администратора:   
    ```bash
    ad@min.ru
    admin
    ```
Данные для входа тестового пользователя:   
    ```bash
    alex@alex.ru
    147qw741
    ```

## Установка

1. Клонируйте репозиторий на свой компьютер.

    ```bash
    git clone git@github.com:<ВАШ_USERNAME_GITHUB>/foodgram-project-react.git
    ```
    ```bash
    cd foodgram-project-react
    ```
2. Создайте файл .env в папке infra и заполните его своими данными. Перечень данных указан в корневой директории проекта в файле .env.example.

3. Находясь в папке infra, выполните команду ```docker-compose up```  
Документация к API доступна по адресу http://localhost/api/docs/ 

### Создание Docker-образов

1.  Создаём образы для установки на сервер. Замените username на ваш логин на DockerHub:

    ```bash
    cd ..
    docker build -t username/foodgram_backend:latest backend/
    docker build -t username/foodgram_frontend:latest frontend/
    ```

2. Загрузите образы на DockerHub:

    ```bash
    docker push username/foodgram_frontend
    docker push username/foodgram_backend
    ```

### Деплой на сервере

1. Подключитесь к удаленному серверу

    ```bash
    ssh -i путь_до_файла_с_SSH_ключом/название_файла_с_SSH_ключом имя_пользователя@ip_адрес_сервера 
    ```

2. Создайте на сервере директорию foodgram через терминал

    ```bash
    mkdir foodgram
    ```

3. Установка docker compose на сервер:

    ```bash
    sudo apt update
    sudo apt install curl
    curl -fSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh
    sudo apt-get install docker-compose-plugin
    ```

4. В директорию foodgram/ скопируйте файлы docker-compose.production.yml и .env:

    ```bash
    scp -i path_to_SSH/SSH_name docker-compose.production.yml username@server_ip:/home/username/foodgram/docker-compose.production.yml
    * path_to_SSH — путь к файлу с SSH-ключом;
    * SSH_name — имя файла с SSH-ключом (без расширения);
    * username — ваше имя пользователя на сервере;
    * server_ip — IP вашего сервера.
    ```

5. Запустите docker compose в режиме демона:

    ```bash
    sudo docker compose -f docker-compose.production.yml up -d
    ```

6. Выполните миграции, соберите статические файлы бэкенда и скопируйте их в /static/:

    ```bash
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations recipes
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations users
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic --no-input
    sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /static/
    ```
    Создайте администратора:

    ```bash
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
    ```
    Заполните базу данных:
    ```bash
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py load_ingredients
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py load_tags
    ```

7. На сервере в редакторе nano откройте конфиг Nginx:

    ```bash
    sudo nano /etc/nginx/sites-enabled/default
    ```

8. Измените настройки location в секции server:

    ```bash
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
    ```

9. Проверьте работоспособность конфига Nginx:

    ```bash
    sudo nginx -t
    ```
    Если ответ в терминале такой, значит, ошибок нет:
    ```bash
    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful
    ```

10. Перезапускаем Nginx
    ```bash
    sudo systemctl reload nginx
    ```

### Настройка CI/CD

1. Файл workflow уже написан. Он находится в директории

    ```bash
    foodgram/.github/workflows/main.yml
    ```

2. Для адаптации его на своем сервере добавьте секреты в GitHub Actions:

    ```bash
    DOCKER_USERNAME                # имя пользователя в DockerHub
    DOCKER_PASSWORD                # пароль пользователя в DockerHub
    HOST                           # ip_address сервера
    USER                           # имя пользователя
    SSH_KEY                        # приватный ssh-ключ (cat ~/.ssh/id_rsa)
    SSH_PASSPHRASE                 # кодовая фраза (пароль) для ssh-ключа

    TELEGRAM_TO                    # id телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
    TELEGRAM_TOKEN                 # токен бота (получить токен можно у @BotFather, /token, имя бота)
    ```

<br>

## Автор:
Кирилишин Алексей  
(alexkak@inbox.ru)