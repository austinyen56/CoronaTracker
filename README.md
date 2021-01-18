# Corona Tracker 2021

This is a COVID tracker which calculates the percentage of you getting COVID depending on where you are and showing your geolocation through an HTML file.

# Requirements

This project is made in Python and these libraries are required in order for it to work (run the main.py):



* **[folium](https://python-visualization.github.io/folium/quickstart.html#Getting-Started)** :This library is used to create the map and generate the HTML file.
* **[geocoder](https://github.com/DenisCarriere/geocoder)** : Takes in your current IP and generates your location.
* **[geopy](https://pypi.org/project/geopy/)** : Takes in longtitude/latitude or user input and generate location.
* **csv** : Allows csv files to be taken in.
* **webbrowser** : Allows HTML file to be created.
* Obtained all cities/counties in each state [here](https://simplemaps.com/data/us-cities)
* Ask ted for the corona count xdd

**Project unfinished due to time lel but here are some suggestions/references:**

***Known bugs:***

* When selected option 2 for multi location, if there is no input, then shit will crash (no data for null).

* If you search for UCSC, there will be double circle so take out ucsc circle to fix issue.

color in/ shade/highlight states or cities and show corona stats

***Suggestions/Improvements:***

* Create lines from point A => B => C ... etc

* Create waypoints/ show nearest pharmacy or hospital to get vaxxinated

* More dense areas = higher chance of corona??

* Account for day stayed? 14 days later no symptom == - half chance of having it?

* Make it an android app??

Reference for [bootstrap icons](https://getbootstrap.com/docs/3.3/components/)

https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/

https://www.youtube.com/watch?v=HChq5_7yTGk&ab_channel=JieJenn

https://stackoverflow.com/questions/60578408/is-it-possible-to-draw-paths-in-folium

https://www.gps-coordinates.net/

Remember to change repo name to CoronaTracker_old


































































