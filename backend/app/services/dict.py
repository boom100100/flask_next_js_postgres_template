class DictService:
    @staticmethod
    def to_dict(db_model_instance) -> dict:
        """Converts a db.Model instance into a dict representation of the entire data row."""
        # excluding fields not necessary
        # columns only (no relationships) included
        return {
            column.name: db_model_instance.__getattribute__(column.name)
            for column in db_model_instance._sa_instance_state.mapper.columns
        }
