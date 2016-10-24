import enum

class circuit_breaker:
  def __init__(self, myfirstarg):
    self.state = CircuitBreakerState.close
    print("hello {}".format(myfirstarg))

  def run(self, f):
    try:
      f()
    except:
      #count the number of exception in the given time frame
      print("hello")

  def call(self, f):
    return f()


class CircuitBreakerState(enum.Enum):
  open = 0
  half_open = 1
  close = 3


if __name__ == "__main__":
  a = circuit_breaker("mike")
  f = lambda: 2
      
  a.run(f)
