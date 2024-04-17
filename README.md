YouTube Data Harvesting and Warehousing using SQL and Streamlit
Project Overview
This project aims to create a Streamlit application for accessing and analyzing data from multiple YouTube channels. The application allows users to input YouTube channel IDs, retrieve relevant data such as channel information, video details, likes, dislikes, and comments using the YouTube API. The collected data can be stored in a data lake and later migrated to a SQL database (MySQL ) for further analysis. Users can search and retrieve data from the SQL database using various search options, including joining tables to get comprehensive channel details.
Skills Takeaway
•	Python scripting
•	Data collection from APIs (YouTube API)
•	Streamlit for building interactive web applications
•	API integration
•	Data Management using SQL (MySQL or PostgreSQL)
Domain
Social Media
Problem Statement
The task is to develop a Streamlit application with the following features:
1.	Data Retrieval: Allow users to input YouTube channel IDs and retrieve relevant data including channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, and comments for each video using the YouTube API.
2.	Data Collection: Provide an option to collect data for up to 10 different YouTube channels and store them in a data lake.
3.	Data Querying: Enable users to search and retrieve data from the SQL database using different search options, including joining tables to get comprehensive channel details.
Approach
1.	Set up Streamlit App: Utilize Streamlit to build a user-friendly interface for data input, retrieval, and visualization.
2.	Connect to YouTube API: Utilize the Google API client library for Python to fetch channel and video data from the YouTube API.
3.	Store and Clean Data: Use pandas DataFrames or similar in-memory data structures to temporarily store and clean the retrieved data before migrating it to the data warehouse.
4.	Migrate Data to SQL Data Warehouse: Once data for multiple channels is collected, migrate it to a SQL database such as MySQL or PostgreSQL for long-term storage and analysis.
5.	Query the SQL Data Warehouse: Utilize SQL queries, possibly with a Python SQL library like SQLAlchemy, to interact with the SQL database, perform data manipulation, and retrieve relevant information based on user input.
6.	Display Data in Streamlit App: Finally, display the retrieved data in the Streamlit app using Streamlit's data visualization features, including charts and graphs, to facilitate data analysis.
Example Data Extraction from YouTube API
jsonCopy code
{ "Channel_Name": { "Channel_Name": "Example Channel", "Channel_Id": "UC1234567890", "Subscription_Count": 10000, "Channel_Views": 1000000, "Channel_Description": "This is an example channel.", "Playlist_Id": "PL1234567890" }, "Video_Id_1": { "Video_Id": "V1234567890", "Video_Name": "Example Video 1", "Video_Description": "This is an example video.", "Tags": ["example", "video"], "PublishedAt": "2022-01-01T00:00:00Z", "View_Count": 1000, "Like_Count": 100, "Dislike_Count": 10, "Favorite_Count": 5, "Comment_Count": 20, "Duration": "00:05:00", "Thumbnail": "https://example.com/thumbnail.jpg", "Caption_Status": "Available", "Comments": { "Comment_Id_1": { "Comment_Id": "C1234567890", "Comment_Text": "This is a comment.", "Comment_Author": "Example User", "Comment_PublishedAt": "2022-01-01T00:01:00Z" }, "Comment_Id_2": { "Comment_Id": "C2345678901", "Comment_Text": "This is another comment.", "Comment_Author": "Another User", "Comment_PublishedAt": "2022-01-01T00:02:00Z" } } }, "Video_Id_2": { "Video_Id": "V2345678901", "Video_Name": "Example Video 2", "Video_Description": "This is another example video.", "Tags": ["example", "video"], "PublishedAt": "2022-01-02T00:00:00Z", "View_Count": 2000, "Like_Count": 200, "Dislike_Count": 20, "Favorite_Count": 10, "Comment_Count": 30, "Duration": "00:10:00", "Thumbnail": "https://example.com/thumbnail.jpg", "Caption_Status": "Not Available", "Comments": {} } } 
SQL Query Outputs Displayed in Streamlit Application
1.	Names of all videos and their corresponding channels.
2.	Channels with the most number of videos and the count of videos they have.
3.	Top 10 most viewed videos and their respective channels.
4.	Number of comments on each video and their corresponding video names.
5.	Videos with the highest number of likes and their corresponding channel names.
6.	Total likes and dislikes for each video and their corresponding names.
7.	Total views for each channel and their corresponding names.
8.	Names of channels that have published videos in the year 2022.
9.	Average duration of all videos in each channel and their corresponding names.
10.	Videos with the highest number of comments and their corresponding channel names.
References
•	Streamlit Documentation
•	YouTube API Reference
Conclusion
This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on YouTube channels, stores it in a SQL database, and enables users to search for channel details and join tables to view data in the Streamlit app.
For detailed instructions on setting up and using the application, please refer to the documentation provided in the repository.

