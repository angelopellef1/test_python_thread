
import random
import time
from queue import Queue

def produce_random_user_request(request_queue: Queue, stop_event):
    """
    Produces random user requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 7,
            "type": "random_user",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 7: Sent random user request")
        
        response = response_queue.get()
        print(f"Producer 7: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 7 is stopping.")
