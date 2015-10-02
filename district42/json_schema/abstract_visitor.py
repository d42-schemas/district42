class AbstractVisitor:
  def visit_null(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_boolean(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_number(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_integer(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_float(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_string(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_array(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_array_of(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_object(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_any(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_any_of(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_one_of(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_enum(self, schema, *args, **kwargs):
    raise NotImplementedError()

  def visit_undefined(self, schema, *args, **kwargs):
    raise NotImplementedError()
