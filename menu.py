'''
#MENU
#Parker Dinkins
#Python 3.6

This is a simple module for displaying a menu, making a choice, and calling the linked function.


USE:

    1. import menu
    
    2. define menu choice functions
    
    3. define menu dictionary
        {'menu choice label': corresponding function}
    
    4. menu.initialize_menu(**menu_dictionary, **menutitle)


EXAMPLE WIHT SUB-MENU:
    
    import menu 

    # Define menu choice function 
    def stuff():
        print('stuff function 1')

    def submenu():
        menu.initialize_menu(funcdict2, 'Sub Menu')

    def submenu_stuff():
        print('hello from the sub menu')

    #Define menu dictionarys
    funcdict = {
        'stuff': stuff,
        'sub menu': submenu
    }

    funcdict2 = {
        'sub menu stuff': submenu_stuff
    }

    #Initialize the menu
    menu.initialize_menu(funcdict, "Main Menu")

'''

def display_menu_choices(menu_dictionary, menutitle):
    menulist = list(menu_dictionary.keys())
    j = 1
    print('\n' + menutitle, '\n')
    for i in range(0,len(menulist)):
        print(j,'-', menulist[i])
        j += 1 
    choose_from_menu(menulist, menu_dictionary)


def choose_from_menu(menulist, menu_dictionary):
    try:
        menuchoice = int(input('\nMenu Choice:  '))
        menuchoice -= 1
        print()
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('***invalid choice***')


def initialize_menu(menu_dictionary, menutitle):
    display_menu_choices(menu_dictionary, menutitle)
