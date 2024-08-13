import sqlite3  # Import the SQLite library for database operations.

class Database:
    def __init__(self, db_name):
        """Initialize the Database class by connecting to the database."""
        self.connection = None
        self.cursor = None
        try:
            # Attempt to establish a connection to the SQLite database.
            self.connection = sqlite3.connect(db_name)
            # Create a cursor object to execute SQL commands.
            self.cursor = self.connection.cursor()
            print(f"Connected to the database '{db_name}' successfully.")
        except sqlite3.Error as e:
            # Handle exceptions if the connection to the database fails.
            print(f"Failed to connect to the database '{db_name}'. Error: {e}")
    
    def execute_query(self, query, parameters=None):
        """Execute a SQL query and return the result."""
        try:
            # Execute the SQL query with or without parameters.
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            # Commit the transaction (for queries that modify data).
            self.connection.commit()
            print("Query executed successfully.")
            return self.cursor.fetchall()  # Return the fetched results (for SELECT queries).
        except sqlite3.Error as e:
            # Handle exceptions if the query fails.
            print(f"Failed to execute query. Error: {e}")
            return None
    
    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            # Close the cursor and the connection.
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")
