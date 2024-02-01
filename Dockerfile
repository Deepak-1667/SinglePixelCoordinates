FROM python:3.10.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools
RUN pip install tensorflow==2.14.0
RUN python -m pip install -r requirements.txt --extra-index-url https://pypi.org/simple

# code
COPY code /app/code 

# Models
COPY models /app/models 

# Datasets  
COPY datasets /app/datasets

VOLUME [ "/app/datasets" ]  


CMD [ "python", "/app/code/main.py" ]