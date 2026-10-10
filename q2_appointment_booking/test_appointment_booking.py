from datetime import datetime, timedelta

from appointment_booking import AppointmentBookingSystem


def test_book_available_slot():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=1)

    result = system.book_appointment("U001", "D001", slot)

    assert result is True
    assert system.is_slot_available("D001", slot) is False


def test_reject_already_booked_slot():
    system = AppointmentBookingSystem(
        users={"U001", "U002"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=1)

    assert system.book_appointment("U001", "D001", slot) is True
    assert system.book_appointment("U002", "D001", slot) is False


def test_cancel_appointment():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=1)

    assert system.book_appointment("U001", "D001", slot) is True
    assert system.cancel_appointment("U001", "D001", slot) is True
    assert system.is_slot_available("D001", slot) is True


def test_reject_past_appointment():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    past_slot = datetime.now() - timedelta(days=1)

    assert system.book_appointment("U001", "D001", past_slot) is False


def test_reject_invalid_user():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=1)

    assert system.book_appointment("INVALID", "D001", slot) is False


def test_reject_invalid_doctor():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=1)

    assert system.book_appointment("U001", "INVALID", slot) is False


def test_reject_incomplete_appointment_details():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=1)

    assert system.book_appointment("", "D001", slot) is False
    assert system.book_appointment("U001", "", slot) is False
    assert system.book_appointment("U001", "D001", None) is False
def test_two_users_cannot_book_same_doctor_slot():
    system = AppointmentBookingSystem(
        users={"U001", "U002"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=2)

    assert system.book_appointment("U001", "D001", slot) is True
    assert system.book_appointment("U002", "D001", slot) is False
    assert system.is_slot_available("D001", slot) is False


def test_cancel_nonexistent_appointment():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=2)

    assert system.cancel_appointment("U001", "D001", slot) is False
    assert system.is_slot_available("D001", slot) is True


def test_reject_appointment_in_the_past():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    past_slot = datetime.now() - timedelta(hours=1)

    assert system.book_appointment("U001", "D001", past_slot) is False


def test_reject_incomplete_appointment_details():
    system = AppointmentBookingSystem(
        users={"U001"},
        doctors={"D001"}
    )

    future_slot = datetime.now() + timedelta(days=2)

    assert system.book_appointment("", "D001", future_slot) is False
    assert system.book_appointment("U001", "", future_slot) is False
    assert system.book_appointment("U001", "D001", None) is False


def test_cancelled_slot_can_be_booked_again():
    system = AppointmentBookingSystem(
        users={"U001", "U002"},
        doctors={"D001"}
    )

    slot = datetime.now() + timedelta(days=2)

    assert system.book_appointment("U001", "D001", slot) is True
    assert system.cancel_appointment("U001", "D001", slot) is True
    assert system.book_appointment("U002", "D001", slot) is True