from app.models import Example
from app.services.crud import CrudService


class ExampleService(CrudService):
    def __init__(self):
        super().__init__(Example)
