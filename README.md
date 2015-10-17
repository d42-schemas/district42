# district42

Data description language (DDL) for defining data models.

### Usage

```python
import district42.json_schema as schema

BlogPost = schema.object({
  'id':         schema.integer.positive,
  'text':       schema.string.max_length(140),
  'lang':       schema.enum('en', 'fr', 'de', 'es', 'it', 'ru'),
  'author':     schema.object({
                  'id':        schema.string.alpha_num.lowecase,
                  'name':      schema.string.length(3, 16),
                  'image_url': schema.string.uri
                }),
  'created_at': schema.timestamp.iso
})
```

### Installation

```sh
$ pip3 install district42
```

### See Also

- [valeera](https://github.com/nikitanovosibirsk/valeera) - Validator for district42 schema
- [blahblah](https://github.com/nikitanovosibirsk/blahblah) - Fake data generator for district42 schema
