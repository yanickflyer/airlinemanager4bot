import os

class auth:
    session={
        "PHPSESSID":os.environ["PHP_SESSION"]
    }
    url="https://airlinemanager.com/"