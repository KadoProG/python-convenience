from youtube_transcript_api import YouTubeTranscriptApi

url = "F0dnw3zvack"  # ここにYouTubeのリンク？を入力すると、字幕が取得できる

transcript_list = YouTubeTranscriptApi.list_transcripts(url)

text = ""
for transcript in transcript_list:
    for tr in transcript.fetch():
        # {'text': '字幕のテキスト情報', 'start': 字幕の開始時間,
        # 'duration': 字幕が表示されている時間 }
        print(tr["text"])
        text += tr["text"]
