
#  FastAPI Projects

> Repository with projects using FastAPI as a base.

![](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

##  Requirements (Prerequisites)

Libs used in the development of projects.

* Python 3.8+ [Install](https://www.python.org/downloads/)
* FastAPI [Install](https://fastapi.tiangolo.com/)

##  Installation

```
$ pip install requirements.txt
```

##  Screenshots



##  Features


Basically they are APIs connected to the database.

##  Usage example

Create a file main.py with:

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```