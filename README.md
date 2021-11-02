# puffercloud

Relevant Files
1) abr.py - The main program/script to bring up and start up machines
2) commands_b.txt - The list of commands that need to be run on a machine that has been brought up
3) exp.html - The html file of cloudLab page: can be skipped if selenium is used
4) private key file

Setup - abr.py
1) Go to main()
2) Install the time, selenium, and paramiko libraries for Python
3) Fill in the following fields at the top of the main function:

chrome_driver_path: The path to the chrome driver for selenium
cloud_user: Username for cloudLab
cloud_pass = Password for cloudLab
link = Link to the webpage with list of machine IPs - This step can be automated in the future if a naming convention is established
html_file = If you do not want to use selenium, rename this file to whatever your html file name is. If you want to use selenium, leave it as "exp.html"
priv_key_file = The path to the private key for ssh connection
ssh_username = The ssh username

After setting up the program, to run the program, simply run abr.py
