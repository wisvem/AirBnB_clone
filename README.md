![Airbnb clone project](https://i.imgur.com/sftSnOT.png)

# AirBnB Clone - Console
This is the first step towards building the first full web application: the AirBnB clone. The goal of this project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

![Airbnb clone project](https://i.imgur.com/ovMNyEZ.png)

#### Goal of the Command interpreter :
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/el-dani-cortes/AirBnB_clone"`
* Run hbnb(interactively): `./console` and enter commands
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - Contains the entry point of command interpreter. Commands that this console accepts: 

* `EOF` - exits console
* `quit` - exits console
* `emptyline` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id. Save the change into the JSON file. 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` --- Directory that contains main classes:
[base_model.py](/models/base_model.py) - The BaseModel class is the main class  where where other classes will be derived. This class gives the main attributes like id, created and updated time when a instance occurs.

Methods inside this class:
* `def __init__(self, *args, **kwargs)` - Initialization of the BaseModel class
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys and values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` --- Directory that contains File Storage class that manages JSON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the Test_BaseModel_class

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the Test_Amenity_class

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the Test_City_class

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the Test_Place_class

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the Test_Review_class

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the Test_State_class

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the Test_User_class

[/test_models/test_engine/test_file_storage.py](/tests/test_models/test_engine/test_file_storage.py) - Contains the Test_engine

## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time. 

## Authors
Daniel Cortes Sully - [Github](https://github.com/el-dani-cortes) / [Twitter](https://twitter.com/El_Dani_Cortes)  
Wiston Venera Macias - [Github](https://github.com/wisvem) / [Twitter](https://twitter.com/wisvem)

## License
Public Domain. No copy write protection.