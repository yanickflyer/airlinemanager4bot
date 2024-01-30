import requests, re
from session import auth
from money import money
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
            hold=int(holding)
            if (hold>2500000):
                print('No Need to buy FUEL. Hold is at '+holding+'LBS')
                return
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
            elif (int(current)>650 and int(current)<=1000 and hold < 1000000):
                purchase="200000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Emergency FUEL Purchased 200000lbs for $'+str(price)+".  Hold was at "+holding+" LBS")
            elif (int(current)>1000 and int(current)<=1250 and hold < 800000):
                purchase="100000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Emergency FUEL Purchased 100000lbs for $'+str(price)+".  Hold was at "+holding+" LBS")
            else:
                print("Fuel too expensive $"+current+"/1000lbs.")
        except:
            print("Connection Lost for Purchasing FUEL. Retrying")
            if retry < 10:
                retry+=1
                actions.purchase_fuel(retry)
                return
            else:
                print("Max Number of Retries Reached. Will try again in 30 minutes")
                return
    
    def buy_quota(retry):
        try:
            page="co2.php"
            resp=requests.get(auth.url+page, cookies=auth.session)
            html_read=BeautifulSoup(resp.text,'html.parser')
            holding=html_read.find("span",{"id": "holding"}).string
            holding_int=int(holding.replace(',',''))
            cost=int(html_read.find("span",{"id": "sumCost"}).string)
            if (holding_int>1000000):
                print("No Need to buy CO2 Quota. Hold is at "+holding+" Quotas")
                return
            
            if (cost <= 120):
                purchase="1000000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(cost)/1000)
                print('Purchased 1000000 CO2 Quotas for $'+str(price))
            elif (holding_int < 300000 and cost <= 150):
                purchase="300000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(cost)/1000)
                print('Emergency 300000 CO2 Quotas purchased for $'+str(price))
            else:
                print('CO2 Quota too expensive. Cost is at $'+str(cost))

        except:
            print("Connection Lost for Purchasing CO2 Quota. Retrying")
            if retry < 10:
                retry+=1
                actions.purchase_fuel(retry)
                return
            else:
                print("Max Number of Retries Reached. Will try again in 30 minutes")
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
        
    
        
        
