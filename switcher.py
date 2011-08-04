#!/usr/bin/env python

#  
#  Copyright (C) 2011 Joseph Henrich
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import os
import random
import time
from subprocess import check_call
path = "/home/loki/backgrounds"
list_path = path + "/list"
link_files = [path + "/left", path + "/right"]
sleep_time = 60*5 #seconds * minutes 

def swap_em():
  files = os.listdir(list_path)
  random.shuffle(files)

  for f in link_files:
    check_call(["ln", "-f", "-s", "{}/{}".format(list_path, files.pop()), f])
  output = check_call(["nitrogen", "--restore"])

if __name__ == "__main__":
  while(True):
    try:
      swap_em()
      time.sleep(sleep_time)
    except KeyboardInterrupt:
      break

