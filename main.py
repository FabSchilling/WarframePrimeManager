from table_wanted_functions import getListOfPartsFromWanted
from relic_functions import findRelicForPartList
from database_functions import resetDatabase

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

from functools import partial

class LoginScreen(BoxLayout):

    def addWidgetForPartsInWanted2(self, *args):
        box_layout = self.ids['text_Box']
        box_layout.clear_widgets()
        list_of_parts = getListOfPartsFromWanted()
        grid_Layout = GridLayout(rows=2)
        for parts in list_of_parts:
            btn = Button(text=parts, size_hint_y=None,
                         height=100, font_size=dp(50))
            btn.bind(on_press=partial(LoginScreen.addWidgetForRelicsOfPart, box_layout))

            grid_Layout.add_widget(btn)
            box_layout.add_widget(grid_Layout)

    def addWidgetForPartsInWanted(self, *args):
        box_layout = self.ids['text_Box']
        box_layout.clear_widgets()
        list_of_parts = getListOfPartsFromWanted()
        #list_of_relics = findRelicForPartList(list_of_parts)
        grid_layout_row_default_height = 100
        grid_layout_height = (len(list_of_parts) + 1) * grid_layout_row_default_height
        grid_layout = GridLayout(cols=2, row_force_default=True, row_default_height=grid_layout_row_default_height,
                                 size_hint_y=None, height=grid_layout_height)
        #relic_filter = ['Lith', 'Meso', 'Neo', 'Axi']
        #for filter in relic_filter:
        #    btn = Button(text=filter, size_hint_y=None,
        #                 height=100, font_size=dp(50))
        #    btn.bind(on_press=partial(LoginScreen.filterRelics, [box_layout, filter]))
        #    grid_layout.add_widget(btn)
        for part in list_of_parts:
            btn = Button(text=part, size_hint_y=None,
                         height=100)
            btn.bind(on_press=partial(LoginScreen.addWidgetForRelicsOfPart, box_layout))
            btn2 = Button(text='X',size_hint_y=None,
                         height=100)
            btn2.bind(on_press=partial(LoginScreen.addWidgetForRelicsOfPart, box_layout))

            grid_layout.add_widget(btn)
            grid_layout.add_widget(btn2)
        box_layout.add_widget(grid_layout)

    def addWidgetForRelicsOfPart(box_layout, button):
        box_layout.clear_widgets()
        list_of_relics = findRelicForPartList([button.text])

        grid_layout_row_default_height = 100
        grid_layout_height = (len(list_of_relics)+1) * grid_layout_row_default_height
        grid_layout = GridLayout(cols=4,row_force_default=True, row_default_height=grid_layout_row_default_height,size_hint_y= None, height = grid_layout_height)
        for relic in list_of_relics:
            for attribut in relic:
                #print(attribut)
                grid_layout.add_widget(Button(text=attribut))
        box_layout.add_widget(grid_layout)

        #print(button.text)
        #print(findRelicForPartList([button.text]))

    def addWidgetForRelic(self):
        box_layout = self.ids['text_Box']
        box_layout.clear_widgets()
        list_of_parts = getListOfPartsFromWanted()
        list_of_relics = findRelicForPartList(list_of_parts)
        grid_layout_row_default_height = 100
        grid_layout_height = (len(list_of_relics)+1) * grid_layout_row_default_height
        grid_layout = GridLayout(cols=4, row_force_default=True, row_default_height=grid_layout_row_default_height,
                                 size_hint_y=None, height=grid_layout_height)
        relic_filter = ['Lith','Meso','Neo','Axi']
        for filter in relic_filter:
            btn = Button(text=filter, size_hint_y=None,
                         height=100, font_size=dp(50))
            btn.bind(on_press=partial(LoginScreen.filterRelics, [box_layout, filter]))
            grid_layout.add_widget(btn)
        for relic in list_of_relics:
            for attribut in relic:
                #print(attribut)
                grid_layout.add_widget(Button(text=attribut))
        box_layout.add_widget(grid_layout)

    def filterRelics(self,button):
        self[0].clear_widgets()
        list_of_relics = findRelicForPartList(getListOfPartsFromWanted(), self[1])

        grid_layout_row_default_height = 100
        grid_layout_height = (len(list_of_relics)+1) * grid_layout_row_default_height
        grid_layout = GridLayout(cols=4, row_force_default=True, row_default_height=grid_layout_row_default_height,
                                 size_hint_y=None, height=grid_layout_height)
        relic_filter = ['Lith', 'Meso', 'Neo', 'Axi']
        for filter in relic_filter:
            btn = Button(text=filter, size_hint_y=None,
                         height=100, font_size=dp(50))
            btn.bind(on_press=partial(LoginScreen.filterRelics, [self[0],filter]))
            grid_layout.add_widget(btn)
        for relic in list_of_relics:
            for attribut in relic:
                #print(attribut)
                grid_layout.add_widget(Button(text=attribut))
        self[0].add_widget(grid_layout)


    pass







class WarframePrimeManagerApp(App):

    def build(self):
        return LoginScreen()

#resetDatabase()
#print(getListOfPartsFromWanted())
if __name__ == '__main__':
    WarframePrimeManagerApp().run()

'''
print(db.search(qr.table == "warframe"))
print(db.search(qr.name.matches('Ember Prime Chassis*')))
print(db.search((qr.table == 'relic') & (where("name").matches("Nekros*"))))
findRelicForPartList(["Vectis Prime Stock"])
findRelicForPartList(getListOfPartsFromItem("Ash Prime"))
addPartsFromItemToWanted("Ash Prime")
addPartsFromItemToWanted("Akbronco Prime")
removePartFromWanted("Ankyros Prime Gauntlet")
insertPartToWanted("Bo Prime Ornament")
print(db.search(qr.table == "wanted"))
searchPartOrItemByName("Ash")
getListOfPartsFromItem("Ash Prime")
print(searchPartOrItemByName("Ash Prime"))
getListOfPartsFromWanted()
printRelicList(findRelicForPartList(getListOfPartsFromWanted()))
insertPartToWanted("Ankyros Prime Gauntlet")
resetDatabase()
print(getListOfPartsFromWanted())
'''
