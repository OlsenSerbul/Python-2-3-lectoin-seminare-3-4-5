import model
import view

def click():
    view.show_menu()
    if view.get_value() == 1:
        view.print_console(model.show_all(model.tel_book))
    elif view.get_value() == 2:
        value_number = view.get_value_number()
        view.print_console(model.find_contact(value_number, model.tel_book))
    elif view.get_value() == 3:
        value_number = view.get_value_number()
        if value_number != int():
            model.add_name(value_number, model.tel_book)
            value_number = view.get_value_number()
            model.add_number(value_number, model.tel_book)
        else:
            model.add_number(value_number, model.tel_book)
            value_number = view.get_value_number()
            model.add_name(value_number, model.tel_book)
        view.print_console(model.tel_book)
    elif view.get_value() == 4:
        value_number = view.get_value_number()
        view.print_console(model.del_cont(value_number, model.tel_book))
    elif view.get_value() == 5:  
         value_number = view.get_value_number()
         new_value_number = view.get_new_value_number()
         view.print_console(model.change_cont(new_value_number, value_number, model.tel_book))
    else:
        model.exit()



    
        