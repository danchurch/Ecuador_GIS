import csv

## we need to see the BPs that I think are touched by one or concessions

## read in csv, from map of intersection of BPs and concessions
## make a list of dicts:

with open('bp_conc_intersect.csv','r') as f:
    reader = csv.DictReader(f)
    aa = list(reader)

## get the names:
bb = [ i['nombre'] for i in aa ]

## get the unique names:

cc = set(bb)

with open('unique_bp_conc.txt','w') as w:
    for i in cc:
        w.write(i+ '\n')

len(cc)
