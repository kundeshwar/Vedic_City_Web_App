#-------------------------------------------------------import your labrary here 
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import youtube_dl
import requests
import pprint
from video_text import auth_key
from time import sleep
from youtube_transcript_api import YouTubeTranscriptApi
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup
import pandas as pd 
import requests
#----------------------------------------page title 
st.set_page_config(page_title="Vedic City", page_icon="🪴", initial_sidebar_state="expanded")

#---------------------------------------------sidebar                              t.button("Click Me 👈")

with st.sidebar:
    option = " Vedic City ♨️"
    st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)
    option = "Let's Vedic Again"
    st.markdown(f"<h4 style='text-align: center;'><b>{option}</b></h4>",unsafe_allow_html=True)
    st.markdown("------------------")
    option_m = option_menu("SELECT(Data Scrapping) ➡️", options=["Link", "Video"],
    icons=[":grinning:",":stuck_out_tongue_winking_eye:",":grinning:","kissing"], default_index=0)
    st.markdown("------------------")
    option = "❤️"
    st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)
    option = "CEO & Founder"
    st.markdown(f"<h2 style='text-align: center;'><b>{option}</b></h2>",unsafe_allow_html=True)
    option = "Mr.Suraj Racha"
    st.markdown(f"<h3 style='text-align: center;'><b>{option}</b></h3>",unsafe_allow_html=True)
    option = "CTO & Co-Founder"
    st.markdown(f"<h2 style='text-align: center;'><b>{option}</b></h2>",unsafe_allow_html=True)
    option = "Mr.Kundeshwar Pundalik"
    st.markdown(f"<h3 style='text-align: center;'><b>{option}</b></h3>",unsafe_allow_html=True)
    st.markdown("------------------")
    option = "💡 Objective"
    st.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.markdown('''- 1. Copy the URL of the YouTube video you want to extract the text from''')

    st.markdown('''- 2. Paste the YouTube video URL into the input field.
    ''')
    add_vertical_space(4)
    st.write('Made with ❤️ by Kundeshwar Pundalik 😍')
#---------------------------------------------headline for app

option = "🌿 Vedic City 🌿"
st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)

#--------------------------------------------Assembly AI 

def get_video_transcript(video_url):
    try:
        video_id = video_url.split('v=')[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([line['text'] for line in transcript])
        return text

    except Exception as e:
        print('Error:', str(e))
#--------------------------------------------------
import io
#----------------------------------------------------
# Function to save text to a file
def save_text_as_file(text):
    # Create a BytesIO buffer
    buffer = io.BytesIO()
    # Convert the text to bytes and write it to the buffer
    buffer.write(text.encode())
    # Set the buffer's cursor to the beginning
    buffer.seek(0)
    # Return the buffer
    return buffer
#----------------------------------------------------write for link acces and function 
if option_m == "Video":
        link = st.text_input('Enter your YouTube video link')
        #button = st.button("Click Me 👈")
        if link:
                st.video(link)
                if st.button("Extract Text👈"):
                    transcript = get_video_transcript(link)
                    if transcript:
                        # Save extracted text as a file
                        file_buffer = save_text_as_file(transcript)
                        st.download_button(
                                            "Download Extracted Text👈",
                                            file_buffer,
                                            file_name="extracted_text.txt",
                                            mime="text/plain"
                                        )
                        
                        st.markdown("Transcript")
                        st.success(transcript)
                    else:
                        st.markdown("Transcript not found")

if option_m == "Link":
     link_2 = st.text_input('Enter your link')
     if link_2:
        page = requests.get(link_2)
        content = page.content
        soup = BeautifulSoup(content, "html.parser")
        p_tags = soup.find_all('p')
        p_tags = [p.get_text() for p in p_tags]
        last_text = p_tags[16:-2]
        print(last_text)
        a = []
        for i in last_text:
            a.append(i)
        paragraph = " ".join(a)
        if paragraph:
            file_buffer = save_text_as_file(paragraph)
            st.download_button(
                                            "Download Extracted Text File👈",
                                            file_buffer,
                                            file_name="extracted_text.txt",
                                            mime="text/plain"
                                        )
                        
            st.markdown("Data")
            st.success(paragraph)
        else:
            st.markdown("Transcript not found")
             
     











