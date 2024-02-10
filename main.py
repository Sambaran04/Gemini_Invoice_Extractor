from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables from .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

# def get_gemini_response(input, image, prompt):
#     response =