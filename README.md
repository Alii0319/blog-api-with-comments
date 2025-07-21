# Blog API with Comments

A RESTful blog backend built using Django and Django REST Framework.  
It supports full CRUD operations for blog posts along with nested comments.

## 🚀 Features

- Create, Read, Update, Delete blog posts
- Add and view comments on posts (nested serialization)
- Browsable API using Django REST Framework
- Ready for deployment on Render

## 📦 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite 
- Render

## 🔗 API Endpoints (Examples)

- `GET /api/posts/` – List all blog posts
- `GET /api/posts/<id>/` – Retrieve a single post with nested comments
- `POST /api/posts/` – Create a blog post
- `POST /api/posts/<id>/comments/` – Add a comment to a post
