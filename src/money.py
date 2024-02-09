import requests
from session import auth
from bs4 import BeautifulSoup

class money:
    def get_finance():
        try:
            resp=requests.get(auth.url, cookies=auth.session)
        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for Finances. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            money.get_finance()
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for Finances. Retrying")
            print("Time out")
            print(errrt)
            money.get_finance()
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for Finances. Retrying")
            print("Connection error")
            print(conerr)
            money.get_finance()
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for Finances. Retrying")
            print("Exception request")
            print(errex)
            money.get_finance()
            return
        
        html_read=BeautifulSoup(resp.text,'html.parser')
        amt=html_read.find("span",{"id":"headerAccount"}).string
        # amt=amt.replace(",","")
        print("Current Account Balance is $"+amt)