# Название проекта

Программа для заполнения резюме по информации, полученной из API

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://git.miem.hse.ru/biv23x-ps/dakaznacheev
    ```
   
2. Перейти в директорию проекта:

    ```bash
    cd ваш_проект
    ```

4. Cоздайте виртуальное окружение

    ```bash
    python3 -m venv venv
    ```

5. Активируйте виртуальное окружение

    - Unix

    ```bash
    source venv/bin/activate
    ```

    - Windows

    ```
    venv\Scripts\activate
    ```

3. Установить зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Заполните данные в .env

    ```bash
    GITLAB_KEY = {your personal acces token}
    GITLAB_API_URL = https://git.miem.hse.ru/api/v4/projects
    ```

## Использование

    ```bash
    python main.py
    ```

## Роуты

    - /
    Получение текущего резюме с отображением html файла

    - /generate_resume [POST, PUT]
    Генерация резюме с актуальной информацией

