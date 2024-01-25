import requests, re, sys
from session import auth
from bs4 import BeautifulSoup

class maintenance:
    def get_aircraft(retry):
        page="maint_plan.php"
        try:
            resp=requests.get(auth.url+page, cookies=auth.session)
        except requests:
            print('FAILED to get list of aircraft for maintenance')
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
            maintenance.AircraftCheck(js_data=js_data,retry=1)
    
    def AircraftCheck(js_data,retry):
        page="maint_plan_do.php"
        if js_data["Status"] == "At base":
            if int(int(js_data["Hours to Check"] < 30)):
                parameter={
                    "mode":"do",
                    "type":"check",
                    "id":js_data["id"]
                }
                try:
                    requests.post(auth.url+page,cookies=auth.session,params=parameter)
                except:
                    print('FAILED to plan A Check for'+js_data["Reg"])
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
            
            requests.post(auth.url+page,cookies=auth.session,params=parameter)
            print("Maintenance Scheduled for "+js_data["Reg"]+" "+js_data["Type"])
