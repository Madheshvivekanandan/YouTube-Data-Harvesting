import streamlit as st
import mysql.connector as ms
import pandas as pd
mydb=ms.connect(host="localhost",user="root",password="")
def question1():
    st.write("Names of all the videos and their corresponding channels")
    def fetch_data():
        query = "SELECT DISTINCT channel_name, video_name FROM youtube.youtube_channel_details"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)
def question2():
    st.write("Channels with the most number of videos, and how many videos they have")
    def fetch_data():
        query = "SELECT channel_name, COUNT(video_name) AS video_count FROM youtube.youtube_channel_details GROUP BY channel_name ORDER BY video_count desc LIMIT 1"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)
def question3():
    st.write("Top 10 most viewed videos and their respective channels")
    def fetch_data():
        query = "SELECT DISTINCT channel_name, video_name, CAST(video_viewCount AS UNSIGNED) AS views FROM youtube.youtube_channel_details ORDER BY views DESC LIMIT 10"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)
def question4():
    st.write("Number of comments on each video and their corresponding video names")
    def fetch_data():
        query = "SELECT DISTINCT video_name,video_commentCount FROM youtube.youtube_channel_details"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)
def question5():
    st.write("Videos with the highest number of likes and their corresponding channel names")
    def fetch_data():
        query = "SELECT DISTINCT channel_name, video_name, CAST(video_likeCount AS UNSIGNED) AS views FROM youtube.youtube_channel_details ORDER BY views DESC LIMIT 10"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)

def question6():
    st.write("Total number of likes and dislikes for each video and their corresponding video names")
    def fetch_data():
        query = "SELECT DISTINCT video_name,video_likeCount FROM youtube.youtube_channel_details"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)

def question7():
    st.write("Total number of views for each channel and their corresponding channel names")
    def fetch_data():
        query = "SELECT DISTINCT channel_name, channel_view FROM youtube.youtube_channel_details"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)

def question8():
    st.write("Names of all the channels that have published videos in the year 2022")
    def fetch_data():
        query = "SELECT DISTINCT channel_name,video_publishedAt  FROM youtube.youtube_channel_details where  SUBSTRING(video_publishedAt, 1, 4) = '2022'"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)

# def question9():
#     st.write("Average duration of all videos in each channel and their corresponding channel names")
#     def fetch_data():
#         query = """SELECT
#                     channel_name,
#                     SEC_TO_TIME(AVG(
#                         CASE
#                             WHEN video_duration LIKE 'PT%M%S' THEN
#                                 TIME_TO_SEC(SUBSTRING(video_duration, 3, INSTR(video_duration, 'M') - 3)) * 60 + SUBSTRING(video_duration, INSTR(video_duration, 'M') + 1, INSTR(video_duration, 'S') - INSTR(video_duration, 'M') - 1)
#                             WHEN video_duration LIKE 'PT%S' THEN
#                                 SUBSTRING(video_duration, 3, INSTR(video_duration, 'S') - 3)
#                         END
#                     )) AS avg_duration
#                 FROM
#                     youtube.youtube_channel_details
#                 GROUP BY
#                     channel_name"""
#         df = pd.read_sql(query,mydb)
#         return df
#     data = fetch_data()
#     st.write(data)


def question9():
    st.write("Average duration of all videos in each channel and their corresponding channel names")
    def fetch_data():
        query = """SELECT
    channel_name,
    AVG(
        CASE
            WHEN video_duration LIKE 'PT%M%S' THEN
                TIME_TO_SEC(SUBSTRING(video_duration, 3, INSTR(video_duration, 'M') - 3)) * 60 + SUBSTRING(video_duration, INSTR(video_duration, 'M') + 1, INSTR(video_duration, 'S') - INSTR(video_duration, 'M') - 1)
            WHEN video_duration LIKE 'PT%S' THEN
                SUBSTRING(video_duration, 3, INSTR(video_duration, 'S') - 3)
        END
    ) AS avg_duration_in_seconds,
    SEC_TO_TIME(AVG(
        CASE
            WHEN video_duration LIKE 'PT%M%S' THEN
                TIME_TO_SEC(SUBSTRING(video_duration, 3, INSTR(video_duration, 'M') - 3)) * 60 + SUBSTRING(video_duration, INSTR(video_duration, 'M') + 1, INSTR(video_duration, 'S') - INSTR(video_duration, 'M') - 1)
            WHEN video_duration LIKE 'PT%S' THEN
                SUBSTRING(video_duration, 3, INSTR(video_duration, 'S') - 3)
        END
    )) AS avg_duration
FROM
    youtube.youtube_channel_details
GROUP BY
    channel_name
"""
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)

def question10():
    st.write("Videos with the highest number of comments and their corresponding channel names")
    def fetch_data():
        query = "SELECT DISTINCT channel_name, video_name,cast(video_commentCount as unsigned) as count FROM youtube.youtube_channel_details order by count desc"
        df = pd.read_sql(query,mydb)
        return df
    data = fetch_data()
    st.write(data)

# Dropdown menu to select the question
selected_question = st.selectbox('Select a question', 
                                ['Names of all the videos and their corresponding channels?',
                                'Channels with the most number of videos, and how many videos they have?',
                                'Top 10 most viewed videos and their respective channels?',
                                'Number of comments on each video and their corresponding video names?',
                                'Videos with the highest number of likes and their corresponding channel names?',
                                'Total number of likes and dislikes for each video and their corresponding video names?',
                                'Total number of views for each channel and their corresponding channel names?',
                                'Names of all the channels that have published videos in the year 2022?',
                                'Average duration of all videos in each channel and their corresponding channel names?',
                                'Videos with the highest number of comments and their corresponding channel names?'])

# Display the selected question
if selected_question == 'Names of all the videos and their corresponding channels?':
    question1()
elif selected_question == 'Channels with the most number of videos, and how many videos they have?':
    question2()
elif selected_question == 'Top 10 most viewed videos and their respective channels?':
    question3()
elif selected_question == 'Number of comments on each video and their corresponding video names?':
    question4()
elif selected_question == 'Videos with the highest number of likes and their corresponding channel names?':
    question5()
elif selected_question == 'Total number of likes and dislikes for each video and their corresponding video names?':
    question6()
elif selected_question == 'Total number of views for each channel and their corresponding channel names?':
    question7()
elif selected_question == 'Names of all the channels that have published videos in the year 2022?':
    question8()
elif selected_question == 'Average duration of all videos in each channel and their corresponding channel names?':
    question9()
elif selected_question == 'Videos with the highest number of comments and their corresponding channel names?':
    question10()
