# from flask import Flask, jsonify # type: ignore
# from flask_cors import CORS # type: ignore

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # @app.route('/api/data')
# # def get_data():
# #     data = {'message': 'Hello from Flask backend!'}
# #     return jsonify(data)

# @app.route('/')
# def home():
#     return jsonify("Welcome to the Flask application!")


# # @app.route('/api/submit', methods=['POST'])
# # def submit_data():
# #     # In a real application, you would process the incoming data here
# #     return jsonify({'message': 'Data received successfully!'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)



# # from flask import Flask, jsonify
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # @app.route('/api/data')
# # def get_data():
# #     data = {'message': 'hello from flask backend!'}
# #     return jsonify(data)

# # @app.route('/api/submit', methods = ['POST'])
# # def submit_data():
# #     return jsonify({'message': 'data received successfully!'})

# # if __name__ == '__main__':
# #     app.run(debug = True, port=5000)


# from flask import Flask, jsonify, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route('/')
# def home():
#     return jsonify("Welcome to the Flask application!")

# @app.route('/api/data')
# def get_data():
#     data = {'message': 'Hello from Flask backend!'}
#     return jsonify(data)

# @app.route('/api/submit', methods=['POST'])
# def submit_data():
#     data = request.get_json()
#     print(data)
#     return jsonify({'message': 'Data received successfully!'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from googleapiclient.discovery import build

app = Flask(__name__)
CORS(app)

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017"

DATABASE_NAME = "youtube_data"
COLLECTION_NAME = "videos"

YOUTUBE_API_KEY = "AIzaSyBrh3-BL3wLdf8RLz8GaZXVmnF9amooPjA"  #API key need to add
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# MongoDB Client
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
videos_collection = db[COLLECTION_NAME]

@app.route('/')
def home():
    return jsonify("Welcome to the Flask application!")

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from Flask backend!'}
    return jsonify(data)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Data received successfully!'})


@app.route('/api/search_youtube', methods=['POST'])
def search_youtube():
    try:
        search_query = request.get_json()['query']
        request1 = youtube.search().list(
            part="snippet",
            maxResults=10,  # You can adjust the number of results
            q=search_query,
            type="video"
        )
        response = request1.execute()

        video_ids = [item['id']['videoId'] for item in response['items'] if item['id']['kind'] == 'youtube#video']

        video_details = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        videos = []
        for item in video_details['items']:
            video = {
                'video_id': item['id'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'thumbnail': item['snippet']['thumbnails']['default']['url'],
                'views': item['statistics']['viewCount'],
                'likes': item['statistics'].get('likeCount', 0),  # Handle cases where likeCount is not available
                'comments': item['statistics'].get('commentCount', 0)  # Handle cases where commentCount is not available
            }
            videos.append(video)

        return jsonify(videos)
    except Exception as e:
        return jsonify({'error': str(e)})

    
@app.route('/api/save_video', methods=['POST'])
def save_video():
    video_data = request.get_json()
    try:
        videos_collection.insert_one(video_data)
        return jsonify({'message': 'Video saved to MongoDB!'})
    except Exception as e:
        return jsonify({'error': str(e)})
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
