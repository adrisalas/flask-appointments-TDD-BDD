from behave import given, when, then

@given(u'un usuario ha pedido una cita a las "{time}" el día "{day}"')
def flask_setup(context,time,day):
    context.client.get('/logout') # If you do not check you've already logout, errors may arise
    context.page = context.client.post('/login', data=dict(
        email="jorge@uma.es",
        password="1234"
    ), follow_redirects=True)
    context.page = context.client.post('/areaprivada/citas', data=dict(
        time=time,
        day=day
    ), follow_redirects=True)
    assert context.page

@when(u'su medico navega hasta su horario')
def doctor_schedule(context):
    context.client.get('/logout') # If you do not check you've already logout, errors may arise
    context.page = context.client.post('/login', data=dict(
        email="doctor@uma.es",
        password="1234"
    ), follow_redirects=True)
    context.page = context.client.get('/areaprivada/horario')
    assert context.page

@then(u've la cita pedida por el usuario a las "{time}" el día "{day}"')
def logged_out(context,time,day):
    assert ("""<th colspan="2">""" + day + """</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td class="">""" + time + """</td>
                    
                    <td class="table-danger col">
                        Salas Troya, Jorge""").encode("utf-8") in context.page.data