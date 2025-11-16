import threading
import time
from queue import Queue
import requests

from producer1 import produce_weather_request
from producer2 import produce_joke_request
from producer3 import produce_cat_fact_request
from producer4 import produce_dog_image_request
from producer5 import produce_ip_request
from producer6 import produce_bitcoin_price_request
from producer7 import produce_random_user_request
from producer8 import produce_number_fact_request
from producer9 import produce_bored_activity_request
from producer10 import produce_agify_request

def main():
    """
    Main function to run the consumer and producers.
    """
    request_queue = Queue()
    stop_event = threading.Event()

    producers = [
        threading.Thread(target=produce_weather_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_joke_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_cat_fact_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_dog_image_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_ip_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_bitcoin_price_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_random_user_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_number_fact_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_bored_activity_request, args=(request_queue, stop_event)),
        threading.Thread(target=produce_agify_request, args=(request_queue, stop_event)),
    ]

    # Start producer threads
    for p in producers:
        p.start()

    tasks_processed = 0
    # Consume data from the queue
    try:
        while True:
            if not request_queue.empty():
                request = request_queue.get()
                tasks_processed += 1
                
                response_queue = request["response_queue"]
                response = None

                try:
                    if request["type"] == "weather":
                        city = request["data"]
                        response = requests.get(f"https://goweather.herokuapp.com/weather/{city}").json()
                    elif request["type"] == "joke":
                        response = requests.get("https://official-joke-api.appspot.com/random_joke").json()
                    elif request["type"] == "cat_fact":
                        response = requests.get("https://catfact.ninja/fact").json()
                    elif request["type"] == "dog_image":
                        response = requests.get("https://dog.ceo/api/breeds/image/random").json()
                    elif request["type"] == "ip":
                        response = requests.get("https://api.ipify.org?format=json").json()
                    elif request["type"] == "bitcoin_price":
                        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
                    elif request["type"] == "random_user":
                        response = requests.get("https://randomuser.me/api/").json()
                    elif request["type"] == "number_fact":
                        response = requests.get("http://numbersapi.com/random/trivia").text
                    elif request["type"] == "bored_activity":
                        response = requests.get("https://www.boredapi.com/api/activity").json()
                    elif request["type"] == "agify":
                        name = request["data"]
                        response = requests.get(f"https://api.agify.io?name={name}").json()
                except requests.exceptions.RequestException as e:
                    response = {"error": str(e)}

                response_queue.put(response)

            time.sleep(0.1)  # Prevent busy-waiting
    except KeyboardInterrupt:
        print("\nShutting down...")
        stop_event.set()
        for p in producers:
            p.join()
        print("All threads have been stopped.")
        print(f"Total tasks processed: {tasks_processed}")

if __name__ == "__main__":
    main()

