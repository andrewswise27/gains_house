class Session:
    def __init__(self, _name, _tod, _doy, _length, _capacity, _description, _level, _id=None):
        self.name = _name
        self.tod = _tod
        self.doy = _doy
        self.length = _length
        self.capacity = _capacity
        self.description = _description
        self.level = _level
        self.id = _id