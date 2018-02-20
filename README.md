# proto3-duplicate-fields

Investigating proto3 behaviour when handling duplicate fields

## Instructions

Install `protoc` compiler. I'm using the following from the GitHub releases.

```
$ protoc --version
libprotoc 3.5.1
```

Install `protobuf` Python `pip` module

```bash
pip install -r requirements.txt
```

Compile the protos

```bash
protoc -I=schema/ --python_out=. schema/can.proto
```

This isn't actually necessary, since I've committed the file already (see the 
`can_pb2.py` file).

Then run `main.py`

```bash
python main.py
```

## Expected Behaviour

Since `messages.asciipb` has a duplicate field, shouldn't it fail to unpack the
proto?

According to the [Specifying Field Rules](https://developers.google.com/protocol-buffers/docs/proto3#specifying-field-rules)
proto3 documentation, it seems to indicate that message fields can be one of 
the following:

> * singular: a well-formed message can have zero or one of this field (but not more than one).
> * `repeated`: this field can be repeated any number of times (including zero) in a well-formed message. The order of the repeated values will be preserved.

## Actual Behaviour

It seems to successfully unpack, and silently drops the fields occurring before
the last value.
