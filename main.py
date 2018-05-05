import database_functions
import table_wanted_functions
import relic_functions
import gui_functions
import os.path

from kivy.lang import Builder
from kivy.app import App



from kivy.uix.screenmanager import ScreenManager, Screen

from functools import partial

Builder.load_file('./warframeprimemanager.kv')

class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        StartScreen.addWidgetForPartsInWanted(self)


    def addWidgetForPartsInWanted(self, *args):
        box_layout = self.ids['text_Box']
        box_layout.clear_widgets()
        list_of_parts = table_wanted_functions.getListOfPartsFromWanted()

        grid_layout = gui_functions.getGridLayout(list_of_parts, 2)

        for part in list_of_parts:
            btn = gui_functions.getDefaultButton(part)
            btn2 = gui_functions.getDefaultButton('X', 20, 0.1)

            btn.bind(on_press=partial(StartScreen.addWidgetForRelicsOfPart, box_layout))
            btn2.bind(on_press=partial(StartScreen.removePartFromWanted, [box_layout, grid_layout, part, btn, btn2]))

            grid_layout.add_widget(btn)
            grid_layout.add_widget(btn2)

        box_layout.add_widget(grid_layout)

        return grid_layout

    def addWidgetForRelicsOfPart(self, button):
        self.clear_widgets()
        list_of_relics = relic_functions.getRelicForPartList([button.text])

        grid_layout = gui_functions.getRelicGridFromWanted(list_of_relics)

        self.add_widget(grid_layout)

    def addWidgetForRelic(self):
        box_layout = self.ids['text_Box']
        box_layout.clear_widgets()
        list_of_relics = relic_functions.getFilteredRelicList()

        grid_layout = gui_functions.getGridLayout([1], cols = 4, grid_layout_row_default_height=40)
        relic_filter = ['Lith','Meso','Neo','Axi']
        for filter in relic_filter:
            btn = gui_functions.getDefaultButton(filter, 40, height=40)
            btn.bind(on_press=partial(StartScreen.filterRelics, [box_layout, filter]))
            grid_layout.add_widget(btn)
        box_layout.add_widget(grid_layout)
        grid_layout = gui_functions.getRelicGridFromWanted(list_of_relics)

        box_layout.add_widget(grid_layout)

    def filterRelics(self, button):
        self[0].clear_widgets()
        list_of_relics = relic_functions.getFilteredRelicList(self[1])
        grid_layout = gui_functions.getGridLayout([1], 4, grid_layout_row_default_height=40)
        relic_filter = ['Lith', 'Meso', 'Neo', 'Axi']
        for filter in relic_filter:
            btn = gui_functions.getDefaultButton(filter, 40, height=40)
            btn.bind(on_press=partial(StartScreen.filterRelics, [self[0], filter]))
            grid_layout.add_widget(btn)
        self[0].add_widget(grid_layout)

        grid_layout = gui_functions.getRelicGridFromWanted(list_of_relics)
        self[0].add_widget(grid_layout)

    def removePartFromWanted(self, button):
        print(self[2])
        table_wanted_functions.removePartFromWanted(self[2])
        self[1].remove_widget(self[3])
        self[1].remove_widget(self[4])



class ScreenTwo(Screen):
    def __init__(self,name,**kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        relic_list = database_functions.getAllRelics()
        tier_list = ['Lith', 'Meso', 'Neo', 'Axi']

        for i in range(4):
            grid_layout1 = self.ids['grid' + str(i)]
            for relic in relic_list[i]:
                if relic_functions.isRelicInRelicDB(tier_list[i], relic):
                    if database_functions.isRelicVaulted(tier_list[i], relic):
                        relic = str(relic) + " ([b]V[b])"
                    btn = gui_functions.getRelicToggleButtonForTier(text=relic, state="down", tier=tier_list[i])
                else:
                    if database_functions.isRelicVaulted(tier_list[i], relic):
                        relic = str(relic) + " ([b]V[b])"
                    btn = gui_functions.getRelicToggleButtonForTier(text=relic, state="normal", tier=tier_list[i])
                btn.bind(on_press=partial(ScreenTwo.relicButton, btn, tier_list[i], relic))
                grid_layout1.add_widget(btn)
        self.name = name

    def relicButton(btn, tier, relic_type, self):
        state = btn.state
        if state == "down":
            relic_functions.addRelicToRelicDB(tier, relic_type)
        elif state == "normal":
            relic_functions.removeRelicFromRelicDB(tier, relic_type)
        else:
            print("Error")

class SettingsScreen(Screen):
    pass







if(os.path.isfile("./allinone.json") == False):
    database_functions.updateDatabase()


screen_manager = ScreenManager()
screen_manager.add_widget(StartScreen(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(SettingsScreen(name="settingScreen"))







class WarframePrimeManagerApp(App):

    def build(self):
        return screen_manager

#database_functions.resetDatabase()
if __name__ == '__main__':
    WarframePrimeManagerApp().run()

