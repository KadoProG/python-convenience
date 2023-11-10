# 22:09-23:39
# 22:09-23:39 90min と自動計算してくれるプログラム
# 複数行に対応、複数行の場合は時間を合算する処理がある

from datetime import datetime
import pyperclip

text = pyperclip.paste()
text_re = text.split("\n\n")

arr_min = []

def calc_time(time_range):
    # 入力文字列を分割して開始時間と終了時間に分ける
    start_time_str, end_time_str = time_range.split('-')

    # 時間文字列をdatetimeオブジェクトに変換
    format_str = "%H:%M"
    start_time = datetime.strptime(start_time_str, format_str)
    end_time = datetime.strptime(end_time_str, format_str)

    # 時間の差を計算して経過時間（分）を取得
    time_difference = end_time - start_time
    elapsed_minutes = time_difference.total_seconds() / 60
    return int(elapsed_minutes)
    # print(f"経過時間（分）: {int(elapsed_minutes)} 分")


time_sum = 0

result_text = ""

for te in text_re:
    min = calc_time(te.split(" ")[0])
    text_other = ""
    for childNo in range(1, len(te.split(" "))):
        text_other += te.split(" ")[childNo]
        
    time_sum += min
    arr_min.append(min)
    re_te = te.split(" ")[0] + " " + str(min) + "min"  # " + te.split(" ")[1]
    result_text += re_te + " "+ text_other + "\n\n"

result_text += "+".join([f'{num}'for num in arr_min]) + "=" + str(time_sum) + "min"
result_text +=" " + str(int(time_sum / 60)) + "h" + str(int(time_sum % 60)) + "min"

print(result_text)


# pyperclip.copy(result_text)
