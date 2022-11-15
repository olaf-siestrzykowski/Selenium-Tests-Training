from booking.booking import Booking
import time

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.accept_cookies()
        #bot.change_currency(currency='EUR')
        bot.select_place('Madera')
        bot.select_dates(check_in='2022-12-09',
                         check_out='2022-12-11')
        #bot.room_size(adults=2, room=3)
        bot.search()
        bot.filtrations()
        bot.refresh()
        bot.results()
        time.sleep(3)

except Exception as e:
    if 'in PATH' in str(e):
        print("There was an error with running from CLI")
    else:
        raise e
