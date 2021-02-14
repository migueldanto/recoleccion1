# Proyecto recolección

### scripts utiles provisionales

```bash 
export $(cat .env | xargs)

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
#generar el usuario admin
python manage.py g_superuser

#generar set de empleados y camiones, y rellenos aleatorio
python manage.py g_random1
```

en bd
```sql
create database recoleccion1;
create extension postgis;
select postgis_version();
```


