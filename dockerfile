FROM python:latest

# set working directory
WORKDIR /app

# install dependencies  
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the script to the folder 
COPY . /app

# start the server
CMD ["chrome.exe", "--remote-debugging-port=9222", '--user-data-dir="C:\selenum\ChromeProfile"', "\n", "main.py"]