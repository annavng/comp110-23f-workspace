"""Working with csv data."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dict with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 

def column_vals(table: list[dict[str, str]], header: str) -> list(str):
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        # append every value under key reader
        result.append(row[header])
    return result