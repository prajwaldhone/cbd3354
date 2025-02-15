from flask import Flask, jsonify
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Retrieve the MongoDB URI from the environment variable.
# This value will be securely provided at runtime (e.g., via your Docker container or GitLab CI/CD variables).
mongo_uri = os.getenv('MONGO_URI')
if not mongo_uri:
    raise ValueError("The MONGO_URI environment variable is not set.")

# Connect to MongoDB using the provided URI.
client = MongoClient(mongo_uri)
db = client["sample_mflix"]


@app.route('/')
def home():
    """
    Basic endpoint that confirms the app is running.
    It also lists the collections available in the connected database.
    """
    try:
        collections = db.list_collection_names()
    except Exception as e:
        collections = f"Error fetching collections: {e}"

    return jsonify({
        "message": "Welcome to the Flask CI/CD App!",
        "collections": collections
    })


if __name__ == '__main__':
    # Run the Flask application on all interfaces on port 5000.
    app.run(host='0.0.0.0', port=5000, debug=True)
