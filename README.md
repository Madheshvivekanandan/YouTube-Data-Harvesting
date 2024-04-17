# YouTube Data Harvesting and Warehousing using SQL and Streamlit

## Project Overview

This project aims to create a Streamlit application for accessing and analyzing data from multiple YouTube channels. The application allows users to input YouTube channel IDs, retrieve relevant data such as channel information, video details, likes, dislikes, and comments using the YouTube API. The collected data can be stored in a data lake and later migrated to a SQL database (MySQL) for further analysis.

### Skills Takeaway

- Python scripting
- Data collection from APIs (YouTube API)
- Streamlit for building interactive web applications
- API integration
- Data Management using SQL (MySQL)

## Domain: Social Media

### Problem Statement

The task is to develop a Streamlit application with the following features:

#### Data Retrieval:

Allow users to input YouTube channel IDs and retrieve relevant data including channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, and comments for each video using the YouTube API.

#### Data Collection:

Provide an option to collect data from different YouTube channels and store them in a database.

#### Data Querying:

Enable users to select the mention questions in streamlit application and retrieve data from the SQL database.

## Approach

1. **Set up Streamlit App**: Utilize Streamlit to build a user-friendly interface for data input, retrieval, and visualization.
2. **Connect to YouTube API**: Utilize the Google API client library for Python to fetch channel and video data from the YouTube API.
3. **Store and Clean Data**: Use pandas DataFrames or similar in-memory data structures to temporarily store and clean the retrieved data before migrating it to the data warehouse.
4. **Migrate Data to SQL Data Warehouse**: Once data for multiple channels is collected, migrate it to a SQL database such as MySQL for long-term storage and analysis.
5. **Query the SQL Data Warehouse**: Utilize SQL queries, possibly with Mysql, to interact with the SQL database, perform data manipulation, and retrieve relevant information based on user input.
6. **Display Data in Streamlit App**: Finally, display the retrieved data in the Streamlit app using Streamlit's data visualization features, including tables, to facilitate data analysis.

### Example Data Extraction from YouTube API JSON

```json
{ 
  "Channel_Name": { 
    "Channel_Name": "Example Channel",
    "Channel_Id": "UC1234567890",
    "Subscription_Count": 10000,
    "Channel_Views": 1000000,
    "Channel_Description": "This is an example channel.",
    "Playlist_Id": "PL1234567890"
  },
  "Video_Id_1": { 
    "Video_Id": "V1234567890",
    "Video_Name": "Example Video 1",
    ...
  },
  "Video_Id_2": { 
    "Video_Id": "V2345678901",
    "Video_Name": "Example Video 2",
    ...
  }
}
```

## SQL Query Outputs Displayed in Streamlit Application

- Names of all videos and their corresponding channels.
- Channels with the most number of videos and the count of videos they have.
- Top 10 most viewed videos and their respective channels.
- Number of comments on each video and their corresponding video names.
- Videos with the highest number of likes and their corresponding channel names.
- Total likes and dislikes for each video and their corresponding names.
- Total views for each channel and their corresponding names.
- Names of channels that have published videos in the year 2022.
- Average duration of all videos in each channel and their corresponding names.
- Videos with the highest number of comments and their corresponding channel names.

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [YouTube API Reference](https://developers.google.com/youtube/v3)

## Conclusion

This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on YouTube channels, stores it in a SQL database, and enables users to search for channel details and join tables to view data in the Streamlit app. For detailed instructions on setting up and using the application, please refer to the documentation provided in the repository.
