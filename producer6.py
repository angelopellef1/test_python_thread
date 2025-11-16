
import random
import time
from queue import Queue

def produce_bitcoin_price_request(request_queue: Queue, stop_event):
    """
    Produces bitcoin price requests and waits for a response.
    """
    response_queue = Queue()
    while not stop_event.is_set():
        request = {
            "producer_id": 6,
            "type": "bitcoin_price",
            "response_queue": response_queue
        }
        request_queue.put(request)
        print("Producer 6: Sent bitcoin price request")
        
        response = response_queue.get()
        print(f"Producer 6: Received response: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 6 is stopping.")
