from dotenv import load_dotenv
load_dotenv()

import os

API_HOST = os.environ.get("API_HOST", "你的host地址")  # 建议在环境变量中设置API_HOST
API_KEY = os.environ.get("API_KEY", "你的API密钥")    # 建议在环境变量中设置API_KEY
DEFAULT_ID = os.environ.get("DEFAULT_ID", "101280606")  # 默认龙岗区，可自定义