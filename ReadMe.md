# Django Project Setup

This guide walks you through installing Django and running your project on the `0.0.0.0` host (which exposes the app on all available network interfaces — useful for development on remote servers or Docker).

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- (Optional but recommended) `virtualenv`

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/asbn223/flutter_sabin_nakarmi_backend.git
cd flutter_sabin_nakarmi_backend
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, you can install Django directly:

```bash
pip install django
pip install django-rest-knox
pip install django-utils
pip install djangorestframework
pip install pillow
```

Then generate `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

To run the server on `0.0.0.0` (accessible externally):

```bash
python manage.py runserver 0.0.0.0:8000
```

Now your project will be accessible at `http://<your-server-ip>:8000`

## Notes

- You may need to update `ALLOWED_HOSTS` in `settings.py` to include the server IP or `'*'` during development:

```python
ALLOWED_HOSTS = ['*']  # For development only!
```

---

## Helpful Commands

```bash
# Create a superuser for admin access
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

## Security Reminder

Do **not** use `ALLOWED_HOSTS = ['*']` or run on `0.0.0.0` in a production environment without proper firewall or reverse proxy configurations.

---

Happy coding! 🚀
