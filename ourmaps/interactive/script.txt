## okay, and made a sample index file to show this.
## but with the thousands of concessions, I think 
## we'll need to set up a database to display them

## move into python, setup mongoDB for this:

python3

import json
import pandas as pd
from pymongo import MongoClient

## initialize db
client=MongoClient()
db = client.concessions
coll = db.conc_01_2018 ## will be concession collection

## okay, but we want our concessions into a json, 
## then into a list of dictionaries, I think,
## to feed into the mongodb

## make df
aa = pd.read_csv('Conc_01_18.csv')

## df to json
aa.to_json('Conc_01_18.json', orient="records")

## json to dictionaries
with open('Conc_01_18.json') as f:
    bb = json.load(f)

## list of dictionary to mongodb collection

coll.insert(bb)

bb[0]

## test ride, find lc concessions:

lcs = coll.find({'nam':'40000339'})
list(lcs)

lcs = coll.find({'nam':'40000340'})
list(lcs)

lcs = coll.find( { '$or': [ {'nam':'40000339'}, {'nam':'40000340'} ] } )
list(lcs)

## ok, pretty simple. Can we do the same with the
## cantons? Try them as a geojson from qgis...

## json to dictionaries
with open('cantons.geojson') as f:
    cc = json.load(f)

## did this work?

len(cc['features']) ##224

cc['features'][0].keys()

cc['features'][0]['properties'] ## 

zz = cc['features']

##  looks good. we want these features as a collection, I think:

cants = db.cantons 
 
cants.insert(cc['features'])

## did this work?

dd = cants.find(
