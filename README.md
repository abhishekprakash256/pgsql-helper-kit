# pgsql-helper-kit


The run docker command , the password will be changed in production
create 

```
docker run -d --name postgres-container \
  --network=my_network \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=test_db \
  -e POSTGRES_USER=abhi \
  -p 5432:5432 \
  postgres


  docker exec -it postgres-container psql -U abhi -d test_db




docker run -d --name postgres-container \
  -e POSTGRES_USER=abhi \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=contact \
  -v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql \
  -p 5432:5432 \
  postgres
```
