# myDB

## COMMAND TO DOWNLOAD

##### download manually. install by pipwill be implemented soon.

#### TO IMPORT THE DATABASE 

  ```import myDB```
  
  ```db = myDB.db([filename])```
  
IF THE FILENAME NOT PROVIDED , BY DEFAULT IF TAKES "default.db" IN CURRENT DIRECTORY.
THE FILENAME CAN BE OF ANY EXTENSION (EX: .db, .pickle, .json, SOME CUSTOM EXTENSIONS LIKE .in, .com, .akash ETC.)

#### SAVING A VALUE 

  ```db.set([key], [value])```

KEY SHOULD BE A STRING & VALUE SHOULD BE A VALID PRIMITIVE PYTHON OBJECT

#### GETING A VALUE :

  ```db.get([key])```
  
  return a dictionary object if the key exists, else return False
  
#### SAVING A DICTIONARY :

  ```db.put([dict object])```
  
#### GETTING A DATABASE :

  ```db.get_all()```

RETURN A dictionary OBJECT OF THE DATABASE.

#### REMOVING A DATA:

  ```db.remove([key])```
  
  returns False if the key does not exists
  
#### CLEARING A ENTIRE DATABASE:

  ```db.clear()```
