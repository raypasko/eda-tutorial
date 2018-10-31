import time

class CallCenter:
    def __init__(self, blacklist=[], *, time_adaptor=None):
        if time_adaptor is None:
            time_adaptor = lambda: time.time()
        self.time_adaptor = time_adaptor
        self.call_logs = []
        self.alert_logs = []
        self.blacklist = set(blacklist)

    def call(self, phone_number):
        t = self.time()
        self.call_logs.append((t, phone_number))
        if phone_number in self.blacklist:
            self.alert_logs.append((self.time(), phone_number))

    def time(self):
        return self.time_adaptor()

    @property
    def number_of_calls(self):
        return len(self.call_logs)

def get_area_code(phone_number):
    return phone_number.split('/')[0]

class CallAgency(CallCenter):
    def __init__(self, call_centers, blacklist=[], *, time_adaptor=None):
        super().__init__(blacklist, time_adaptor=time_adaptor)
        self.call_centers = {}
        for call_center in call_centers:
            self.call_centers[call_center.area_code] = call_center

    def call(self, phone_number):
        super().call(phone_number)

        area_code = get_area_code(phone_number)
        call_center = self.call_centers[area_code]
        call_center.call(phone_number)

class LocalCallCenter(CallCenter):
    def __init__(self, area_code, blacklist=[], *, time_adaptor=None):
        super().__init__(blacklist, time_adaptor=time_adaptor)
        self.area_code = area_code
