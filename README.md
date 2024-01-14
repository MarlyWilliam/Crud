# Flask CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application using Flask. It provides API endpoints to manage items in a dataset.

## Table of Contents

- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Rate Limiting](#rate-limiting)
- [Additional Notes](#additional-notes)

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MarlyWilliam/Crud.git
   cd Crud
   ```

2. **Create a Virtual Environment:**

To manage dependencies and isolate your project's environment, it's recommended to use a virtual environment. Follow the steps below to create one:

- On Windows:

```bash
python -m venv venv
```

- On macOS/Linux:

```bash
python3 -m venv venv
```

3. **Activate the Virtual Environment:**

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Application
Run the Flask application by executing the following command in the project directory:

```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

## Running Tests
Run the tests using the following command:

```bash
pytest
```
Make sure to have the virtual environment activated before running the tests.



## API Endpoints
- Create Item:

   - Endpoint: **/items** (POST)  
   - Rate Limit: 5 requests per minute
   - Example: 
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name":"Example Item","description":"Test Description","price":10.99}' http://127.0.0.1:5000/items

- Read All Items:

   - Endpoint: **/items** (GET)
   - Rate Limit: 10 requests per minute
   - Example: 
   ```bash
   curl http://127.0.0.1:5000/items

- Read Item:

   - Endpoint: **/items/<item_id>** (GET)
   - Rate Limit: 10 requests per minute
   - Example: 
   ```bash
   curl http://127.0.0.1:5000/items/1

- Update Item:

   - Endpoint: **/items/<item_id>** (PUT)
   - Rate Limit: 5 requests per minute
   - Example: 
   ```bash
   curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Item","description":"Updated Description","price":19.99}' http://127.0.0.1:5000/items/1

- Delete Item:

   - Endpoint: **/items/<item_id>** (DELETE)
   - Rate Limit: 5 requests per minute
   - Example: 
   ```bash
   curl -X DELETE http://127.0.0.1:5000/items/1


## Rate Limiting
API endpoints have rate limiting to prevent abuse:

- Create Item: 5 requests per minute
- Read All Items: 10 requests per minute
- Read Item: 10 requests per minute
- Update Item: 5 requests per minute
- Delete Item: 5 requests per minute

## Additional Notes
- The application is using an in-memory data structure to store items. In a production environment, consider using a database.