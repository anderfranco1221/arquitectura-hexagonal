from app.domain.repositories.table import TableRepository 

class TableInDBRepository(TableRepository):

    count_rows = 777

    def get_count_row(self, nameTable: str) -> int:
        try:
            #TODO: Realizar la consulta en esta parte
            return self.count_rows 
        except StopIteration:
            return None
