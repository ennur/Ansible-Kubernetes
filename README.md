# Ansible-Kubernetes

<img width="747" alt="image" src="https://user-images.githubusercontent.com/58693641/189537180-7189401c-d32e-4a5d-8f60-1e6cebfc2f61.png">

İstenen bir hipervisor kullanarak, virtual machine'ler oluşturulur.

VM'lerin içerisinde kubeadm kurulur.

## Jenkins kurulumu

```jenkins``` klasöründe bulunan yaml dosyaları, ```control machine``` içerisindeki cluster'da apply edilir.

## Scriptin yüklemmesi

Ana dizinde bulunan run.sh scripti çalıştırılır.

Bu script, ansible-playbook komutu çalıştırır. 

Ansible, ```get-crt.py``` script'ini yükler ve çalıştırır.

## Sertifikaların Alınması

Jenkins ssh ile sunucuya bağlanıp, script çıktısını alır.
