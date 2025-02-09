import streamlit as st
import time

# Set page title and icon
st.set_page_config(page_title="Love for Pucchkuu ❤️", page_icon="❤️")

# Use custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-family: 'Helvetica', sans-serif;
            color: #FF1493;
            font-size: 48px;
            font-weight: bold;
        }
        .subtitle {
            font-family: 'Arial', sans-serif;
            color: #FF69B4;
            font-size: 30px;
        }
        .message {
            font-family: 'Courier New', Courier, monospace;
            font-size: 20px;
            color:#ADD8E6;
        }
        .footer {
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            color: #FF1493;
        }
    </style>
""", unsafe_allow_html=True)

# Title with big heart emoji
st.markdown('<h1 class="title">To My Dearest Pucchkuu 💖</h1>', unsafe_allow_html=True)

# Romantic subheading with some delay for effect
st.markdown('<h2 class="subtitle">You are my everything! 🌹💫</h2>', unsafe_allow_html=True)

# Adding an animated "Love" heart emoji
st.markdown(":heartpulse: :heartpulse: :heartpulse:", unsafe_allow_html=True)

# Romantic message with some pauses for effect
st.markdown('<p class="message">I love you more than words can say, Pucchkuu. Every moment with you is magical! ✨</p>', unsafe_allow_html=True)
time.sleep(1)  # Pause to add dramatic effect
st.markdown('<p class="message">You make my world more beautiful every single day. 💫🌷</p>', unsafe_allow_html=True)
time.sleep(1)
st.markdown('<p class="message">I feel so lucky to have you in my life. Here’s to forever together. 💖</p>', unsafe_allow_html=True)

# Heart emojis for more sweetness
st.markdown(":heart_eyes: :rose: :sparkles: :heart_eyes:", unsafe_allow_html=True)

# Display an image with some custom styling
image_path = "bond.jpeg"  # Change to the path of the image
st.image(image_path, caption="Together Forever 💑", use_column_width=True)

# Footer message with personalized text
st.markdown('<p class="footer">With all my love, [pucchu] 💖</p>', unsafe_allow_html=True)

