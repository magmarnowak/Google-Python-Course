#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from pprint import pprint as pp

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

  final_list = []
  # extract the year
  year = (re.search(r'Popularity in (\d\d\d\d)', names_file)).group(1)
  # extract the rank and names into a list
  names_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', names_file)
  # get the names data into a dict
  names_dict = {}
  for x in names_list:
      # first add all the male names to the dictionary
      names_dict[x[1]] = x[0]
  # then add the female ones, checking whether the name already exsists as a key
  for x in names_list:
      if x[2] in names_dict.keys():
          #if yes, then keep the name with the lower rank
          if names_dict[x[2]] >= x[0]:
              pass
          else:
              # otherwise just add the name
              names_dict[x[2]] = x[0]
  # build the final list
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
  pp(args)

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # for x in args:
  #     if summary:
  #         with open(x +'.summary', 'w') as f:
  #             summaryfile = f.write(extract_names(x))
  #     else:
  #         pp(extract_names(x))
  pp(extract_names(args[0]))

if __name__ == '__main__':
  main()
