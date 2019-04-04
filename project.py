from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/restaurants')
def restaurants():
    restaurants = session.query(Restaurant)
    return render_template("restaurants.html", restaurants = restaurants)

@app.route('/newrestaurant', methods=['GET', 'POST'])
def newrestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name = request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return render_template('index.html')
    else:
        return render_template('newrestaurant.html')


@app.route('/menu/<int:restaurant_id>')
def menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template("menu.html", items = items, restaurant = restaurant)


@app.route('/newitem/<int:restaurant_id>', methods=['GET', 'POST'])
def newitem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(
            url_for('menu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'newitem.html', restaurant_id=restaurant_id)


@app.route('/edititem/<int:restaurant_id>/<int:item_id>', methods=['GET', 'POST'])
def edititem( restaurant_id , item_id):
    
    if request.method == 'POST':
        editedItem = session.query(MenuItem).filter_by(id=item_id).one()
        print (editedItem.name)
        print (editedItem.id)
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()

        return redirect(
            url_for('menu', restaurant_id=restaurant_id))
    
    else:
        return render_template('edititem.html' , restaurant_id=restaurant_id ,  item_id = item_id)


@app.route('/deleteitem/<int:restaurant_id>/<int:item_id>', methods=['GET', 'POST'])
def deleteitem( restaurant_id , item_id):
    
    if request.method == 'POST':
        deletedItem = session.query(MenuItem).filter_by(id=item_id).one()
        session.delete(deletedItem)
        session.commit()
        
        return redirect (url_for('menu' ,restaurant_id=restaurant_id))

    else:
        return render_template('deleteitem.html' , restaurant_id=restaurant_id ,  item_id = item_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)