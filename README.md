# Library Management API

This project provides a simple Library Management API built using Flask. It allows users to add, list, search, update, and delete books. The API is Dockerized for easy deployment.

## Table of Contents
1. [Project Setup](#project-setup)
2. [Docker Setup](#docker-setup)
   - [Building the Docker Image](#building-the-docker-image)
   - [Running the Docker Container](#running-the-docker-container)
3. [Swagger API Documentation](#swagger-api-documentation)
4. [API Endpoints](#api-endpoints)

---

## 1. Project Setup

To run this project locally, you need Python 3.x and the following dependencies:

- Flask
- Flask-Swagger-UI

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
Ensure you have the data.json file for book storage. You can initialize this file with an empty list or add sample book data.

## 2. Docker Setup
To easily deploy and run the API, you can use Docker. Below are the steps for building and running the Docker container.

### 2.1. Building the Docker Image
1. Clone this repository to your local machine.

2. Build the Docker image by running the following command in the root directory of the project (where the Dockerfile is located):

```bash
docker build -t library-management-api .
```

This will create a Docker image named library-management-api.

### 2.2. Running the Docker Container

1. Run the Docker container using the following command:

```bash
docker run -p 3000:3000 library-management-api
```

This will start the API inside a Docker container and expose it on port 3000 on your local machine.

2. To stop the container, use:
This will start the API inside a Docker container and expose it on port 3000 on your local machine.
To stop the container, use:

```bash
docker stop <container_id>
```
You can find the <container_id> by running docker ps.
## 3. Swagger API Documentation

Once the API is running, you can interactively test the API endpoints using the Swagger documentation.

### Accessing Swagger UI
1. Open your browser and go to:

```bash
http://localhost:3000/api-docs
```

2. This will load the Swagger UI, where you can see all available API endpoints and interact with them directly.

## 4. API Endpoints

The following API endpoints are available:
### 1. List All Books
- Method: GET
- Endpoint: /books
- Description: Lists all books in the library.
- Response: A list of all books with details like title, author, published year, etc.

### 2. Add a New Book
- Method: POST
- Endpoint: /books
- Description: Adds a new book to the library.
- Request Body:
- json

```bash
{
  "title": "Book Title",
  "author": "Author Name",
  "published_year": "2024",
  "isbn": "1234567890123",
  "genre": "Fiction"
}
```
Response: The newly added book details.

### 3. Search for Books
- Method: GET
- Endpoint: /books/search
- Description: Searches for books based on author, year, or genre.
- Query Parameters:
- author: The author of the book.
- year: The publication year.
- genre: The genre of the book.


### 4. Update a Book
- Method: PUT
- Endpoint: /books/{isbn}
- Description: Updates details of a book using its ISBN.
- Request Body:
- json
```bash
{
  "title": "Updated Book Title",
  "author": "Updated Author Name",
  "published_year": "2025",
  "genre": "Updated Genre"
}
```
Response: The updated book details.

### 5. Delete a Book
- Method: DELETE
- Endpoint: /books/{isbn}
- Description: Deletes a book from the library using its ISBN.
- Response: A confirmation message that the book has been deleted.