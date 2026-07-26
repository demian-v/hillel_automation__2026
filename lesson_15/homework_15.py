import csv
import json
import xml.etree.ElementTree as ET
import pathlib
import logging

'''Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv'''

FILE_NAME = "Vyrozub"

base = pathlib.Path(__file__).parent
csv_dir = base / "work_with_csv"

file1 = csv_dir / "random-michaels.csv"
file2 = csv_dir / "r-m-c.csv"
result_file = base / f"result_{FILE_NAME}.csv"

all_rows = []
for file_path in (file1, file2):
    with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = list(csv.reader(csvfile))
        all_rows += reader

unique_rows = []
seen = set()
for row in all_rows:
    key = tuple(row)
    if key not in seen:
        seen.add(key)
        unique_rows.append(row)

with open(result_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)

print(f"Прочитано рядків: {len(all_rows)}")
print(f"Унікальних: {len(unique_rows)}")
print(f"Прибрано дублікатів: {len(all_rows) - len(unique_rows)}")

'''Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу 
виведіть через логер на рівні еррор у файл json__<your_second_name>.log'''

base = pathlib.Path(__file__).parent
json_dir = base / "work_with_json"
log_file = base / f"json__{FILE_NAME}.log"

logger = logging.getLogger("json_validator")
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(handler)

for json_file in sorted(json_dir.glob("*.json")):
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            json.load(f)
            print(f"{json_file.name}: валідний")
        except json.JSONDecodeError as e:
            logger.error("Invalid JSON in %s: %s", json_file.name, e)
            print(f"{json_file.name}: НЕВАЛІДНИЙ (записано у {log_file.name})")

'''Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення 
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо'''

base = pathlib.Path(__file__).parent
xml_file = base / "work_with_xml" / "groups.xml"

logger = logging.getLogger("xml_search")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))
logger.addHandler(handler)


def find_incoming_by_number(xml_path, group_number):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        if group.findtext("number") == str(group_number):
            timing = group.find("timingExbytes")
            incoming = timing.findtext("incoming") if timing is not None else None

            if incoming is not None:
                logger.info("group %s: timingExbytes/incoming = %s", group_number, incoming)
            else:
                logger.info("group %s: немає timingExbytes/incoming", group_number)
            return incoming

    logger.info("group %s: не знайдено", group_number)
    return None


find_incoming_by_number(xml_file, 0)
find_incoming_by_number(xml_file, 4)
find_incoming_by_number(xml_file, 1)
find_incoming_by_number(xml_file, 99)
