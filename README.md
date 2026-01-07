# 🎭 Gemini 3.0 Meme Generator

這是一個基於 **Gemini 3 Pro Image** 模型建構的 AI 謎因產生器，使用者可以透過文字描述（與可選的參考圖）直接生成極具幽默感的梗圖。

## 🌟 特色
- **多模態生成**：支援文字轉圖片，並可理解上傳的參考圖進行創作。
- **個人化金鑰**：支援使用者輸入自己的 Google AI Studio API Key。
- **雲端就緒**：完美適配 Google Cloud Run 部署架構。

## 🚀 快速開始

### 本地執行
1. 克隆專案：`https://github.com/Octoberlobster/meme_generator.git`
2. 安裝套件：`pip install -r requirements.txt`
3. 執行：`streamlit run app.py`

### GCP Cloud Run 部署
使用以下指令快速部署到雲端：
```bash
gcloud builds submit --tag asia-east1-docker.pkg.dev/YOUR_PROJECT_ID/meme-repo/meme-app .
gcloud run deploy meme-service --image asia-east1-docker.pkg.dev/YOUR_PROJECT_ID/meme-repo/meme-app --region asia-east1 --allow-unauthenticated
