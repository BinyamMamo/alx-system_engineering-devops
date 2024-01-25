# 0x1A. Application server

<img src="https://files.realpython.com/media/flask-nginx-gunicorn-architecture.012eb1c10f5e.jpg">

This project is about installing an application server (gunicorn) on our own servers and serving dynamic content with it. The goal of this project is to add this piece to our infrastructure, plug it to Nginx and make it serve our Airbnb clone project.

| Task | Files | Description |
| ---- | ----- | ----------- |
| 0. Set up development with Python | 2-app_server-nginx_config, 3-app_server-nginx_config, 4-app_server-nginx_config, 5-app_server-nginx_config | Configure Nginx to serve the Flask app on port 5000 |
| 1. Set up production with Gunicorn | gunicorn.conf | Configure Gunicorn to run the Flask app with 3 workers |
| 2. Serve a page with Nginx | 2-app_server-nginx_config | Configure Nginx to proxy requests to Gunicorn |
| 3. Add a route with query parameters | 4-app_server-nginx_config | Add a route to the Flask app that accepts two numbers and an operator as query parameters and returns the result of the calculation |
| 4. Let's do this for your API | 5-app_server-nginx_config | Configure Nginx to serve the API from the previous project on port 5001 |
| 5. Serve your AirBnB clone | 5-app_server-nginx_config | Configure Nginx and Gunicorn to serve the AirBnB clone web app |
