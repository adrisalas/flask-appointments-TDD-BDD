Feature: Cierre de sesión

Scenario: Un paciente cierra sesion
Given un paciente inicio sesion
When pulsa el boton de cierre de sesion
Then la sesion esta cerrada

Scenario: Un doctor cierra sesion
Given un doctor inicio sesion
When pulsa el boton de cierre de sesion
Then la sesion esta cerrada