import json


def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []

    lines = text.strip().split('\n')
    headers = lines[0].split(',')
    records = []

    for line in lines[1:]:
        values = line.split(',')
        record = {}

        for i in range(len(headers)):
            record[headers[i].strip()] = values[i].strip()

        records.append(record)

    return records


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    for line in lines:
        line = line.split('#')[0].strip()

        if not line:
            continue

        if line.startswith('- '):
            if current_list is not None:
                current_list.append(convert_value(line[2:].strip()))
            continue

        if ':' not in line:
            continue

        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()

        if not value:
            settings[key] = []
            current_list = settings[key]
        else:
            settings[key] = convert_value(value)
            current_list = None

    return settings


def convert_value(value: str):
    if value in ('true', 'yes'):
        return True
    if value in ('false', 'no'):
        return False

    try:
        return int(value)
    except ValueError:
        pass

    if '.' in value:
        try:
            return float(value)
        except ValueError:
            pass

    return value

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []

    for row in rows:
        record = extra.get(row.get(key), {}).copy()
        record.update(row)
        result.append(record)

    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
