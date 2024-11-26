import pymongo
import certifi
from datetime import datetime, timedelta
from hw9_no_sql_databases.data_for_collections.data_for_products_collection import products_list
from hw9_no_sql_databases.data_for_collections.data_for_orders_collection import orders_list
from sensetive_data import db_pass

get_rid_of_id = {"_id": 0}

try:
	uri = (f"mongodb+srv://Cluster87609:{db_pass}@cluster87609.3rhb1.mongodb.net/"
	       "?retryWrites=true&w=majority&appName=Cluster87609")

	client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
	print("Connected successfully")

	database = client["online_store"]
	collection_with_products = database["collection_products"]
	collection_with_orders = database["collection_orders"]
	collection_with_products.create_index("category")


	def insert_data():
		collection_with_products.insert_many(products_list)
		collection_with_orders.insert_many(orders_list)


	def retrieve_data():
		today = datetime.today()
		thirty_days_ago = today - timedelta(days=30)

		filter_query = {
			"order_date": {
				"$gte": thirty_days_ago}
		}

		result = collection_with_orders.find(filter_query, get_rid_of_id)

		for order in result:
			print(order)


	def update_data(item):
		collection_with_orders.insert_one({"item": item, "Price": 20000, "Color": "Blue",
		                                   "Discount": 1, "is_paid": False,
		                                   "order_date": datetime(2024, 10, 12)})

		res = list(collection_with_products.find({"item": item}))
		current_amount = res[0]['Amount']

		query_filter = {"item": item}
		update_operation = {"$set": {"Amount": current_amount - 1}}
		collection_with_products.update_one(query_filter, update_operation)


	def delete_data():

		query_filter = {
			"$or": [
				{"Amount": {"$lte": 0}},
				{"for_sale": False}
			]
		}

		collection_with_products.delete_many(query_filter)


	def sales_during_period(from_date, to_date):

		filter_query = {
			"$and": [
				{"order_date": {"$gte": from_date}},
				{"order_date": {"$lte": to_date}},
			]
		}

		res = collection_with_orders.find(filter_query, get_rid_of_id)

		for i in res:
			print(i)


	def total_value_per_customer():
		pipeline = [{
			"$group": {
				"_id": "$customer_id",
				"first_purchase_date": {"$first": "$order_date"},
				"total_value": {"$sum": "$price"},
				"total_orders": {"$sum": 1},
				"orders": {"$push": {"order_date": "$order_date", "price": "$price"}}
			}
		}]

		agr_res = collection_with_orders.aggregate(pipeline)

		for i in agr_res:
			print('\n')
			print(f"Customer {i['_id']}")
			print(f"The first purchase date - {i['first_purchase_date']}")
			print(f"Total sum of money has been spent in the store - {i['total_value']}")
			print(f"Total orders in the store - {i['total_orders']}")
			[print(i) for i in i['orders']]

	# insert_data()
	# update_data("Iphone 14")
	# retrieve_data()
	# sales_during_period(datetime(2024, 10, 1), datetime(2024, 12, 31))
	# delete_data()
	# total_value_per_customer()


except Exception as e:
	raise Exception(
		"The following error occurred: ", e)
