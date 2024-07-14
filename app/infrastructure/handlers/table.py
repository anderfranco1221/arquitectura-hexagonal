from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from app.infrastructure.container import Container
from app.application.services.table import TableService

from app.infrastructure.schemas.table import TableCountOutput


router = APIRouter(
    prefix="/table",
    tags=["table"]
)
@router.get('/{name_table}/count', response_model=TableCountOutput)
@inject
def get_count_row(name_table: str, table_services: TableService  = Depends(Provide[Container.table_services]))-> int:
    response: int = table_services.table_count_rows(name_table)
    #print({'name': name_table, 'countRow': response})
    return {'table_name': name_table, 'count_row': response}