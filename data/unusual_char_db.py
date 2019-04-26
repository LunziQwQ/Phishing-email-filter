class UnusualCharDB:

    def __init__(self):
        with open("data/unusual_char", "r", encoding="utf-8") as f:
            self.datas = f.read()

    def have_unusual(self, url):
        for c in self.datas:
            if c in url:
                return True

        return False
