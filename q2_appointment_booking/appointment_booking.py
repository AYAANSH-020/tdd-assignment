from datetime import datetime


class AppointmentBookingSystem:
    def __init__(self, users, doctors):
        self.users = set(users)
        self.doctors = set(doctors)
        self.appointments = set()

    def book_appointment(self, user_id, doctor_id, slot):
        # Validate appointment details
        if not user_id or not doctor_id or slot is None:
            return False

        if user_id not in self.users:
            return False

        if doctor_id not in self.doctors:
            return False

        # Reject appointments in the past
        if not isinstance(slot, datetime):
            return False

        if slot <= datetime.now():
            return False

        # Prevent double booking
        for appointment in self.appointments:
            booked_doctor, booked_slot = appointment[1], appointment[2]

            if booked_doctor == doctor_id and booked_slot == slot:
                return False

        # Save the appointment
        self.appointments.add((user_id, doctor_id, slot))
        return True

    def cancel_appointment(self, user_id, doctor_id, slot):
        appointment = (user_id, doctor_id, slot)

        if appointment not in self.appointments:
            return False

        self.appointments.remove(appointment)
        return True

    def is_slot_available(self, doctor_id, slot):
        if doctor_id not in self.doctors:
            return False

        if not isinstance(slot, datetime):
            return False

        for appointment in self.appointments:
            booked_doctor, booked_slot = appointment[1], appointment[2]

            if booked_doctor == doctor_id and booked_slot == slot:
                return False

        return True