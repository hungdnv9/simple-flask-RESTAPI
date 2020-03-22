# Simple Python Flask REST API

# Setup
```shell
pip install -r requirements.txt
```

# Method: 
- Get(GET)
```shell
# GET all object
$ curl -X GET http://127.0.0.1:5000/api/v1/resources/roles -i
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 140
Server: Werkzeug/1.0.0 Python/3.7.5
Date: Sun, 22 Mar 2020 09:12:42 GMT

[
  {
    "group": "System", 
    "id": 1, 
    "name": "hungdnv9"
  }, 
  {
    "group": "Dev", 
    "id": 2, 
    "name": "khanhhv"
  }
]

# GET by object id
$ curl -X GET http://127.0.0.1:5000/api/v1/resources/roles/1 -i
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 59
Server: Werkzeug/1.0.0 Python/3.7.5
Date: Sun, 22 Mar 2020 09:13:08 GMT

{
  "group": "System", 
  "id": 1, 
  "name": "hungdnv9"
}

```
- Create(POST)
```shell
# Create user sontt, group system
$ curl -i -H "Content-Type: application/json" -X POST -d '{"name":"sontt", "group": "System"}' http://127.0.0.1:5000/api/v1/resources/roles
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 89
Server: Werkzeug/1.0.0 Python/3.7.5
Date: Sun, 22 Mar 2020 09:13:46 GMT

{
  "role": {
    "group": "System", 
    "name": "sontt"
  }, 
  "status": "susccess"
}

hungdnv@epson 16:13:46 ~/data/simple-flask-api/api 
$ curl -X GET http://127.0.0.1:5000/api/v1/resources/roles
[
  {
    "group": "System", 
    "id": 1, 
    "name": "hungdnv9"
  }, 
  {
    "group": "Dev", 
    "id": 2, 
    "name": "khanhhv"
  }, 
  {
    "group": "System", 
    "id": 3, 
    "name": "sontt"
  }
]
```
- Update(PUT)
```shell
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"name": "hungdnv9", "group": "DevOps"}' http://127.0.0.1:5000/api/v1/resources/roles/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 92
Server: Werkzeug/1.0.0 Python/3.7.5
Date: Sun, 22 Mar 2020 09:14:52 GMT

{
  "role": {
    "group": "DevOps", 
    "name": "hungdnv9"
  }, 
  "status": "susccess"
}

hungdnv@epson 16:14:52 ~/data/simple-flask-api/api 
$ curl -X GET http://127.0.0.1:5000/api/v1/resources/roles/1
{
  "group": "DevOps", 
  "id": 1, 
  "name": "hungdnv9"
}
```
- Delete(DELETE)

```shell
$ curl -X DELETE http://127.0.0.1:5000/api/v1/resources/roles/3 -i
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 76
Server: Werkzeug/1.0.0 Python/3.7.5
Date: Sun, 22 Mar 2020 09:15:46 GMT

[
  {
    "action": "delete", 
    "id": 3, 
    "status": "susccess"
  }
]

hungdnv@epson 16:15:54 ~/data/simple-flask-api/api 
$ curl -X GET http://127.0.0.1:5000/api/v1/resources/roles
[
  {
    "group": "DevOps", 
    "id": 1, 
    "name": "hungdnv9"
  }, 
  {
    "group": "Dev", 
    "id": 2, 
    "name": "khanhhv"
  }
]

```

# Ref
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask