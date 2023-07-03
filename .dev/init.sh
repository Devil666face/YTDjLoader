#/bin/bash
mkdir python
tar -xf .dev/python-3.10.8-debian10.tgz -C python
./python/bin/python3.10 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .dev/cipher.py venv/lib/python3.10/site-packages/pytube/cipher.py
# Generate ssl for dev
# openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt