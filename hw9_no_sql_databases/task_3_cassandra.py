from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()


print('OK')

session.shutdown()
cluster.shutdown()