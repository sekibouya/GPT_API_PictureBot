# PictureBot
![画像8](https://github.com/sekibouya/GPT_API_PictureBot/assets/99582134/d034068d-0d7c-40db-b6aa-0a814e9a4edc)

## Overview
描かれる対象物と画風を指定し、その画風に応じた画像を生成することができる画像生成アプリです。

## Requirement
* streamlit
* requests
* openai
* audio_recorder_streamlit

## Usage
### 実行方法
```
streamlit run .\PictureBot.py
```

### 1. Open AIのAPI-KEYを入力
![画像1](https://github.com/sekibouya/GPT_API_PictureBot/assets/99582134/58adbdc3-feb6-4dca-86d6-4e76ce45b7b5)

### 2. 画風の選択(以下の５つから選択)
   * リアル
   * ドット絵
   * ５歳児のクレヨン
   * 葛飾北斎
   * モノクロ
![画像3](https://github.com/sekibouya/GPT_API_PictureBot/assets/99582134/3a7de946-5f2a-4ce6-9128-42c99697b504)

### 3. 描く物を入力(音声入力可)
![画像4](https://github.com/sekibouya/GPT_API_PictureBot/assets/99582134/1693de3b-0b96-48d6-8fb7-28c83679d202)

### 4. 画像が生成され表示される
![画像7](https://github.com/sekibouya/GPT_API_PictureBot/assets/99582134/6734b335-cf06-4f97-9f06-61fd7588dd82)

(画風:５歳児のクレヨン, 入力:Mount Fuji)<br>

※繰り返し画像を生成すると下ように複数表示される
![画像6(2)](https://github.com/sekibouya/GPT_API_PictureBot/assets/99582134/f787bd04-a3e2-4570-a5d2-cb3cd16c34be) 

## Features
* Open AIのAPIを使用
* Web上で動作
* シンプルなUI
* 5種類の画風から選択
* 音声入力に対応
* 画像の複数表示

## Author
name: せき<br>
X: @sekibouya_
