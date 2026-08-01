from ingestion_pipeline import IngestionPipeline

def main_procces():
    pipeline_ingestion = IngestionPipeline()
    data_products = pipeline_ingestion.read_csv_data()
    print(data_products)

    data_users = pipeline_ingestion.read_json_data()
    print(data_users)

    sql_statuses = "SELECT * FROM order_statuses"
    data_db_statuses = pipeline_ingestion.read_db_data(sql_statuses)
    print(data_db_statuses)

    sql_query_orders = "SELECT * FROM orders"
    data_db_orders = pipeline_ingestion.read_db_data(sql_query_orders)
    print(data_db_orders)

    sql_query_items = "SELECT * FROM order_items"
    data_db_items = pipeline_ingestion.read_db_data(sql_query_items)
    print(data_db_items)

if __name__ == "__main__":
    main_procces()
