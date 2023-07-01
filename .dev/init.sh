#/bin/bash
mkdir python
tar -xf .dev/python-3.10.8-debian10.tgz -C python
./python/bin/python3.10 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .dev/cipher.py venv/lib/python3.10/site-packages/pytube/cipher.py