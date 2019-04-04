from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

restaurants = session.query(Restaurant).all()

items = session.query(MenuItem).all()

""" for restaurant in restaurants:
    print(restaurant.name) """


peperoni_pizza = session.query(MenuItem).filter_by (name = "Peperoni Pizza").all()

for pizza in peperoni_pizza:
    if pizza.id != 3:
        session.delete(pizza)
        session.commit()

