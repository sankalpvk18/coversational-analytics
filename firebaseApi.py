import firebase_admin
from firebase_admin import credentials, db


# Initialize Firebase app
def initialize_firebase():
    cred = credentials.Certificate("secrets.json")
    firebase_admin.initialize_app(
        cred, {"databaseURL": "https://conversational-analytics-4f8b7-default-rtdb.firebaseio.com"}
    )


# Function to insert data into Firebase Realtime Database
def insert_data_into_firebase(prompt, data, sql, insight, chart, x_column, y_column):
    # Initialize Firebase if not already initialized
    if not firebase_admin._apps:
        initialize_firebase()

    # Reference to the database
    ref = db.reference("Questions")
    payload = {
        "prompt": prompt,
        "data": data,
        "sql": sql,
        "insight": insight,
        "chart": chart,
        "x_column": x_column,
        "y_column": y_column,
        "feedback": "null",
    }

    query = ref.order_by_child("prompt").equal_to(prompt).get()
    if query:
        # If exists, update the existing node
        key = list(query.keys())[0]
        existing_ref = ref.child(key)
        existing_ref.update(payload)
        print(f"Updated existing node with key: {key}")
    else:
        # If not exists, push new data
        new_ref = ref.push(payload)

    return (
        list(query.keys())[0] if query else new_ref.key
    )  # Return the key of the newly inserted data


def add_feedback(node_key, feedback):
    # Initialize Firebase if not already initialized
    if not firebase_admin._apps:
        initialize_firebase()

    # Reference to the specific node in the database
    ref = db.reference(f"Questions/{node_key}/")

    # Update the node with the new data point
    ref.update(feedback)

    return f"Feedback recieved thank you!"


def get_result_from_db(prompt):
    # Initialize Firebase if not already initialized
    if not firebase_admin._apps:
        initialize_firebase()

    # Reference to the database
    ref = db.reference("Questions")

    # Query to find the node with the specified prompt
    query = ref.order_by_child("prompt").equal_to(prompt).get()

    # Extract the key and data of the matched node
    for key, value in query.items():
        print(value)
        return (
            key,
            value.get("data"),
            value.get("sql"),
            value.get("insight"),
            value.get("chart"),
            value.get("x_column"),
            value.get("y_column"),
        )

    return None, None, None, None, None, None, None  # Return None if no node is found
