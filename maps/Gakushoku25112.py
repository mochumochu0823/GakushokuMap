from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "アロハのフレンチトースト"
    def get_summary(self):
        return "おいしい"
    def get_author(self):
        return "坂野光"