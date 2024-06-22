class Course:
    def __init__(self, id=None, name=None, no=None, descr=None, times=None, teacher=None):
        self.id = id
        self.name = name
        self.no = no
        self.descr = descr
        self.times = times
        self.teacher = teacher

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'no': self.no,
            'descr': self.descr,
            'times': self.times,
            'teacher': self.teacher
        }