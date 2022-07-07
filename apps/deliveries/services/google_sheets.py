import gspread
from string import ascii_uppercase as alph_upper


class GoogleSheet:

    def __init__(self, sheet_name: str, table_name: str):
        self._account = gspread.service_account(filename="service_account.json")
        self._sheet = self._account.open(table_name).worksheet(sheet_name)

    def extract_table(self):
        first_row = 1

        while not len(self._sheet.row_values(first_row)):
            first_row += 1

        empty_col = self._sheet.row_values(first_row).count("")

        first_col = alph_upper[(empty_col + 1) % 26] * (((empty_col + 1) // 26) + 1)

        last_row = len(self._sheet.col_values(empty_col+1))

        last_col = alph_upper[(empty_col + 4) % 26] * (((empty_col + 4) // 26) + 1)

        return self._sheet.get(f"{first_col}{first_row+1}:{last_col}{last_row}")
