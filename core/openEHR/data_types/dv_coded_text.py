class DV_TEXT:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"DV_TEXT(value={self.value!r})"
    
class DV_CODED_TEXT(DV_TEXT):
    def __init__(self, value, defining_code):
        super().__init__(value)
        self.defining_code = defining_code

    def __repr__(self):
        return f"DV_CODED_TEXT(value={self.value!r}, defining_code={self.defining_code!r})"

