import sys
import jpholiday
import xml.dom.minidom
from dateutil.parser import parse as parse_date
from datetime import datetime, date, timedelta


def main():

    args = sys.argv
    start = datetime.now().date()
    try:
        start = parse_date(args[1]).date()
    except:
        pass

    end = datetime.now().date()
    try:
        end = parse_date(args[2]).date()
    except:
        pass
    holidays = jpholiday.holidays(start, end)

    dom = xml.dom.minidom.Document()
    root = dom.createElement('holidays')
    root.setAttribute('start', start.strftime('%Y/%m/%d'))
    root.setAttribute('end', end.strftime('%Y/%m/%d'))
    dom.appendChild(root)

    for holiday in holidays:
        node = dom.createElement('holiday')
        node.setAttribute('date', holiday[0].strftime('%Y/%m/%d'))
        node.setAttribute('name', holiday[1])
        root.appendChild(node)

    print(dom.toprettyxml())


if __name__ == "__main__":
    main()
