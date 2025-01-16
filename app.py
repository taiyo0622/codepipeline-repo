from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a containerised app. Updating the app in-class. I still hate Cloud. I still hate AWS. Hate is a strong word.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
