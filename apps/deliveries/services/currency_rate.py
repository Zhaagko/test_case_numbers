import requests
from xml.etree import ElementTree
import datetime


def get_rate(currency_name: str = "Доллар США") -> float:
    current_date = datetime.date.today().strftime("%d/%m/%Y")
    req = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}&d=0")

    xml_tree = ElementTree.fromstring(req.text)

    for item in xml_tree:
        if item[3].text == currency_name:
            return float(item[4].text.replace(",", "."))
