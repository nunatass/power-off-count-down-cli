"""
MIT License

Copyright (c) 2021 Nuno Tavares Andrade

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import fire
import os
import time


# power off the computer
def shutdown(minutes: float):
  """ 
    Shutdown the computer after waiting the given minutes
    :param minutes
  """
  mintues_to_second = minutes *  60
  time.sleep(mintues_to_second)
  os.system("shutdown /s /t 1")
  


"""
  Put your computer at very low power state, screen off but everything 
  else is on but at very low power so that you can resume your work where you left off
  but if battery die you loose all your unsaved data.
"""
def suspend(minutes: float):
  """ 
    Suspend the computer after waiting the given minutes
    :param minutes
  """
  mintues_to_second = minutes *  60
  time.sleep(mintues_to_second)
  os.system("systemctl suspend")
  

"""
  suspend to disk; includes power-off, looks like shutdown. Basically, 
  everything in the Ram is copied to swap memory and system shutdown completely. 
  when you start your computer back everything copies back to Ram and you continue 
  where you left off.
"""
def hibernate(minutes: float):
  """ 
    Hibernate the computer after waiting the given minutes
    :param minutes
  """
  mintues_to_second = minutes *  60
  time.sleep(mintues_to_second)
  os.system("systemctl hibernate")



if __name__ == "__main__":
  fire.Fire({
    "shutdown" : shutdown,
    "suspend"  : suspend,
    "hibernate": hibernate
  })

