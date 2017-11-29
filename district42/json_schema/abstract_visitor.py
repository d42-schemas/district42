class AbstractVisitor:

    def visit_null(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_boolean(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_number(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_string(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_timestamp(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_array(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_array_of(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_object(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_any(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_any_of(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_one_of(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_enum(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()

    def visit_undefined(self, schema_inst, *args, **kwargs):
        raise NotImplementedError()
