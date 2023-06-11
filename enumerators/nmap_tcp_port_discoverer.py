import subprocess
import json
import xmltodict
import os
import xml.etree.ElementTree as ET


class NmapTcpPortDiscoverer:
    def __init__(self,ip_addr):
        self.ip_addr = ip_addr
        self.results_output_file = os.path.abspath("/tmp/horus_results/tcp_all_ports.xml")
        self.cmd = [
            "nmap",
            "-v2",
            "-n",
            "-Pn",
            "-p-",
            "-T4",
            "--min-rate",
            "1000",
            "-oX",
            self.results_output_file,
            self.ip_addr
        ]
    
    def scan(self):
        print("Starting port discovery")
        subprocess.run(self.cmd, check=True)
        open_ports = self.extract_open_ports()
        print("Finished port discovery")
        print(open_ports)
        return open_ports
        # subprocess.run(self.cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # convert_xml_file_to_json_file(self.results_output_file_xml,self.results_output_file_json)

    def extract_open_ports(self):
        open_ports = []
        tree = ET.parse(self.results_output_file)
        root = tree.getroot()
        for port in root.findall('.//port'):
            state = port.find('state')
            if state is not None and state.get('state') == 'open':
                port_id = port.get('portid')
                open_ports.append(port_id)
        
        return open_ports

