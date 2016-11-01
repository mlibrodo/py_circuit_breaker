import math, random

class Exponential_Backoff:

  def __init__(self, slot_time, max_fail_count):
    self.slot_time = slot_time
    self.failure_count = 0
    self.max_fail_count = max_fail_count

  def try_call(self,f, default_val):
    if(self.failure_count == self.max_fail_count):
      return default_val
    else:
      slot = self.slot_time * random.randint(0, math.pow(2, self.failure_count) - 1)
      print("slot {}  ".format(slot))
      try:
        return f()
      except:
        self.failure_count += 1
        return self.try_call(f, default_val)
