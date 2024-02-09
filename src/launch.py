import functions, maintenance, money, time

class launch:
    def fuel():
        while True:
            functions.actions.purchase_fuel()
            functions.actions.buy_quota()
            time.sleep(1800)
    
    def depart_maintenance():
        while True:
            maintenance.maintenance.get_aircraft()
            functions.actions.depart_all()
            money.money.get_finance()
            time.sleep(300)