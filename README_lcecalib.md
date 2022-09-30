# E2Calib: How to Calibrate Your Event Camera
### Run E2Calib for LCE-CALIB
1. Download the project: 
  
    ```git clone http://gitlab.ram-lab.com/ramlab_dataset_sensor/multisensor_calibration/e2vid```

2. Open a docker container
  * build an image: 
  
    ```cd docker && docker build . -t nvidia/cuda:10.1-py3-conda-torc```

  * build a container: 
  
    ```nvidia-docker run -e DISPLAY -v ~/.Xauthority:/root/.Xauthority --network host -p 8001:8888 -v /home/jjiao/lcecalib_ws/:/Titan/code/lcecalib_ws -v /Titan/dataset:/Titan/dataset --privileged --cap-add sys_ptrace -it --name lcecalib jjiao/e2vid:cuda10.1-conda-py3  /bin/bash```

  * open a container: 
    
    ```docker exec -it lcecalib /bin/bash```

3. Convert *rosbag* into *h5 file*: 

    ```python3 convert.py --input_file xxx.bag --output_file xxx.h5 --ros_topic /davis/events```

4. Generate trigger timestamps in the integer type: 

    ```python3 format_timestamps.py --timestamps_file trigger.txt --timestamps_file_save trigger_format.txt```

5. Reconstruct frame images without trigger: 

    ```python3 offline_reconstruction.py  --h5file xxx.h5 --output_folder path_to_folder --freq_hz 5 --upsample_rate 4 --height 260 --width 346```

6. Reconstruct frame images with trigger: 

    ```python3 offline_reconstruction.py  --h5file xxx.h5 --output_folder path_to_folder --timestamps_file trigger_format.txt --upsample_rate 4 --height 260 --width 346```
