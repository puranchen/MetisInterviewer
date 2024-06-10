def class_property(cls):
    def getter(instance):
        return getattr(instance, f"_{cls.__name__.lower()}")
    
    def setter(instance, value):
        if value is not None:
            if isinstance(value, cls):
                setattr(instance, f"_{cls.__name__.lower()}", value)
            elif isinstance(value, dict):
                setattr(instance, f"_{cls.__name__.lower()}", cls(**value))
            else:
                raise ValueError(f"Invalid value for {cls.__name__.lower()}: {value!r}")
        else:
            setattr(instance, f"_{cls.__name__.lower()}", None)

    return property(getter, setter)