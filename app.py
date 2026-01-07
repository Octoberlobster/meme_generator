import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- 1. 網頁設定 ---
st.set_page_config(page_title="Gemini AI Meme Studio", page_icon="🎭", layout="wide")

# 套用深色風格 CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #FF4B4B; color: white; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 側邊欄：金鑰管理 ---
st.sidebar.title("🔑 Configuration")
user_api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")
st.sidebar.caption("Get your API key at [Google AI Studio](https://aistudio.google.com/app/apikey)")

if user_api_key:
    genai.configure(api_key=user_api_key)
    st.sidebar.success("✅ API Key Ready")
else:
    st.sidebar.warning("⚠️ Please enter API Key")

st.sidebar.divider()
st.sidebar.info(f"SDK Version: {genai.__version__}")

# --- 3. 核心影像生成邏輯 ---
def generate_meme(user_prompt, style, reference_image=None):
    if not user_api_key:
        st.error("Missing API Key!")
        return None

    # 使用支援產圖的最新模型
    model = genai.GenerativeModel('gemini-2.0-flash-exp') 
    
    prompt = f"You are a professional meme creator. Generate a funny meme based on: '{user_prompt}' with style: '{style}'. Include humorous text in the image."
    
    inputs = [prompt]
    if reference_image:
        inputs.append(Image.open(reference_image))

    # 使用字典格式確保相容性
    config = {"response_modalities": ["IMAGE"]}

    try:
        response = model.generate_content(inputs, generation_config=config)
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                return part.inline_data.data
        return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# --- 4. 主介面佈局 ---
st.title("🎭 Gemini 2.0 Meme Generator")
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("💡 Inspiration")
    user_text = st.text_area("Describe your meme idea:", placeholder="e.g. When the code finally runs but you don't know why...")
    meme_style = st.selectbox("Style:", ["Classic Meme", "Anime", "Cyberpunk", "3D Render"])
    uploaded_file = st.file_uploader("Upload reference (Optional)", type=['jpg', 'png', 'jpeg'])
    generate_btn = st.button("🚀 Generate Meme!")

with col2:
    st.subheader("🖼️ Result")
    if generate_btn and user_text:
        with st.spinner("Gemini is cooking..."):
            meme_output = generate_meme(user_text, meme_style, uploaded_file)
            if meme_output:
                st.image(meme_output, use_container_width=True)
                st.download_button("📥 Download", data=meme_output, file_name="meme.png", mime="image/png")
