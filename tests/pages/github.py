

class Issues:
    def __init__(self, browser):
        self.links = browser.all('[id^=issue_]:not([id$=_link])')