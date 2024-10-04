class CCCD():
    def __init__(self, side: str, path: str):
        self.side = side
        self.path = path

    def set_side(self, side):
        self.side = side

    def set_path(self, path):
        self.path = path

    def get_side(self):
        return self.side

    def get_path(self):
        return self.path

    def __str__(self):
        return f"CCCD: {self.side}, {self.path}"
