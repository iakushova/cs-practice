from logstats import parse_event, count_levels, top_errors, format_report


def main():
    filename = input().strip()

    with open(filename, encoding="utf-8") as log:
        total = 0
        error_count = 0
        broken_count = 0

        for line in log:
            if not line.strip():
                continue

            total += 1

            try:
                event = parse_event(line)

                if event["level"] == "ERROR":
                    error_count += 1

            except ValueError:
                broken_count += 1

    print(total)
    print(error_count)
    print(broken_count)

    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    main()
