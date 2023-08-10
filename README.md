### AirBnB Clone Project
## Phase I: Commandline Interpreter
This commandline interpreter will be able to:
    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file, a database etc…
    Do operations on objects (count, compute stats, etc…)
    Update attributes of an object
    Destroy an objec
In this stage of the project we create a Base class which will handle data serialization and deserialization for other classes.
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine


### Usage:
1. ./console.py: to start the application
2. help: shows what commands are available
3. 
