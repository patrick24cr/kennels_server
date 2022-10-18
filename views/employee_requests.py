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
