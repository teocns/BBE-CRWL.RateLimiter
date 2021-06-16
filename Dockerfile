  
FROM python:3


RUN apt update -y && \
    apt install -y python3-pip && \ 
    apt install - build-essential && \ 
    apt install -y python3-dev 



COPY . .


RUN pip3 install --no-cache-dir -r  /requirements.txt

EXPOSE 5071



CMD ["uwsgi", "--plugin" , "python" , "--ini-paste", "uwsgi.ini"]


