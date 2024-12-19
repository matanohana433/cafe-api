# ☕ Cafe API

## 🌟 Overview

The **Cafe API** is a Flask-based RESTful API that provides access to a database of cafes. Users can retrieve random cafes, search for cafes by location, add new cafes, update coffee prices, and report closed cafes. The API is designed for flexibility and ease of integration with frontend or mobile applications.

---

## 🛠 Features
* **Retrieve Cafes**:
  - Get a random cafe.
  - Retrieve all cafes in the database.
  - Search cafes by location.
* **Manage Cafes**:
  - Add new cafes to the database.
  - Update the coffee price of a cafe.
  - Delete cafes using secure API key authorization.
* **JSON Responses**:
  - All responses are returned in JSON format for easy integration.

---

## 📂 Project Structure

    .
    ├── app.py                 # Main Flask application
    ├── templates/             # HTML templates
    │   ├── index.html         # Homepage template
    ├── cafe.db                # SQLite database for storing cafe details
    ├── requirements.txt       # Project dependencies
    ├── README.md              # Project documentation

---

## 🔧 Setup Guide

**Prerequisites**
* Python 3.x installed.

**Installation**

1. Clone this repository:

    ```bash
    git clone https://github.com/matanohana433/cafe-api.git
    cd cafe-api
    ```

2. Create and activate a virtual environment (optional but recommended):

**Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

**macOS/Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Set up environment variables:

   * Create a `.env` file or set variables manually:

    ```plaintext
    TopSecretAPIKey=your_top_secret_api_key
    ```

---

## 🚀 Usage

1. **Run the Application**:

    
    python app.py
    

2. **Access the API**:

   - Open a web browser or API client (e.g., Postman) and use the endpoints below.

---

## 🔗 API Endpoints

### Base URL
```
http://127.0.0.1:5000
```

### Endpoints Overview
- **GET `/random`**: Get a random cafe.
- **GET `/all`**: Retrieve all cafes.
- **GET `/search?loc=<location>`**: Search cafes by location.
- **POST `/add`**: Add a new cafe.
- **PATCH `/update-price/<int:cafe_id>?new_price=<price>`**: Update a cafe's coffee price.
- **DELETE `/report-closed/<int:cafe_id>?TopSecretAPIKey=<your_api_key>`**: Delete a cafe (API key required).

---

## 📑 API Documentation

Detailed API documentation, including request and response examples, is available in **Postman**:
[Postman Documentation](https://web.postman.co/workspace/My-Workspace~0dfa0c46-30e4-4444-8beb-ca2f69a51050/documentation/37162890-a0c6b8e5-f399-48e2-897c-b574c8faf732)

---

## 🌟 Key Features

1. **RESTful Design**:
   - Adheres to REST principles for intuitive integration.
2. **Secure Deletions**:
   - API key required for deleting cafes.
3. **Dynamic Data**:
   - Retrieve, search, and manage cafes with minimal effort.

---

## 🚀 Future Enhancements

1. Add user authentication for personalized cafe lists.
2. Implement advanced search filters (e.g., WiFi availability, price range).
3. Extend database support to PostgreSQL or MySQL.

---

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** [matanohana433](https://github.com/matanohana433)

--- 
