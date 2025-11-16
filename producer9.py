
import random
import time
from queue import Queue

def produce_bored_activity_request(request_queue: Queue, stop_event):
    """
    Produces bored activity requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 9,
            "type": "bored_activity",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 9: Sent bored activity request")
        
        response = response_queue.get()
        print(f"Producer 9: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 9 is stopping.")
