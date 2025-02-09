# YouTube Search Application

## Overview

This is an Angular-based web application that allows users to search for videos on YouTube, view video details, and save their favorite videos to a MongoDB database. The application utilizes the YouTube Data API for searching and retrieving video information, a Flask backend to handle API requests and database interactions, and a MongoDB database to store saved videos.

## Features

*   **YouTube Search:** Search for videos on YouTube using keywords or phrases.
*   **Video Details:** View video thumbnails, titles, descriptions, view counts, like counts, and comment counts.
*   **Save Videos:** Save your favorite videos to a MongoDB database for later viewing.
*   **Responsive Design:** The application is designed to be responsive and accessible on various devices.

## Technologies Used

*   **Frontend:**
    *   Angular
    *   Bootstrap (or your CSS framework)
    *   HTML
    *   CSS
    *   TypeScript
*   **Backend:**
    *   Flask
    *   Flask-CORS
    *   Python
*   **Database:**
    *   MongoDB
    *   PyMongo

## Prerequisites

Before running the application, ensure you have the following installed:

*   **Node.js and npm:** [https://nodejs.org/](https://nodejs.org/)
*   **Python:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **MongoDB:** [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

## Installation

1.  **Clone the repository:**

    ```
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install frontend dependencies:**

    ```
    cd frontend
    npm install
    ```

3.  **Install backend dependencies:**

    ```
    cd backend
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    *   Create a `.env` file in the `backend` directory.
    *   Add the following variables to the `.env` file:

        ```
        MONGO_URI="mongodb://localhost:27017/"  # Replace with your MongoDB URI
        YOUTUBE_API_KEY="YOUR_YOUTUBE_API_KEY"  # Replace with your YouTube Data API key
        ```

## Configuration

1.  **YouTube Data API Key:**

    *   Obtain a YouTube Data API key from the Google Cloud Console: [https://console.cloud.google.com/](https://console.cloud.google.com/)
    *   Enable the YouTube Data API v3 for your project.
    *   Replace `"YOUR_YOUTUBE_API_KEY"` in the `.env` file with your actual API key.

2.  **MongoDB URI:**

    *   Ensure that your MongoDB server is running.
    *   Replace `"mongodb://localhost:27017/"` in the `.env` file with your MongoDB connection URI if necessary.

## Running the Application

1.  **Start the backend server:**

    ```
    cd backend
    python app.py
    ```

2.  **Start the frontend development server:**

    ```
    cd frontend
    ng serve --open
    ```

    This will open the application in your default browser.

## API Endpoints

The backend provides the following API endpoints:

*   `POST /api/search_youtube`: Searches for videos on YouTube based on a query.
    *   Request body: `{ "query": "search_term" }`
    *   Response: A JSON array of video objects with details like `video_id`, `title`, `description`, `thumbnail`, `views`, `likes`, and `comments`.
*   `POST /api/save_video`: Saves a video to the MongoDB database.
    *   Request body: A JSON object containing video details.
    *   Response: `{ "message": "Video saved to MongoDB!" }` on success, or an error message on failure.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
