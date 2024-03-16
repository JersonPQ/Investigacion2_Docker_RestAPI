# Documentación API REST con Docker

Integrantes:

- Anthony Guevara
- Darío Espinoza
- Jerson Prendas
- Marbel Brenes

Este proyecto requiere de tener funcional Docker, ya que este incluye sus respectivos archivos para poder correr desde un contenedor de Docker.

## Tecnologías

- Docker
- Docker Compose
- Rest API
- PostgreSQL
- PostMan

## Construcción y Despliegue

 1. Verificar que Docker esté instalado en la maquina a contruir y desplegar.
 2. Clonar este repositorio localmente.
 3. Para correr el contenedore se debe ejecutar el comando
 **`docker-compose up`** en el directorio de la aplicacion.
 4. Una vez hecho esto, se puede acceder a la aplciación a través de **`http://localhost:5002`**

    Una vez concluido con estos pasos, la aplicación puede ser accesada para utilizar y probar sus funciones.

### Autenticación de los endpoints

Para poder hacer alguna peticion, tiene que ir el nombre de usuario y la contraseña

- Ejemplo:
localhost:**puerto**/**user**/**password**

## Funcionamiento y EndPoints

Para poder realizar pruebas se pueden hacer a traves de PostMan, del puerto local, y con el archivo `pruebas.py`.
A través del archivo pruebas, se realizan pruebas unitarias y de integración con los endpoints.

Para alcanzar esto además, podemos accesar con de la siguiente forma:

- **Crear Tarea:** `POST /tasks`
- Permite a los usuarios añadir una nueva tarea.
- Campos de entrada:
  - title - Título de la tarea.
  - description - Descripción.
  - due_date - Fecha de vencimiento.
  - status - Estado (e.g., pendiente, completado).
  - usuario - id del usuario que creó la tarea.
- **Listar Tareas:** `GET /tasks/:id`
  - Recupera una lista de todas las tareas
- **Obtener Detalle de Tarea:** `GET /tasks/:id`
  - Obtiene los detalles de una tarea específica.
- **Actualizar Tarea:** `PUT /tasks/:id`
  - Actualiza los detalles de una tarea existente.
- **Eliminar Tarea:** `DELETE /tasks/:id`
  - Permite a los usuarios eliminar una tarea.
