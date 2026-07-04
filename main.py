from src.scraper import run
from src.uploader import (
    get_or_create_vector_store,
    upload_all_files
)

if __name__ == "__main__":
    # Run the scraper to fetch articles and save them as markdown files
    run()
    
    # Get or create the Vector Store and upload all markdown files to it
    vector_store_id = get_or_create_vector_store()
    upload_all_files(vector_store_id)

    print("Done!")