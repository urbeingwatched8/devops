Best practices:

Hard-coded credentials shouldn't be committed to github or published online in any ways.
Instead, credentials can be exported via command line:  'export AWS_ACCESS_KEY_ID', then = and the key id, same with aws secret access key.

It is recommended to use version control, to integrate TF with configuration management, to restrict non-terraform access. 

More can be found here - https://www.terraform.io/docs/cloud/guides/recommended-practices/part3.html

In the beginning of this lab, VirtualBox is needed (https://www.virtualbox.org/wiki/Downloads):
In my OS, it is recommended to download the suitable version as the exe file from VirtualBox website

The work on Virtualbox:
At first I tried applying terraform-only solutions (specified in files old_main.tf, old_versions.tf and old_outputs.tf). Sadly, I didn't succeed, but after being allowed to use Vagrant, I tried going with it as well.

The Vagrant process:
1. Install Vagrant (using the suitable version from their website - https://www.vagrantup.com/downloads)
   
2. In the newly created 'vagrant' folder, create Vagrantfile by doing 'vagrant init ubuntu/trusty64' via command line (before that, please disable the antivirus)
   
3. Run 'vagrant up' to create a VM, run 'vagrant destroy' to destroy it

Result: VM named vagrant_default_1630299074417_649 has been created, it is now visible in the VirtualBox app
   
The AWS process:

1. Make sure that everything is fine with AWS, create secret id and secret key, find out the number of needed AMI
   
2. Create main.tf file using needed AMI and example from documentation: https://learn.hashicorp.com/tutorials/terraform/aws-variables
   
3. Export secret id and secret key via command line, NOT hardcode it

4. To create the VM: 'terraform fmt', 'terraform validate', 'terraform plan', 'terraform apply' 

A new VM could be seen on AWS website in the specified region: new-vm i-092092d41ebad5b85

5. Destroy the VM via 'terraform destroy'