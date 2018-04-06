# MENU

This is a simple module for displaying a menu, making a choice, and calling the linked function.


### USE:

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
