# # from fastapi import FastAPI, Query
# # from fastapi.middleware.cors import CORSMiddleware
# # import json

# # app = FastAPI()

# # # Enable CORS
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["GET"],
# #     allow_headers=["*"],
# # )

# # # Load marks data
# # with open("q-vercel-python.json", "r") as file:  
# #     marks_list = json.load(file)
# #     # print(marks_list)

# # # Convert list to a dictionary for fast lookup
# # marks_data = {entry["name"]: entry["marks"] for entry in marks_list}

# # @app.get("/api")
# # def get_marks(name: list[str] = Query([])):
# #     result = [marks_data.get(n, None) for n in name]
# #     return {"marks": result}

# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# import json
# import os

# app = FastAPI()

# # Enable CORS to allow GET requests from any origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["GET"],
#     allow_headers=["*"],
# )

# # Load marks data (ensure this path is correct on Vercel)
# json_file_path = "q-vercel-python.json"

# # Check if the file exists
# if os.path.exists(json_file_path):
#     with open(json_file_path, "r") as file:  
#         marks_list = json.load(file)
#         # Convert list to a dictionary for fast lookup
#         marks_data = {entry["name"]: entry["marks"] for entry in marks_list}
# else:
#     marks_data = {}
# # with open("q-vercel-python.json", "r") as file:
# #     marks_list = json.load(file)
# #     print(marks_list)  # Check if your data is correctly loaded

# @app.get("/api")
# def get_marks(name: list[str] = Query([])):
#     # Log the received query names for debugging
#     print(f"Received names: {name}")
#     result = [marks_data.get(n, None) for n in name]
#     print(f"Resulting marks: {result}")
#     return {"marks": result}
import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Load student data from the JSON file
def load_data():
    with open('q-vercel-python.json', 'r') as file:
        data = json.load(file)
    return data

# Handler class to process incoming requests
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)

        # Get 'name' parameters from the query string
        names = query.get('name', [])

        # Load data from the JSON file
        data = load_data()

        # Prepare the result dictionary
        result = {"marks": []}
        for name in names:
            # Find the marks for each name
            for entry in data:
                if entry["name"] == name:
                    result["marks"].append(entry["marks"])

        # Send the response header
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS for any origin
        self.end_headers()

        # Send the JSON response
        self.wfile.write(json.dumps(result).encode('utf-8'))