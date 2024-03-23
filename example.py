from data_processing import XMLProcessor

if __name__ == "__main__":
    xml_processor = XMLProcessor()
    xml_root = xml_processor.read_xml("data/data.xml")

    if xml_root is not None:
        data = xml_processor.process_xml()
        print(data.count)
        print(data.attributes)
        print(data.values)
