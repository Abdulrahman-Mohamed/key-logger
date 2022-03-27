import psutil
import os
# ppp=os.system(r'netstat -ano -p tcp |findstr /i "465"')
# # ppp=exec ("cmd /c netstat -ano -p tcp ")
# print(ppp[])

smtp_ports_list = [465, 587]
last=0
while True:
    pid = psutil.pids()
    pid.reverse()
    if True:
        last = pid[0]
        #print(pid)
        for p in pid:
            print(p)
            try:
                process = psutil.Process(p)

                #print(process)
                port_in_use = process.connections()
                #print("did that 10")
                if len(port_in_use)>=1:
                    if len(port_in_use[0][4])>=1:
                        #print(port_in_use[0][4][1])
                        target_port=port_in_use[0][4][1]
                        if target_port in smtp_ports_list:
                            #print("did that 16")
                            print("found port ",port_in_use[0][4][1])
                            process.suspend()
                            print(process)
                            try:
                                print(process.open_files())
                                if len(process.open_files())>=1:
                                    print(process.open_files()[0][0])

                                    print(f"this process {process.open_files()[0][0]} try to reach the email ports would u ike to allow it?")
                                    answer=input("press y if yes and n for no")
                                    if answer.lower() == "y":
                                        process.terminate()
                                        process.kill()
                                    elif answer.lower() == "no":
                                        process.resume()
                                    else:
                                        print("wrong choice")
                                        process.resume()
                                        break
                                #print(process.environ())
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                                pass
            except psutil.NoSuchProcess:
                print(f"there was process{p}")
                pass
                    #p.suspend()

# p.open_files()
# [popenfile(path='/home/giampaolo/monit.py', fd=3, position=0, mode='r', flags=32768),
#  popenfile(path='/var/log/monit.log', fd=4, position=235542, mode='a', flags=33793)]
# p.suspend()
# >>> p.resume()
# >>>
# >>> p.terminate()
# >>> p.kill()

# 587

# smtp.live.com	    SSL         465
# smtp.live.com       StartTLS    587
#
# smtp.office365.com  StartTLS	587
#
# smtp.mail.yahoo.com SSL         465
#
# smtp.aol.com	    StartTLS	587
#
# smtp.att.yahoo.com  SSL         465
