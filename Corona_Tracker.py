#import pandas as pd
import folium
from IPython.core.display import display
#from IPython.core.display import display, HTML
import webbrowser
import csv
import geocoder
#import geopy
from geopy.geocoders import Nominatim
from functools import partial
#[city(0),stateshort(1),statename(2),county(3),lat(4),long(5),population(6)]

def staticLoc():
    #sends the city to main.py
    staticLoc.locationtomain = ""
    enterMode = True
    while enterMode:
        searchMode = input("1 for entering city in CA, 2 for detecting your current location ")
        #Search specific city in CA
        if searchMode == '1':
            #print("u pressed 1")
            enterMode = False
            searchLocation = input("Which place do u wanna search? (city in California) \n")
            with open("CAcities.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                checking = True
                for column in csv_reader:
                    if searchLocation.lower() == column[0].lower():
                        lat = column[4]
                        long = column[5]
                        la ,lo = lat,long
                        checking = False
                        staticLoc.locationtomain = searchLocation

                if checking:
                    print(searchLocation," is not a city in California")
                    exit(0)

            print("The coordinates of {0} seems to be ({1},{2})\n".format(searchLocation,la,lo))
            print("Opening map, please wait...")
            m = folium.Map([la, lo], zoom_start=12, tiles="Stamen Terrain")
            # Creating current marker
            folium.Marker(location=[la,lo],
                          popup="<b>You are here!</b>",
                          tooltip="Estimated Location",
                          icon=folium.Icon(icon="user")).add_to(m)
            folium.Circle(radius=8000,location=[la,lo],
                          popup="Active Area",color="#3186cc",fill=True,
                          fill_color="#3186cc").add_to(m)
            folium.Marker(location=[37.00012445, -122.06221067580847],popup='UC Santa Cruz',icon=folium.Icon(color='red', icon='book')).add_to(m)
            folium.Circle(radius=1000,location=[37.00012445, -122.06221067580847],popup="Active Area",color="#3186cc",fill=True,fill_color="#3186cc").add_to(m)
            m.add_child(folium.LatLngPopup())

            display(m)
            m.save('corona.html')
            webbrowser.open("corona.html",new=2)
        #Detect current location
        elif searchMode == '2':
            #print("U pressed 2")
            enterMode = False

            geolocator = Nominatim(user_agent="CruzHacks2021")
            g = geocoder.ip('Me')
            la = g.latlng[0]
            lo = g.latlng[1]
            lalo2geo = partial(geolocator.reverse, language="en")   #Takes in lat/long from ip and translate to address
            print("\nIt seems that your current location is at:")
            print(lalo2geo("{0}, {1}".format(la,lo)))
            print("(Your estimated coordinates:",g.latlng,")")
            #Takes the address (folium object) and extract the city name
            location = geolocator.reverse(str(la) + ', ' +str(lo),language="en")
            data = location.raw
            data = data['address']
            address = str(data)
            #print(address)
            l =[]
            final =[]
            x = address.find("'city': '")

            for k in range(x+9,len(address)):
                if address[k] != "'":
                    l.append(address[k])
                else:
                    break
            final = [''.join(l)]
            staticLoc.locationtomain = final[0]     #put it to staticLoc.locationtomain which will be sent to main.py
            final.clear()                           #clearing the list (optional)

            confirmLocation = input("\nIs this ur current location?? (yes/no) ")
            if confirmLocation == "no":
                userInLocation = input("Please type in where you are at \n").lower()    #Custom location
                if userInLocation == "ucsc" or userInLocation =="uc santa cruz":
                    location = geolocator.geocode("University of California Santa Cruz")
                else:
                    location = geolocator.geocode(userInLocation)

                la = location.latitude
                lo = location.longitude

                print("\nI assume this should be more like it")
                print(location.address)

                #Takes the address (folium object) and extract the city name
                location = geolocator.reverse(str(la) + ', ' +str(lo),language="en")
                data = location.raw
                data = data['address']
                address = str(data)
                #print(address)
                l =[]
                final =[]
                x = address.find("'city': '")
                for k in range(x+9,len(address)):
                    if address[k] != "'":
                        l.append(address[k])
                    else:
                        break
                final = [''.join(l)]
                staticLoc.locationtomain = final[0] #put it to staticLoc.locationtomain which will be sent to main.py
                final.clear()                       #clearing the list (optional)

            print("Opening map, please wait...")

            #Creating the map
            m = folium.Map([la, lo], zoom_start=14, tiles="Stamen Terrain")
            # Creating current marker
            folium.Marker(location=[la,lo],
                          popup="<b>You are here!</b>",
                          tooltip="Current Location",
                          icon=folium.Icon(icon="user")).add_to(m)
            folium.Circle(radius=500,location=[la,lo],
                          popup="Active Area",color="#3186cc",fill=True,
                          fill_color="#3186cc").add_to(m)
            folium.Marker(location=[37.00012445, -122.06221067580847],popup='UC Santa Cruz',icon=folium.Icon(color='red', icon='book')).add_to(m)
            folium.Circle(radius=1000,location=[37.00012445, -122.06221067580847],popup="Active Area",color="#3186cc",fill=True,fill_color="#3186cc").add_to(m)
            m.add_child(folium.LatLngPopup())

            display(m)
            m.save('corona.html')
            webbrowser.open("corona.html",new=2)

        else:
            print("Thats not 1 or 2 dude...")

#staticLoc()
# voice ctrl?? or voice answer
#vaxination places nearby