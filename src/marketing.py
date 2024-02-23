import requests, re
from session import auth
from bs4 import BeautifulSoup
from am4_req import am4_url

class marketing:
    def eco_campaign():
        parameter={
                    "type":"5"
        }
        resp = am4_url.send_req("marketing_new.php",parameter=parameter)
        html_read=BeautifulSoup(resp.text,'html.parser')
        check_active = html_read.find().string
        check_active = re.search(r'You already have an active campaign',check_active)
        if check_active:
            print("Eco Campaign is already Active")
            resp = am4_url.send_req("marketing.php",parameter={})
            html_read=BeautifulSoup(resp.text,'html.parser')
            active = html_read.find("div",{"id": "active-campaigns"})
        else:
            eco_price=html_read.find("button").string
            parameter={
                        "type":"5",
                        "mode":"do",
                        "c":"1"
            }
            resp = am4_url.send_req("marketing_new.php",parameter=parameter)
            print("Eco Campaign Bought for "+eco_price)
