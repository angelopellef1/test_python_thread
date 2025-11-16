
import random
import time
from queue import Queue

def produce_joke_request(request_queue: Queue, stop_event):
    """
    Produces joke requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 2,
            "type": "joke",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 2: Sent joke request")
        
        response = response_queue.get()
        print(f"Producer 2: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 2 is stopping.")
