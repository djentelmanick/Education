import os

from dotenv import load_dotenv

load_dotenv()

GITLAB_KEY = os.getenv("GITLAB_KEY")
GITLAB_API_URL = os.getenv("GITLAB_API_URL")

TEMPLATE_PATH = "./templates/index.html"
INDEX_PATH = "./public/index.html"
