pip2 install sys
pip2 install mechanize
pip2 install cookielib
pip2 install random
pip2 install --upgrade pip
sh logo.sh
read -p Enter-password: pass
echo "$pass" >passwords.txt
python2 guard.py