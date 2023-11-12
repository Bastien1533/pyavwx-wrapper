from dataclasses import dataclass, is_dataclass
import typing
from pyavwx.const import GITHUB_URL


# This function wrapper enable dataclass to have other dataclass as types
# it casts the dict coresponding to the nested dataclass in the types dataclass
# if the Metar class has an info field typed to station, it will cast the dict coresponding to station.
# The same goes for lists of dataclass.
def nested_dataclass(*args, **kwargs):
    def wrapper(cls):
        cls = dataclass(cls, **kwargs)
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            for name, value in kwargs.items():
                field_type = cls.__annotations__.get(name, None)
                # if the value we want to cast in is a dict
                if is_dataclass(field_type) and isinstance(value, dict):
                    new_obj = field_type(
                        **{
                            key: value
                            for key, value in value.items()
                            if key in field_type.__annotations__
                        }
                    )
                    kwargs[name] = new_obj

                # if the value we want to cast in is a list of dict
                if type(value) == list and len(value) != 0 and field_type is not None:
                    # ⇩⇩⇩⇩⇩⇩⇩ https://koor.fr/Python/API/python/types/GenericAlias/Index.wp ⇩⇩⇩⇩⇩⇩⇩

                    list_type = field_type.__args__[0]
                    if list_type != typing.Any:
                        new_obj = list([list_type(**d) for d in value])
                        kwargs[name] = new_obj
            try:
                original_init(self, *args, **kwargs)
            except TypeError as e:
                print(
                    f"Warning: {e}, This might be due to an undocumented aspect of the Api, Please report it at {GITHUB_URL}/issues"
                )

        cls.__init__ = __init__
        return cls

    return wrapper(args[0]) if args else wrapper


# A reusable url builder tailored for this wrapper
def url_builder(
    url_modifier: str,
    base_url: str,
    args: dict,
    main_payload: str,
    include_main: bool = True,
) -> str:
    # Building URL:
    # To get something like that: metar?options=translate&format=json&remove=&filter=
    # We directly take the function args if they are provided, without self and url_modifier
    url = base_url + url_modifier + f"{main_payload if include_main else ''}?"
    if args.get("self"):
        del args["self"]
    if args.get("url_modifier"):
        del args["url_modifier"]

    for arg in args:
        value = args.get(arg)
        if value and value != main_payload:
            if type(value) == bool:
                if value:
                    value = "true"
                else:
                    value = "false"
            url = url + f'{arg}={str(value).replace(" ", "")}&'
    return url
