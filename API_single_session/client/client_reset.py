import requests
from PIL import Image
from io import BytesIO

# 送信するPIL形式の画像データ
image_file_path = '00016-331097358.png'
# FastAPIエンドポイントのURL
url = 'http://0.0.0.0:8001/reset/'  # FastAPIサーバーのURLに合わせて変更してください
# POSTリクエストを送信
response = requests.post(url)
# レスポンスを表示     return {"message": "Image received ","chatbot": chatbot}
if response.status_code == 200:
    result = response.json()
    print("サーバーからの応答message:", result.get("message"))
    print("サーバーからの応答message:", result.get("key"))
else:
    print("リクエストが失敗しました。ステータスコード:", response.status_code)
