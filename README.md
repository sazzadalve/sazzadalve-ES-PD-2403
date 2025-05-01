# ES-PD-2403-SMS-Project

A Django-based Student Management System.

## Installation & Setup

Follow these steps to clone and run the project locally.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ES-PD-2403-SMS-Project
```

### 2. Create a Virtual Environment
```bash
python -m venv env
```
Activate the virtual environment:
- **Windows:**  
  ```bash
  env\Scripts\activate
  ```
- **Mac/Linux:**  
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 6. Run the Development Server
```bash
python manage.py runserver
```
The project should now be accessible at `http://127.0.0.1:8000/`

## Project Structure
```
ES-PD-2403-SMS-Project/
├── Project_Config/       # Django project settings and configuration
├── student_management_app/  # Main application logic
├── env/                 # Virtual environment (not included in Git)
├── db.sqlite3           # Database file (if using SQLite)
├── manage.py            # Django management script
├── requirements.txt     # Dependencies file
```

## Troubleshooting
- If dependencies are missing, run `pip install -r requirements.txt` again.
- If migrations fail, try `python manage.py makemigrations` followed by `python manage.py migrate`.
- If the server does not start, ensure the virtual environment is activated.

## Contributing
Pull requests are welcome. Please ensure changes are tested before submission.

## License
This project is licensed under the MIT License.
