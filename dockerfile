FROM python:3-alpine

# alpine uses apk instead of apt-get
RUN apk update && apk add --no-cache python3 py3-pip bash 
WORKDIR /app
COPY ["requirements.txt", "rds.py", "input.sh", "./"] 
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x input.sh
#ENTRYPOINT ["bash", "input.sh"]

