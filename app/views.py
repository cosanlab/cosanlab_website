from app import app, db, models
from flask import render_template, flash, redirect, jsonify

# Helper Functions

def get_sorted_people(data):
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
    return utitle

def get_sorted_years(data):
    years = [int(x.year) for x in data]
    uyear = list(set(years)) #get unique years - may need to reverse sort eventually
    uyear.sort(reverse=True)
    return uyear

def flatten_list(tags):
    flat = []
    for sublist in tags:
        for i in sublist:
            flat.append(i)
    return flat

def get_tag_counts(data):
    tags = [x.tags for x in data]
    flat = flatten_list(tags)
    tag_list = list(set(flat))
    return dict((i, flat.count(i)) for i in tag_list)

def get_resource_type_list(data):
    resource_list = list(set([x.type for x in data]))
    if 'Software' in resource_list:
        sorted_resources = ['Software']
    if 'Tutorials' in resource_list:
        sorted_resources.append('Tutorials')

    for i in list(set(resource_list) - set(sorted_resources)):
        sorted_resources.append(i)
    return sorted_resources

def get_type_list(data):
    resource_list = list(set([x.type for x in data]))
    resource_list.sort(reverse=False)
    return resource_list

def get_position_type_list(data):
    resource_list = list(set([x.position for x in data]))
    resource_list.sort(reverse=False)
    return resource_list

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

    return render_template('people.html', utitle = get_sorted_people(data))

@app.route('/publications')
def publications():
    data = models.Papers.query.all()
    return render_template('publications.html',
                            uyear=get_sorted_years(data),
                            utags=get_tag_counts(data))

@app.route('/resources')
def resources():
    data = models.Resources.query.all()

    return render_template('resources.html',
                            resource_type_list=get_resource_type_list(data),
                            resource_list=data)

@app.route('/teaching')
def teaching():
    data = models.Teaching.query.all()
    return render_template('teaching.html',
                            teaching_type_list=get_type_list(data),
                            teaching_list=data)

@app.route('/positions')
def positions():
    data = models.Positions.query.all()
    return render_template('positions.html',
                            position_type_list=get_position_type_list(data),
                            positions_list=data)

@app.route('/news')
def news():
    return render_template('news.html')

@app.errorhandler(404)
def fourohfour(error):
	return render_template('fourohfour.html')

    
