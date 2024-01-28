import functions, maintenance, money, time

class launch:
    def fuel():
        while True:
            functions.actions.purchase_fuel(1)
            functions.actions.buy_quota(1)
            time.sleep(1800)
    
    def depart_maintenance():
        while True:
            maintenance.maintenance.get_aircraft(1)
            functions.actions.depart_all(1)
            money.money.get_finance(1)
            time.sleep(300)