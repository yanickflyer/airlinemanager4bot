import requests, re
from session import auth
from money import money
from bs4 import BeautifulSoup

class actions:
    def purchase_fuel():
        try:
            page = "fuel.php"
            resp=requests.get(auth.url+page, cookies=auth.session)
            html_read=BeautifulSoup(resp.text,'html.parser')
            current=html_read.find("span",{"id": "sumCost"}).string
            holding=html_read.find("span",{"id": "holding"}).string
            current=current.replace(",","")
            holding=holding.replace(",","")
            hold=int(holding)
            if (hold>3000000):
                print('No Need to buy FUEL. Hold is at '+holding+'LBS')
                return
            if (int(current)<=750 and int(current)>450):
                purchase="500000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Purchased 500000lbs for $'+str(price))
            elif (int(current)<=450):
                purchase="750000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Purchased 750000lbs for $'+str(price))
            elif (int(current)>750 and int(current)<=1000 and hold < 1500000):
                purchase="300000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Emergency FUEL Purchased 300000lbs for $'+str(price)+".  Hold was at "+holding+" LBS")
            elif (int(current)>1000 and int(current)<=1250 and hold < 1000000):
                purchase="150000"
                parameter={
                    "mode":"do",
                    "amount":purchase
                }
                resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
                price=int(purchase)*(int(current)/1000)
                print('Emergency FUEL Purchased 150000lbs for $'+str(price)+".  Hold was at "+holding+" LBS")
            else:
                print("Fuel too expensive $"+current+"/1000lbs.")
        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for Purchasing FUEL. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            money.get_finance()
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for Purchasing FUEL. Retrying")
            print("Time out")
            print(errrt)
            money.get_finance()
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for Purchasing FUEL. Retrying")
            print("Connection error")
            print(conerr)
            money.get_finance()
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for Purchasing FUEL. Retrying")
            print("Exception request")
            print(errex)
            money.get_finance()
            return
    
    def buy_quota():
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

        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for Purchasing CO2 Quota. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            actions.buy_quota()
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for Purchasing CO2 Quota. Retrying")
            print("Time out")
            print(errrt)
            actions.buy_quota()
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for Purchasing CO2 Quota. Retrying")
            print("Connection error")
            print(conerr)
            actions.buy_quota()
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for Purchasing CO2 Quota. Retrying")
            print("Exception request")
            print(errex)
            actions.buy_quota()
            return

    
    def depart_all():
        page = "route_depart.php"
        parameter={
                "mode":"all",
                "ids":"x"
            }
        try:
            resp=requests.post(auth.url+page, cookies=auth.session, params=parameter)
        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for Departing all Aircraft. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            money.get_finance()
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for Departing all Aircraft. Retrying")
            print("Time out")
            print(errrt)
            money.get_finance()
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for Departing all Aircraft. Retrying")
            print("Connection error")
            print(conerr)
            money.get_finance()
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for Departing all Aircraft. Retrying")
            print("Exception request")
            print(errex)
            money.get_finance()
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
        
    
        
        
