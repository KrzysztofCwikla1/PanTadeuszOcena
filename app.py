from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ksiega/<int:ksiega_nr>')
def ksiega(ksiega_nr):
        return render_template(f'k{ksiega_nr}.html')


if __name__ == '__main__':
    app.run(debug=True)