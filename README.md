# Создание своего резюме с проектами из GitHub

Программа для заполнения резюме по информации, полученной из API

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/djentelmanick/Education
    ```
   
2. Перейти в директорию проекта:

    ```bash
    cd ваш_проект
    ```

3. Cоздайте виртуальное окружение

    ```bash
    python3 -m venv venv
    ```

4. Активируйте виртуальное окружение

    - Unix

    ```bash
    source venv/bin/activate
    ```

    - Windows

    ```bash
    venv\Scripts\activate
    ```

5. Установить зависимости:

    ```bash
    pip install -r requirements.txt
    ```

6. Заполните данные в .env

    ```bash
    GITHUB_KEY = {your personal acces token}
    GITHUB_NAME = 
    ```

## Использование

```bash
python main.py
```

## Роуты

    - /
    Получение текущего резюме с отображением html файла

    - /generate_resume
    Генерация резюме с актуальной информацией

## Для деплоя

1. Откройте Docker Desktop.

2. Перейдите в каталог, содержащий ваш файл docker-compose.yml.

3. Выполните следующую команду для запуска контейнеров, описанных в файле docker-compose.yml:

    ```bash
    docker-compose up --build
    ```
