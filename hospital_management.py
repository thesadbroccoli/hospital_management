import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ritheeshx12",
        database="hospital_management"
    )

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender VARCHAR(10),
            address VARCHAR(255)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            specialization VARCHAR(255),
            department VARCHAR(255),
            schedule VARCHAR(255)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing (
            bill_id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            total_amount DECIMAL(10, 2),
            payment_status VARCHAR(50),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

def register_patient(name, age, gender, address):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO patients (name, age, gender, address) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, gender, address))
    connection.commit()
    cursor.close()
    connection.close()
    print("Patient registered .")

def update_patient(patient_id, name, age, gender, address):
    connection = get_connection()
    cursor = connection.cursor()
    query = "UPDATE patients SET name=%s, age=%s, gender=%s, address=%s WHERE patient_id=%s"
    cursor.execute(query, (name, age, gender, address, patient_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Patient information updated.")

def view_patient_records():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM patients"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()

def search_patient(name):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM patients WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()

def add_doctor(name, specialization, department, schedule):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO doctors (name, specialization, department, schedule) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, specialization, department, schedule))
    connection.commit()
    cursor.close()
    connection.close()
    print("Doctor added successfully.")

def view_doctor_schedules():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM doctors"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()

def assign_doctor_to_department(doctor_id, department):
    connection = get_connection()
    cursor = connection.cursor()
    query = "UPDATE doctors SET department=%s WHERE doctor_id=%s"
    cursor.execute(query, (department, doctor_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Doctor assigned to department.")

def generate_bill(patient_id, total_amount):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO billing (patient_id, total_amount, payment_status) VALUES (%s, %s, %s)"
    cursor.execute(query, (patient_id, total_amount, "Pending"))
    connection.commit()
    cursor.close()
    connection.close()
    print("Bill generated.")

def track_payments():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM billing"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()

def main():
    create_tables()
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Register Patient")
        print("2. Update Patient Information")
        print("3. View Patient Records")
        print("4. Search Patient")
        print("5. Add New Doctor")
        print("6. View Doctor Schedules")
        print("7. Assign Doctor to Department")
        print("8. Generate Bill")
        print("9. Track Payments")
        print("10. Exit")

        choice = input("Choose an option (1-10): ")

        if choice == "1":
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            address = input("Enter patient address: ")
            register_patient(name, age, gender, address)
        
        elif choice == "2":
            patient_id = int(input("Enter patient ID to update: "))
            name = input("Enter updated name: ")
            age = int(input("Enter updated age: "))
            gender = input("Enter updated gender: ")
            address = input("Enter updated address: ")
            update_patient(patient_id, name, age, gender, address)
        
        elif choice == "3":
            view_patient_records()
        
        elif choice == "4":
            name = input("Enter patient name to search: ")
            search_patient(name)
        
        elif choice == "5":
            name = input("Enter doctor name: ")
            specialization = input("Enter specialization: ")
            department = input("Enter department: ")
            schedule = input("Enter schedule: ")
            add_doctor(name, specialization, department, schedule)
        
        elif choice == "6":
            view_doctor_schedules()
        
        elif choice == "7":
            doctor_id = int(input("Enter doctor ID to assign: "))
            department = input("Enter department to assign: ")
            assign_doctor_to_department(doctor_id, department)
        
        elif choice == "8":
            patient_id = int(input("Enter patient ID for bill: "))
            total_amount = float(input("Enter total amount: "))
            generate_bill(patient_id, total_amount)
        
        elif choice == "9":
            track_payments()

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

main()
