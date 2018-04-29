from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton



def getDefaultButton(text, fontsize = 20, width = 1, height = 35):
    btn = Button(text=text, size_hint_y=None, height=dp(height), font_size = dp(fontsize), size_hint_x=width)
    return btn

def getGridLayout(list_of_parts, cols = 1, grid_layout_row_default_height = 35):
    grid_layout_height = len(list_of_parts) * (grid_layout_row_default_height + dp(2)) + dp (4)
    grid_layout = GridLayout(cols=cols, row_force_default=True, row_default_height=dp(grid_layout_row_default_height),
                             size_hint_y=None, height=dp(grid_layout_height), spacing = dp(2), padding= dp(2))
    return grid_layout

def getRelicToggleButtonForTier(text, state, tier):
    tier = tier.lower()
    btn = ToggleButton(text="[color=000000]" + text + "[/color]", font_size=dp(30), markup=True ,state=state, border=[0, 0, 0, 0], background_normal='./gfx/relic_' + tier + '_down.png', background_down='./gfx/relic_' + tier + '.png')

    return btn
