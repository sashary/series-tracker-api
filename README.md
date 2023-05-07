# Series Tracker API
A WIP GraphQL API that utilizes AWS DynamoDB, Docker, and GraphQL to store a user's reading list and the last chapter (or page) read. Refer to the client version for the web app (currently not available).

This is mostly a personal project to experiment with [Strawberry](https://strawberry.rocks/) and the AWS ecosystem. I've also lost track of too many series and books I've been reading due to bad bookingmarking habits, woops 🤷.

## Setup
- Install the latest Python version
- Set a venv and install the python libraries

(Mac/Linux)
```
python3 -m venv venv
source ./venv/bin/activate 
```
(Windows)
```
python3 -m venv venv
.\venv\Scripts\activate 
```
- Install requirements.txt
```
pip install -r requirements.txt
```

## Run the server
Using uvicorn, you can run the server locally by using:
```
uvicorn main:app --reload
```
(At the moment, AWS DynamoDB is required to store/retrieve items. Refer to the next section for more details)

## Environment Variables
Because the server uses AWS infastructure, there are some things that must be done beforehand if you want to get the server working (In the near future, support for MongoDB and MySQL will be added).

- An AWS DynamoDB table must be created with a partition key called `id` and sort key called `type`. 
- Create a dotenv file that fills out the `.env.sample` variables.