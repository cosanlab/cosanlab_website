from app import app, db, models
from flask import render_template, flash, redirect

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/people')
def people():
    data = models.User.query.all()
    titles = [x.title for x in data]
    if 'Director' in titles:
        utitle=['Director']
    if 'Postdocs' in titles:
        utitle.append('Postdocs')
    if 'Graduate Students' in titles:
        utitle.append('Graduate Students')
    if 'Lab Manager' in titles:
        utitle.append('Lab Manager')
    if 'Research Assistants' in titles:
        utitle.append('Research Assistants')
    if 'Coding Companion' in titles:
        utitle.append('Coding Companion')
    if 'Lab Alumni' in titles:
        utitle.append('Lab Alumni')
    return render_template('people.html', utitle = utitle)

@app.route('/publications')
def publications():
	data = models.Papers.query.all()
	years = [int(x.year) for x in data]
	uyear = list(set(years)) #get unique years - may need to reverse sort eventually
	uyear.sort(reverse=True)
	return render_template('publications.html', uyear = uyear)

@app.route('/resources')
def resources():
        return render_template('resources.html')

@app.route('/teaching')
def teaching():
        return render_template('teaching.html')

@app.route('/participate')
def participate():
    return render_template('participate.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.errorhandler(404)
def fourohfour(error):
	return render_template('fourohfour.html')

@app.route('/login')
def login():
	return render_template('login.html')
