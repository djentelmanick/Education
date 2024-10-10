import zulip
import requests

from jinja2 import Template
from src.config import GITLAB_KEY, GITLAB_API_URL, GITHUB_KEY, GITHUB_NAME, TEMPLATE_PATH, INDEX_PATH


def get_zulip_info():
    """Получаем информацию из Zulip"""
    # Получаем информацию о пользователе согласно документации
    client = zulip.Client(config_file="zuliprc")
    result = client.get_profile()

    return result


def get_gitlab_info():
    """Получаем информацию о проектах из gitlab"""
    # Создаем настройки для подходящего запроса
    params = {"owned": True}
    headers = {"PRIVATE-TOKEN": GITLAB_KEY}

    # Делаем запрос
    result = requests.get(url=GITLAB_API_URL, params=params, headers=headers)

    return result.json()


def get_github_info():
    """Получаем информацию о проектах из github"""
    # Создаем настройки для подходящего запроса
    headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer: {GITHUB_KEY}",
               "X-GitHub-Api-Version": "2022-11-28"}
    url = f'https://api.github.com/users/{GITHUB_NAME}/repos'

    # Делаем запрос
    result = requests.get(url=url, headers=headers)
    return result.json()


def generate_resume():
    """Генерация нового файла резюме"""
    zulip_person_info = get_zulip_info()
    # gitlab_person_info = get_gitlab_info()
    github_person_info = get_github_info()
    print(github_person_info)
    
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as template_file:
        template_text = template_file.read()
        template = Template(template_text)
        render_file = template.render(
            name=zulip_person_info,
            email=zulip_person_info["email"],
            projects=github_person_info
        )
        with open(INDEX_PATH, "w", encoding="utf-8") as index:
            index.write(render_file)
      
            
def get_resume():
    """Получение текущего файла резюме"""
    with open(INDEX_PATH, "r", encoding="utf-8") as index:
        return index.read()
