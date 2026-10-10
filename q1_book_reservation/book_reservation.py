class BookReservationSystem:
    def __init__(self, students, books):
        self.students = set(students)
        self.books = dict(books)
        self.reservations = set()

    def reserve_book(self, student_id, book_id):
        if student_id not in self.students:
            return False

        if book_id not in self.books:
            return False

        if self.books[book_id] <= 0:
            return False

        reservation = (student_id, book_id)

        if reservation in self.reservations:
            return False

        self.reservations.add(reservation)
        self.books[book_id] -= 1

        return True

    def check_availability(self, book_id):
        if book_id not in self.books:
            return None

        return self.books[book_id]

    def cancel_reservation(self, student_id, book_id):
        reservation = (student_id, book_id)

        if reservation not in self.reservations:
            return False

        self.reservations.remove(reservation)
        self.books[book_id] += 1

        return True