import subprocess
import json
import xmltodict
import os
import xml.etree.ElementTree as ET


# Should move the file locations to a config file later on

class NmapTcpServiceDiscoverer:
    def __init__(self,ip_addr,open_ports):
        self.ip_addr = ip_addr
        # self.port_discoverer_results_file = os.path.abspath("../scan_results/nmap/tcp_all_ports.xml")
        self.results_output_file = os.path.abspath("/tmp/horus_results/tcp_services.xml")
        self.open_ports = open_ports

        self.cmd = [
            "nmap",
            "-v2",
            "-Pn",
            "-p", ",".join(self.open_ports),
            "-sV",
            "-T4",
            "--min-rate", "1000",
            "-oX", 
            self.results_output_file,
            self.ip_addr
        ]
        
    def extract_services(self):
        tree = ET.parse(self.results_output_file)
        root = tree.getroot()
        services = []
        for port in root.findall('.//port'):
            portid = port.get('portid')
            service = port.find('service').get('name')
            services.append((portid, service))
        
        return services

    
    def scan(self):
        print("Starting service nmap scan")
        subprocess.run(self.cmd, check=True)
        services = self.extract_services()
        print("Finished service nmap scan")
        return services
        # subprocess.run(self.cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
