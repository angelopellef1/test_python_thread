
import random
import time
from queue import Queue

def produce_number_fact_request(request_queue: Queue, stop_event):
    """
    Produces number fact requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 8,
            "type": "number_fact",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 8: Sent number fact request")
        
        response = response_queue.get()
        print(f"Producer 8: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 8 is stopping.")
