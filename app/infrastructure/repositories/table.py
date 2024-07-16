from app.domain.repositories.table import TableRepository 
from app.infrastructure.database.config import conexion
from app.infrastructure.exceptions import InvalidNameTable

class TableInDBRepository(TableRepository):

    #* Get count the rows in the table
    def get_count_row(self, name_table: str) -> int:
        db = conexion()
        cur = db.cursor()

        try:
            # Query the table
            cur.execute("SELECT COUNT(*) FROM " + name_table)
            count = cur.fetchone()[0]

            cur.close()
            return count 
        except :
            raise InvalidNameTable
