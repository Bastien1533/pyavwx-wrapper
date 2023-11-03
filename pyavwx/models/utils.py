from dataclasses import dataclass, is_dataclass


def nested_dataclass(*args, **kwargs):
    def wrapper(cls):
        cls = dataclass(cls, **kwargs)
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            for name, value in kwargs.items():
                field_type = cls.__annotations__.get(name, None)
                if is_dataclass(field_type) and isinstance(value, dict):
                    new_obj = field_type(
                        **{key: value for key, value in value.items() if key in field_type.__annotations__})
                    kwargs[name] = new_obj
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__
        return cls

    return wrapper(args[0]) if args else wrapper


def url_builder(url_modifier: str, base_url: str, args: dict, main_payload: str) -> str:
    # Building URL: 
    # To get something like that: metar?options=translate&format=json&remove=&filter=
    # We directly take the function args if they are provided, without self and url_modifier
    url = base_url + url_modifier + f"{main_payload}?"
    if args.get("self"):
        del args["self"]
    if args.get("url_modifier"):
        del args["url_modifier"]

    for arg in args:
        value = args.get(arg)
        if value:
            url = url + f'{arg}={str(value).replace(" ", "")}&'
    return url
