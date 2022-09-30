# E2Calib: How to Calibrate Your Event Camera
### Run E2Calib for LCE-CALIB
1. Download the project: ```git clone https://git.ram-lab.com/gogojjh/E2VID```
2. Open a docker container
  * build an image: 
  ```cd docker && docker build . -t nvidia/cuda:10.1-py3-conda-torc```
  * build a container: 
  ```nvidia-docker run -it --name e2calib -v /home/jjiao/Docker_ws/docker_fold/documents:/usr/app -p 8001:8888 nvidia/cuda:10.1-py3-conda-torch /bin/bash```
  * open a container: 
  ```docker exec -it e2calib /bin/bash```
  ```cd e2calib/python```
3. Convert *rosbag* into *h5 file*: 
  ```python convert.py --input_file xxx.bag --output_file xxx.h5 --ros_topic /davis/events```
4. Generate trigger timestamps in the integer type: 
  ```python format_timestamps.py --timestamps_file trigger.txt --timestamps_file_save trigger_format.txt```
5. Reconstruct frame images without trigger: 
  ```python3 offline_reconstruction.py  --h5file xxx.h5 --output_folder path_to_folder --freq_hz 5 --upsample_rate 4 --height 260 --width 346```
6. Reconstruct frame images with trigger: 
  ```python3 offline_reconstruction.py  --h5file xxx.h5 --output_folder path_to_folder --timestamps_file trigger_format.txt --upsample_rate 4 --height 260 --width 346```
