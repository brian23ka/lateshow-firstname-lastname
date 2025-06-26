# Late Show API 🎤

**Phase 4 Code Challenge | Flatiron School**

This Flask API models episodes of a late-night show and their guest appearances. It allows retrieval of episodes and guests, as well as creation of new guest appearances with rating validation.

---

## 📁 Repository Structure

```
lateshow-your-name/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── seed.py
├── migrations/
├── instance/
├── challenge-4-lateshow.postman_collection.json
├── guests.csv
├── config.py
├── README.md
└── requirements.txt
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/brian23ka/lateshow-firstname-lastname
cd lateshow-firstname-lastname
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pipenv install -r requirements.txt
```

### 4. Set up the database

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 5. Seed the database

```bash
python seed.py
```

---

## 📬 Postman Testing

Import the provided Postman collection:

- File: `challenge-4-lateshow.postman_collection.json`
- [How to import a Postman collection](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/)

---

## 📘 Models and Relationships

- **Episode**
  - `id`, `date`, `number`
  - has many **Guests** through **Appearances**

- **Guest**
  - `id`, `name`, `occupation`
  - has many **Episodes** through **Appearances**

- **Appearance**
  - `id`, `episode_id`, `guest_id`, `rating`
  - belongs to **Episode** and **Guest**
  - cascade deletes configured

---

## ✅ Validations

**Appearance**
- `rating`: must be between 1 and 5 (inclusive)

---

## 🔗 API Endpoints

### `GET /episodes`

**Response:**

```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]
```

---

### `GET /episodes/:id`

**Success Response:**

```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
```

**Error Response:**

```json
{
  "error": "Episode not found"
}
```

---

### `GET /guests`

**Response:**

```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  },
  {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
]
```

---

### `POST /appearances`

**Request Body:**

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```

**Success Response:**

```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "date": "1/12/99",
    "id": 2,
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

**Validation Error Response:**

```json
{
  "errors": ["rating must be between 1 and 5"]
}
```

---

## 🧪 Testing

- Test all endpoints using Postman.
- Use `guests.csv` to seed the database with sample guest data.

---

## 🧹 Features Summary

| Feature                     | Status ✅ |
|----------------------------|-----------|
| Models with relationships  | ✔️        |
| Cascading deletes          | ✔️        |
| Validations on Appearance  | ✔️        |
| JSON serialization         | ✔️        |
| Full CRUD for episodes     | Partial   |
| POST route for appearances | ✔️        |

---

## 🛠 Tech Stack

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- Marshmallow (for serialization)

---

## 👨‍💻 Author

- **Your Name**
- GitHub: [@brian23ka](https://github.com/brian23ka)

---

## 📝 License

This project is part of the Flatiron School curriculum and is intended for educational purposes only.
