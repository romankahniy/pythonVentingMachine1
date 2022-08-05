import sqlite3
from art import *
from datetime import date

connect = sqlite3.connect('VentingMachine.db')
cursor = connect.cursor()

def greeting():
    print('Welcome to:')
    tprint('Venting Machine')
    next = input('Press Enter to continue: ')
    print('-' * 34)
    print('Select the option:')

def category_search():
    cursor.execute(" SELECT id, item_name, item_price"
                   " FROM Items"
                   " WHERE item_count > 0")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    pass

def add_category():
    try:
        item_name = str(input('Enter the product name: '))
        item_price = float(input('Enter the product price: '))
        item_count = int(input('Enter the quantity of the product: '))
        category_list = [item_name, item_price, item_count]
        cursor.execute("INSERT INTO Items(item_name, item_price, item_count)"
                       " VALUES(?, ?, ?);", category_list)
        connect.commit()
        print('Category was added successfully',"\U0001F917")
    except:
        print('Something went wrong!',"\U0001F62A")

def item_add():
    try:
        cursor.execute(" SELECT id, item_name, item_price, item_count"
                       " FROM Items")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        pass
        item_sel = input('Please type the code of item (1 column): ')
        cursor.execute("SELECT id, item_name, item_count"
                       " FROM Items"
                       " WHERE id = ? ", (item_sel))
        sel_result = cursor.fetchall()
        print('You select:')
        print(sel_result)
        earn_item = int(input('Enter the quantity of the product you want to add: '))
        cursor.execute('UPDATE Items'
                       ' SET item_count = ? '
                       'WHERE id = ?', (earn_item, item_sel))
        connect.commit()
        print(f'You changed the quantity of the product in the machine to: {earn_item}',"\U0001F917")
    except:
        print('Something went wrong!')
        print("\U0001F62A")

def purchase():
    try:
        item_sel = input('Please type the code of item (1 column): ')
        cursor.execute(" SELECT item_name "
                       " FROM Items "
                       " WHERE id = " + item_sel)
        sel_result = cursor.fetchall()
        cursor.execute(" SELECT item_price "
                       " FROM Items "
                       " WHERE id = " + item_sel)
        price_result = cursor.fetchall()
        print(f'You select: {sel_result}. His price is: {price_result}')
        purchase = input('Pay the price of the selected product: ')
        cursor.execute(f" SELECT item_price "
                       f" FROM Items "
                       f" WHERE item_price =" + purchase)
        pur_result1 = cursor.fetchall()
        cursor.execute(f" UPDATE Items "
                       f" SET item_count = item_count -1 "
                       f" WHERE id =" +item_sel)
        connect.commit()
        today = date.today()
        cursor.execute(f' INSERT INTO Purchases(item_id, purchases_at) '
                       f' VALUES (?, ?)', (item_sel, today))
        connect.commit()
        print(f"You pay {pur_result1}. Have a good day!")
        print(today)
    except:
        print('Something went wrong!')
        print("\U0001F62A")

def list():
    cursor.execute(' SELECT * '
                   ' FROM Items '
                   ' ORDER BY item_count DESC')
    result = cursor.fetchall()
    for row in result:
        print(row)

def report():
    date = input('Enter the date from which you want to start the search in the format "YYYY-MM-DD": ')
    date1 = input('Enter the date by which you want to end the search in the format "YYYY-MM-DD": ')
    cursor.execute(f' SELECT item_name'
                   f' FROM Items s1  '
                   f' INNER JOIN Purchases s2 ON s1.[id]=s2.[item_id] '
                   f' WHERE purchases_at BETWEEN "{date}" AND "{date1}"')
    name = cursor.fetchall()
    print("On this day was sold: ")
    for row in name:
        print(row)
    pass
    cursor.execute(f' SELECT SUM(s1.[item_price]) AS Total_sales'
                   f' FROM Items s1  '
                   f' INNER JOIN Purchases s2 ON s1.[id]=s2.[item_id] '
                   f' WHERE purchases_at BETWEEN "{date}" AND "{date1}"')
    res = cursor.fetchall()
    print("In the amount: ")
    for row in res:
        print(row)
    pass

def report1():
    date = input('Write the date in the format "YYYY-MM-DD": ')
    cursor.execute(f' SELECT item_name'
                   f' FROM Items s1  '
                   f' INNER JOIN Purchases s2 ON s1.[id]=s2.[item_id] '
                   f' WHERE purchases_at LIKE "{date}"')
    name = cursor.fetchall()
    print("On this day was sold: ")
    for row in name:
        print(row)
    pass
    cursor.execute(f' SELECT SUM(s1.[item_price]) AS Total_sales'
                   f' FROM Items s1  '
                   f' INNER JOIN Purchases s2 ON s1.[id]=s2.[item_id] '
                   f' WHERE purchases_at LIKE "{date}"')
    res = cursor.fetchall()
    print("In the amount: ")
    for row in res:
        print(row)
    pass
