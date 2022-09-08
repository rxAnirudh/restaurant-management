import os
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv(dotenv_path='/Users/anirudh.chawla/restaurant-management/.env.dev')

class Config: 
    RZP_KEY_ID = os.getenv('RZP_KEY_ID')
    RZP_KEY_SECRET = os.getenv('RZP_KEY_SECRET')
    PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
    DB_NAME = os.getenv('DB_NAME')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    SECRET_KEY = os.getenv('SECRET_KEY')
    
