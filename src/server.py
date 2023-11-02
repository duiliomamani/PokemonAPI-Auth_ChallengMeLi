import os
from app import create_app
from dotenv import load_dotenv

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
app = create_app(os.getenv("FLASK_ENV") or "default")


def main():
    app.run()


if __name__ == "__main__":
    main()
