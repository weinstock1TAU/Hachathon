import time

import redis
from flask import Flask
import streamlit as st
import calendar
import time
from PIL import Image


header =  st.container()
creat_btn = st.button("create")
join_btn = st.button("join")

with header:
    st.title("Welcome to UNIFriends")
    st.text("A social network for creating study meeting.\nImprove your learning environment,and make new friends.")

if creat_btn:
    # with st.form(key='columns_in_form'):
    #     cols = st.columns('')
    #     for i, col in enumerate(cols):
    #         col.selectbox(f'Course', ['click', 'or click'], key=i)
    #     submitted = st.form_submit_button('Submit')
   with st.form(key='columns_in_form'):
       course = st.selectbox(
           'Course',
           ('choose Course ','algorithms', 'chemistry', 'Economics'))
       date = st.selectbox(
           'Date',
           ('choose Date','January ', 'February', 'March','April','May','June','July','August',
            'September','October','November ','December'))
       time = st.selectbox(
           'Time',
           ('choose Time','8:00', '9:00', '10:00','11:00', '12:00', '13:00','14:00', '15:00', '16:00','17:00', '18:00', '19:00'))
       location = st.selectbox(
           'Location',
           ('choose Location','Wladimir Schreiber Institute of Mathematical Sciences, Tel Aviv-Yafo, Israel',
            'Dan David Building, Tel Aviv-Yafo, Israel',
            'Building Orenstein, Tel Aviv-Yafo, Israel'))
       submitted = st.form_submit_button('Submit')

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

