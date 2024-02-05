import streamlit as st
import requests
import openai
from audio_recorder_streamlit import audio_recorder

#$streamlit run .\PictureBot.py
#で実行


#変数（streamlitでは変数の変更ができないため）
if 'count' not in st.session_state:
    st.session_state["count"] = 0

#タイトル
st.title("PictureBot")
#API Keyの入力欄
api = st.sidebar.text_input("API-KEY",type = "password")

#画像を生成する関数
def createImage(prompt,style,count):
    response=openai.Image.create(
      prompt=prompt+","+style,
      n=1,
      size="1024x1024"
    )
    image_url=response["data"][0]["url"]
    image_data = requests.get(image_url).content
    with open(f"generatedImage{count}.jpg", "wb") as f:
        f.write(image_data)
    col = st.columns(count)
    for i in range(count):
        with col[i]:
            st.header(f"画像{i+1}")
            st.image(f"generatedImage{i+1}.jpg", use_column_width=True)

#API Keyの設定
if api:
    openai.api_key = api
else:
    st.error("No API found")

#画風の選択リスト
styleList=["リアル","ドット絵(Pixel art)","5歳児のクレヨン","葛飾北斎","モノクロ"]

# 音声入力を使う時
audio_bytes = audio_recorder(text="音声入力>>")
if audio_bytes:
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_bytes)
    st.audio(audio_bytes, format="audio/wav")
    audio_file = open("recorded_audio.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    text = transcript.text
else:  # 音声を使ってない場合の入力フォーム文字列
    text = ""

#入力フォーム
with st.form("Prompt", clear_on_submit=False):
    style = st.selectbox(label='画風', options=styleList)
    user_input = st.text_input('なんの画像？（音声入力は上のアイコン）', text)
    submitted = st.form_submit_button("画像を生成")

#submittedボタンが押されたらプロンプトを加工してcreateImage関数を呼び出す
if submitted:
    st.session_state["count"] += 1
    if style=="リアル":
        stylePrompt=""
    elif style=="ドット絵(Pixel art)":
        stylePrompt="Generate a pixel art of this"
    elif style=="5歳児のクレヨン":
        stylePrompt="Generate a crayon drawing by a five-year-old"
    elif style=="葛飾北斎":
        stylePrompt="Paint this in the style of Katsushika Hokusai"
    elif style=="モノクロ":
        stylePrompt="Generate a monochrome image of this"
    createImage(user_input,stylePrompt,st.session_state["count"])

#リセットボタン
if st.session_state["count"]!=0:
    if st.button("リセット", key=0):
        st.session_state["count"] = 0