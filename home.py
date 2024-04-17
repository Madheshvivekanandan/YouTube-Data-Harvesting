import streamlit as st
def set_background_image(image_url):
    bg_image = f"""<style>.stApp {{background-image: url("{image_url}");background-size: cover;}}</style>"""
    st.markdown(bg_image, unsafe_allow_html=True)
def set_custom_styles():
    custom_css = """<style>body {font-family: 'Arial', sans-serif;}.stApp {color: ##000000;}</style>"""
    st.markdown(custom_css, unsafe_allow_html=True)
def main():
    set_background_image("https://img.freepik.com/free-photo/photorealistic-stone-wall-surface_23-2151214703.jpg?t=st=1712990886~exp=1712994486~hmac=690339ab0e5628add94820bdff96adc43f235cc126bb7b811eb08eaae11b5afe&w=1380")
    set_custom_styles()
    st.title("My Streamlit App on Youtube")
    st.write("### YouTube Data Harvesting and Warehousing using SQL and Streamlit")

if __name__ == "__main__":
    main()
st.page_link("http://www.youtube.com", label="Youtube", icon="🤖")
# if st.button("Home🏡"):
#     st.switch_page(r"pages/youtube.py")
if st.button("Main_workstation"):
    st.switch_page(r"pages/_main.py")
if st.button("Question dropdown"):
    st.switch_page(r"pages/dropdown.py")
st.header("Aim of the project")
st.write("#### This project aims to develop a Streamlit application that facilitates the retrieval, storage, and analysis of data from multiple YouTube channels. The application allows users to input YouTube channel IDs, retrieve relevant data using the YouTube API, store the data in a SQL data warehouse, and perform data analysis using SQL queries.")
st.header("Features")
st.write("### 🎯**YouTube API Integration:** Connects to the YouTube API to retrieve channel details, video details, likes, dislikes, comments, etc., based on the provided channel IDs.")
st.write("### 🎯**Streamlit Interface:** Provides a user-friendly interface built with Streamlit, allowing users to input channel IDs, view channel details, and select channels for data migration.")
st.write("### 🎯**Data Storage and Cleaning:** Stores retrieved data in a temporary format before migrating it to a SQL data warehouse. Performs data cleaning and preprocessing as necessary.")
st.write("### 🎯**SQL Data Warehouse:** Utilizes MySQL or PostgreSQL for storing collected YouTube data. Sets up tables and schema to accommodate the data efficiently.")
st.write("### 🎯**SQL Querying:** Allows users to query the SQL data warehouse using SQL queries to retrieve data based on various search options and join tables for insights.")
st.write("### 🎯**Data Visualization:** Utilizes Streamlit's data visualization features to present retrieved data in tables for effective analysis.")