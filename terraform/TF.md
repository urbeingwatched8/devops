Best practices:

In the beginning of this lab, VirtualBox is needed (https://www.virtualbox.org/wiki/Downloads):
In my OS, it is recommended to download the suitable version as the exe file from VirtualBox website

The work on Virtualbox:
At first I tried applying terraform-only solutions (specified in files old_main.tf, old_versions.tf and old_outputs.tf). Sadly, I didn't succeed, but after being allowed to use Vagrant, I tried going with it as well.

The Vagrant process:
1. Install Vagrant (using the suitable version from their website - https://www.vagrantup.com/downloads)
2. In the newly created 'vagrant' folder, create Vagrantfile by doing 'vagrant init ubuntu/trusty64' via command line (before that, please disable the antivirus)
3. Run 'vagrant up' to create a VM
Result: VM named vagrant_default_1630299074417_649 has been created, it is now visible in the VirtualBox app
   
The AWS process:
1.
2.
3.
