## Postgresql CI Example Scripts
The programs in this repo show how to perform CRUD operations
on an example, locally hosted, [database](https://github.com/lerocha/chinook-database) using python libraries. The `psql-psycopg2.py` script shows how to use the `psycopg2` library to do CRUD operations by executing raw SQL. The `artist-orm.py` and `shopping-orm.py` scripts demonstrate the use of the `sqlalchemy` library to take a class based ORM approach to CRUD. ([This article](https://vegibit.com/interacting-with-a-database-using-sqlalchemy-crud-operations/) is useful background for the ORM approach).
### Useful postgresql terminal commands
```bash
$ set_pg # tell terminal we are using postgresql (at main prompt)
$ psql # call postgresql prompt (at main prompt)
\l # list postgresql databases in file (psql prompt)
\c chinook # connect to chinook db (for example)
\dt # display tables in connected db
\q # quit psql prompt
ctrl+z # exit table list etc
```
