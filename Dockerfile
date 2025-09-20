FROM ubuntu:latest
LABEL authors="jkotesh"

ENTRYPOINT ["top", "-b"]
#Use Python a base image
From python:3.10-slim

#Set Working directory
WORKDIR /app
#Copy Requirements and install dependencies
Copy requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy project files into container
COPY . .

#Expose Flask Default Port
Expose 5000

#Run the Flask app
CMD ["python","app.py"]
