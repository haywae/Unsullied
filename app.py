from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Legal Representative',
    'location': 'New York, NY',
    'salary': '$50,000'
  },
  {
    'id': 2,
    'title': 'Software Developer',
    'location': 'San Francisco, CA',
    'salary': '$60,000'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Los Angeles, CA',
    'salary': '$70,000'
  },
  {
    'id': 4,
    'title': 'Marketing Manager',
    'location': 'Chicago, IL',
    
  }
]

@app.route('/')
def mk_home():
  return render_template('home.html', jobs = jobs)

@app.route('/jobs')
def mk_jobs():
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
