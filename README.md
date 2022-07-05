### Requerimientos

- Python 3.10
- Django 4.0.4

# ReadMe.md

![](Beers.png)

![](https://img.shields.io/bower/v/editor.md.svg)

## Integrantes ##
 - Gaston Leegstra
 - Gabriel Rodriguez

Busqueda: Se realiza en la pagina principal
**link del video de la presentacion**

https://youtu.be/Wm0Kn1QYVT4

**Tabla de Contenidos**

Para acceder a la Gestión: 
  -1. A traves del Boton Registrarse.
    -1.1. Ingresar un nombre de usuario.
    -1.2. Ingresar un correo electronico.
    -1.3. Ingresar una contraseña.
    -1.4. Repetir la misma contraseña.
    -1.5. Presionar el boton ingresar.
  -2 Una vez logueado ingresar en el boton de gestion:
    -2.1. En la seccion de Account (Y se visualiza el nombre de usuario), presionar sobre account y aparecerá la opción las crear el perfil.
    -2.2. completar los campos y podemos selecionar para subir una imagen.
    -2.3. una vez creado el perfil, presionado en Account se desplegarás las opciones para Editar y eliminarlo.
  -3 Ingresar en la administración de Django ingresando http://127.0.0.1:8000/admin/ en el navegador:
    -3.1. ingresar con el usuario admin contraseña admin.
    -3.2. Ingresar en usuario buscar el usuario creado en el punto 1, en parte de permisos seleccionar el combo "Es staff"y presionar el botón guarda.
    -3.3 Cerrar la sesión del admin.
    -3.4 volver a la aplicación http://127.0.0.1:8000/ 
    -3.5 seleccionar "Login".
    -3.6 ingresar los datos del usuario del punt 1.
    -3.7 Volver a Gestion.
    -3.8 hacer click en la seccion productos.
    -3.9 y podemos realizar las siguientes acciones:
      -3.9.1  Registrar Categoria.
      -3.9.2  Registrar Envase.
      -3.9.3. Registrar Brew.
      -3.9.4  Registrar Cerveza.
    -3.10 Por cada unos de los puntos mencionados en el 3.9, podemos crearlo, editar, eliminarlo. (para editarlo nos cargara los datos previamente ingresado al momento de crearlo)
    -3.11 Si Seleecionamos una cerveza en el boton "Ver más" no lleva al sitio de Registro de cerveza.
  -4. Busqueda en la pagina principal:
    -4.1 en el cuadro de dialogo "nombre del producto" y presionar el boton buscar.
