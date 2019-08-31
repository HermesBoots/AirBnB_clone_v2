# Holberton AirBnB Clone Engine Package

Jump to [`storage`](#storage-module) [`file_storage`](#file_storage-module)

## Storage Module

### Classes

#### Storage

```python
class Storage (ABC)
```

Known Subclasses:
* [`FileStorage`](#filestorage)

As `Storage` is an abstract class, it cannot be instantiated directly. Instead, it serves as the base class for the rest of the storage engine classes. It defines methods for adding, retrieving, deleting, and saving data model objects. Mutating objects can be achieved by retrieving them and modifying them afterward, since all known data model classes are fully mutable.

Keep in mind that changes to objects, as well as calls to [`new`](#storage-new) and [`delete`](#storage-delete), are not immediately reflected in persistent storage. Use [`save`](#storage-save) to commit your changes.

---

##### Method Summary

| Method | Description |
| ------ | ----------- |
| [`__contains__(self, obj)`](#storage-__contains__) | check if an object exists in storage |
| [`add(self, cls=None)`](#storage-all) | get all stored objects |
| [`delete(self, obj, id=None)`](#storage-delete) | delete an object in storage |
| [`get(self, cls, id)`](#storage-get) | retrieve an object from storage |
| [`new(self, obj)`](#storage-new) | add a new object to storage |
| [`reload(self)`](#storage-reload) | reload objects and discard changes |
| [`save(self)`](#storage-save) | commit changes to stored objects |
| [`tryGet(self, cls, id, default)`](#storage-tryget) | try retrieving an object with a fallback vaulue |

---

##### Method Details

###### Storage. \_\_contains\_\_

```python
@abstractmethod
def __contains__(self, obj: models.base_model.BaseModel) -> bool
```

Exceptions:
* none

Check if an object exists in storage, returning `True` if that object is stored and `False` if it isn't. This method is called automatically when the `in` or `not in` operator is used, allowing you to write something like `if State(id='1234') in storage:`.

`Storage` subclasses must be able to find stored objects this way when `obj` has the same type and ID as a stored object. Subclasses may also support other types for `obj`.

---

###### Storage. all

```python
def all(self, cls: Union[str, Type[models.base_model.BaseModel]] = None) -> Dict[str, models.base_model.BaseModel]
```

Exceptions:
* none

Return all stored data model objects as a dictionary, optionally only those with the type or type name given in `cls`. The keys in this dictionary are strings that consist of the object's class name, then a dot, then the object's ID. The values in the dictionary are references to the objects used by the storage engine, so changing them will affect the contents of persistent storage.

---

###### Storage. delete

```python
@abstractmethod
def delete(self, obj: Union[type, str, models.base_model.BaseModel], id: [UUID, str]) -> None
```

Exceptions:
* `KeyError` if `id` is given and the identified object is not in storage
* `TypeError` if `obj` is not an instance of [`BaseModel`](../#basemodel) and `id` is not given

Delete an object from storage. Since data model objects of different types are often stored in different locations, you must pass the object's class as well as its ID (if you aren't passing the object itself).

Remember that deleted objects are not removed from persistent storage immediately; see [`save`](#Storage-save).

---

###### Storage. get

```python
@abstractmethod
def get(self, cls: Union[type, str], id: Union[UUID, str]) -> models.base_model.BaseModel
```

Exceptions:
* `KeyError` if the identified object isn't in storage

Retrieve an object from storage. Since data model objects of different types are often stored in different locations, you must pass the object's class as well as its ID.

---

###### Storage. new

```python
@abstractmethod
def new(self, obj: models.base_model.BaseModel) -> None
```

Exceptions:
* none

Add a new object to storage. Using this method to modify stored objects is not recommended and may cause issues. Instead use the workflow described in the `Storage` class summary.

Remember that new objects aren't added to persistent storage immediately; see [`save`](#Storage-save).

---

###### Storage .reload

```python
@abstractmethod
def reload(self) -> None
```

Exceptions:
* varies depending on subclass

Reload objects from storage into memory, also discarding any un-saved changes.

Subclasses that use a sophisticated storage system like an SQL database may not do any work to load objects from storage, but must still discard changes.

---

###### Storage. save

```python
@abstractmethod
def save(self) -> None
```

Exceptions:
* varies depending on subclass

Commit in-memory changes to stored objects into some persistent storage medium. This allows you to bundle small changes together, removing the need to run expensive disk IO or database accesses for every change.

---

###### Storage. tryGet

```python
@abstractmethod
def tryGet(self, cls: Union[type, str], id: Union[UUID, str], default: Any) -> Any
```

Exceptions:
* none

Try to retrieve an object and return it, but return `default` instead if the identified object does not exist in storage. Since data model objects of different types are often stored in different locations, you must pass the object's class as well as its ID.

---

## DB\_Storage Module

### Classes

#### DBStorage

```python
class DBStorage (models.engine.storage.Storage)
```

`DBStorage` implements all abstract methods of [`Storage`](#storage) and thus can be instantiated. However, this isn't very useful, since it uses class fields to connect to the database and none of the methods use their `self` parameters. Using this class like `DBStorage.get(None, 'City', '1234')` works just fine. This means a running application may only use one database.

This storage engine uses a MySQL server that may be local or remote. The connection uses these environment variables:

| `HBNB_MYSQL_USER` | user name |
| `HBNB_MYSQL_PASS` | pass phrase |
| `HBNB_MYSQL_HOST` | server host name / address |
| `HBNB_MYSQL_DB` | name of database |

In addition, if the environment variable `HBNB_ENV` is set to "test", the database is emptied completely before it is used.

SQLAlchemy ORM is used to represent the database records as Python objects. Relationships between the data models are enforced by MySQL, so don't commit any changes until all new instances have their constraints satisfied.

---

##### Method Summary

| Method | Description |
| ------ | ----------- |
| [`__contains__(self, obj)`](#storage-__contains__) | check if an object is in storage |
| [`all(self, cls=None)`](#dbstorage-all) | get all stored objects |
| [`delete(self, cls, id)`](#storage-delete) | delete an object from storage |
| [`get(self, cls, id)`](#storage-get) | retrieve an object from storage |
| [`new(self, obj)`](#storage-new) | add a new object to storage |
| [`reload(self)`](#dbstorage-reload) | reload objects from storage and discard changes |
| [`save(self)`](#dbstorage-save) | save changes to storage |
| [`tryGet(self, cls, id, default)`](#storage-tryget) | try to retrieve an object from storage with a fallback value |

---

##### Method Details

###### DBStorage. all

```python
def all(self, cls: Union[str, Type[models.base_model.BaseModel]] = None) -> Dict[str, models.base_mode.BaseModel]
```

Exceptions:
* `sqlalchemy.exc.SQLAlchemyError` if [`reload`](#dbstorage-reload) has not been called or the connection has failed

Return all stored data model objects as a dictionary. The keys in this dictionary are strings that consist of the object's class name, then a dot, then the object's ID. While these keys are created just for this method, the values in the dictionary are references to the real ORM objects and thus changing them will affect the database (once those changes are saved).

---

###### DBStorage. reload

```python
def reload(self) -> None
```

Exceptions:
* `sqlalchemy.exc.SQLAlchemyError` if the connection variables are incorrect or the connection can not be established

Reload all objects from the database. If any data model tables are missing, this method first creates them. All pending changes are discarded.

---

###### DBStorage. save

```python
def save(self) -> None
```

Exceptions:
* `sqlalchemy.exc.SQLAlchemyError` if the connection fails or if pending changes violate database constraints

Commit all pending changes to the database. Be careful with relationship constraints (foreign keys): if a state object can't exist without residing in a city object, then the construction of a city will always be allowed, but it will fail to save if it is not affiliated with a state.

---

## File\_Storage Module

### Functions

#### file\_storage. key

```python
def key(cls: Union[type, str], id: Union[UUID, str]) -> str
```

Exceptions:
* none

Return a string formatted for use as a key with the `FileStorage` class. These keys are used internally, but it can also be convenient to use this function with [`FileStorage.__contains__`](#filestorage-__contains__) rather than construct a dummy data model object.

---

### Classes

#### FileStorage

```python
class FileStorage (models.engine.storage.Storage)
```

`FileStorage` implements all abstract methods of [`Storage`](#storage) and thus can be instantiated. However, this isn't very useful, since it uses class fields to keep track of stored objects and none of the methods use the `self` parameter. Using this class like `FileStorage.get(None, 'BaseModel', '1234')` works just fine. This means the entire project shares a storage file, so be wary of conflicting changes between multiple pieces of code that use this class.

This storage engine uses a local JSON file in the working directory of the project with a fixed name: "storage.json". All stored objects are loaded into memory at once and kept in a single dictionary, where they keys are strings consisting the object's class name, then a dot, then the object's ID.

This storage engine is slow and is a memory hog, but it is easy to implement and easy to debug, so it's useful when testing other parts of the project.

---

##### Method Summary

| Method | Description |
| ------ | ----------- |
| [`__contains__(self, obj)`](#filestorage-__contains__) | check if an object is in storage |
| [`all(self)`](#storage-all) | get all stored objects |
| [`delete(self, cls, id)`](#storage-delete) | delete an object from storage |
| [`get(self, cls, id)`](#storage-get) | retrieve an object from storage |
| [`new(self, obj)`](#storage-new) | add a new object to storage |
| [`reload(self)`](#filestorage-reload) | reload objects from storage and discard changes |
| [`save(self)`](#filestorage-save) | save changes to storage |
| [`tryGet(self, cls, id, default)`](#storage-tryget) | try to retrieve an object from storage with a fallback value |

---

##### Method Details

###### FileStorage. \_\_contains\_\_

```python
def __contains__(self, obj: Union[models.base_model.BaseModel, str])
```

Exceptions:
* none

In addition to the mandatory behavior of [`Storage.__contains__`](#storage-__contains__), this method allows `obj` to be a string in the format returned by [`key`](#file_storage-key).

---

###### FileStorage. reload

```python
def reload(self) -> None
```

Exceptions:
* `OSError` if the storage file cannot be read
* `ValueError` if the storage file is not valid JSON

Reload all objects from a file called "storage.json" in the working directory into an internal dictionary, discarding any un-saved changes. If this file does not exist, instead do nothing.

---

###### FileStorage. save

```python
def save(self) -> None
```

Exceptions:
* `OSError` if the storage file cannot be written to
* `TypeError` if one of the objects contains a value that is not JSON-serializable

Save all objects in memory to a file called "storage.json" in the working directory. If this file doesn't exist, create it first. If it exists, first truncate it so it is empty.
