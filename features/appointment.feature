Feature: Pedir cita

Scenario: Un usuario pide cita y se actualiza el horario del medico
Given un usuario ha pedido una cita a las "09:00" el día "Día 01/06/2020, Lunes"
When su medico navega hasta su horario
Then ve la cita pedida por el usuario a las "09:00" el día "Día 01/06/2020, Lunes"