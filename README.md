# Building an API for Article Management with FastAPI

A practical project that demonstrates step-by-step how to build an API for managing articles using the **FastAPI** framework. The project includes features for creating, updating, viewing, and deleting articles.

---

## **Features**

- Easily create and manage articles with a REST API.
- Beginner-friendly design for learning FastAPI.
- Practical project that can be further developed.

---

## **EndPoints - CRUD**

| Method | Endpoint               | Description                       |
|--------|------------------------|-----------------------------------|
| POST   | `/articles/`           | Create a new article              |
| GET    | `/articles/`           | Retrieve all articles             |
| PUT    | `/articles/{article_id}` | Update an existing article         |
| DELETE | `/articles/{article_id}` | Delete an article                 |


## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-article-management.git
   cd fastapi-article-management

2. Create and activate a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the dependencies:
   ```bash
    pip install -r requirements.txt

4. Run the FastAPI server:
   ```bash
    uvicorn main:app --reload


## 📺 **Check Out My YouTube Channel**  
[![Code With Mezo YouTube Channel](https://img.youtube.com/vi/bhwGIzSjq7U/0.jpg)](https://youtube.com/watch?v=bhwGIzSjq7U&t=70s)

