# Simple Ecommerce Store

A simple ecommerce website built with Python and Flask.

## Features

- Product listing
- Product details
- Shopping cart
- Mock checkout

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/`

## Project Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: CSS and static files
- `requirements.txt`: Python dependencies

## Deployment to Azure App Service

1. Create an Azure App Service (Web App) in the Azure Portal
2. Set runtime stack to Python 3.9+ (or latest)
3. In Configuration > General settings, set Startup Command: `gunicorn --bind=0.0.0.0 --timeout 600 app:app`
4. Deploy your code via Git (connect to this repo) or ZIP upload
5. Set environment variables in Configuration > Application settings:
   - `SECRET_KEY`: A secure random string
   - `FLASK_ENV`: production

## Note

This is a basic implementation. In a real application, you would need to add:
- Database for products and orders
- User authentication
- Payment integration
- Security measures