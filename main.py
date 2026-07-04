from src.scraper import run
from src.uploader import (
    attach_vector_store,
    get_or_create_vector_store,
    upload_all_files,
)

if __name__ == "__main__":
    # Run the scraper to fetch articles and save them as markdown files
    run()
    
    vector_store_id = get_or_create_vector_store()
    upload_all_files(vector_store_id)
    attach_vector_store(vector_store_id)

    print("Done!")