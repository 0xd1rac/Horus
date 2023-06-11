def convert_xml_file_to_json_file(xml_file_path,json_file_path):
    # Load XML file and convert to JSON
    with open(xml_file_path, 'r') as xml_file:
        xml_data = xml_file.read()
        json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

    # Save JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)