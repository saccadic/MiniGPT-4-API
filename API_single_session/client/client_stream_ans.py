import requests
from PIL import Image
from io import BytesIO
import json
# 送信するデータを準備
data = {
    "temperature": 0.6,
}
# FastAPIエンドポイントのURL
url = 'http://0.0.0.0:8001/get_stream/'  # FastAPIサーバーのURLに合わせて変更してください
# POSTリクエストを送信
response = requests.post(url, json=data)
# レスポンスを表示 return {"message": "ask_completed ","chatbot":chatbot}
if response.status_code == 200:
    result = response.json()
    print("サーバーからの応答message:", result.get("message"))
    print("サーバーからの応答chatbot:", result.get("chatbot"))
    print("サーバーからの応答html_txt:", result.get("html_txt"))
    print("サーバーからの応答text:", result.get("text"))
else:
    print("リクエストが失敗しました。ステータスコード:", response.status_code)

