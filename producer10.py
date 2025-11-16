
import random
import time
from queue import Queue

def produce_agify_request(request_queue: Queue, stop_event):
    """
    Produces agify requests and waits for a response.
    """
    response_queue = Queue()
    names = ["michael", "matthew", "jane", "peter", "joan"]
    while not stop_event.is_set():
        name = random.choice(names)
        request = {
            "producer_id": 10,
            "type": "agify",
            "data": name,
            "response_queue": response_queue
        }
        request_queue.put(request)
        print(f"Producer 10: Sent agify request for {name}")
        
        response = response_queue.get()
        print(f"Producer 10: Received response for {name}: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 10 is stopping.")
