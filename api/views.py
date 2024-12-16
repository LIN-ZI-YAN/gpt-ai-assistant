from django.http import HttpResponse
from .services.line_bot_service import handler

def line_webhook(request):
    # 從 LINE 請求中取得簽名與 body
    signature = request.headers['X-Line-Signature']
    body = request.body.decode('utf-8')

    # 驗證簽名並處理訊息
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
    return HttpResponse(status=200)
