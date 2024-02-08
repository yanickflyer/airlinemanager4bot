import requests, re, sys
from session import auth
from bs4 import BeautifulSoup

class maintenance:
    def get_aircraft(retry):
        page="maint_plan.php"
        try:
            resp=requests.get(auth.url+page, cookies=auth.session)
        except requests.exceptions.HTTPError as errh:
            print("FAILED to get list of aircraft for maintenance")
            print("HTTP Error") 
            print(errh.args[0])
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("FAILED to get list of aircraft for maintenance")
            print("Time out")
            print(errrt)
            return
        except requests.exceptions.ConnectionError as conerr:
            print("FAILED to get list of aircraft for maintenance")
            print("Connection error")
            print(conerr)
            return
        except requests.exceptions.RequestException as errex:
            print("FAILED to get list of aircraft for maintenance")
            print("Exception request")
            print(errex)
            return
        html_read=BeautifulSoup(resp.text,'html.parser')
        ListView=html_read.find("div",{"id":"acListView"})
        ListView=ListView.find_all("div",{"class","row"})
        for air in ListView:
            try:
                air.find("button").attrs['onclick']
            except:
                continue
            get_id=air.find("button").attrs['onclick']
            get_id=re.search(r'id=[0-9]+',get_id).group()
            get_id=get_id.lstrip('id=')
            js_data = {
                "Flight Hours":air.find("b").string,
                "Hours to Check":air.find_all("b")[1].string,
                "Wear":air.find_all("b")[2].string,
                "Status":air.find_all("span")[3].string,
                "Reg":str(air.attrs['data-reg']).upper(),
                "Type":str(air.attrs['data-type']).upper(),
                "id":get_id
            }
            maintenance.AircraftCheck(js_data=js_data)
    
    def AircraftCheck(js_data):
        page="maint_plan_do.php"
        if js_data["Status"] == "At base":
            if int(int(js_data["Hours to Check"]) < 20):
                parameter={
                    "mode":"do",
                    "type":"check",
                    "id":js_data["id"]
                }
                try:
                    requests.post(auth.url+page,cookies=auth.session,params=parameter)
                except requests.exceptions.RequestException as errh:
                    print(errh) 
                    print('FAILED to plan A Check for '+js_data["Reg"])
                    return
                print("A Check Scheduled for "+js_data["Reg"]+" "+js_data["Type"])
                return
        wear=js_data["Wear"]
        wear=float(wear.replace("%",""))
        if (wear) >= 30.0:
            parameter={
                    "mode":"do",
                    "type":"repair",
                    "id":js_data["id"]
            }
            try:
                requests.post(auth.url+page,cookies=auth.session,params=parameter)
                print("Maintenance Scheduled for "+js_data["Reg"]+" "+js_data["Type"])
            except requests.exceptions.HTTPError as errh:
                print("FAILED to schedule Maintenance for "+js_data["Reg"])
                print("HTTP Error") 
                print(errh.args[0]) 
            except requests.exceptions.ReadTimeout as errrt:
                print("FAILED to schedule Maintenance for "+js_data["Reg"])
                print("Time out")
                print(errrt)
            except requests.exceptions.ConnectionError as conerr:
                print("FAILED to schedule Maintenance for "+js_data["Reg"])
                print("Connection error")
                print(conerr)
            except requests.exceptions.RequestException as errex:
                print("FAILED to schedule Maintenance for "+js_data["Reg"])
                print("Exception request")
                print(errex)
