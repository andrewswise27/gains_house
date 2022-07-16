class Session:
    def __init__(self, _name, _tod, _length, _capacity, _description, _level, _members_booked, _id=None):
        self.name = _name
        self.tod = _tod
        self.length = _length
        self.capacity = _capacity
        self.description = _description
        self.level = _level
        self.members_booked = _members_booked
        self.id = _id