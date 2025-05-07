# 🏥 Healthcare Backend System

This project is a backend system for a healthcare application built with **Django**, **Django REST Framework**, and **PostgreSQL**. It supports user authentication, patient and doctor management, and patient-doctor mappings using secure and RESTful APIs.

---

## 🚀 Features

- JWT authentication
- Secure user registration and login
- Patient and doctor CRUD operations
- Mapping between patients and doctors
- PostgreSQL database integration
- Django ORM and REST Framework usage
- Environment-based configuration management

---

## 🛠 Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt

---

## 📦 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # or `env\Scripts\activate` on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database and configure `.env`**  
   Create a `.env` file:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication Endpoints

- `POST /api/auth/register/` — Register a new user
- `POST /api/auth/login/` — Login and get JWT token

---

## 👨‍⚕️ Patient Management Endpoints

- `POST /api/patients/` — Add a new patient (Authenticated only)
- `GET /api/patients/` — List all patients (Authenticated only)
- `GET /api/patients/<id>/` — Get details of a patient
- `PUT /api/patients/<id>/` — Update a patient
- `DELETE /api/patients/<id>/` — Delete a patient

---

## 👩‍⚕️ Doctor Management Endpoints

- `POST /api/doctors/` — Add a new doctor (Authenticated only)
- `GET /api/doctors/` — List all doctors
- `GET /api/doctors/<id>/` — Get details of a doctor
- `PUT /api/doctors/<id>/` — Update a doctor
- `DELETE /api/doctors/<id>/` — Delete a doctor

---

## 🔗 Patient-Doctor Mapping Endpoints

- `POST /api/mappings/` — Assign a doctor to a patient
- `GET /api/mappings/` — List all mappings
- `GET /api/mappings/<patient_id>/` — Get all doctors for a specific patient
- `DELETE /api/mappings/<id>/` — Remove a doctor from a patient

---

## 🧪 Testing the API

Use Postman, Insomnia, or any API client. For authenticated routes, include the JWT token in the `Authorization` header:

```http
Authorization: Bearer <your_token>
```

---

## ✅ Expected Outcome

- Users can register and log in securely.
- Authenticated users can manage patients and doctors.
- Doctors can be assigned to patients.
- All data is stored in PostgreSQL.

---

## 📄 License

This project is for educational purposes and is not licensed for commercial use.

---

Happy Coding! 💙
