import os
import subprocess

with open('/tmp/output.txt',"w") as f:
    for root,dirs,files in os.walk(r'/etc/kubernetes/pki/'):
        for file in files:
            if "crt" in file:
                cmd = "echo " + file + ": " + " && " + " openssl x509 -dates -noout -in /etc/kubernetes/pki/" + file
                print(cmd)
                temp = subprocess.run(cmd,shell=True,stdout=f)