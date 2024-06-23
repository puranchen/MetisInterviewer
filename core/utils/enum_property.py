def enum_property(enum_cls):
    def getter(instance):
        return getattr(instance, f"_{enum_cls.__name__.lower()}")

    def setter(instance, value):
        if value is not None:
            if isinstance(value, enum_cls):
                setattr(instance, f"_{enum_cls.__name__.lower()}", value)
            elif isinstance(value, str) and value.upper() in enum_cls.__members__:
                setattr(instance, f"_{enum_cls.__name__.lower()}", enum_cls[value.upper()])
            else:
                raise ValueError(f"Invalid value for {enum_cls.__name__.lower()}: {value!r}")
        else:
            setattr(instance, f"_{enum_cls.__name__.lower()}", None)
    
    return property(getter, setter)
