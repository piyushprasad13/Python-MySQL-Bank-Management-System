import mysql.connector as sql

# =========================================================
# MYSQL CONNECTION
# =========================================================

con = sql.connect(
    host='localhost',
    user='root',
    password='YOUR_MYSQL_PASSWORD',
    database='bank1'
)

if con.is_connected():
    print("MYSQL CONNECTED SUCCESSFULLY")


# =========================================================
# OPEN NEW ACCOUNT
# =========================================================

def openacc():

    print("\n========== OPEN NEW ACCOUNT ==========")

    name = input("Enter Your Name: ")
    acc = input("Enter Your Account No: ")
    pno = input("Enter Your Phone No: ")
    add = input("Enter Your Address: ")
    ob = int(input("Enter Opening Balance: "))

    cur = con.cursor()

    st1 = """
    INSERT INTO account
    (name, accno, address, phno, openingbalance)
    VALUES (%s, %s, %s, %s, %s)
    """

    st2 = """
    INSERT INTO amount
    (name, accno, balance)
    VALUES (%s, %s, %s)
    """

    data1 = (name, acc, add, pno, ob)
    data2 = (name, acc, ob)

    try:
        cur.execute(st1, data1)
        cur.execute(st2, data2)
        con.commit()
        print("\nACCOUNT OPENED SUCCESSFULLY")

    except sql.Error as e:
        con.rollback()
        print("\nERROR:", e)

    cur.close()


# =========================================================
# DEPOSIT AMOUNT
# =========================================================

def depoamo():

    print("\n========== DEPOSIT AMOUNT ==========")

    acc = input("Enter Account No: ")
    amo = int(input("Enter Amount: "))

    if amo <= 0:
        print("Amount must be greater than 0")
        return

    cur = con.cursor()

    st = """
    SELECT balance
    FROM amount
    WHERE accno=%s
    """

    cur.execute(st, (acc,))
    result = cur.fetchone()

    if result is None:
        print("ACCOUNT NUMBER DOES NOT EXIST")
        cur.close()
        return

    oldbalance = result[0]
    total = oldbalance + amo

    st2 = """
    UPDATE amount
    SET balance=%s
    WHERE accno=%s
    """

    cur.execute(st2, (total, acc))
    con.commit()

    print("\nCREDITED RS:", amo)
    print("NEW BALANCE:", total)

    cur.close()


# =========================================================
# WITHDRAW AMOUNT
# =========================================================

def withdraw():

    print("\n========== WITHDRAW AMOUNT ==========")

    acc = input("Enter Account No: ")
    amo = int(input("Enter Amount: "))

    if amo <= 0:
        print("Amount must be greater than 0")
        return

    cur = con.cursor()

    st = """
    SELECT balance
    FROM amount
    WHERE accno=%s
    """

    cur.execute(st, (acc,))
    result = cur.fetchone()

    if result is None:
        print("ACCOUNT NUMBER DOES NOT EXIST")
        cur.close()
        return

    balance = result[0]

    if amo > balance:
        print("\nINSUFFICIENT BALANCE")
        print("AVAILABLE BALANCE:", balance)
        cur.close()
        return

    total = balance - amo

    st2 = """
    UPDATE amount
    SET balance=%s
    WHERE accno=%s
    """

    cur.execute(st2, (total, acc))
    con.commit()

    print("\nDEBITED RS:", amo)
    print("REMAINING BALANCE:", total)

    cur.close()


# =========================================================
# BALANCE ENQUIRY
# =========================================================

def balance():

    print("\n========== BALANCE ENQUIRY ==========")

    acc = input("Enter Your Account No: ")

    cur = con.cursor()

    st = """
    SELECT balance
    FROM amount
    WHERE accno=%s
    """

    cur.execute(st, (acc,))
    result = cur.fetchone()

    if result is None:
        print("ACCOUNT NUMBER DOES NOT EXIST")
    else:
        print("\nYOUR BALANCE IS:", result[0])

    cur.close()


# =========================================================
# DISPLAY CUSTOMER DETAILS
# =========================================================

def display():

    print("\n========== CUSTOMER DETAILS ==========")

    acc = input("Enter Your Account No: ")

    cur = con.cursor()

    st = """
    SELECT *
    FROM account
    WHERE accno=%s
    """

    cur.execute(st, (acc,))
    result = cur.fetchone()

    if result is None:
        print("ACCOUNT NUMBER DOES NOT EXIST")
    else:
        print("\n--------------------------------")
        print("       CUSTOMER DETAILS")
        print("--------------------------------")
        print("Name            :", result[0])
        print("Account No      :", result[1])
        print("Address         :", result[2])
        print("Phone No        :", result[3])
        print("Opening Balance :", result[4])
        print("--------------------------------")

    cur.close()


# =========================================================
# DELETE ACCOUNT
# =========================================================

def delete():

    print("\n========== DELETE ACCOUNT ==========")

    acc = input("Enter Your Account No: ")

    cur = con.cursor()

    check = """
    SELECT accno
    FROM account
    WHERE accno=%s
    """

    cur.execute(check, (acc,))
    result = cur.fetchone()

    if result is None:
        print("ACCOUNT NUMBER DOES NOT EXIST")
        cur.close()
        return

    st1 = """
    DELETE FROM amount
    WHERE accno=%s
    """

    cur.execute(st1, (acc,))

    st2 = """
    DELETE FROM account
    WHERE accno=%s
    """

    cur.execute(st2, (acc,))
    con.commit()

    print("\nACCOUNT SUCCESSFULLY DELETED")

    cur.close()


# =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        print("""
========================================================
                 WELCOME TO ECE BANK
========================================================

             1. OPEN NEW ACCOUNT
             2. DEPOSIT AMOUNT
             3. WITHDRAW AMOUNT
             4. BALANCE ENQUIRY
             5. DISPLAY CUSTOMER DETAILS
             6. DELETE AN ACCOUNT
             7. EXIT

========================================================
""")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            openacc()
        elif choice == '2':
            depoamo()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            balance()
        elif choice == '5':
            display()
        elif choice == '6':
            delete()
        elif choice == '7':
            print("\n          THANK YOU")
            print("     VISIT ECE BANK AGAIN")
            break
        else:
            print("\n!!!!! WRONG CHOICE !!!!!")


main()

con.close()
