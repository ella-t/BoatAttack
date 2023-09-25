import xml.etree.ElementTree as ET
import argparse

root = None


def get_test_xml():
    global root
    root = ET.fromstring(args.input.read())


def get_test_xml_from_file(finput):
    global root
    root = ET.fromstring(finput.read())


def present_test_header():
    if type(root) is ET.Element:
        headerstring = "\nBoatAttack Startup Test Results\n"
        headerstring += "{} total tests\n".format(root.attrib["total"])
        headerstring += "{} passed, {} failed ".format(root.attrib["passed"], root.attrib["failed"])
        if int(root.attrib["failed"]) > 0:
            headerstring += "❌"
        else:
            headerstring += "✔"
        headerstring += "\n"
        return headerstring


def present_test_fixture(fixture):
    fixturestring = "{} Fixture Results\n".format(fixture.attrib["name"])
    for test in fixture.findall("test-case"):
        fixturestring += test.attrib["name"]
        if test.attrib["result"] == "Passed":
            fixturestring += " - Passed ✔ - "
        elif test.attrib["result"] == "Failed":
            fixturestring += " - Failed ❌ - "
        fixturestring += "{} elapsed".format(test.attrib["duration"])
        fixturestring += "\n"
        if test.attrib["result"] == "Failed":
            fixturestring += test.find("failure").find("message").text
            fixturestring += "\n"
    return fixturestring


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Unity test result XML file to parse and present.", type=argparse.FileType('r'))
    parser.add_argument("-d", "--detailed", help="output detailed test results", action="store_true")
    args = parser.parse_args()
    get_test_xml()
    print(present_test_header())
    if args.detailed:
        for i in root.iter("test-suite"):
            if i.attrib["type"] == "TestFixture":
                print(present_test_fixture(i))
