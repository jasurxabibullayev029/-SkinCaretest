bind = "0.0.0.0:$PORT"
workers = 3
worker_class = "sync"
timeout = 120
chdir = "."  # Set the working directory to the project root
wsgi_app = "app:application"  # Point to our app.py file
