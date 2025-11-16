
import random
import time
from queue import Queue

def produce_weather_request(request_queue: Queue, stop_event):
    """
    Produces weather requests for random cities and waits for a response.
    """
    response_queue = Queue()
    cities = ["London", "Paris", "Tokyo", "New York", "Dubai"]
    while not stop_event.is_set():
        city = random.choice(cities)
        request = {
            "producer_id": 1,
            "type": "weather",
            "data": city,
            "response_queue": response_queue
        }
        request_queue.put(request)
        print(f"Producer 1: Sent weather request for {city}")
        
        response = response_queue.get()
        print(f"Producer 1: Received response for {city}: {response}")
        
        time.sleep(random.uniform(1, 3))
    print("Producer 1 is stopping.")
