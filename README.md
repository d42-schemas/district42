# district42

[![Codecov](https://img.shields.io/codecov/c/github/nikitanovosibirsk/district42/master.svg?style=flat-square)](https://codecov.io/gh/nikitanovosibirsk/district42)
[![PyPI](https://img.shields.io/pypi/v/district42.svg?style=flat-square)](https://pypi.python.org/pypi/district42/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/district42?style=flat-square)](https://pypi.python.org/pypi/district42/)
[![Python Version](https://img.shields.io/pypi/pyversions/district42.svg?style=flat-square)](https://pypi.python.org/pypi/district42/)

Data description language for defining data models

(!) Work in progress, breaking changes are possible until v2.0 is released

## Installation

```sh
pip3 install district42
```

## Usage

```python
from district42 import schema

UserSchema = schema.dict({
    "id": schema.int.min(1),
    "name": schema.str | schema.none,
    "is_deleted": schema.bool,
})

print(UserSchema)
```

More powerful with:
- [blahblah](https://github.com/nikitanovosibirsk/blahblah) — Fake data generator
- [valera](https://github.com/nikitanovosibirsk/valera) — Validator
- [revolt](https://github.com/nikitanovosibirsk/revolt) — Value substitutor

And [more](https://github.com/topics/district42)


## Documentation

* [Documentation](#documentation)
  * [None](#none)
    * [schema.none](#schemanone)
  * [Bool](#bool)
    * [schema.bool](#schemabool)
    * [schema.bool(`value`)](#schemaboolvalue)
  * [Int](#int)
    * [schema.int](#schemaint)
    * [schema.int(`value`)](#schemaintvalue)
    * [schema.int.min(`value`)](#schemaintminvalue)
    * [schema.int.max(`value`)](#schemaintmaxvalue)
  * [Float](#float)
    * [schema.float](#schemafloat)
    * [schema.float(`value`)](#schemafloatvalue)
    * [schema.float.min(`value`)](#schemafloatminvalue)
    * [schema.float.max(`value`)](#schemafloatmaxvalue)
  * [Str](#str)
    * [schema.str](#schemastr)
    * [schema.str.len(`length`)](#schemastrlenlength)
    * [schema.str.len(`min_length`, `max_length`)](#schemastrlenmin_length-max_length)
    * [schema.str.alphabet(`letters`)](#schemastralphabetletters)
    * [schema.str.contains(`substr`)](#schemastrcontainssubstr)
    * [schema.str.regex(`pattern`)](#schemastrregexpattern)
  * [List](#list)
    * [schema.list](#schemalist)
    * [schema.list(`elements`)](#schemalistelements)
    * [schema.list(`type`)](#schemalisttype)
    * [schema.list(`type`).len(`length`)](#schemalisttypelenlength)
    * [schema.list(`type`).len(`min_length`, `max_length`)](#schemalisttypelenmin_length-max_length)
  * [Dict](#dict)
    * [schema.dict](#schemadict)
    * [schema.dict(`keys`)](#schemadictkeys)
  * [Any](#any)
    * [schema.any](#schemaany)
    * [schema.any(`*types`)](#schemaanytypes)
  * [Custom Types](#custom-types)
    * [1. Declare Schema](#1-declare-schema)
    * [2. Register Representor](#2-register-representor)
    * [3. Use](#3-use)

### None

#### schema.none

```python
sch = schema.none
```

### Bool

#### schema.bool

```python
sch = schema.bool
```

#### schema.bool(`value`)

```python
sch = schema.bool(True)
```

### Int

#### schema.int

```python
sch = schema.int
```

#### schema.int(`value`)

```python
sch = schema.int(42)
```

#### schema.int.min(`value`)

```python
sch = schema.int.min(0)
```

#### schema.int.max(`value`)

```python
sch = schema.int.max(0)
```

### Float

#### schema.float

```python
sch = schema.float
```

#### schema.float(`value`)

```python
sch = schema.float(3.14)
```

#### schema.float.min(`value`)

```python
sch = schema.float.min(0.0)
```

#### schema.float.max(`value`)

```python
sch = schema.float.max(0.0)
```

### Str

#### schema.str

```python
sch = schema.str
```

#### schema.str.len(`length`)

```python
sch = schema.str.len(10)
```

#### schema.str.len(`min_length`, `max_length`)

```python
sch = schema.str.len(1, ...)
```

```python
sch = schema.str.len(..., 32)
```

```python
sch = schema.str.len(1, 32)
```

#### schema.str.alphabet(`letters`)

```python
digits = "01234567890"
sch = schema.str.alphabet(digits)
```

#### schema.str.contains(`substr`)

```python
sch = schema.str.contains("@")
```

#### schema.str.regex(`pattern`)

```python
import re
sch = schema.str.regex(r"[a-z]+")
```

### List

#### schema.list

```python
sch = schema.list
```

#### schema.list(`elements`)

```python
sch = schema.list([schema.int(1), schema.int(2)])
```

#### schema.list(`type`)

```python
sch = schema.list(schema.int)
```

#### schema.list(`type`).len(`length`)

```python
sch = schema.list(schema.int).len(3)
```

#### schema.list(`type`).len(`min_length`, `max_length`)

```python
sch = schema.list(schema.int).len(1, ...)
```

```python
sch = schema.list(schema.int).len(..., 10)
```

```python
sch = schema.list(schema.int).len(1, 10)
```

### Dict

#### schema.dict

```python
sch = schema.dict
```

#### schema.dict(`keys`)

```python
sch = schema.dict({
    "id": schema.int,
    "name": schema.str | schema.none,
    optional("platform"): schema.str,
})
```

### Any

#### schema.any

```python
sch = schema.any
```

#### schema.any(`*types`)

```python
sch = schema.any(schema.str, schema.int)
```

### Custom Types

#### 1. Declare Schema

```python
from typing import Any
from uuid import UUID
from district42 import Props, SchemaVisitor, SchemaVisitorReturnType as ReturnType
from district42.types import Schema
from niltype import Nilable


class UUIDProps(Props):
    @property
    def value(self) -> Nilable[UUID]:
        return self.get("value")


class UUIDSchema(Schema[UUIDProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        return visitor.visit_uuid(self, **kwargs)

    def __call__(self, /, value: UUID) -> "UUIDSchema":
        return self.__class__(self.props.update(value=value))
```

#### 2. Register Representor

```python
from typing import Any
from district42.representor import Representor
from niltype import Nil


class UUIDRepresentor(Representor, extend=True):
    def visit_uuid(self, schema: UUIDSchema, *, indent: int = 0, **kwargs: Any) -> str:
        r = f"{self._name}.uuid"

        if schema.props.value is not Nil:
            r += f"({schema.props.value!r})"

        return r
```

#### 3. Use

```python
from uuid import uuid4
from district42 import register_type, schema

register_type("uuid", UUIDSchema)

print(schema.uuid(uuid4()))
# schema.uuid(UUID('ce80d2b7-cdce-4e24-ab26-00c75471ce78'))
```

Full code available here: [district42_exp_types/uuid](https://github.com/nikitanovosibirsk/district42-exp-types/tree/master/district42_exp_types/uuid)
