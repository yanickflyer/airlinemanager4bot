import requests, re
from session import auth
from bs4 import BeautifulSoup

class actions:
    def purchase_fuel(retry):
        try:
            page = "fuel.php"
            resp=requests.get(auth.url+page, cookies=auth.session)
            html_read=BeautifulSoup(resp.text,'html.parser')
            current=html_read.find("span",{"class": "text-danger"}).string
            holding=html_read.find("span",{"id": "holding"}).string
            current=current.lstrip("$ ").replace(",","")
            holding=holding.replace(",","")
            if (int(current)<=650 and int(current)>450):
                purchase="250000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Purchased 250000lbs for $'+str(price))
            elif (int(current)<=450):
                purchase="500000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Purchased 500000lbs for $'+str(price))
            elif (int(current)>650 and int(current)<=1000):
                purchase="200000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Purchased 200000lbs for $'+str(price))
            elif (int(current)>1000 and int(current)<=1250):
                purchase="100000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Purchased 100000lbs for $'+str(price))
            else:
                print("Fuel too expensive $"+current+"/1000lbs")
        except requests:
            print("Connection Lost for Purchasing FUEL. Retrying")
            if retry < 10:
                retry+=1
                actions.purchase_fuel(retry)
                return
            else:
                print("Max Number of Retries Reached. Will try again in 5 minutes")
                return
    
    def depart_all(retry):
        page = "route_depart.php"
        parameter={
                "mode":"all",
                "ids":"x"
            }
        try:
            resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
        except:
            print("Connection Lost for Departing all Aircraft. Retrying")
            if retry < 10:
                retry+=1
                actions.depart_all(retry)
                return
            else:
                print("Max Number of Retries Reached. Will try again in 5 minutes")
                return
            
        no_aircraft=re.search(r'\'No routes departed\'',resp.text)
        if no_aircraft:
            print('All Aircraft are in the air')
        else:
            x = re.findall("routeReg: \'.*\'", resp.text)
            for flight in x:
                flightno=flight.lstrip("routeReg: \'")
                flightno=flightno.rstrip("\'")
                print(flightno+" is now in the air")
        
    
        
        
