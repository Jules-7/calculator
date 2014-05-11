from flask import Flask

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY='hello123')

import createdb
import views