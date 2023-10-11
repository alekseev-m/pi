To start project:

pip install -r requirements.txt

chmod +x manage.py
./manage.py migrate
./manage.py loaddata data/fixtures/parcel.json
./manage.py runserver 127.0.0.1:8000

Query for API: <br>
http://127.0.0.1:8000/api/ <br>
http://127.0.0.1:8000/api/parcel/ <br>
http://127.0.0.1:8000/api/parcellocker/