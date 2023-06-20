docker-compose up

docker cp GIS.backup pgdb:/var/lib/postgresql/data

docker exec pgdb pg_restore -U postgres -d GIS /var/lib/postgresql/data/GIS.backup
