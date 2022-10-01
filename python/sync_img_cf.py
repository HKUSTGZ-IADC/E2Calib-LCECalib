import argparse
import os
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
  parser = argparse.ArgumentParser('Sync_img_cf.')
  parser.add_argument('--cf_img_folder', help='Path to images which are processed by MF.')
  parser.add_argument('--trigger_file', help='Path to the trigger file')
  parser.add_argument('--output_file', '-o', default="", help='Output path')
  args = parser.parse_args()

  input_img_folder = args.cf_img_folder
  trigger_file = args.trigger_file
  output_file = args.output_file

  img_filename = [f.split('.png')[0] 
    for f in listdir(input_img_folder) if isfile(join(input_img_folder, f))]
  img_filename.sort()
  i = 0

  cnt = 0
  with open(trigger_file, 'r') as f:
    lines = f.readlines()
    for l in lines:
      t_sec = float(l)
      while i < len(img_filename):
        # print('{} - {}'.format(t_sec, img_filename[i]))
        if (abs(t_sec - float(img_filename[i])) < 0.1):
          print('{} - {}'.format(t_sec, img_filename[i]))
          command = 'cp {}/{}.png {}/{:05}.png'.format(
            input_img_folder, img_filename[i], output_file, cnt)
          print(command)
          os.system(command)
          cnt += 1
          i += 1
          break
        i += 1


