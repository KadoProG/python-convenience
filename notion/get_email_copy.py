# 研究室のEMAIL一覧を全て取得【Notion API取得（自分専用）】
import os
from dotenv import load_dotenv
import requests

# .envファイルの内容を読み込見込む
load_dotenv()

database_id = os.environ['NOTION_DATABASE_ID']
token = os.environ["NOTION_TOKEN"]

url = "https://api.notion.com/v1/databases/" + "cff5e8e3016e43dc9549e472067877c2"+ "/query/"

# os.environを用いて環境変数を表示させます
print(os.environ['NOTION_DATABASE_ID'])

print(url)

# 送信するデータ（JSON形式）
data = {}


# カスタムヘッダーを定義
headers = {
    "User-Agent": "MyApp/1.0",  # ユーザーエージェント情報
    "Authorization": "Bearer " + token,  # 認証トークンなど
    "Content-type": "application/json",
    "Notion-Version": "2021-08-16",
}

# POSTリクエストを送信
response = requests.post(url, json=data, headers=headers)

# レスポンスを取得
if response.status_code == 200:  # ステータスコードが200（成功）の場合
    result = response.json()  # JSONレスポンスをPythonデータに変換

else:
    print("リクエストが失敗しました。ステータスコード:", response.status_code)
    print(response.text)  # エラーメッセージなどの詳細を表示
    exit()

print("【メール一覧】" + str(len(result["results"]))+"\n")

for row in result["results"]:
    print(row["properties"]["メール"]["email"])
    # print(row["properties"])
print("\n")
