#Created by: Justin Bronson
#Created on: Oct 2017
#Created for: ICS3U
#This program calculates the cost
#  of your custom pizza

import ui

def calculate_button_touch_up_inside(sender):
    pizzaSize = view['size_control'].selected_index
    pizzaToppings = view['toppings_control'].selected_index

    if pizzaSize == 0:
        sizeCost = 6

    else:
        sizeCost = 10

    if pizzaToppings == 0:
        toppingsCost = 1

    elif pizzaToppings == 1:
        toppingsCost = 1.75

    elif pizzaToppings == 2:
        toppingsCost = 2.5

    elif pizzaToppings == 3:
        toppingsCost = 3.25

    subtotal = toppingsCost + sizeCost
    hst = subtotal * 0.13
    total = subtotal + hst

    view['subtotal_answer'].text = '${:,.2f}'.format(subtotal)
    view['hst_answer'].text = '${:,.2f}'.format(hst)
    view['total_answer'].text = '${:,.2f}'.format(total)

view = ui.load_view()
view.present('sheet')
