import time


def timer(seconds, prompt="Please enter an answer: ", message="Time's up!"):
    """
    Wait for a certain amount of time for user input.

    Args:
        seconds (int): Number of seconds to wait.
        prompt (str): Prompt to show the user.
        message (str): Message to display when time is up.

    Returns:
        None
    """
    start_time = time.time()
    print(prompt)
    answer = input()
    end_time = time.time()

    while end_time - start_time < seconds:
        print(f"Time remaining: {seconds - (end_time - start_time):.1f} seconds")
        time.sleep(0.1)
        end_time = time.time()

    if end_time - start_time >= seconds:
        print(message)
    else:
        print("Your answer is:", answer)


if __name__ == "__main__":
    seconds_to_wait = 10
    print(f"Waiting for {seconds_to_wait} seconds...")
    timer(seconds_to_wait)
