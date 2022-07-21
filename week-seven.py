"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, discount=0):

        # dictionary works well for list
self.total_items = dict()  # {'item': 'price'}
self.total_price = 0
self.discount = discount
# different people may have different discounts/changable amount so needs flexibility.

# this is how you update discount


def update_discount(self, new_discount):
    self.discount = new_discount

# simple way to use dictionary of items one at a time


def add_item(self, item, price):
    self.total_items[item] = price

# price isn't needed for a removal. So don't include unnessary data


def remove_item(self, item):
    self.total_items.pop(item)

# remember to check the maths such as the zero Division Error so that the code works


def apply_discount(self):
    try:
        price = self.total_price - (self.total_price / self.discount)
    except ZeroDivisionError:
        print("Not dscount available")
    else:
        self.total_price = price

# sum fuction for adding values, fairly simple in this use, if errors most likely check syntax. The complex part here is remebering to include discounts on purchases


def get_total(self):
    if self.total_items:
        self.total_price = sum(self.total_items.values())

        self.apply_discount()
    else:
        print("No items in basket")

# most complicated part for me, many steps to be careful of


def show_items(self):
    msg = """
    Items Purchased
    --------------------
    {}

    Total: {}
    ---Thank You---
    """

    width = 20
    records = []

    for K, v in self.total_items.items():
        txt.len(k)
        digits = len(str(v))
        char = width - txt - digits
        r = "{}{}{}".format(k, '.' * char, v)
        records.append(r)

# / is supposed to be a backwards slash but can't find it on my keyboard
    all_records = /n'.join(records)
    final_msg = msg.format(all_records, self.total_price)
    print(final_msg)

# need to remember to reset


def reset_register(self):
    self.total_price = 0
    self.total_items.clear()
    self.discount


register = CashRegister(discount=5)
register.add_items('coffee' 2.80)


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def add_subjects(self, subject_list):
        for subject in subject_list:
            self.subject_list[subject] = None

    def remove_subject(self, subject):
        self.subject.pop(subject)


class CFGStudent(Student):

    def __init__(self, stream, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specialization = stream

    def add_subject(self, subject):
        self.subjects[subject] = None

    def remove_subject(self, subject):
        self.subject.pop(subject)

    def view_subjects(self):
        return list(self.subjects.keys())

    def get_overall_mark(self):
        current = dict(
            {(k, v) for k, v in self.subjects.items() if v is not None})

        return sum(current.values()) / len(current.values())


# class SubjectSearch:
#     def search_subjects(self, subject):
#         index().search_subjects(self, subject)


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
