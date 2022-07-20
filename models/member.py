class Member:
    def __init__(self, _name, _age, _nationality, _mob_number, _email, _membership_type, _active_member=True, _id=None):
        self.name = _name
        self.age = _age
        self.nationality = _nationality
        self.mob_number = _mob_number
        self.email = _email
        self.membership_type =_membership_type
        self.active_member = _active_member
        self.id = _id

    def make_active(self):
        self.active_member = True

    def make_inactive(self):
        self.active_member = False
        