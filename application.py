from flask import Flask, render_template


app = Flask(__name__, template_folder="backend/templates", static_folder='backend/static')

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0', 8888, app, use_reloader=True, use_debugger=True)
    