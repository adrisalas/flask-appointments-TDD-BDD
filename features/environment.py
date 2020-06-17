import os
import tempfile
from app import app

def before_feature(context,feature):
    app.testing = True
    context.client = app.test_client()
    context.session = context.client.__enter__()