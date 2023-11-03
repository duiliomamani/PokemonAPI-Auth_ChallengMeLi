import os
from app import create_app
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app = create_app(os.getenv("FLASK_ENV") or "default")

def __init__():
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")

    port = int(os.environ.get("FLASK_RUN_PORT", "8080"))

    server = os.environ.get("FLASK_ENV", "development")

    if server == "development":
        app.run(host=host, port=port, debug=True)
    else:
        from waitress import serve
        serve(app, host=host, port=port)

if __name__ == "__main__":
    __init__()
