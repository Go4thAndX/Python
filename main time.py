import time

def timer(seconds):
  """
  This function waits for a certain amount of time after an input statement for an answer.

  Args:
    seconds: The number of seconds to wait.

  Returns:
    None.
  """

  start_time = time.time()
  print("Please enter an answer: ")
  answer = input()
  end_time = time.time()

  if end_time - start_time >= seconds:
    print("Time's up!")
  else:
    print("Your answer is:", answer)

if __name__ == "__main__":
    timer(10)