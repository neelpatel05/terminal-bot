python3 -c "import pexpect"
x=$?
echo $x

if [ "$x" -eq "0" ]
then
  echo "Pexpect is already installed on your computer"
else
  echo "Installing Pexpect"
  pip3 install pexpect
  echo "Pexpect Installed"
fi

python3 terminalbot.py
