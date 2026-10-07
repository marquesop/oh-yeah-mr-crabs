class Server:
    def __init__(self, hostname, status, cpu_usage):
        self.hostname = hostname
        self.status = status
        self.cpu_usage = cpu_usage

    def boot(self):
       self.status = True
       print(f"{self.hostname} is now on.")

    def shutdown(self):
        self.status = False
        print(f"{self.hostname} is now off.")

    def load_increase(self, amount):
        self.cpu_usage += amount
        print(f"{self.hostname} CPU's usage increased to {self.cpu_usage}%.")

    def load_decrease(self, amount):
        self.cpu_usage -= amount
        print(f"{self.hostname} CPU's usage decreased to {self.cpu_usage}%.")

    def status(self):
        print(f"{self.hostname}: Status: {'ON' if self.status else 'OFF'}, CPU Usage: {self.cpu_usage}%")


the_server = Server("Server1", False, 10)
the_server.boot()
the_server.load_increase(20)
the_server.status()