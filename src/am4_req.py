import requests
from session import auth

class am4_url:
    def send_req(url,parameter):
        try:
            if parameter == {}:
                resp=requests.get(auth.url+url, cookies=auth.session)
            else:
                resp=requests.get(auth.url+url, cookies=auth.session,params=parameter)
            return resp
        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for AM4. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for AM4. Retrying")
            print("Time out")
            print(errrt)
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for AM4. Retrying")
            print("Connection error")
            print(conerr)
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for AM4. Retrying")
            print("Exception request")
            print(errex)
            return
    def post_send_req(url,parameter):
        try:
            if parameter == {}:
                resp=requests.post(auth.url+url, cookies=auth.session)
            else:
                resp=requests.post(auth.url+url, cookies=auth.session,params=parameter)
            return resp
        except requests.exceptions.HTTPError as errh:
            print("Connection Lost for AM4. Retrying")
            print("HTTP Error") 
            print(errh.args[0])
            return
        except requests.exceptions.ReadTimeout as errrt:
            print("Connection Lost for AM4. Retrying")
            print("Time out")
            print(errrt)
            return
        except requests.exceptions.ConnectionError as conerr:
            print("Connection Lost for AM4. Retrying")
            print("Connection error")
            print(conerr)
            return
        except requests.exceptions.RequestException as errex:
            print("Connection Lost for AM4. Retrying")
            print("Exception request")
            print(errex)
            return
        
