from PIL import Image
import pytesseract

# Tesseractの実行ファイルのパスを指定（デフォルトの場合）
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"


def image_to_text(image_path):
    # 画像を開く
    image = Image.open(image_path)

    # 画像をテキストに変換
    text = pytesseract.image_to_string(image)

    return text


# 画像ファイルのパスを指定
image_path = "./test.png"

# 画像をテキストに変換
result_text = image_to_text(image_path)

# 結果を表示
print(result_text)
