def seats_available(total_seats, booked_seats, book_seat, cancel_seat):
    if cancel_seat in booked_seats:
        booked_seats.remove(cancel_seat)
    if book_seat not in booked_seats:
        booked_seats.append(book_seat)
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
available = seats_available(total_seats, booked_seats, book_seat, cancel_seat)
print("Available seats:", available)
