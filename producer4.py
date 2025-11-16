
import random
import time
from queue import Queue

def produce_dog_image_request(request_queue: Queue, stop_event):
    """
    Produces dog image requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 4,
            "type": "dog_image",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 4: Sent dog image request")
        
        response = response_queue.get()
        print(f"Producer 4: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 4 is stopping.")
