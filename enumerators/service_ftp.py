class Ftp():
    def __init__(ip_addr,port):
        self.ip_addr = ip_addr
        self.port = port
        self.results = {}

    def check_anon_login(self):
        username = "anonymous"
        password = ""
        
        self.results["anonymous_login"] = can_login

    def grab_banner(self):

        self.results["banner"] = banner
        pass

    def brute_force(self):
        valid_creds = []
        """
        valid_creds = [
                [username_1,password_1],
                [username_2,password_2]
            ]
        """

        self.results["credentials"] = "test"
        pass

    def 
