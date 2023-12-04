"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730489972"


def read_csv_rows(name: str) -> list[dict[str, str]]:
    """Read an entire csv of data into a list of dict."""
    product: list[dict[str, str]] = []
    file_handle = open(name, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        product.append(row)
    file_handle.close()
    return product


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return values in a table column under a specific header."""
    product: list[str] = []
    for row in table:
        product.append(row[header])
    return product 


def columnar(table_two: list[dict[str, str]]) -> dict[str, list[str]]:
    """Trasforms a list of rows into a table of dictionary of columns."""
    product: dict[str, list[str]] = {}
    for column in table_two[0]:
        product[column] = column_values(table_two, column)
    return product 


def head(ctable: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Producing a new column based table with a certain parameter of rows."""
    product: dict[str, list[str]] = {}
    if len(ctable) <= row_number:
        return ctable
    for column_names, values in ctable.items():
        empty_list: list[str] = []
        index: int = 0
        while index < row_number:
            empty_list.append(values[index])
            index = index + 1
        product[column_names] = empty_list
    return product 


def select(ctable: dict[str, list[str]], new: list[str]) -> dict[str, list[str]]:
    """Producing a column-based table with only a specific columns."""
    product: dict[str, list[str]] = {}
    for column_names, values in ctable.items():
        if column_names in new:
            product[column_names] = values
    return product


def concat(ctable: dict[str, list[str]], ctable_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Producing column based table from the two ctables combined."""
    product: dict[str, list[str]] = {}
    for column_names, values in ctable.items():
        product[column_names] = values
    for column_names, values in ctable_two.items():
        if column_names in product:
            product[column_names] += values
        else:
            product[column_names] = values
    return product 


def count(values: list[str]) -> dict[str, int]:
    """Count number of times the values appear in list."""
    product: dict[str, int] = {}
    for value in values:
        if value in product:
            product[value] = product[value] + 1
        else:
            product[value] = 1
    return product