def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}

    for path in paths:
        name = path.split("/")[-1]

        if "." in name and not name.startswith("."):
            extension = name.rsplit(".", 1)[1].lower()
        else:
            extension = ""

        if extension in result:
            result[extension] += 1
        else:
            result[extension] = 1

    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    return sorted(paths, key=lambda path: (-path.count("/"), path))[0]


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    index = 0

    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1

    if index == 0:
        return f"{size} {units[index]}"

    return f"{size:.1f} {units[index]}"
