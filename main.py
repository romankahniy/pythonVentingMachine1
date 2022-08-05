from queries import greeting
from queries import category_search
from queries import add_category
from queries import item_add
from queries import purchase
from queries import list
from queries import report
from queries import report1

options = [
    {
        'code': 0,
        'name': 'Buy',
    },
    {
        'code': 1,
        'name': 'Add Category',
    },
    {
        'code': 2,
        'name': 'Add Items',
    },
{
        'code': 3,
        'name': 'Items List',
    },
{
        'code': 4,
        'name': 'Report by period',
    },
{
        'code': 5,
        'name': 'Report by day',
    },
]

greeting()

for i in options:
    print(f"Option Name: {i['name']} - Code: {i['code']}")

print('-' * 34)

query = int(input("Enter the code number of the option you want to get: "))
sel = query

for i in options:
    if query == i['code']:
        option = i
        print(f"Great, you select: {i['name']}")
        print('-' * 34)
    pass

if sel == 0:
    print('There is the items, you can buy: ')
    category_search()
    purchase()
    print('-' * 34)
elif sel == 1:
    add_category()
    print('-' * 34)
elif sel == 2:
    print('Here are the products you can add: ')
    item_add()
    print('-' * 34)
elif sel == 3:
    list()
elif sel == 4:
    report()
elif sel == 5:
    report1()
else:
    print('Invalid Code!')
