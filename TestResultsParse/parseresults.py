import xml.etree.ElementTree as ET
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input", help="Unity test result XML file to parse and present.", type=argparse.FileType('r'))
args = parser.parse_args()

root = None


def get_test_xml():
    global root
    root = ET.fromstring(args.input.read())


def present_test_header():
    if type(root) is ET.Element:
        headerstring = "BoatAttack Startup Test Results\n"
        headerstring += "{} total tests\n".format(root.attrib["total"])
        headerstring += "{} passed, {} failed ".format(root.attrib["passed"], root.attrib["failed"])
        if int(root.attrib["failed"]) > 0:
            headerstring += "❌"
        else:
            headerstring += "✔"
        print(headerstring)


def present_test_fixture():
    pass


def present_tests():
    pass


if __name__ == "__main__":
    get_test_xml()
    present_test_header()
    present_tests()
