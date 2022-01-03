# Usage: python3 data/format_timestamps.py --timestamps_file input_timestamp_file \
# --timestamps_file_save output_timestamp_file

import argparse
import os

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Format timestamps')
  parser.add_argument('--timestamps_file', help='Path to Timestamp file.', default='')
  parser.add_argument('--timestamps_file_save', help='Path to Timestamp file.', default='')
  args = parser.parse_args()

  t_nsec_list = []
  with open(args.timestamps_file, 'r') as f:
    lines = f.readlines()
    for l in lines:
      t_sec = float(l)
      t_nsec = int(t_sec * 1e6)
      t_nsec_list.append(t_nsec) 
  print(t_nsec_list)

  with open(args.timestamps_file_save, 'w') as w:
    for t_nsec in t_nsec_list:
      w.write('{}\n'.format(t_nsec))

