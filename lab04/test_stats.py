import unittest

from stats import (
    parse_record,
    read_valid,
    average_by_city,
    warmest_city,
)


class TestStats(unittest.TestCase):

    def test_parse_record(self):
        record = parse_record("Азов;24.5;2026-07-01")
        self.assertEqual(record["city"], "Азов")
        self.assertEqual(record["temperature"], 24.5)

    def test_invalid_record(self):
        with self.assertRaises(ValueError):
            parse_record("мусор")

    def test_read_valid(self):
        lines = [
            "Азов;24.5;2026-07-01",
            "",
            "мусор",
        ]
        self.assertEqual(len(read_valid(lines)), 1)

    def test_empty_records(self):
        self.assertEqual(average_by_city([]), {})
        self.assertEqual(warmest_city([]), "")

    def test_warmest_city(self):
        records = read_valid([
            "Азов;20;2026-07-01",
            "Таганрог;30;2026-07-01",
        ])
        self.assertEqual(warmest_city(records), "Таганрог")

    def test_alphabetical_tie(self):
        records = read_valid([
            "Батайск;20;2026-07-01",
            "Азов;20;2026-07-01",
        ])
        self.assertEqual(warmest_city(records), "Азов")


if __name__ == "__main__":
    unittest.main()
