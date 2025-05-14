import os

class Ping:
    def execute(self, ip):
        if ip.startswith("192."):
            os.system(f"ping -n 10 {ip}")
        else:
            print("IP no permitida.")

    def executefree(self, ip):
        os.system(f"ping -n 10 {ip}")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)