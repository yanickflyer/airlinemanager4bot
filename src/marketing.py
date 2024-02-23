import re, time, datetime
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
            all_rows = active.find_all("tr")
            for row in all_rows:
                campaign_type = row.text.strip()
                if campaign_type == "Eco friendly":
                    search_timer = row.find_all("td")
                    for row_data in search_timer:
                        if row_data.has_attr("id"):
                            timer_id = row_data["id"]
                            break
            script_timer = html_read.find("script").text
            get_ecotimer=re.search(r'timer\(\'.*\,\d+\)',script_timer).group()
            get_ecotimer=int(get_ecotimer.split(',')[1].rstrip(')'))
            print("Eco Campaign Will activate in: "+str(datetime.timedelta(seconds=get_ecotimer)))
            time.sleep(get_ecotimer)

        eco_price=html_read.find("button").string
        parameter={
                    "type":"5",
                    "mode":"do",
                    "c":"1"
        }
        resp = am4_url.send_req("marketing_new.php",parameter=parameter)
        print("Eco Campaign Bought for "+eco_price)
