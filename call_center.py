import time

class CallCenter:
    def __init__(self, blacklist=[], *, time_adaptor=None):
        if time_adaptor is None:
            time_adaptor = lambda: time.time()
        self.time_adaptor = time_adaptor
        self.call_logs = []
        self.alert_logs = []
        self.blacklist = set(blacklist)

    def call(self, event):
        name, phone_number = event
        
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
    pass


class LocalCallCenter(CallCenter):
    def __init__(self, area_code, blacklist=[], *, time_adaptor=None):
        super().__init__(blacklist, time_adaptor=time_adaptor)
        self.area_code = area_code


