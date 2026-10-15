from maps.AbstractGakushoku import AbstractGakushoku

class Gakushoku_hana(AbstractGakushoku):

    def get_menu(self):
        return "100円朝食"

    def get_summary(self):
        return "安くておいしい！"

    def get_author(self):
        return "黒田花"
