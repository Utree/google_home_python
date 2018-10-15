# # pydubのインストール
# pip install pydub
# # ffmpegのインストール
# brew install ffmpeg --with-libvorbis --with-ffplay --with-theora
# pip install gTTS?


# Google Homeを探す用
import pychromecast
# Google Text-to-speechを使う用
from gtts import gTTS
# 音声ファイル編集用
from pydub import AudioSegment
# ハッシュ生成用
import hashlib
# 一時停止用
from time import sleep
# ファイル削除用
import os

# chromecastを探す
chromecasts = pychromecast.get_chromecasts()
# 入力
text = input("文字列を入力して下さい。：")
# ハッシュ生成
text_token = hashlib.md5(text.encode()).hexdigest()[-10:]
# mp3生成
tts = gTTS(text=text, lang='ja')
tts.save(<dir> + text_token + ".mp3")

# import mp3 file
origin = AudioSegment.from_mp3(<dir> + text_token + ".mp3")
# 音量を変える
loud_sound = origin + 20 # 音量を20dbだけ上げる
# mp3でエクスポート
loud_sound.export(<dir> + text_token + ".mp3")


# 一番最初に見つかったGoogleCast端末に決め打ち
print(chromecasts[0])
chromecasts[0].media_controller.play_media(<localhost_ip + text_token + ".mp3", "audio/mp3")

sleep(1)
#  使い終わったファイルは削除
os.remove(<dir> + text_token + ".mp3")
