from abc import ABC, abstractmethod
from app.domain.repositories.table import TableRepository

class TableUseCases(ABC):

    @abstractmethod
    def __init__(self, table_repository: TableRepository
                 ):
        self.table_repository = table_repository
