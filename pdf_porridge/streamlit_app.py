import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from loguru import logger

logger.add("logs/debug.log", rotation="500 KB")
from pdfminer.high_level import extract_text

img = open("images/pdf_porridge_logo copy.png", "rb").read()
st.set_page_config(page_title="PDF-Porridge", background_image=img)


text = extract_text("images/example.pdf")
st.write(text)
