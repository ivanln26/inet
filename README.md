# Concurso Inet

## Participantes:

* Ivan Nunez
* Juan Cruz Mare

## Correr la app

Utilizar https://github.com/kaajavi/inet_2019_escolar

Crear virtualenv en python3

Luego, correr
```sh
pip install -r requirements.txt
```
para instalar las dependencias.

Luego,
```sh
export FLASK_APP=app
export FLASK_ENV=development
```

Luego, crear y poblar base de datos
```sh
flask seed-command --host localhost --port 9090
```

Y finalmente iniciar la aplicacion con
```sh
flask run
```

Ingresar a http://localhost:5000/
