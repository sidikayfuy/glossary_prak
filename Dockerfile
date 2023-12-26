FROM python:latest
COPY . /var/www/glossary
WORKDIR /var/www/glossary
RUN python3 -m venv venv & source venv/bin/activate & pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]