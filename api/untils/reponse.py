class ResponseDict:
    def __init__(self):
        self.code = 1000
        self.data = None
        self.error = None

    @property
    def dict(self):
        return self.__dict__

    def get_error(self, e):
        self.error = e
