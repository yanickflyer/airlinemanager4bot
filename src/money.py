import requests
from session import auth
from bs4 import BeautifulSoup

class money:
    def get_finance(retry):
        try:
            resp=requests.get(auth.url, cookies=auth.session)
        except requests.exceptions.RequestException as errh:
            print(errh) 
            print("Connection Lost for Finances. Retrying")
            if retry < 10:
                retry+=1
                money.get_finance(retry)
                return
            else:
                print("Max Number of Retries Reached. Will try again in 5 minutes")
                return
        html_read=BeautifulSoup(resp.text,'html.parser')
        amt=html_read.find("span",{"id":"headerAccount"}).string
        # amt=amt.replace(",","")
        print("Current Account Balance is $"+amt)