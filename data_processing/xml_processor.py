import xml.etree.ElementTree as ET

from .data_reader import XMLReport


class XMLProcessor:
    """
    A class for processing XML files using the xml.etree.ElementTree module.
    """

    def read_xml(self, file_path: str) -> ET.Element:
        """
        Read an XML file and return the root element.

        :param file_path: The path to the XML file.
        :return: The root element of the XML file.
        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            return root
        except ET.ParseError:
            return f"Error parsing XML file: {file_path}"

    def process_xml(self, root: ET.Element) -> XMLReport:
        """
        Process the root element of an XML file by calling other methods.

        :param root: The root element of the XML file.
        :return: A object of XMLReport class.
        """
        count = self.get_element_count(root)
        attributes = self.get_element_attributes(root)
        values = self.get_element_values(root)

        report = XMLReport(count, attributes, values)
        return report

    def get_element_count(self, root: ET.Element) -> int:
        """
        Get the number of elements in the XML file.

        :param root: The root element of the XML file.
        :return: A number of elements in the XML file.
        """
        element_count = len(root.findall(".//"))
        return element_count

    def get_element_attributes(self, root: ET.Element) -> list:
        """
        Get the unique attributes in the XML file.

        :param root: The root element of the XML file.
        :return: A unique attributes in the XML file.
        """
        all_attributes = []
        for element in root.findall(".//*"):
            attributes = element.attrib
            all_attributes.extend(list(attributes.keys()))
        unique_attributes = set(all_attributes)
        return unique_attributes

    def get_element_values(self, root: ET.Element) -> list:
        """
        Get the unique element values in the XML file.

        :param root: The root element of the XML file.
        :return: A unique element values in the XML file.
        """
        all_values = []
        for element in root.findall(".//*"):
            element_value = element.text
            if element_value is not None:
                all_values.append(element_value)
        unique_values = set(all_values)
        return unique_values
