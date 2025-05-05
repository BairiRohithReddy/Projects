# Streamlit Username Validation and Login System

## 📝 **Project Overview**

This is a **Streamlit-based registration and login system** that focuses on solving a key problem in user registration:  
👉 **validating whether a username is already taken before allowing a user to register.**

We commonly see this flow in platforms like **Gmail, Instagram, or GitHub**, where as you type your desired username, the system checks availability **in real-time** and prevents duplicate usernames.

This project demonstrates a **small-scale implementation of that core functionality**, integrating:

✅ Username uniqueness validation  
✅ Registration of new users with password hashing  
✅ Login functionality  
✅ Simple database-backed authentication

## 💡 **Why is this a problem?**

In any system that allows users to create accounts:

- Each username (or unique identifier) must be **globally unique**
- Failing to check this properly leads to **duplicate accounts, collisions, and data inconsistency**
- Many platforms check username availability **before actually submitting the registration form**

### 🔍 In large-scale systems:

Big platforms often implement this using:

- **Caching layers** like **Redis** to store "known usernames" for fast lookup
- **Async validation on frontend** (AJAX calls to validate input on every keystroke)
- **Database constraints** to enforce uniqueness at storage level
- **Rate-limiting** & **throttling** on username validation APIs


## 🎯 **How this project addresses the problem (small scale):**

✅ Checks username availability **before registration** using a lookup in **SQLite database**  
✅ Shows immediate feedback **(upon Enter or leaving input field)** whether username is available  
✅ Prevents registration if username already exists  
✅ Ensures username uniqueness enforced **at both application logic & database constraint level**

In this project:

- We don't use caching/Redis → we query SQLite directly
- We check username availability **on field submission** (Streamlit doesn’t support keystroke-level validation without custom components)


## 🚀 **How this would scale to production:**

To handle large-scale username validation:

- Move from SQLite → **PostgreSQL / MySQL / NoSQL databases**
- Add a **caching layer (Redis/Memcached)** → check cache before hitting database
- Implement **frontend async checks (AJAX or WebSockets)** → validate on every keystroke
- Use **message queues (RabbitMQ, Kafka)** for deferred validation if needed
- Introduce **rate limiting / captcha** to prevent abuse
- Use **indexing & optimized queries** to reduce DB load

This app is a **prototype** showing how the validation workflow works at a basic level,  
but can be scaled with additional infrastructure to handle thousands or millions of users.


## 🛠️ **Tech Stack**

| Component        | Purpose                                           |
|-----------------|---------------------------------------------------|
| **Streamlit**    | Web interface / frontend app                      |
| **SQLite**       | Local lightweight relational database              |
| **Python**       | Backend programming language                      |
| **hashlib**      | Used for password hashing (SHA-256)               |


## 🧩 **System Components**

### 1️⃣ `app.py`

- Main Streamlit app
- Handles:
  - Displaying registration form
  - Displaying login form
  - Validating input
  - Providing feedback


### 2️⃣ `db_utils.py`

- Manages database operations:
  - Creating user table
  - Querying for username
  - Inserting new user records


### 3️⃣ `auth_utils.py`

- Handles authentication logic:
  - Hashing usernames/passwords
  - Validating if username exists
  - Validating login credentials


## 📝 **How to Run Locally**

1️⃣ Clone the repo:

```bash
git clone https://github.com/BairiRohithReddy/Projects.git
cd Projects/Streamlit/UsernameValidationProject
````

2️⃣ (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Run the app:

```bash
streamlit run app.py
```

App will open in your browser at `http://localhost:8501`


## 🌍 **Potential Use Cases**

✅ User registration portals
✅ Account creation forms
✅ Any system requiring **unique user IDs or handles**


## ✨ **Key Takeaways**

This project:

* Simulates username availability validation
* Shows how pre-insert checks + database constraints work together
* Demonstrates registration/login flow in a simple web app
* Acts as a foundation for scaling username validation logic


## **Limitations**

* Validation feedback occurs only after ENTER or input focus-out (Streamlit limitation without JS/Custom Components)
* Does not use Redis caching → queries DB directly every time
* Password hashing uses SHA-256 instead of stronger `bcrypt`/`argon2`


## 📈 **Next Steps for Scaling**

✅ Replace SQLite with PostgreSQL/MySQL
✅ Add Redis cache layer to reduce DB hits
✅ Implement live keystroke-level validation via JS frontend or custom Streamlit Component
✅ Use stronger password hashing algorithms (`bcrypt`, `argon2`)
✅ Add session persistence and user-specific dashboards


## 👨‍💻 **Author**

Made by [Bairi Rohith Reddy](https://github.com/BairiRohithReddy)


*This repository serves as an educational and proof-of-concept implementation of username validation and authentication workflows.*

```