from behave import given, when, then

@given(u'estoy en la pagina de login')
def flask_setup(context):
    context.client.get('/logout') # If you do not check you've already logout, errors may arise
    context.page = context.client.get('/login')
    assert "Iniciar Sesión".encode("utf-8") in context.page.data

@given(u'inicio sesion con "{email}" y "{password}"')
@when(u'inicio sesion con "{email}" y "{password}"')
def login(context, email, password):
    context.page = context.client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)
    assert context.page

@then(u'debo ver el mensaje de error "{alert}"')
def logged_in_error(context, alert):
    assert alert.encode("utf-8") in context.page.data

@then(u'debo ver el mensaje de exito "{alert}" y el menu de "{menu}"')
def logged_in_success(context, alert, menu):
    assert alert.encode("utf-8") in context.page.data \
    and menu.encode("utf-8") in context.page.data
    with context.session.session_transaction() as sess:
        assert 'patient' in sess.keys() or 'doctor' in sess.keys()