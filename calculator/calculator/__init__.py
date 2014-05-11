from flask import Flask

app = Flask(__name__)
app.config.update(debug=True)

#import views