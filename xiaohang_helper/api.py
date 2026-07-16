import requests

from config import API_KEY, API_URL, MODEL_NAME
from prompts import ALIASES, IDENTITY_PROMPTS, SAFETY_RULES


def call_api(question, identity, knowledge):
    if not API_KEY:
        return "当前未配置 SILICONFLOW_API_KEY。你可以先测试页面交互和电话黄页展示；配置好 API Key 后再测试智能问答。"

    system_prompt = f"""你是郑州航空工业管理学院的校园信息查询助手。

{IDENTITY_PROMPTS[identity]}

{ALIASES}

{SAFETY_RULES}

【学校资料】
{knowledge}

请基于以上资料回答用户问题，严格遵守防幻觉规则。"""

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    }

    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if "choices" in result:
                return result["choices"][0]["message"]["content"]
            return f"API返回错误：{result.get('error', '未知错误')}"
        return f"API调用失败，状态码：{response.status_code}"
    except requests.exceptions.Timeout:
        return "请求超时，请稍后再试"
    except Exception as e:
        return f"调用出错：{e}"
