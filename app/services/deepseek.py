import os
from loguru import logger
from deepseek import DeepSeekClient  # 假设 deepseek 提供了这类客户端

async def chat_with_deepseek(messages: list[dict], callback=None):
    base_url = os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com/v1')
    model = os.getenv('DEEPSEEK_MODEL', 'deepseek-chat')  # 需要根据实际修改
    api_key = os.getenv('DEEPSEEK_API_KEY')

    deepseek_client = DeepSeekClient(base_url, api_key)

    logger.debug(f"chat with deepseek: {base_url}, model: {model}")

    response = await deepseek_client.chat(
        model=model,
        messages=messages,
        stream=True
    )

    full_content = ""
    for chunk in response:
        content = chunk['content']  # 假设返回内容是这样
        if callback:
            await callback(content)
        full_content += content
    return full_content
