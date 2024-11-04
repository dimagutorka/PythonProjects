from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'])  # Replace with your cluster's IP address
session = cluster.connect()

# Create a keyspace if it doesn't exist
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS my_keyspace
    WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 }
""")

# Set the keyspace
session.set_keyspace('my_keyspace')

# Create a table
session.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id UUID PRIMARY KEY,
        username text,
        email text,
        created_at timestamp
    )
""")


print("Table 'users' created successfully.")

# Close the connection
cluster.shutdown()
