# Como instalarlo

## Pre requisitos
Python 3.5
Conda https://conda.io/docs/installation.html
PostgreSQL https://www.postgresql.org/download/

## Instalación
Asegurarse de tener el entorno desactivado
```
./tools/build.sh
```

## Configurar DB
Crear usuario
```
createuser hackatong2017 --interactive -P
```
password: `geriatrico`
Y responder `y` cuando pregunta si ser superuser

Crear base de datos
```
psql
CREATE DATABASE hackatong2017 OWNER hackatong2017;
```

Correr migración inicial
```
python manage.py migrate
```

## Probar la API local
Activar el entorno
```
source activate geriatrico35
```
Crear un superusuario para probar localmente.
```
python manage.py createsuperuser
```

Levantar el servidor
```
python manage.py runserver
```
Ir al navegador a esta pagina http://127.0.0.1:8000/users/ y con el super user

## Desplagar la aplicacion a Heroku
### Requisitos
Cuenta en heroku.com
Heroku-Cli instalado local https://devcenter.heroku.com/articles/heroku-cli

## Pasos
Configurar el git remoto para poder desplegar el codigo
```
heroku git:remote -a hackatong2017-geriatricos
```

Desplegar una nueva version
```
source activate geriatrico35
pip freeze > requirements.txt
# commit del nuevo requirements.txt
git push heroku master
```

Correr la migración de la base de datos
```
heroku run python manage.py migrate
```

Crear un superuser
```
heroku run python manage.py createsuperuser
```

Ir a https://hackatong2017-geriatricos.herokuapp.com/users/

## Desactivate el entorno
```
source deactivate
```

## Code Styling (Linter)
```
source activate geriatrico35
flake8 .
```

# Links Utiles

## Tecnologias y frameworks
Django Rest Framework - http://www.django-rest-framework.org/tutorial/quickstart/

## Datos de Geríatricos

Los datos de la Ciudad de Córdoba están en el portal de Gobierno Abierto de la Ciudad: [IR](https://gobiernoabierto.cordoba.gob.ar/data/datos-abiertos/categoria/sociedad/geriatricos-habilitados/217).
Incluyen un API: [IR](https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/?tipo_id=1).


## Datos de Geriatricos de Córdoba de Otras Fuentes

### Páginas Amarillas

Dado que Paginas Amarillas no provee un API, usando [Scrapy](https://scrapy.org/), recorrimos todos los resultados de http://www.paginasamarillas.com.ar/b/geriatricos/cordoba/ para obtener los datos de las fichas y normalizarlos para agregarlos a la aplicación junto a otros orígenes de datos.

#### Ejecutar el Scraper
```bash
scrapy runspider spiders/paginasamarillas_geriatricos.py -o data/paginasamarillas_geriatricos.json
```
