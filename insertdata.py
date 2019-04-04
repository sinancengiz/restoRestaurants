from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstRestaurant = Restaurant(name = 'Pizza Place')
session.add(myFirstRestaurant)
session.commit()

mySecondRestaurant = Restaurant(name = 'Cyro King')
session.add(mySecondRestaurant)
session.commit()

myThirdRestaurant = Restaurant(name = 'Chutney')
session.add(myThirdRestaurant)
session.commit()

myFourthRestaurant = Restaurant(name = 'Mission Bay')
session.add(myFourthRestaurant)
session.commit()


cheesePizza = MenuItem( name = "Cheese Pizza", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "8,99", restaurant = myFirstRestaurant)
session.add(cheesePizza)
session.commit()

peperoniPizza = MenuItem( name = "Peperoni Pizza", course = "Entree", 
                        description = " Peperoni pizza with tometos and cheese",
                        price = "15,99", restaurant = myFirstRestaurant)
session.add(peperoniPizza)
session.commit()


hawaianPizza = MenuItem( name = "Hawaian Pizza", course = "Entree", 
                        description = " Hawaian pizza with tometos and cheese",
                        price = "5,99", restaurant = myFirstRestaurant)
session.add(hawaianPizza)
session.commit()

veggiePizza = MenuItem( name = "Veggie Pizza", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "4,99", restaurant = myFirstRestaurant)
session.add(veggiePizza)
session.commit()


beefPizza = MenuItem( name = "Beef Pizza", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "3,99", restaurant = myFirstRestaurant)
session.add(beefPizza)
session.commit()

allstarPizza = MenuItem( name = "allstar Pizza", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "20,99", restaurant = myFirstRestaurant)
session.add(allstarPizza)
session.commit()


cheesePizza = MenuItem( name = "Keser", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "8,99", restaurant = mySecondRestaurant)
session.add(cheesePizza)
session.commit()

peperoniPizza = MenuItem( name = "Doner", course = "Entree", 
                        description = " Peperoni pizza with tometos and cheese",
                        price = "15,99", restaurant = mySecondRestaurant)
session.add(peperoniPizza)
session.commit()


hawaianPizza = MenuItem( name = "Kuzu", course = "Entree", 
                        description = " Hawaian pizza with tometos and cheese",
                        price = "5,99", restaurant = mySecondRestaurant)
session.add(hawaianPizza)
session.commit()

veggiePizza = MenuItem( name = "Corbaa", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "4,99", restaurant = mySecondRestaurant)
session.add(veggiePizza)
session.commit()


beefPizza = MenuItem( name = "Lahana", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "3,99", restaurant = mySecondRestaurant)
session.add(beefPizza)
session.commit()

allstarPizza = MenuItem( name = "Durum", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "20,99", restaurant = mySecondRestaurant)
session.add(allstarPizza)
session.commit()


cheesePizza = MenuItem( name = "Keser", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "8,99", restaurant = myThirdRestaurant)
session.add(cheesePizza)
session.commit()

peperoniPizza = MenuItem( name = "Doner", course = "Entree", 
                        description = " Peperoni pizza with tometos and cheese",
                        price = "15,99", restaurant = myThirdRestaurant)
session.add(peperoniPizza)
session.commit()


hawaianPizza = MenuItem( name = "Kuzu", course = "Entree", 
                        description = " Hawaian pizza with tometos and cheese",
                        price = "5,99", restaurant = myThirdRestaurant)
session.add(hawaianPizza)
session.commit()

veggiePizza = MenuItem( name = "Corbaa", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "4,99", restaurant = myFourthRestaurant)
session.add(veggiePizza)
session.commit()


beefPizza = MenuItem( name = "Lahana", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "3,99", restaurant = myFourthRestaurant)
session.add(beefPizza)
session.commit()

allstarPizza = MenuItem( name = "Durum", course = "Entree", 
                        description = " vegererian pizza with tometos and cheese",
                        price = "20,99", restaurant = myFourthRestaurant)
session.add(allstarPizza)
session.commit()