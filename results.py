import streamlit as st
import json
from Parser import Jparse


def show_result_page():
     st.title("RANSOMWARE DETECTOR")
     upload = st.file_uploader(label="Upload sample here",type=['json','exe','msi'],)
     sample = st.button("Submit Sample")

     if sample:
         if upload is not None:
             #st.write("Sample Submitted!! Await results...")
             json_load = json.load(upload)
             Jparse(json_load)




