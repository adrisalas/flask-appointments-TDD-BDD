Feature: Inicio de sesion

Scenario: Usuario incorrecto
Given estoy en la pagina de login
When inicio sesion con "test@uma.es" y "1234"
Then debo ver el mensaje de error "Usuario y/o contraseña incorrecto"

Scenario: Contraseña incorrecta
Given estoy en la pagina de login
When inicio sesion con "doctor@uma.es" y "1"
Then debo ver el mensaje de error "Usuario y/o contraseña incorrecto"

Scenario: Inicio correcto como Doctor
Given estoy en la pagina de login
When inicio sesion con "doctor@uma.es" y "1234"
Then debo ver el mensaje de exito "Has iniciado sesión con éxito" y el menu de "Horario"

Scenario: Inicio correcto como Paciente
Given estoy en la pagina de login
When inicio sesion con "jorge@uma.es" y "1234"
Then debo ver el mensaje de exito "Has iniciado sesión con éxito" y el menu de "Citas"
