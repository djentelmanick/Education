import os

from dotenv import load_dotenv

load_dotenv()

GITLAB_KEY = os.getenv("GITLAB_KEY")
GITLAB_API_URL = os.getenv("GITLAB_API_URL")
GITHUB_KEY = os.getenv("GITHUB_KEY")
GITHUB_NAME = os.getenv("GITHUB_NAME")

TEMPLATE_PATH = "./templates/index.html"
INDEX_PATH = "./public/index.html"
