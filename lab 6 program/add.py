import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('clinical_appointments.db')
cursor = conn.cursor()

# Create the "appointments" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        appointment_date TEXT,
        doctor_name TEXT
    )
''')
conn.commit()

# Function to add a new appointment
def add_appointment(patient_name, appointment_date, doctor_name):
    cursor.execute('''
        INSERT INTO appointments (patient_name, appointment_date, doctor_name)
        VALUES (?, ?, ?)
    ''', (patient_name, appointment_date, doctor_name))
    conn.commit()
    print("Appointment added successfully!")

# Function to view all appointments
def view_appointments():
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()
    if not appointments:
        print("No appointments found.")
    else:
        print("Appointments:")
        for appointment in appointments:
            print(appointment)

# Function to cancel an appointment by ID
def cancel_appointment(appointment_id):
    cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
    conn.commit()
    print("Appointment canceled successfully!")

# Main program loop
while True:
    print("\nClinical Appointment Management System")
    print("1. Add Appointment")
    print("2. View Appointments")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        patient_name = input("Patient Name: ")
        appointment_date = input("Appointment Date (YYYY-MM-DD): ")
        doctor_name = input("Doctor Name: ")
        add_appointment(patient_name, appointment_date, doctor_name)

    elif choice == '2':
        view_appointments()

    elif choice == '3':
        appointment_id = int(input("Enter Appointment ID to cancel: "))
        cancel_appointment(appointment_id)

    elif choice == '4':
        print("Exiting the program.")
        conn.close()
        break

    else:
        print("Invalid choice. Please select a valid option.")
