from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import plotly.express as px #for visualization
import matplotlib.pyplot as plt
import plotly.io as pio
import requests
app = Flask(__name__)

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the CSV file
file_path = os.path.join(current_directory, 'D:/practice/youtube-churn-predict-main/web development/pythonfiles/dataset1.csv')

# Read the CSV file into a DataFrame
user_data = pd.read_csv(file_path)
data = {
    'Unsubscribed': [100],
    'Category': ['Count = 0', 'Count = 1']

}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'channel123@gmail.com' and password == '123456':
        return redirect(url_for('onscreen'))
    else:
        return 'INVALID!'

@app.route('/onscreen')
def onscreen():  
    # Calculate the total number of YouTube videos and total stream time
    num_of_sub = user_data['Subscriber_id'].count()
    # Calculate genre frequencies
    genre_frequencies = user_data['Genre'].value_counts()
    # Prepare genre count information for rendering
    genre_info = [{'genre': genre, 'count': count} for genre, count in zip(genre_frequencies.index, genre_frequencies.values)]
    # Sort genre_info by count in descending order
    genre_info = sorted(genre_info, key=lambda x: x['count'], reverse=True)
    # Get the top 2 most frequently watched genres
    top2_genres = genre_info[:2]
    active_members = len(user_data[user_data['IsActiveMember'] == 1])
    # Calculate the count of inactive members (IsActiveMember = 0)
    inactive_members = len(user_data[user_data['IsActiveMember'] == 0])
    # Create a dictionary to store the counts
    member_counts = {
        'Active Members': active_members,
        'Inactive Members': inactive_members
    }
    # Calculate the total likes and total dislikes
    total_likes = user_data['Like_Dislike'].sum()
    total_dislikes = len(user_data) - total_likes
    top3_streamedtime = user_data.nlargest(3, 'Streamedtime')[['Subscriber_id', 'Streamedtime']]
    # Pass these random numbers and the combined total to the template
    return render_template('onscreen.html', numn_of_videos=num_of_sub, top3_streamedtime=top3_streamedtime, genree=top2_genres, member_counts=member_counts, random_likes=total_likes, random_dislikes=total_dislikes)
@app.route('/predict')

def predict():
    remote_url = 'http://192.168.225.185:8501'  # Replace with your desired remote URL
    return redirect(remote_url)

@app.route('/recommed')
def recommend():
    return render_template('recommend.html')
if __name__ == '__main__':
    app.run(debug=True)