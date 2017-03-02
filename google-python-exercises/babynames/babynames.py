#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from pprint import pprint as pp
from glob import glob


"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++

  with open(filename, 'rU') as f:
     names_file = f.read()

  # extract the year
  year = (re.search(r'Popularity in (\d\d\d\d)', names_file)).group(1)
  # extract the rank and names into a list
  names_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', names_file)
  # get the names data into a (name: rank) dict
  # in case of duplicates, retain higher ranking ones
  names_dict = {}
  for x in names_list:
      if x[1] not in names_dict.keys(): names_dict[x[1]] = x[0]
      if x[2] not in names_dict.keys(): names_dict[x[2]] = x[0]

  # build the final list
  final_list = []
  for x in names_dict:
      final_list.append(x + ' ' + names_dict[x])
  final_list = sorted(final_list)
  # insert the year as the first element in the final_list
  final_list.insert(0,year)
  return final_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]


  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output or write it to a file

  for filename in glob(args[0]):
      if summary:
          with open(filename +'.summary', 'w') as f:
              for element in extract_names(filename):
                  summaryfile = f.write(element+'\n')
      else:
          pp(extract_names(filename))

if __name__ == '__main__':
  main()

# to compare summary files across years in powershell:
# Get-Content *.summary | Select-String -Pattern ('name')
