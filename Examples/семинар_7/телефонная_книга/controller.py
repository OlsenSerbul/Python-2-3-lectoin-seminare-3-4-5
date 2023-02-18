import model
import view

def start():
    user_choice = 0
    while user_choice != 8:
        user_choice= view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
                
            case 2:
                model.open_phone_book()

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case 7:
                pass


    