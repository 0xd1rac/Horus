from ServiceTags import ServiceTag
class Service:
    def __init__(self,name: str, service_tag: ServiceTag, version: str):
        self.name = name
        self.service_tag = service_tag
        self.version = version