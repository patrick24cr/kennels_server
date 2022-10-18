CUSTOMERS = [
    {
        "id": 1,
        "name": "Matthew"
    },
    {
        "id": 2,
        "name": "Mark"
    },
    {
        "id": 3,
        "name": "Luke"
    },
    {
        "id": 4,
        "name": "John"
    }
]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """Why not try a docstring
    """
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
