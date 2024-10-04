import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_ACCESS_KEY_ID = os.getenv('')
    AWS_SECRET_ACCESS_KEY = os.getenv('')
    REGION_NAME = os.getenv('', 'ap--1')  # Default to 'ap-south-1'

    @staticmethod
    def init_app(app):
        pass
