# Elst test

# Virtualenv
virtualenv venv

Linux: source venv/bin/activate

# Dependencies
MongoDB

# Requirements
pip install -r requirements.txt

# Run project
Linux: cd elst/

uvicorn main:app

# Docs
localhost:8000/docs