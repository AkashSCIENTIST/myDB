# myDB

TO IMPORT THE DATABASE 

  ```import myDB \n```
  ```db = myDB.db([filename])```
  
IF THE FILENAME NOT PROVIDED , BY DEFAULT IF TAKES "default.db" IN CURRENT DIRECTORY.
THE FILENAME CAN BE OF ANY EXTENSION (EX: .db, .pickle, .json, SOME CUSTOM EXTENSIONS LIKE .in, .com, .akash ETC.)

SAVING A VALUE 

  ```db.set([key], [value])```

KEY SHOULD BE A STRING & VALUE SHOULD BE A VALID PRIMITIVE PYTHON OBJECT

GETING A VALUE :

  ```db.get([key])```
  
SAVING A DICTIONARY :

  ```db.put([dict object])```
  
GETTING A DATABASE :

  ```db.get_all()```

RETURN A JSON OBJECT OF THE DATABASE.

REMOVING A DATA:

  ```db.remove([key])```
  
CLEARING A ENTIRE DATABASE:

  ```db.clear()```
