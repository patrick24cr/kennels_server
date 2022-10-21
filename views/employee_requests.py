import random
from views.location_requests import LOCATIONS

EMPLOYEES = [
    {
        "id": 1,
        "name": "Patrick",
        "position": "CIO"
    },
    {
        "id": 2,
        "name": "Kelly",
        "position": "CFO"
    },
    {
        "id": 3,
        "name": "Amanda",
        "position": "COO"
    }
]

def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """Why not try a docstring again
    """
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1
    
    max_locationId = LOCATIONS[-1]["id"]
    new_locationId = random.randint(1, max_locationId)

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id
    
    employee["locationId"] = new_locationId

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)