import requests, re
from session import auth
from bs4 import BeautifulSoup

class marketing:
    def eco_campaign():
        try:
            parameter={
                    "type":"5"
            }
            resp=requests.get(auth.url+"marketing_new.php", cookies=auth.session,params=parameter)
        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for Marketing. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            marketing.eco_campaign()
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for Marketing. Retrying")
            print("Time out")
            print(errrt)
            marketing.eco_campaign()
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for Marketing. Retrying")
            print("Connection error")
            print(conerr)
            marketing.eco_campaign()
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for Marketing. Retrying")
            print("Exception request")
            print(errex)
            marketing.eco_campaign()
            return
        
        html_read=BeautifulSoup(resp.text,'html.parser')
        check_active = html_read.find().string
        check_active = re.search(r'You already have an active campaign',check_active)
        if check_active:
            print("Eco Campaign is already Active")
        else:
            try:
                parameter={
                        "type":"5",
                        "mode":"do"
                }
                resp=requests.post(auth.url+"marketing_new.php", cookies=auth.session,params=parameter)
            except requests.exceptions.HTTPError as errh:
                print("Connection Lost for Marketing. Retrying")
                print("HTTP Error") 
                print(errh.args[0])
                marketing.eco_campaign()
                return
            except requests.exceptions.ReadTimeout as errrt:
                print("Connection Lost for Marketing. Retrying")
                print("Time out")
                print(errrt)
                marketing.eco_campaign()
                return
            except requests.exceptions.ConnectionError as conerr:
                print("Connection Lost for Marketing. Retrying")
                print("Connection error")
                print(conerr)
                marketing.eco_campaign()
                return
            except requests.exceptions.RequestException as errex:
                print("Connection Lost for Marketing. Retrying")
                print("Exception request")
                print(errex)
                marketing.eco_campaign()
                return
