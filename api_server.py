"""
Filename: api_server.py
Author : Vaibhav Joshi (vaibhav.joshi231@gmail.com)
Version : 1.0
Revisions / Logs :


A simple Flask server that contains endpoints to process the transactions of a given based on requests such as
add points, deduct points and view points balance. Constraints imposed are as below :-

-> oldest points should be spent first
- > payers points should not go negative

:return
    [Response]: Returns response with respective status codes and JSON objects based on the type of request
"""

# handling imports
import json
from collections import deque, defaultdict
from flask import Flask, request, jsonify

# Initializing the web server
app = Flask("api_server")

# Global dictionary track the payers points. This will be returned in JSON format when a balance check is called for
accounts = defaultdict(int)
total_points = 0

# Initializing a queue data structure to keep track of and process any incoming transactions in later calculations.
transactions = deque()

# global variables concerning HTTP requests
content_header = {"Content-type" : "application/json"}

# Declaring a class structure to store incoming transaction instances. 
class Transaction:
    def __init__(self, payer_name, points, timestamp):
        self.payer_name = payer_name
        self.points = points
        self.transaction_timestamp = timestamp

    def get_payer_name(self):
        return self.payer_name

    def get_payer_points(self):
        return self.points

    def get_transaction_date(self):
        return self.transaction_timestamp

    def set_payer_name(self, payer_name):
        self.payer_name = payer_name

    def set_payer_points(self, points):
        self.points = points

    def set_transaction_timestamp(self, timestamp):
        self.transaction_timestamp = timestamp


@app.route('/add_points', methods=['POST'])
def add_points():
    """
    REST endpoint that adds payers points to a user's account based on the constraints:
    If payer points are positive, we just append the transaction to the queue
    If payer points are negative then we deal with the below conditions accordingly :
    1) when the payer already exists and deducting the incoming transactional points results in negative points value
    2) when the payer already exists and deducting the incoming transactional points result in positive points value
    3) when the first transactional points value is negative

    :return
        [Response object]: Returns a success message with the OK status code (200) if request is valid else
         returns bad request by client with a status code of 400
    """
    global total_points

    data = request.get_json(force=True)

    payer_name = str(data["payer"])
    points = int(data["points"])
    transaction_timestamp = str(data["transaction_timestamp"])

    # if points are positive, simply add them to the queue as part of a new transaction.
    if points > 0:
        total_points += points
        transactions.append(Transaction(payer_name, points, transaction_timestamp))
        accounts[payer_name] += points

    # if points are negative
    elif points < 0:

        # if the points fall below zero
        if payer_name in accounts and (accounts[payer_name] + points) < 0:
            return "Error : Invalid transaction record", 400, content_header

        # if the points are positive
        elif payer_name in accounts and (accounts[payer_name] + points) > 0:
            accounts[payer_name] += points
            total_points += points
            for i in range(len(transactions)):
                payer = transactions[i].get_payer_name()
                if payer == payer_name:
                    remaining = transactions[i].get_payer_points() + points
                    if remaining <= 0:
                        del transactions[i]
                        points = remaining
                    else:
                        transactions[i].set_payer_points(remaining)
                        break
        else:
            return "Error : invalid transaction record", 400, content_header

    return "Successfully added points to the user's account", 200, content_header


@app.route('/deduct_points', methods=['DELETE'])
def deduct_points():
    """
    REST API endpoint to deduct point from the a user's account per the constraints
    :return
        [Response] : Returns a JSON object list of [payer_name, points deducted] after
        deducting points from the user account as per the constraints
    """
    global total_points

    data = request.get_json(force=True)
    points_to_deduct = int(data["points_to_deduct"])

    if total_points < points_to_deduct:
        return "Error: Not enough points", 400, content_header
    else:
        updated_transactions = []
        while points_to_deduct > 0:
            transaction = transactions.popleft()

            current_points = transaction.get_payer_points()
            payer_name = transaction.get_payer_name()
            points_to_deduct -= current_points
            if points_to_deduct < 0:
                points_deducted = current_points + points_to_deduct
                transaction.set_payer_points(-points_to_deduct)
                transactions.append(transaction)
            else:
                points_deducted = current_points
            transaction.set_payer_points(points_deducted)
            transaction.set_transaction_timestamp("now")
            updated_transactions.append(transaction)
            accounts[payer_name] -= points_deducted
            total_points -= points_deducted

    # adding a minus sign to indicate deduction of points
    for transaction in updated_transactions:
        transaction_value = transaction.get_payer_points()
        transaction.set_payer_points(-transaction_value)

    # prepare the response
    response = []
    for transaction in updated_transactions:
        response.append([transaction.get_payer_name(), transaction.get_payer_points(), transaction.get_transaction_date()])
    return json.dumps(response)


@app.route("/get_balance", methods=['GET'])
def show_balance():
    """
    This REST-API endpoint returns the points balance for a user corresponding to each payer_name
    :return:
        JSON object that shows the balance points of each payer_name
    """
    return json.dumps(accounts)


if __name__ == "__main__":
    """
    Start the Flask server
    """
    app.run(debug=True)
