from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    #bot.change_currency(currency='EUR')
    bot.select_place('Amsterdam')
    bot.select_dates(check_in='2022-12-22',
                     check_out='2022-12-26')
