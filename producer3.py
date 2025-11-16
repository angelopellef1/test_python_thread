
import random
import time
from queue import Queue

def produce_cat_fact_request(request_queue: Queue, stop_event):
    """
    Produces cat fact requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 3,
            "type": "cat_fact",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 3: Sent cat fact request")
        
        response = response_queue.get()
        print(f"Producer 3: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 3 is stopping.")
