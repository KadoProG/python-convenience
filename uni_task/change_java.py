# HTML文→Javaのprintlnを実現
import pyperclip

# グリップボードのデータを入手
text = pyperclip.paste()
# "(ダブルクォーテーション)を'(シングルクォーテーション)に置換
text = text.replace('"', "'")
# 改行で区切って配列にする
text_re = text.split("\n")
text_result = ""
# 改行したものを java 書式の out.println("<h1 class='title'>あああ</h1>"); にして格納
for i in range(len(text_re)):
    tmp = 'out.println("' + text_re[i] + '");\n'
    text_result += tmp

pyperclip.copy(text_result)
