from dependency_injector import containers, providers
from app.infrastructure.handlers import Handlers
from app.infrastructure.repositories.table import TableInDBRepository
from app.application.services.table import TableService

class Container(containers.DeclarativeContainer):
    #* Load all handlers (For me means where to save the endponts) where @Injects are set 
    wiring_config =  containers.WiringConfiguration(modules=Handlers.modules())

    #* Repositories
    table_repository = providers.Singleton(TableInDBRepository)

    #* Services 
    table_services = providers.Factory(TableService, table_repository)