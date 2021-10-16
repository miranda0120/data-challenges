# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """
        SELECT
            Orders.OrderID as order_id,
            Customers.ContactName,
            Employees.FirstName
        FROM Orders
        JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
        JOIN Customers ON Customers.CustomerID  = Orders.CustomerID
        ORDER BY order_id ASC
    """
    db.execute(query)
    results = db.fetchall()
    return results


def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """
        SELECT
            Customers.ContactName,
            SUM(ROUND(OrderDetails.UnitPrice * OrderDetails.Quantity, 2))
            AS cumulative_amount
        FROM Orders
        JOIN Customers ON Customers.CustomerID  = Orders.CustomerID
        JOIN OrderDetails ON OrderDetails.OrderID  = Orders.OrderID
        GROUP BY Customers.ContactName
        ORDER BY cumulative_amount ASC
    """
    db.execute(query)
    results = db.fetchall()
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query = """
        SELECT
            Employees.FirstName, Employees.LastName,
            SUM(OrderDetails.UnitPrice * OrderDetails.Quantity)
            OVER (
            PARTITION BY Orders.EmployeeID
            ) AS cumulative_amount
        FROM Orders
        JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
        JOIN OrderDetails ON OrderDetails.OrderID  = Orders.OrderID
        ORDER BY cumulative_amount DESC
    """
    db.execute(query)
    results = db.fetchone()
    return results
#
def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = """
        SELECT
            Customers.ContactName,
            COUNT(Orders.OrderID) as number_of_orders
        FROM Customers
        LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
        GROUP BY Customers.CustomerID
        ORDER BY number_of_orders ASC
    """
    db.execute(query)
    results = db.fetchall()
    return results
