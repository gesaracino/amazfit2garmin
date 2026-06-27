from pathlib import Path
from xml.etree.ElementTree import Element, parse

TCX_NAMESPACE = "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"

NS = {
    "tcx": TCX_NAMESPACE,
}


def parse_tcx(path: str | Path) -> Element:
    """
    Parse a TCX file and return its root XML element.
    """

    return parse(path).getroot()


def find(root: Element, xpath: str):
    """
    Find a single XML element using the Garmin TCX namespace.
    """

    return root.find(xpath, NS)


def find_all(root: Element, xpath: str):
    """
    Find all XML elements matching an XPath using the Garmin TCX namespace.
    """

    return root.findall(xpath, NS)