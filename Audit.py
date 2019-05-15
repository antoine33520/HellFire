#!/bin/python
def audit():
    import os 
    import subprocess as sp


    def audit_debian():
        print ("################################################")
        print ("################################################")
        print ("################################################")
        print (" ('-. .-.   ('-.                                       _  .-')     ('-.   ")
        print ("( OO )  / _(  OO)                                     ( \( -O )  _(  OO)  ")
        print (",--. ,--.(,------.,--.      ,--.        ,------.,-.-') ,------. (,------. ")
        print ("|  | |  | |  .---'|  |.-')  |  |.-') ('-| _.---'|  |OO)|   /`. ' |  .---' ")
        print ("|   .|  | |  |    |  | OO ) |  | OO )(OO|(_\    |  |  \|  /  | | |  |     ")
        print ("|       |(|  '--. |  |`-' | |  |`-' |/  |  '--. |  |(_/|  |_.' |(|  '--.  ")
        print ("|  .-.  | |  .--'(|  '---.'(|  '---.'\_)|  .--',|  |_.'|  .  '.' |  .--'  ")
        print ("|  | |  | |  `---.|      |  |      |   \|  |_)(_|  |   |  |\  \  |  `---. ")
        print ("`--' `--' `------'`------'  `------'    `--'    `--'   `--' '--' `------' ")
                                                                
        print ("###############################################")
        print ("Welcome to Hellfire:")
        print ("###############################################")
        print ("Script will automatically gather the required info:")
        print ("The checklist can help you in the process of hardening your system:")
        print ("Note: it has been tested for Debian Linux Distro:")
        os.system('sleep 3')
        print ("###############################################")
        print ("OK....HOSTNAME..lets move on...wait for it to finish:")
        print ("Script Starts ;)")
        os.system('START=$(date +%s)') # add fonction pour timer 
        print  (" Linux Kernel Information")
        os.system('uname -a')
        print ("###############################################")
        print  (" Current User and ID information")
        os.system('whoami')
        os.system('id')
        print ("###############################################")
        print ("Linux Distribution Information")
        os.system('lsb_release -a')
        print ("###############################################")
        print  ("List Current Logged In Users")
        os.system('w')
        print ("###############################################")
        print ("HOSTNAME uptime Information")
        os.system('uptime')
        print ("###############################################")
        print  ("Running Services")
        os.system('service --status-all |grep "+"')
        print ("###############################################")
        print  ("Active internet connections and open ports")
        os.system('netstat -natp')
        print ("###############################################")
        print  ("Check Available Space")
        os.system('df')
        print ("###############################################")
        print  ("Check Memory")
        os.system('free -h')
        print ("###############################################")
        print ("Check SSH Configuration")
        os.system('cat /etc/ssh/sshd_config')
        print ("###############################################")
        print ("###############################################")
        print ("Network Parameters")
        os.system('cat /etc/sysctl.conf')
        print ("###############################################")
        print ("Password Policies")
        os.system('cat /etc/pam.d/common-password')
        print ("###############################################")
        print (" Check your Source List file")
        os.system('cat /etc/apt/sources.list')
        print ("###############################################")
        print  ("Check for broken dependencies")
        os.system('apt-get check')
        print ("###############################################")
        print  ("MOTD banner message")
        os.system('cat /etc/motd')
        print ("###############################################")
        print ("List user names")
        os.system('cut -d: -f1 /etc/passwd')
        print ("###############################################")
        print ("###############################################")
        #print("Socket Investigation")
        #os.system('ss')
        #print ("###############################################")
        print ("#--------------------------------------------------------------------------------------------------------------")
        print ("# SSH Setup")
        print ("#--------------------------------------------------------------------------------------------------------------")
        
        port_ssh = sp.getoutput('grep -E "Port " /etc/ssh/sshd_config')

        if port_ssh == "Port 22":
            print("SHD Config: Port is set to default (22).  Recommend change to a non-standard port to make your SSH server more difficult to find/notice.  (Remember to restart SSHD with /etc/init.d/ssh restart after making changes)")
        else:
            print(port_ssh)

        ssh_listen_address = sp.getoutput('grep -E "ListenAddress ::" /etc/ssh/sshd_config')
        if ssh_listen_address == "ListenAddress ::":
            print("SSHD Config: ListenAddress is set to default (all addresses).  SSH will listen on ALL available IP addresses.  Recommend change to a single IP to reduce the number of access points.")
        else:
            print(ssh_listen_address)
        permit_root_login = sp.getoutput('grep -E PermitRootLogin /etc/ssh/sshd_config')

        if permit_root_login != "PermitRootLogin no":
            print("SSHD Config: PermitRootLogin should be set to no (prefer log in as a non-root user, then sudo/su to root)")
        else:
            print(permit_root_login)
        permit_empty_passwords = sp.getoutput('grep -E PermitEmptyPasswords /etc/ssh/sshd_config')

        if permit_empty_passwords != "PermitEmptyPasswords no":
            print("SSHD Config: PermitEmptyPasswords should be set to no (all users must use passwords/keys). ")
        else:
            print(permit_empty_passwords)

        privilege_separation = sp.getoutput('grep -E UsePrivilegeSeparation /etc/ssh/sshd_config')

        if privilege_separation != "UsePrivilegeSeparation yes" :
            print("SSHD Config: UsePrivilegeSeparation should be set to yes (to chroot most of the SSH code, unless on older RHEL). ")
        else:
            print(privilege_separation)
        sshd_protocol = sp.getoutput('grep -E Protocol /etc/ssh/sshd_config')

        if sshd_protocol != "Protocol 2"  :
            print("SSHD Config: Protocol should be set to 2 (unless older Protocol 1 is really needed).")
        else:
            print(sshd_protocol)

    
        print('END')




    Distrib = os.uname()

    print (Distrib[2])



    if  'MANJARO' in Distrib[2] :
        audit_debian()
    if 'kali' in Distrib[2]:
        audit_debian()
    if 'debian' in Distrib[2] :
        audit_debian()
    #if 'ubuntu' in Distrib[2] :
    #    audit_ubuntu()


