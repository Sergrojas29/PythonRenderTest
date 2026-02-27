from app import create_app

# Render's Gunicorn server looks for this 'app' object
app = create_app('production')