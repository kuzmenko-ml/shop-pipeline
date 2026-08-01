import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class IngestionPipeline():
    def read_csv_data(self):
        print("START(csv)")
        try:
            filepath = os.getenv('FILE_PATH_CSV')
            df = pd.read_csv(filepath)
            print("SUCCESS(csv)")
            return df
        except Exception as e:
            print(f"ERROR: {e}")
            print("STOP(csv)")

    def read_json_data(self):
        print("START(json)")
        try:
            filepath = os.getenv('FILE_PATH_JSON')
            df = pd.read_json(filepath)
            print("SUCCESS(json)")
            return df
        except Exception as e:
            print(f"ERROR: {e}")
            print("STOP(json)")

    def read_db_data(self, query):
        try:
            print("START(sql)")
            conn = psycopg2.connect(
                host = os.getenv('DB_HOST'),
                port = os.getenv('DB_PORT'),
                database = os.getenv('DB_NAME'),
                user = os.getenv('DB_USER'),
                password = os.getenv('DB_PASSWORD')
            )

            df = pd.read_sql(query, conn)
            print("SUCCESS(sql)")
            return df
        except Exception as e:
                print(f"ERROR: {e}")
                print("STOP(sql)")
