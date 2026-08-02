import os
from dotenv import load_dotenv

load_dotenv()

class LoadPipeline():
    def save_to_parquet(self, data, filename):
        path = os.getenv('STORAGE_PATH')
        file_path = os.path.join(path, filename)
        data.to_parquet(file_path, index=False)
        print(f"Saved: {file_path}")