from Service import Service

class Port:
    def __init__(self,port_num: int,state: str,transport_protocol: str, service: Service):
        self.port_num = port_num
        self.state = state 
        self.transport_protocol = transport_protocol
        self.service = service
        
