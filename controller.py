from enumerators.nmap_tcp_port_discoverer import NmapTcpPortDiscoverer
from enumerators.nmap_tcp_service_discoverer import NmapTcpServiceDiscoverer


open_ports = NmapTcpPortDiscoverer("10.150.150.69").scan()
services = NmapTcpServiceDiscoverer("10.150.150.69",open_ports).scan()
print(services)



# class Controller:
#     def __init__(self,ip_addr):
#         self.ip_addr = ip_addr
#         self.open_ports = NmapTcpPortDiscoverer(self.ip_addr)
#         self.services = NmapTcpServiceDiscoverer(self.ip_addr,self.open_ports)

    
