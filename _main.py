#maincode
import streamlit as st
import pandas as pd
import googleapiclient.discovery
import mysql.connector
bg_image = f"""<style>.stApp {{background-image: url("{"https://img.freepik.com/premium-photo/youtube-logo-3d-render_41204-3548.jpg"}");background-size: cover;}}</style>"""
st.markdown(bg_image, unsafe_allow_html=True)
mydb = mysql.connector.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor(buffered=True)

api_service_name = "youtube"
api_version = "v3"
api_key ='AIzaSyDVXsjQzIam-YuLQEyxP7_U9ItUhIoRZTI'

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
st.title('YOUTUBE')
st.subheader('''
    :red[YouTube] :orange[Data] :green[Harvesting] :blue[and] :violet[Warehousing] :gray[using] :green[and] :rainbow[Streamlit].''')
channel_id=st.text_input("enter youtube id")   
# channel_id = 'UCWCVYwLvaTq5Q90c4874X5g'
def commentcount(count):
    if count > 100:
        return 100
    else:
        return count


def main():
    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id)
    response = request.execute()
    channel_data = response.get('items', [{}])[0]
    channel_name = channel_data.get('snippet', {}).get('title', 'Unknown')
    channel_description = channel_data.get('snippet', {}).get('description', 'Unknown')
    channel_playlist = channel_data.get('contentDetails', {}).get('relatedPlaylists', {}).get('uploads', 'Unknown')
    channel_subcount = channel_data.get('statistics', {}).get('subscriberCount', 'Unknown')
    channel_videoCount = channel_data.get('statistics', {}).get('videoCount', 'Unknown')
    channel_viewCount = channel_data.get('statistics', {}).get('viewCount', 'Unknown')
    channel_logo_url = channel_data.get('snippet', {}).get('thumbnails', {}).get('default', {}).get('url', 'Unknown')
    st.subheader("channel_Logo", divider='rainbow')
    st.image(channel_logo_url,width=300)
    st.subheader(channel_name, divider='rainbow')
    request = youtube.playlistItems().list(part="snippet", playlistId=channel_playlist, maxResults=50)
    video_ids = []

    while request:
        response = request.execute()
        video_ids.extend([item["snippet"]["resourceId"]["videoId"] for item in response["items"]])
        if "nextPageToken" in response:
            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=channel_playlist,
                maxResults=50,
                pageToken=response["nextPageToken"]
            )
        else:
            request = None

    for video_id in video_ids:
        response = youtube.videos().list(part="snippet,contentDetails,statistics", id=video_id).execute()
        video_data = response["items"][0]

        video_name = video_data['snippet']['title']
        video_description = video_data['snippet']['description']
        video_publishedAt = video_data['snippet']['publishedAt']
        video_thumbnails = str(video_data['snippet']['thumbnails'])
        video_duration = video_data['contentDetails']['duration']
        video_viewCount = video_data['statistics']['viewCount']
        video_likeCount = video_data['statistics']['likeCount']
        video_favoriteCount = video_data['statistics']['favoriteCount']
        video_commentCount = video_data['statistics'].get('commentCount', 0)


        if int(video_commentCount) > 0:
            try:
                comments = youtube.commentThreads().list(part="id,snippet", videoId=video_id, maxResults=100).execute()
                count = commentcount(int(video_commentCount))
                for j in range(count):
                        comment_id = comments["items"][j]["id"]
                        comment_text = comments["items"][j]["snippet"]['topLevelComment']["snippet"]['textDisplay']
                        comment_author = comments["items"][j]["snippet"]['topLevelComment']["snippet"]['authorDisplayName']
                        comment_publishedAt = comments["items"][j]["snippet"]['topLevelComment']["snippet"]["publishedAt"]
                        
                        query = """INSERT INTO youtube.youtube_channel_details
                                (channel_name, channel_description, channel_playlist, channel_subcount,
                                channel_videoCount, channel_viewCount, video_name, video_description,
                                video_publishedAt, video_thumbnails, video_duration, video_viewCount,
                                video_likeCount, video_favoriteCount, video_commentCount, comment_id,
                                comment_text, comment_author, comment_publishedAt)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                                
                        values = (channel_name, channel_description, channel_playlist, channel_subcount,
                                    channel_videoCount, channel_viewCount, video_name, video_description,
                                    video_publishedAt, video_thumbnails, video_duration, video_viewCount,
                                    video_likeCount, video_favoriteCount, video_commentCount, comment_id,
                                    comment_text, comment_author, comment_publishedAt)

                        mycursor.execute(query, values)
                mydb.commit()

            except Exception as e:
                pass
        else:
                    query = """INSERT INTO youtube.youtube_channel_details
                    (channel_name, channel_description, channel_playlist, channel_subcount,
                    channel_videoCount, channel_viewCount, video_name, video_description,
                    video_publishedAt, video_thumbnails, video_duration, video_viewCount,
                    video_likeCount, video_favoriteCount, video_commentCount)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                    values = (channel_name, channel_description, channel_playlist, channel_subcount,
                                    channel_videoCount, channel_viewCount, video_name, video_description,
                                    video_publishedAt, video_thumbnails, video_duration, video_viewCount,
                                    video_likeCount, video_favoriteCount, video_commentCount)
                                    
                    mycursor.execute(query, values)
        mydb.commit()
if st.button("chennal details table"):
    main()

