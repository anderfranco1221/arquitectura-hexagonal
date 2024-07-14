from pydantic import BaseModel

class TableCountOutput(BaseModel):
    table_name: str
    count_row: int