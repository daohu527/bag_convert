## User-defined conversion type
We will provide user registration interface to customize type conversion.
```python
register.add(topic, convert_func)

register.add(type, convert_func)
```

For convenience, we provide a config file where users can customize the conversion.


## Message asymmetry
There is no one-to-one correspondence between ros message and cyber message. Therefore, we have done an asymmetric conversion here, converting from a message to an approximate message.

Another feasible solution is to implement all ros common_msg in protobuf and perform peer-to-peer transplantation. In this way, except for a few types, most messages can be directly compatible.

This might be a cooler solution!!!
