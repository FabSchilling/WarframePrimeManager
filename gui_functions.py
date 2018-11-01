from kivy.uix.button import Button
from kivy.metrics import dp, sp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton



def getDefaultButton(text, fontsize = 20, width = 1, height = 35):
    btn = Button(text=text, size_hint_y=None, height=dp(height), font_size = dp(fontsize), size_hint_x=width)
    return btn

def getGridLayout(list, cols = 1, grid_layout_row_default_height = 35):
    grid_layout_height = len(list) * (grid_layout_row_default_height + 2) + 4
    grid_layout = GridLayout(cols=cols, row_force_default=True, row_default_height=dp(grid_layout_row_default_height),
                             size_hint_y=None, height=dp(grid_layout_height), spacing = dp(2), padding= dp(2))
    return grid_layout

def getRelicToggleButtonForTier(text, state, tier):
    tier = tier.lower()
    btn = ToggleButton(text="[color=000000]" + text + "[/color]", font_size=dp(15), markup=True ,state=state, border=[0, 0, 0, 0], background_normal='./gfx/relic_' + tier + '_down.png', background_down='./gfx/relic_' + tier + '.png')

    return btn


def getRelicGridFromWanted(list_of_relics):
    grid_layout = getGridLayout(list_of_relics, 4)

    for relic in list_of_relics:
        counter = 0
        for attribute in relic:
            if counter == 0:
                btn = getDefaultButton(attribute, width=0.15)
            elif counter == 2:
                btn = getDefaultButton(attribute[0], width=0.1)
            elif counter == 3:
                btn = getDefaultButton(attribute[:25], width=0.7)
            else:
                btn = getDefaultButton(attribute, width=0.1)
            grid_layout.add_widget(btn)
            counter += 1
    return grid_layout

def removePartFromWanted(self):
    self[1].remove_widget(self[3])
    self[1].remove_widget(self[4])
    self[1].height=self[1].height - dp(37)
