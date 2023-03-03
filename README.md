# API Restful para el funcionamiento de kfreeze app

Esta api esta diseñada a base de python usando el framework de flask
su funcionamiento esta pensado para liberar carga local de la aplicacion 
y poder servir donde sea en un servidor centralizado
orignalmente su funcionamiento estaba pensado para heroku, pero con ciertas
adaptaciones puede funcionar donde sea 

tiene algunas features basadas en CRUD y otras mas interesantes

/users (GET) = ver listado de usuarios
/log_user (GET) = landing de loggeo
/users (POST) = registrar usuarios
/users (PUT) = modificar usuarios
/users (DELETE) = eliminar usuario
/users/mouseketools (POST) = promote de usuario a nivel de admin (usar "ClaveBelica1" para confirmar la promocion)
/users/demote (POST) = demote de nivel de usuario a regular
/dpbernal/add (POST) = agregar displaypicture al usuario (NOTA: usar solamente si la conexion a la bdd tiene gran almacenamiento y bandwidth)
/dpbernal/check (GET) = obtener displaypicture al usuario (NOTA: usar solamente si se tiene buen bandwidht)
/dpbernal/mod (POST) = elimiar displaypicture

landing 404 obtenido de alguna plantilla alrededor del 2017, no tengo la referencia
landing index obtenido de alguna plantilla alrededor del 2018, tampoco dispongo la referencia

# Restful api for kfreeze app working

This api was designed for the correct working of kfreeze app and designed with python and love
the main objective about this is for free up the processing loading for the app

features: 
/users (GET) = get user list
/log_user (GET) = log in landing page
/users (POST) = sign up users
/users (PUT) = modify users 
/users (DELETE) = delete users
/users/mouseketools (POST) = promote any user to 'admin' level (be sure of use "ClaveBelica1" for make this commit)
/users/demote (POST) = demote any admin user to a regular one
/dpbernal/add (POST) = add a display picture for the user (NOTE: you shouldnt use it if your instance doesnt have good bandwidht and storage)
/dpbernal/check (GET) = get display picture for the user (NOTE: you shouldnt use it if your instance doesnt have good bandwidht and storage)
/dpbernal/mod (POST) = delete display picture
