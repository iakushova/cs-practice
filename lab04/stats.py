def parse_record(line: str) -> dict:
    """Разбирает одну строку журнала."""

    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("В строке должно быть ровно три поля")

    city = parts[0].strip()
    temp_text = parts[1].strip().replace(",", ".")
    date = parts[2].strip()

    if not city:
        raise ValueError("Не указан город")

    if not date:
        raise ValueError("Не указана дата")

    try:
        temperature = float(temp_text)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    """Возвращает только корректные записи."""

    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records


def average_by_city(records: list[dict]) -> dict:
    """Вычисляет среднюю температуру каждого города."""

    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0) + temperature
        counts[city] = counts.get(city, 0) + 1

    averages = {}

    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    """Возвращает город с самой высокой средней температурой."""

    averages = average_by_city(records)

    if not averages:
        return ""

    return sorted(averages, key=lambda city: (-averages[city], city))[0]
