import requests
import subprocess
import os

def check_for_updates(current_version):
    try:
        # GitHub deposunda bulunan version.txt dosyasının URL'sini belirtin
        version_url = "https://raw.githubusercontent.com/vigorexd/benimveyssionphh/master/version.txt"
        response = requests.get(version_url)
        latest_version = response.text.strip()
        if latest_version != current_version:
            return True
        else:
            return False
    except Exception as e:
        print("Güncelleme kontrol edilirken bir hata oluştu:", e)
        return False

def download_update():
    try:
        # Güncellenmiş betiği GitHub deposundan indirin
        update_url = "https://raw.githubusercontent.com/vigorexd/benimveyssionphh/master/updated_script.py"
        response = requests.get(update_url)
        with open('updated_script.py', 'wb') as file:
            file.write(response.content)
        return True
    except Exception as e:
        print("Güncelleme indirilirken bir hata oluştu:", e)
        return False

def run_update():
    try:
        # Güncellenmiş betiği çalıştırın
        subprocess.call(['python', 'updated_script.py'])
        return True
    except Exception as e:
        print("Güncelleme çalıştırılırken bir hata oluştu:", e)
        return False

if __name__ == "__main__":
    current_version = "1.2"  # Uygulamanın mevcut sürümü
    if check_for_updates(current_version):
        print("Yeni bir güncelleme mevcut.")
        if download_update():
            print("Güncelleme başarıyla indirildi.")
            if run_update():
                print("Güncelleme başarıyla uygulandı.")
                os.remove('updated_script.py')  # Güncellenmiş betiği sil
            else:
                print("Güncelleme uygulanırken bir hata oluştu.")
        else:
            print("Güncelleme indirilemedi.")
    else:
        print("Güncelleme mevcut değil veya mevcut sürüm zaten en güncel sürüm.") 

asdasdasdasdsa
