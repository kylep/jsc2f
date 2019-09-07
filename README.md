# JSC2F: JSON SQL Cell to File

This module contains functions to save a JSON cell from a MySQL or Mariadb
database to a file in a nice and easy to use format. It can also upload JSON
files back to the database.


---


# Installation

JSC2FF can be installed by cloning the github repo or from PyPi.

```bash
pip install jsc2f
```


---


# CLI Usage Example

- `download` will save the JSON string from the SQL cell to a nicely formatted
  file for editing.
- `upload` will update the cell with the JSON file
- `--where` is used as a selector: `--where "id == 3"`

```bash
# Download a cell to a file
jsc2f download \
  --db-ip $database_ip \
  --db-name $database_name  \
  --db-password $database_password \
  --db-user $database_user \
  --filename $file_path \
  --table $table_name \
  -column $column_name

# Upload a file to a cell
jsc2f upload \
  --db-ip $database_ip \
  --db-name $database_name  \
  --db-password $database_password \
  --db-user $database_user \
  --filename $file_path \
  --table $table_name \
  -column $column_name
```

```bash
# jsc2f  --help
Usage: jsc2f [OPTIONS]

  Upload/Download JSON SQL Cell from/to a local file

Options:
  --where TEXT
  --table TEXT           [required]
  --column TEXT          [required]
  --db-name TEXT         [required]
  --db-password TEXT     [required]
  --db-user TEXT         [required]
  --db-port INTEGER
  --db-ip TEXT           [required]
  --filename TEXT        [required]
  --upload / --download  Upload or download  [required]
  --help                 Show this message and exit.
```


---


# Python Module Usage Example

```python
import jsc2f.lib as jsc2f

# Get data from SQL cell and write it to JSON file
jsc2f.save_to_file(filename=filename, host=db_ip, user=db_user,
                   password=db_password, database=db_name, column=column,
                   table=table, where=where, port=db_port)

# Get JSON from file and write it to SQL cell
jsc2f.update_from_file(filename=filename, host=db_ip, user=db_user,
                       password=db_password, database=db_name,
                       column=column, table=table, where=where,
                       port=db_port)
```
