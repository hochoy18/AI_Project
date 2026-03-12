from dotenv import load_dotenv
import os

# 加载 .env 文件（默认在当前目录查找）
load_dotenv()
# 火山引擎
ARK_API_KEY = os.getenv('ARK_API_KEY')
ARK_BASE_URL = os.getenv('ARK_BASE_URL')

