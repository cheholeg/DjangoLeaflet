# Map with using Django + Leaflet
____
To launch the application, just type 

`docker-compose up` 

from the application directory.

then you need to enter commands to restore the data
`docker cp GIS.backup pgdb:/var/lib/postgresql/data` 

and 

`docker exec pgdb pg_restore -U postgres -d GIS /var/lib/postgresql/data/GIS.backup` 

Open http://localhost:8000 to view it in the browser.

## Solved tasks
A Django application was created that contains a map using leaflet, objects with information are displayed on the map, and search is also implemented

