amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7
amarkr@voyant-algoithm-gpu:~$ cd /home/
amarkr@voyant-algoithm-gpu:/home$ cd jupyter/
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls
=2.0.1  cut1.mp4  cut2.mp4  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls
=2.0.1  cut1.mp4  cut2.mp4  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ pwd
/home/jupyter
amarkr@voyant-algoithm-gpu:/home/jupyter$ scp *.* .
cp: '=2.0.1' and './=2.0.1' are the same file
cp: 'cut1.mp4' and './cut1.mp4' are the same file
cp: 'cut2.mp4' and './cut2.mp4' are the same file
cp: 'video.mp4' and './video.mp4' are the same file
amarkr@voyant-algoithm-gpu:/home/jupyter$ scp -r *.* amarkr/
amarkr/: No such file or directory
amarkr@voyant-algoithm-gpu:/home/jupyter$ scp -r *.* /amarkr/
/amarkr/: No such file or directory
amarkr@voyant-algoithm-gpu:/home/jupyter$ scp -r *.* /home/amarkr/
amarkr@voyant-algoithm-gpu:/home/jupyter$ cd
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ gsutil cp /home/jupyter/*.mp4 gs://data_jupyter
Copying file:///home/jupyter/cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp /home/jupyter/*.mp4 gs://data_jupyter
Copying file:///home/jupyter/cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ ^C
amarkr@voyant-algoithm-gpu:~$ logout
Connection to 34.75.239.233 closed by remote host.
Connection to 34.75.239.233 closed.
amarkr@Amars-MacBook-Pro ~ % gcloud compute ssh voyant-algoithm-gpu --zone us-east1-c -- -L 8080:localhost:8080
======================================
Welcome to the Google Deep Learning VM
======================================

Version: pytorch-gpu.1-4.m56
Based on: Debian GNU/Linux 9.13 (stretch) (GNU/Linux 4.9.0-13-amd64 x86_64\n)

Resources:
 * Google Deep Learning Platform StackOverflow: https://stackoverflow.com/questions/tagged/google-dl-platform
 * Google Cloud Documentation: https://cloud.google.com/deep-learning-vm
 * Google Group: https://groups.google.com/forum/#!forum/google-dl-platform

To reinstall Nvidia driver (if needed) run:
sudo /opt/deeplearning/install-driver.sh
Linux voyant-algoithm-gpu 4.9.0-13-amd64 #1 SMP Debian 4.9.228-1 (2020-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp /home/jupyter/*.mp4 gs://data_jupyter
Copying file:///home/jupyter/cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp /home/jupyter/*.mp4 gs://data_jupyter
Copying file:///home/jupyter/cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ rm -r ~/.gsutil
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp /home/jupyter/*.mp4 gs://data_jupyter
Copying file:///home/jupyter/cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ logout
Connection to 34.75.239.233 closed.
amarkr@Amars-MacBook-Pro ~ % gcloud compute ssh voyant-algoithm-gpu --zone us-east1-c -- -L 8080:localhost:8080
======================================
Welcome to the Google Deep Learning VM
======================================

Version: pytorch-gpu.1-4.m56
Based on: Debian GNU/Linux 9.13 (stretch) (GNU/Linux 4.9.0-13-amd64 x86_64\n)

Resources:
 * Google Deep Learning Platform StackOverflow: https://stackoverflow.com/questions/tagged/google-dl-platform
 * Google Cloud Documentation: https://cloud.google.com/deep-learning-vm
 * Google Group: https://groups.google.com/forum/#!forum/google-dl-platform

To reinstall Nvidia driver (if needed) run:
sudo /opt/deeplearning/install-driver.sh
Linux voyant-algoithm-gpu 4.9.0-13-amd64 #1 SMP Debian 4.9.228-1 (2020-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
amarkr@voyant-algoithm-gpu:~$ rm ~/.gsutil
rm: cannot remove '/home/amarkr/.gsutil': No such file or directory
amarkr@voyant-algoithm-gpu:~$ rm /.gsutil
rm: cannot remove '/.gsutil': No such file or directory
amarkr@voyant-algoithm-gpu:~$ sudo ls /.
bin   dev  home        initrd.img.old  lib64	   media  opt	root  sbin  sys  usr  vmlinuz
boot  etc  initrd.img  lib	       lost+found  mnt	  proc	run   srv   tmp  var  vmlinuz.old
amarkr@voyant-algoithm-gpu:~$ sudo rm ~/.gsutil
rm: cannot remove '/home/amarkr/.gsutil': No such file or directory
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp /home/jupyter/*.mp4 gs://data_jupyter
Copying file:///home/jupyter/cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp *.mp4 gs://data_jupyter
Copying file://cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp *.mp4 gs://data_jupyter
Copying file://cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ logout
Connection to 34.75.208.241 closed.
amarkr@Amars-MacBook-Pro ~ % gcloud compute ssh voyant-algoithm-gpu --zone us-east1-c -- -L 8080:localhost:8080
======================================
Welcome to the Google Deep Learning VM
======================================

Version: pytorch-gpu.1-4.m56
Based on: Debian GNU/Linux 9.13 (stretch) (GNU/Linux 4.9.0-13-amd64 x86_64\n)

Resources:
 * Google Deep Learning Platform StackOverflow: https://stackoverflow.com/questions/tagged/google-dl-platform
 * Google Cloud Documentation: https://cloud.google.com/deep-learning-vm
 * Google Group: https://groups.google.com/forum/#!forum/google-dl-platform

To reinstall Nvidia driver (if needed) run:
sudo /opt/deeplearning/install-driver.sh
Linux voyant-algoithm-gpu 4.9.0-13-amd64 #1 SMP Debian 4.9.228-1 (2020-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp *.mp4 gs://data_jupyter
Copying file://cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ gcloud auth login

You are running on a Google Compute Engine virtual machine.
It is recommended that you use service accounts for authentication.

You can run:

  $ gcloud config set account `ACCOUNT`

to switch accounts if necessary.

Your credentials may be visible to others with access to this
virtual machine. Are you sure you want to authenticate with
your personal account?

Do you want to continue (Y/n)?  y

Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?client_id=32555940559.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcompute+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Faccounts.reauth&code_challenge=_gm_GCTK4Vdjb_yJGaliWHIBJ1wGv1lKVXJlyR88nd0&code_challenge_method=S256&access_type=offline&response_type=code&prompt=select_account


Enter verification code: 4/5QGI0GEVwW4stMo-bBmD3HrAdk-S5ERoYrxDZvhXqElmanziAVnw--Y

You are now logged in as [amarkumarmcgill@gmail.com].
Your current project is [entered].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
amarkr@voyant-algoithm-gpu:~$ sudo gsutil cp *.mp4 gs://data_jupyter
Copying file://cut1.mp4 [Content-Type=video/mp4]...
AccessDeniedException: 403 Insufficient Permission                              
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ ls ~/
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ ls /home/jupyter/
=2.0.1  cut1.mp4  cut2.mp4  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:~$ cd /home/jupyter/
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls
=2.0.1  cut1.mp4  cut2.mp4  cut3.mp4  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ pwd
/home/jupyter
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls /home/jupyter/
=2.0.1  cut1.mp4  cut2.mp4  cut3.mp4  cut4.mp4  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls
=2.0.1  cut1.mp4  cut2.mp4  cut3.mp4  cut4.mp4  detectron2  trial.py  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ python
Python 3.7.8 | packaged by conda-forge | (default, Jul 31 2020, 02:25:08) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
amarkr@voyant-algoithm-gpu:/home/jupyter$ nvidia-smi
Mon Oct 19 01:38:10 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   46C    P0   129W / 250W |   2039MiB / 16280MiB |     38%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     15025      C   python                                      2029MiB |
+-----------------------------------------------------------------------------+
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls
=2.0.1  cut1.mp4  cut2.mp4  cut3.mp4  cut4.mp4  detectron2  out.mkv  trial.py  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ nvidia-smi
Mon Oct 19 01:42:25 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   54C    P0   159W / 250W |   6224MiB / 16280MiB |     91%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     15936      C   python                                      1867MiB |
|    0     15940      C   python                                      1499MiB |
|    0     15941      C   python                                      1499MiB |
|    0     15943      C   python                                      1349MiB |
+-----------------------------------------------------------------------------+
amarkr@voyant-algoithm-gpu:/home/jupyter$ nvidia-smi
Mon Oct 19 01:45:50 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   45C    P0    29W / 250W |      0MiB / 16280MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ nvidia-smi
Mon Oct 19 01:53:59 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   46C    P0   154W / 250W |   5628MiB / 16280MiB |    100%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     18511      C   python                                      1349MiB |
|    0     18515      C   python                                      1421MiB |
|    0     18517      C   python                                      1499MiB |
|    0     18518      C   python                                      1349MiB |
+-----------------------------------------------------------------------------+
amarkr@voyant-algoithm-gpu:/home/jupyter$ nvidia-smi
Mon Oct 19 01:54:07 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   48C    P0   153W / 250W |   5628MiB / 16280MiB |     40%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     18511      C   python                                      1349MiB |
|    0     18515      C   python                                      1421MiB |
|    0     18517      C   python                                      1499MiB |
|    0     18518      C   python                                      1349MiB |
+-----------------------------------------------------------------------------+
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ nvidia-smi
Mon Oct 19 02:44:15 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   58C    P0   185W / 250W |   9444MiB / 16280MiB |    100%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     28304      C   python                                      1691MiB |
|    0     28306      C   python                                      1585MiB |
|    0     28308      C   python                                      1421MiB |
|    0     28311      C   python                                      1661MiB |
|    0     28314      C   python                                      1727MiB |
|    0     28315      C   python                                      1349MiB |
+-----------------------------------------------------------------------------+
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ sudo vi trial.py 
amarkr@voyant-algoithm-gpu:/home/jupyter$ python
Python 3.7.8 | packaged by conda-forge | (default, Jul 31 2020, 02:25:08) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import moviepy
>>> 
amarkr@voyant-algoithm-gpu:/home/jupyter$ ls
=2.0.1  cut1.mp4  cut2.mp4  cut3.mp4  detectron2  my_concatenation.mp4  out1.mkv  out2.mkv  out3.mkv  output.mkv  trial.py  tutorials  video.mp4
amarkr@voyant-algoithm-gpu:/home/jupyter$ cd 
amarkr@voyant-algoithm-gpu:~$ ls
=0.0.7  =2.0.1  cut1.mp4  cut2.mp4  video.mp4
amarkr@voyant-algoithm-gpu:~$ cd -
/home/jupyter
amarkr@voyant-algoithm-gpu:/home/jupyter$ cd detectron2/demo/
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ ;s
-bash: syntax error near unexpected token `;'
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ ls
colormap.py  custom_visualizer.py  demo_instanceseg_video.py  demo.py  __init__.py  predictor_custom.py  predictor.py  __pycache__  README.md
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ vi demo_instanceseg_video.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ sudo vi demo_instanceseg_video.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ ls
colormap.py  custom_visualizer.py  demo_instanceseg_video.py  demo.py  __init__.py  predictor_custom.py  predictor.py  __pycache__  README.md
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ sudo vi custom_visualizer.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ sudo vi custom_visualizer.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ sudo vi custom_visualizer.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ vi demo_instanceseg_video.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ vi predictor_custom.py 
amarkr@voyant-algoithm-gpu:/home/jupyter/detectron2/demo$ sudo -i
(base) root@voyant-algoithm-gpu:~# ls
(base) root@voyant-algoithm-gpu:~# cd /home/jupyter/detectron2/demo/
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# ls
colormap.py  custom_visualizer.py  demo_instanceseg_video.py  demo.py  __init__.py  predictor_custom.py  predictor.py  __pycache__  README.md
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi custom_visualizer.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi predictor_custom.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# nvidia-smi
Mon Oct 19 07:23:21 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   56C    P0    45W / 250W |   1721MiB / 16280MiB |     42%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      2814      C   python                                      1711MiB |
+-----------------------------------------------------------------------------+
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# 
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# nvidia-smi
Mon Oct 19 08:14:59 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.01    Driver Version: 418.87.01    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   40C    P0    28W / 250W |      0MiB / 16280MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# client_loop: send disconnect: Broken pipe
ERROR: (gcloud.compute.ssh) [/usr/bin/ssh] exited with return code [255].
amarkr@Amars-MacBook-Pro ~ % gcloud compute ssh voyant-algoithm-gpu --zone us-east1-c -- -L 8080:localhost:8080
======================================
Welcome to the Google Deep Learning VM
======================================

Version: pytorch-gpu.1-4.m56
Based on: Debian GNU/Linux 9.13 (stretch) (GNU/Linux 4.9.0-13-amd64 x86_64\n)

Resources:
 * Google Deep Learning Platform StackOverflow: https://stackoverflow.com/questions/tagged/google-dl-platform
 * Google Cloud Documentation: https://cloud.google.com/deep-learning-vm
 * Google Group: https://groups.google.com/forum/#!forum/google-dl-platform

To reinstall Nvidia driver (if needed) run:
sudo /opt/deeplearning/install-driver.sh
Linux voyant-algoithm-gpu 4.9.0-13-amd64 #1 SMP Debian 4.9.228-1 (2020-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
amarkr@voyant-algoithm-gpu:~$ sudo -i
(base) root@voyant-algoithm-gpu:~# ls
(base) root@voyant-algoithm-gpu:~# cd /home/jupyter/
(base) root@voyant-algoithm-gpu:/home/jupyter# ls
=2.0.1	cut1.mp4  cut2.mp4  cut3.mp4  detectron2  out1.mkv  out2.mkv  out3.mkv	output.mkv  output_video.mp4  result.csv  segmented_video2.mp4	trial.py  tutorials  video.mp4
(base) root@voyant-algoithm-gpu:/home/jupyter# cd detectron2/
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2# ls
configs  datasets  demo  detectron2  dev  docker  docs	GETTING_STARTED.md  INSTALL.md	LICENSE  MODEL_ZOO.md  projects  README.md  setup.cfg  setup.py  tests	tools
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2# cd demo/
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# ls
colormap.py  custom_visualizer.py  demo_instanceseg_video.py  demo.py  __init__.py  predictor_custom.py  predictor.py  __pycache__  README.md
(base) root@voyant-algoithm-gpu:/home/jupyter/detectron2/demo# vi demo_instanceseg_video.py 

        print("frames per sec:", frames_per_second)

        if args.output:
            if os.path.isdir(args.output):
                output_fname = os.path.join(args.output, basename)
                output_fname = os.path.splitext(output_fname)[0] + ".mkv"
            else:
                output_fname = args.output
            assert not os.path.isfile(output_fname), output_fname
            output_file = cv2.VideoWriter(
                filename=output_fname,
                # some installation of opencv may not support x264 (due to its license),
                # you can try other format (e.g. MPEG)
                fourcc=cv2.VideoWriter_fourcc(*"x264"),
                fps=float(frames_per_second),
                frameSize=(width, height),
                isColor=True,
            )
        assert os.path.isfile(args.video_input)
        files = open('result.csv', 'w')
        writer = csv.writer(files)
        writer.writerow(["Frame number","Attribute","Values"])
        i=0
        for vis_frame,prediction in tqdm.tqdm(demo.run_on_video(video), total=num_frames):
            dnary = prediction.__dict__
            new_dnary = dnary['_fields']
            j=0
            for key,value in new_dnary.items():
                if j==0:
                    line = [i,key,value]
                    j=1
                else:
                    line = ['',key,value]
                writer.writerow(line)
            i=i+1
            #print('keys:',dnary.keys())
            #print('prediction:',dnary['_fields'])
            #print(type(dnary['_fields']))
            #print(dnary['_fields'].keys())
            #json.dump(prediction.__dict__,files)
            if args.output:
                output_file.write(vis_frame)
            else:
                cv2.namedWindow(basename, cv2.WINDOW_NORMAL)
                cv2.imshow(basename, vis_frame)
                if cv2.waitKey(1) == 27:
                    break  # esc to quit
        video.release()
        if args.output:
            output_file.release()
            files.close()
        else:
            cv2.destroyAllWindows()                                                                                                                                                  174,49        Bot
