# myDB

## COMMAND TO DOWNLOAD

##### download manually. install by "pip" will be implemented soon.

#### TO IMPORT THE DATABASE 

  ```python
  import myDB
  db = myDB.db(<string : filename>)]
  ```
  
IF THE FILENAME NOT PROVIDED , BY DEFAULT IF TAKES "default.db" IN CURRENT DIRECTORY.
THE FILENAME CAN BE OF ANY EXTENSION (EX: .db, .pickle, .json, SOME CUSTOM EXTENSIONS LIKE .in, .com, .akash ETC.)

#### SAVING A VALUE 

 ```python
 db.set(<string : key>, <value>)
 ```

KEY SHOULD BE A STRING & VALUE SHOULD BE A VALID PRIMITIVE PYTHON OBJECT

#### GETING A VALUE :

```python
db.get(<string : key>)
```
  
  return a dictionary object if the key exists, else return False
  
#### SAVING A DICTIONARY :

```python
db.put(<dict object>)
```
  
#### GETTING A DATABASE :

```python
db.get_all()
```

RETURN A dictionary OBJECT OF THE DATABASE.

#### REMOVING A DATA:

```python
db.remove(<string : key>)
```
  
returns False if the key does not exists
  
#### CLEARING A ENTIRE DATABASE:

```python
db.clear()
```
