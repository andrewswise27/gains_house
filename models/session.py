class Session:
    def __init__(self, _name, _date, _time, _length, _capacity, _description, _level, _members_booked, _id=None):
        self.name = _name
        self.date = _date
        self.time = _time
        self.length = _length
        self.capacity = _capacity
        self.description = _description
        self.level = _level
        self.members_booked = _members_booked
        self.id = _id