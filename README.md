# Local Crimes Map

A Django project that displays crime data from the data.police.uk RESTful API on a map, and as a report style breakdown. The crime data from the report style breakdown is then saved in a PostGIS.

This project is deployed on [Heroku](https://localcrimesmap.herokuapp.com/).

## Important Info

This project uses the dj_database_url package to set the database connection in settings.py. This connection string must be specified in a .env file, following the format of the example below.

> DATABASE_URL=postgis://{DBUSERNAME}:{DBPASSWORD}@localhost:{PORT}/{DBNAME}

'SECRETKEY'and 'DJANGODEBUG' must also be set as a string enviroment variables

GDAL must be installed on whatever machine you are running this project on.
