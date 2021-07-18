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
