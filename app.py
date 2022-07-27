# Dependencies
import datetime as dt
import numpy as np
import pandas as pd

# dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the flask dependencies after SQLAlchemy
from flask import Flask, jsonify

# set up our database engine for the Flask application in much the same way we did for climate_analysis.ipynb
engine = create_engine("sqlite:///hawaii.sqlite")

# The create_engine() function allows us to access and query our SQLite database file. Now let's reflect the database into our classes.
Base = automap_base()

# Add the following code to reflect the database:
Base.prepare(engine, reflect=True)

# We'll create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# Next, we need to define our app for our Flask application.
# create a Flask application called "app."
app = Flask(__name__)

# define the welcome route
@app.route("/") # welcome route, is set up - next step is to add the routing information for each of the other routes
# we'll create a function, and our return statement will have f-strings as a reference to all of the other routes
# This will ensure our investors know where to go to view the results of our data.
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# The next route we'll build is for the precipitation analysis. This route will occur separately from the welcome route.
@app.route("/api/v1.0/precipitation")

# Next, we will create the precipitation() function.
# First, we want to add the line of code that calculates the date one year ago from the most recent date in the database
# Next, write a query to get the date and precipitation for the previous year.
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
# # create a dictionary with the date as the key and the precipitation as the value
# To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# the stations route. For this route we'll simply return a list of all the stations.
@app.route("/api/v1.0/stations")

# With our route defined, we'll create a new function called stations()
# we need to create a query that will allow us to get all of the stations in our database
def stations():
    results = session.query(Station.station).all()
    # unraveling our results into a one-dimensional array. To do this, we want to use the function np.ravel(), with results as our parameter.
    # convert the results to a list, we will need to use the list function, which is list(), and then convert that array into a list. 
    # Then we'll jsonify the list and return it as JSON
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# For this route, the goal is to return the temperature observations for the previous year
@app.route("/api/v1.0/tobs")

# Next, create a function called temp_monthly() by adding the following code:
def temp_monthly():
    # calculate the date one year ago from the last date in the database. 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # next step is to query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
        # Finally, as before, unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
        # jsonify the list and return our results    
    return jsonify(temps=temps)

# Last route will be to report on the minimum, average, and maximum temperatures
# this route is different from the previous ones in that we will have to provide both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats() to put our code in.
# We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None.
def stats(start=None, end=None):
# With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. 
# We'll start by just creating a list called sel
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
# we need to determine the starting and ending date, add an if-not statement to our code
# This will help us accomplish a few things. We'll need to query our database using the list that we just made. 
# Then, we'll unravel the results into a one-dimensional array and convert them to a list. 
# Finally, we will jsonify our results and return them.
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
# Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
# We'll use the sel list, which is simply the data points we need to collect. 
# Let's create our next query, which will get our statistics data.
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)        

# This code tells us that we have not specified a start and end date for our range. 
# Fix this by entering any date in the dataset as a start and end date. 
# The code will output the minimum, maximum, and average temperatures. 
# For example, let's say we want to find the minimum, maximum, and average temperatures for June 2017. 
# You would add the following path to the address in your web browser:
# /api/v1.0/temp/2017-06-01/2017-06-30
# When you run the code, it should return the following result:
# ["temps":[71.0,77.21989528795811,83.0]]
