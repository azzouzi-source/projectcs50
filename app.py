from flask import Flask, render_template, jsonify
app = Flask(__name__)

OPTIONS = [
  
  {
    'id': 1,
    'title': 'TC',
    'nubre_elev': 220,
    'exist': True
  },
  {
    'id': 2,
    'title': '1Bac',
    'nubre_elev': 210,
    
  },
  {
    'id': 3,
    'title': '2Bac',
    'nubre_elev': 160,
    'exist': True
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', options=OPTIONS, name_lycee="IbnKhaldoune")

@app.route('/option')
def option():
  return jsonify(OPTIONS)

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)


