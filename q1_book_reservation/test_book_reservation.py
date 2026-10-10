from book_reservation import BookReservationSystem


def test_reserve_available_book():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 3}
    )

    result = system.reserve_book("S001", "B001")

    assert result is True
    assert system.check_availability("B001") == 2


def test_check_book_availability():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 3}
    )

    assert system.check_availability("B001") == 3


def test_prevent_duplicate_reservation():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 3}
    )

    assert system.reserve_book("S001", "B001") is True
    assert system.reserve_book("S001", "B001") is False
    assert system.check_availability("B001") == 2


def test_cancel_reservation():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 3}
    )

    system.reserve_book("S001", "B001")

    result = system.cancel_reservation("S001", "B001")

    assert result is True
    assert system.check_availability("B001") == 3

def test_reserve_last_available_copy():
    system = BookReservationSystem(
        students={"S001", "S002"},
        books={"B001": 1}
    )

    assert system.reserve_book("S001", "B001") is True
    assert system.check_availability("B001") == 0
    assert system.reserve_book("S002", "B001") is False


def test_reject_reservation_when_book_unavailable():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 0}
    )

    assert system.reserve_book("S001", "B001") is False
    assert system.check_availability("B001") == 0


def test_reject_invalid_student_id():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 2}
    )

    assert system.reserve_book("INVALID", "B001") is False
    assert system.check_availability("B001") == 2


def test_reject_invalid_book_id():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 2}
    )

    assert system.reserve_book("S001", "INVALID") is False


def test_cannot_cancel_reservation_twice():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 2}
    )

    assert system.reserve_book("S001", "B001") is True
    assert system.cancel_reservation("S001", "B001") is True
    assert system.cancel_reservation("S001", "B001") is False
    assert system.check_availability("B001") == 2


def test_cannot_cancel_nonexistent_reservation():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 2}
    )

    assert system.cancel_reservation("S001", "B001") is False
    assert system.check_availability("B001") == 2


def test_check_invalid_book_id():
    system = BookReservationSystem(
        students={"S001"},
        books={"B001": 2}
    )

    assert system.check_availability("INVALID") is None