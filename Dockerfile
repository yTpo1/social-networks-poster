FROM python:3.6-alpine
WORKDIR '/usr/src/app'

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && touch /var/log/hello_soc.log

COPY . .

#CMD ["python", "main.py", "-h"]
CMD chown root:root /etc/crontabs/root && /usr/sbin/crond -f
