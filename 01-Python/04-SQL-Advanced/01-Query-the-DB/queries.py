# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    query = """
        SELECT *
        FROM Orders
   """
    db.execute(query)
    orders = db.fetchall()
    return orders

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between date_from and date_to
    query = """
        SELECT *
        FROM Orders
        WHERE Orders.OrderDate > ?
            AND Orders.OrderDate <= ?
    """
    db.execute(query,(date_from, date_to))
    results = db.fetchall()
    return results

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query = """
        SELECT *,
            julianday(Orders.ShippedDate) - julianday(Orders.OrderDate) TimeDelta
        FROM Orders
        ORDER BY TimeDelta ASC
    """
    db.execute(query)
    results = db.fetchall()
    return results
