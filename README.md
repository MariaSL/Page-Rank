# PageRank

## Purpose ##
The project I did for my Information Retrieval course. This project is solely for sharing my implementation, not for further development.

## Description ##
Implementation of PageRank algorithm using the flights data from http://www.openflights.org
The algorithm calculates the PageRank value for each airport in the input data and returns the TOP-15 most popular airports.

## Data ##
The input file `data/routes.csv` contains 59036 routes between 3209 airports on 531 airlines spanning the globe. The file contains two data fields: 3 letter IATA code for an origin airport and for a destination airport. Routes are directional: if an airline operates services from A to B and from B to A, both A - B and B - A are listed separately.
## Stack ##
* Language : Python 2.7
* Libraries : NetworkX, Pandas, Datetime, CSV, Operator
    
## How to run ##
* Run `src/PageRank.py`
* Specify the full path to the input file `routes.csv`

## Notes ##
* For the purpose of PageRank performance optimization, the `src/GraphConstruction.py` file pre-processes the input data on routes by first building a weighted graph of routes and further representing it as a nested dictionary.
* You can modify the damping factor and the number of iterations in the following line of `src/PageRank.py` : `airports_page_rank = page_rank(0.85, 100)`
* For a full description of data pre-processing and PageRank algorithm check my report in the `docs` folder.