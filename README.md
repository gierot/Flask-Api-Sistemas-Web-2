# Instalação
`docker build -t flask-rest-api .`
`docker run --name FlaskApi -d -p 5000:5000 flask-rest-api`

# Rotas
As rotas seguem um padrão

GET https://localhost:5000/user/

POST https://localhost:5000/user/create

PUT https://localhost:5000/user/update/{id}

DELETE https://localhost:5000/user/delete/{id}


Temos a rota /user, /cursos e /comentarios

Collation do Postman: https://www.getpostman.com/collections/4449753d0e4b846d049f
