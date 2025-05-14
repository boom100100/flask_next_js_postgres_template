from typing import List, Optional, Tuple, Union

from app.database import db
from app.services.dict import DictService


class CrudService(DictService):
    """Create, Read, Update, and Delete and represent in API-compatible data formats."""
    def __init__(self, model):
        self.session = db.session
        self.model = model

    def _filter(self, filters: Tuple = (), sort_by: Union[str, List[Tuple[str, str]]] = None):
        '''
        Input:
        tuple of filter arguments
        
        Output:
        query
        Example argument:
        filters = (
            Person.first_name != '',
            Person.id > 1,
            Person.id.in_([child.id for child in children])
        )
        '''
        result = self.session.query(self.model).filter(*filters)

        if not sort_by:
            return result
        order_by_criteria = []
        for criteria in sort_by:
            if isinstance(criteria, str):
                order_by_criteria.append(getattr(self.model, criteria))
                continue

            field = getattr(self.model, criteria[0])
            field_order_method = getattr(field, criteria[1])
            order_by_criteria.append(field_order_method())

        return result.order_by(*order_by_criteria)

    def create_from_dict(self, args) -> db.Model:
        return self.model(**args)

    def update_from_dict(self, args) -> db.Model:
        model_instance = self.session.query(self.model).get(args['id'])
        for key, value in args.items():
            setattr(model_instance, key, value)

        return model_instance

    def delete_from_dict(self, args):
        model_instance = self.session.query(self.model).get(int(args['id']))
        self.session.delete(model_instance)

    def get_one_by_filter(self, data: Tuple = ()) -> Optional[db.Model]:
        return self._filter(data).first()

    def get_many_by_filter(self, data: Tuple = (), sort_by=None) -> list[db.Model]:
        return self._filter(data, sort_by).all()

    def get_one_by_id(self, id) -> Optional[db.Model]:
        return self.session.query(self.model).get(id)
