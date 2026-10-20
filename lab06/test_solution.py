from solution import count_by_extension, deepest_path, human_size

paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

assert count_by_extension(paths) == {
    "pdf": 1,
    "txt": 1,
    "png": 1,
    "": 1
}

assert count_by_extension([]) == {}

assert deepest_path(paths) == "docs/img/logo.png"
assert deepest_path([]) == ""
assert deepest_path(["a/b/c.txt", "x/y/z.txt"]) == "a/b/c.txt"

assert human_size(900) == "900 Б"
assert human_size(1536) == "1.5 КБ"
assert human_size(5242880) == "5.0 МБ"
assert human_size(0) == "0 Б"
assert human_size(3221225472) == "3.0 ГБ"

print("Все тесты пройдены!")
