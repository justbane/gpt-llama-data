import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core.readers import SimpleDirectoryReader

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index: ", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))

    return index

pdf_path = os.path.join("data", "Passenger_vehicles_in_the_United_States.pdf")
pass_car_info = SimpleDirectoryReader(input_files=[pdf_path]).load_data()
pass_car_index = get_index(pass_car_info, "passenger_car_info")
pass_car_engine = pass_car_index.as_query_engine()