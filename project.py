#!/usr/bin/python
# Rest API which produces GET, POST, PUT, DELETE methods 
import os
import sqlite3
import json
from flask import Flask, request, g, jsonify

# creating the application
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'project.db'),
                       SECRET_KEY='devlopment_key'))
app.config.from_envvar('PROJECT_SETTINGS', silent=True)


def connect_db():
    '''Connects to the specific database.'''
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    ''' Opens a database connection for initializing '''
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    '''Initializes the database.'''
    init_db()
    print 'Initialized the database'


def get_db():
    '''Opens a new database connection if there is none yet for the
    current application context.
    '''
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    '''Closes the database again at the end of the request.'''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/postAd', methods=['GET', 'POST'])
def post_ad():
    '''Creates a url /postAd using app.route() it has the methds 
    GET and POST. Accepts the data from the user in json 
    format and inserts this data into the sqlite3 database.Returns 
    the inserted values to the user in json format using jsonify() 
    '''

    input_data = request.json
    print input_data
    fname = input_data['firstname']

    db = get_db()
    # Insert into databse
    db.execute('insert into postAd(firstname, title, category, description, \
                phone)\
                values(?,?,?,?,?)', [
                  input_data['firstname'], input_data['title'],
                  input_data['category'], input_data['description'],
                  input_data['phone']]) 
    # Commit the changes.(It must be explicitly called)                             
    db.commit()

    query = \
        db.execute('select firstname, title, category, description,phone\
                    from postAd where firstname=?', [fname])

    return_data = [dict(firstname=row[0], title=row[1],
                   category=row[2], description=row[3], phone=row[4])
                   for row in query.fetchall()]
    return jsonify(return_data)


@app.route('/showAds')
def show_ads():
    ''' Reads all records in the database an returns the same to the user'''
    db = get_db()
    # select all the records
    query = \
        db.execute('select id, firstname, title, category,description, phone\
                    from postAd order by id desc')
    entries = [dict(
        id=row[0],
        firstname=row[1],
        title=row[2],
        category=row[3],
        description=row[4],
        phone=row[5],
        ) for row in query.fetchall()]
    return jsonify(entries)


@app.route('/deleteAd', methods=['DELETE'])
def delete_ad():
    '''The firstname of the user and the title of the Ad to be deleted is 
    taken in json format, and the record containing the firstname and the 
    title is deleted
    '''
    
    input_data = request.json
    fname = input_data['firstname']
    title = input_data['title']
    
    db = get_db()
    cur = db.execute('delete from postAd where firstname=? and title=?', [
                      fname, title])
    db.commit()
    # If no row is affected or the data is not in the database
    if cur.rowcount == 0:        
         return jsonify({'Delete':'Error'})
    else:        
        return jsonify({'Deleted': 'SuccessFully'})
       


@app.route('/updateAd/<fname>/<title>', methods=['PUT'])
def update_ad(fname, title):
    '''The firstname of the user and the title of the Ad to be updated is 
    taken in url,and the new data to be put is taken in the json format and
    the record containing the firstname and the title is updated with new values
    '''
    input_data = request.json
    new_fname = input_data['firstname']
    new_title = input_data['title']
    category = input_data['category']
    description = input_data['description']
    phone = input_data['phone']

    db = get_db()
    cur = \
        db.execute('update postAd set firstname=?, title=?, category=?,\
                    description=?, phone=? where firstname=? and title=?', [
                        new_fname, new_title, category, description, phone,
                        fname, title])
    db.commit()
    if cur.rowcount == 0:        
         return jsonify({'Update':'Error'})
    else:        
        return jsonify({'Updated': 'SuccessFully'})


if __name__ == '__main__':
    # Set the host and the port on which the API is run
    app.run(debug=True, host='127.0.0.1', port=8080)

