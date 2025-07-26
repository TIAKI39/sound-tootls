# Arc Volume Auto Adjuster

Windowsで「既定のサウンド出力デバイス（イヤホン / スピーカー）」が切り替わった際に、
Webブラウザー「Arc」の音量を自動的に調整する Python スクリプトです。

---

## 🔧 概要

- 既定のオーディオデバイスが **Earphones** に変わると Arc の音量を 15% に設定
- **Speaker** に変わると 60%、その他のデバイス時には 40% に設定
- 5秒間隔でデバイス変更を監視

---

## 📷 動作イメージ

```text
[既定デバイス: Earphones] → Arc 音量 15%
[既定デバイス: Speaker] → Arc 音量 60%
[既定デバイス: その他]  → Arc 音量 40%

---

## 動作環境

OS: Windows 10 / 11
Python 3,10（推奨）

---

## インストール手順

git clone https://github.com/あなたのユーザー名/arc-volume-adjuster.git
cd arc-volume-adjuster

---

## ライブラリをインストール
pip install -r requirements.txt

---

## 実行
python SoundTool.py

