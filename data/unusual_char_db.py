class UnusualCharDB:

    def __init__(self):
        with open("unusual_char", "r") as f:
            self.datas = f.read()

    def have_unusual(self, url):
        for c in self.datas:
            if c in url:
                return True

        return False
