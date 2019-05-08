from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def Home():
    return ("SQL Alchemy / Flask HW Routes /api/v1.0: /precipitation, /stations, /tobs, /<start>, /<start>/<end>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    lastyear = "2017-08-23"
    prcpdata = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > lastyear).all()
    prcpdict = {date: prcp for date, prcp in prcpdata}
    return jsonify(prcpdict)


@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station).all()
    #stationlist = []
    #for i in stationstest:
    #   stationlist.add(stationstest[i][0])
    #jsonify(stationslist)
    #Doesn't Work WIP


if __name__ == "__main__":
    app.run(debug=True)
