# Proyecto recolección

### scripts utiles provisionales

para levantar bd
```bash
docker run -d --name "my_postgis" -v my_postgis:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=<pass> -e POSTGRES_USER=<user> --network=host postgis/postgis:12-master

```

en bd
```sql
create database recoleccion1;
create extension postgis;
select postgis_version();

drop database recoleccion1;
```
en django

```bash 
export $(cat .env-dev | xargs)

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
#generar el usuario admin
python manage.py g_superuser

#generar set de empleados y camiones, y rellenos aleatorio
python manage.py g_random1
```




