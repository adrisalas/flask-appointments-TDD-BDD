from behave import given, when, then

@given(u'un paciente inicio sesion')
def flask_setup_paciente(context):
    context.client.get('/logout') # If you do not check you've already logout, errors may arise
    context.page = context.client.post('/login', data=dict(
        email="jorge@uma.es",
        password="1234"
    ), follow_redirects=True)
    with context.session.session_transaction() as sess:
        assert sess['patient'] == "jorge@uma.es"
    assert context.page

@given(u'un doctor inicio sesion')
def flask_setup_doctor(context):
    context.client.get('/logout') # If you do not check you've already logout, errors may arise
    context.page = context.client.post('/login', data=dict(
        email="doctor@uma.es",
        password="1234"
    ), follow_redirects=True)
    with context.session.session_transaction() as sess:
        assert sess['doctor'] == "doctor@uma.es"
    assert context.page

@when(u'pulsa el boton de cierre de sesion')
def click_logout(context):
    context.client.get('/logout')

@then(u'la sesion esta cerrada')
def logged_out(context):
    with context.session.session_transaction() as sess:
        assert 'patient' not in sess.keys()
        assert 'doctor' not in sess.keys()
    assert "Has cerrado sesión".encode("utf-8") in context.page.data