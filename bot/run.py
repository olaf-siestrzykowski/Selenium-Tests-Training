from booking.booking import Booking
import time


with Booking() as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.change_currency(currency='EUR')
    bot.select_place('Amsterdam')
    bot.select_dates(check_in='2022-12-07',
                       check_out='2022-12-16')
    #bot.room_size(adults=2, room=3)
    bot.search()
    bot.filtrations()
    time.sleep(25)
