# puffercloud

Relevant Files
1) abr.py - The main program/script to bring up and start up machines
2) commands_b.txt - The list of commands that need to be run on a machine that has been brought up
3) exp.html - The html file of cloudLab page: can be skipped if selenium is used
4) private key file

Initial Setup
1) Clone this repository 
2) Create a public/private key combo with PuTTYgen or some other method and save them
3) Go To the follwing CloudLab URL and add the public key: https://www.cloudlab.us/ssh-keys.php - This will ensure that the next time you bring up machines on CloudLab, you can SSH into them using your private key
4) Go to the following URL: https://www.cloudlab.us/user-dashboard.php
5) Go to Experiments -> Start Experiment 
6) Click "change profile" and change it to "geniscript" then click "Select Profile" then click "Next". If there is some other profile you would like to use instead, select it at this stage
7) Enter the number of machines you want to bring up and press "Next"
8) Name the experiment, and select a cluster with available resources
9) Schedule the experiment to begin (Only happens every hour)
10) Wait for the experiment to begin
11) Go to the following URL: https://www.cloudlab.us/user-dashboard.php
12) Click on the name of the experiment you started, and copy the URL for that webpage to be used in the next step 
13) Complete the "Setup - abr.py" section
14) Run "abr.py"

Setup - abr.py
1) Go to main()
2) Fill in the following fields at the top of the main function:

chrome_driver_path: The path to the chrome driver for selenium  
cloud_user: Username for cloudLab  
cloud_pass = Password for cloudLab  
link = Link to the webpage with list of machine IPs - This step can be automated in the future if a naming convention is established  
html_file = If you do not want to use selenium, rename this file to whatever your html file name is. If you want to use selenium, leave it as "exp.html"  
priv_key_file = The path to the private key for ssh connection  
ssh_username = The ssh username  

After setting up the program, to run the program, simply run abr.py  

Modification - Using different Disk Images
While using puffer, you may want to use different disk images. For example, you might want to change the video files that are being played by Puffer. Note that for files to be copied in a disk image, the files need to be in a root directory such as /opt. The files under /users/<username> will not be copied. To facilitate this, complete the following procedure:
1) Go to the experiment page for the experiment you want to take a disk image of
2) Click on "Experiment expires: ...." at the top of the screen 
3) Click "Create Disk Image"
4) Select a Node, name, and description then press "continue"
5) Wait for the disk image to be created
6) Got to the following URL https://www.cloudlab.us/list-images.php
7) To the right of the relevant disk image, click on and copy the URN
8) Go to https://www.cloudlab.us/user-dashboard.php#projectprofiles
9) To the right of "geniscript" click "edit this profile"
10) Click "Edit Code"
11) On line 33, change the existing disk image URN for the new disk image URN
12) Accept and Save everything

Modification - Running different commands 
  
  
  
  
  
  
