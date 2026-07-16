import os


BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
API_URL = "https://api.siliconflow.cn/v1/chat/completions"
API_KEY = "sk-cwbbcrgirsvtcbhnvyompslhmkzflknzgmwqtjtukjeoqofa"
MODEL_NAME = "deepseek-ai/DeepSeek-V4-Flash"
DATA_UPDATE_DATE = "2026-07-14"
KNOWLEDGE_FILES = {
    "新生入学": "01_新生入学.md",
    "办事流程": "02_办事流程.md",
    "电话黄页": "03_电话黄页.md",
    "应急防骗": "04_应急防骗.md",
}
