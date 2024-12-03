"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
ADDITIONAL_TIME_BY_LAYER = 2

def bake_time_remaining(time):
  """ Calculate the remaining time based on elapsed time
  
  :param time: int - the elapsed time
  :return: int - The remaining time of cooking.

  This function calculates the remaining of cooking based on
  the elapsed time.
  """
  return EXPECTED_BAKE_TIME - time

def preparation_time_in_minutes(number_of_layers):
  """ Calculate the extra time based in the number of layers
  
  :param number_of_layers: int - the number of layers in the lasagna
  :return:int - The additional preparation time (in minutes) extra.

  This function provides the additional extra time that the lasagna 
  requires to be cooking.
  """
  return number_of_layers * ADDITIONAL_TIME_BY_LAYER

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  """ Calculate the elapsed cooking time
  
  :param number_of_layers: int - the number of layers in the lasagna
  :param elapsed_bake_time: int - elapsed cooking time
  :return: int - total time elapsed (in minutes)

  This function takes two integers representing the number of lasagna layers
  and the time already spent baking and calculates the total elapsed 
  minutes spent cooking the lasagna.
  """
  return EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time) + preparation_time_in_minutes(number_of_layers)

elapsed_time = elapsed_time_in_minutes(1,3)
print(elapsed_time)