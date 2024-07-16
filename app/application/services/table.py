from app.domain.use_cases.table import TableUseCases
from app.domain.repositories.table import TableRepository # type: ignore


class TableService(TableUseCases):

    def __init__(self, table_repository: TableRepository):
        super().__init__(table_repository)

    def table_count_rows(self, name_table: str) -> int:
        count_rows = self.table_repository.get_count_row(name_table)

        return count_rows