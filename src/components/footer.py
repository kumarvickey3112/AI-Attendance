import streamlit as st

def footer_home():
    logo_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqEqdFfNIsBSslrXLaHerir4LJ3GQYMKgaTh8NnhLj5Q&s=10"

    st.markdown(f"""
            <div style="margin-top:2rem; display:flex; gap:6px;justify-content:center; items-align:center">
            <p style="font-weight:bold;"> Created by </p>
            <img src='{logo_url}' style='max-height:30px' />
            </div>
            


                """, unsafe_allow_html=True
    )