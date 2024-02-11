import requests
from PIL import Image
from io import BytesIO


def save_image_from_url(url):
    try:
        # 画像をダウンロードしてメモリ上に取得
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)

        # メモリ上の画像を開いて表示
        img = Image.open(img_data)
        img.show()

    except Exception as e:
        print(f"エラーが発生しました: {e}")


# 画像を保存したいURLと保存先のパスを指定

videoId = "F0dnw3zvack"  # ここにYouTubeVideoIdを入力すると、字幕が取得できる
image_url = "https://img.youtube.com/vi/" + videoId + "/maxresdefault.jpg"

# 関数を呼び出して画像を保存

save_image_from_url(image_url)
