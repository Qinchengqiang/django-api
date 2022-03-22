# django-api

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

#### django graphql api

## Details

- expose a GraphQL endpoint at `/graphql`.
- The GraphQL schema should consist of a single query, person, which must return a `Person` object.
- A Person object should have the following fields: `email (string)`, `name (string)`, `address (Address)`.
- An Address object should have the following fields: `number (integer)`, `street (string)`, `city (string)`, `state (GraphQL enum)`.



## Table of Contents

- [Install](#install)
- [API](#api)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install

- step1:
```
$ mkdir myApi

$ cd myApi

$ git clone https://github.com/Qinchengqiang/django-api.git

$ virtualenv env

$ source env/bin/activate
```

- step2:

open the file at `ene/lib/`
`(env/lib/python3.8/site-packages/graphene_django/utils/utils.py)`

use `force_str` to replace `force_text` at line 6 & line 29, 
change codes to 
```
from django.utils.encoding import force_str
...

def _camelize_django_str(s):
    if isinstance(s, Promise):
        s = force_str(s)
    return to_camel_case(s) if isinstance(s, six.string_types) else s
```
- step3:
```
(env) $ cd django-api

(env) $ pip3 install -r requirements.txt

(env) $ ./manage.py loaddata data.json

(env) $ python3 manage.py runserver
```
Starting development server at http://127.0.0.1:8000/
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 22, 2022 - 08:44:42
Django version 4.0.3, using settings 'clients_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


## API

go to http://127.0.0.1:8000/graphql

The following query will be used to validate your implementation:
```
query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```
then will get the result after running query:
```
{
  "data": {
    "person": [
      {
        "email": "ah@gmail.com",
        "name": "A.H",
        "address": {
          "number": 12,
          "street": "Gold St",
          "city": "Sydney",
          "state": "NSW"
        }
      },
      {
        "email": "bk@gmail.com",
        "name": "B.K",
        "address": {
          "number": 20,
          "street": "Queen St",
          "city": "Sydney",
          "state": "NSW"
        }
      },
      {
        "email": "cl@gmail.com",
        "name": "C.L",
        "address": {
          "number": 101,
          "street": "King St",
          "city": "Sydney",
          "state": "NSW"
        }
      }
    ]
  }
}
```

## Github

## Maintainers

[@Steven](https://github.com/Qinchengqiang)

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2022 Steven Qin
