from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout



def createDefaultButton(text, fontsize = 20, width = 1, height = 35):
    btn = Button(text=text, size_hint_y=None, height=dp(height), font_size = dp(fontsize), size_hint_x=width)
    return btn

def createGridLayout(list_of_parts,cols = 1, grid_layout_row_default_height = 35):
    grid_layout_height = len(list_of_parts) * (grid_layout_row_default_height + dp(2)) + dp (4)
    grid_layout = GridLayout(cols=cols, row_force_default=True, row_default_height=dp(grid_layout_row_default_height),
                             size_hint_y=None, height=dp(grid_layout_height), spacing = dp(2), padding= dp(2))
    return grid_layout