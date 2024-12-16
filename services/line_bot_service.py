from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai

# LINE Bot 初始化
line_bot_api = LineBotApi('YOUR_LINE_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_LINE_CHANNEL_SECRET')

# OpenAI 初始化
openai.api_key = 'YOUR_OPENAI_API_KEY'

# 處理 LINE 訊息並轉發到 OpenAI
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text  # 使用者傳送的訊息

    # 呼叫 OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    reply_message = response['choices'][0]['message']['content']

    # 回覆 LINE 使用者
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message)
    )
