# Local Crimes Map

A Django project that displays crime data from the data.police.uk RESTful API on a map, and as a report style breakdown. The crime data from the report style breakdown is then saved in a PostGIS.



## Important Info

Sensitive information, such as DB hosts and passwords, are read from a secrets.json file in the project root. To run the project yourself you will need your own PostGIS database and set the json key values used in settings.py.

GDAL must be installed on whatever machine you are running this project on.