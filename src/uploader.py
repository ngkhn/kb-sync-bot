from openai import OpenAI

from .config import OPENAI_API_KEY
from .constants import MARKDOWN_DIR, VECTOR_STORE_NAME

client = OpenAI(api_key=OPENAI_API_KEY)


def get_or_create_vector_store() -> str:
    """
    Return an existing Vector Store if it exists,
    otherwise create a new one.
    """
    vector_stores = client.vector_stores.list()

    for vector_store in vector_stores.data:
        if vector_store.name == VECTOR_STORE_NAME:
            print(f"Using existing Vector Store: {vector_store.id}")
            return vector_store.id

    vector_store = client.vector_stores.create(
        name=VECTOR_STORE_NAME,
    )

    print(f"Created Vector Store: {vector_store.id}")

    return vector_store.id


def upload_all_files(vector_store_id: str):
    """
    Upload all markdown files to the Vector Store.
    """
    markdown_files = list(MARKDOWN_DIR.glob("*.md"))

    if not markdown_files:
        raise ValueError("No markdown files found.")

    streams = [open(file, "rb") for file in markdown_files]

    try:
        file_batch = client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=streams,
        )

        print(f"Status: {file_batch.status}")
        print(f"File Counts: {file_batch.file_counts}")

    finally:
        for stream in streams:
            stream.close()

