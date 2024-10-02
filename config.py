import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_ACCESS_KEY_ID = os.getenv('AKIASIVGK4BWSJKUAZL7')
    AWS_SECRET_ACCESS_KEY = os.getenv('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')
    REGION_NAME = os.getenv('AWS_REGION', 'ap-south-1')  # Default to 'ap-south-1'

    @staticmethod
    def init_app(app):
        pass
