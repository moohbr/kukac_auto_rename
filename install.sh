printf "Auto-Rename in Pyhton by GitHub@moohbr: Installer\n\n"

if [ $(id -u) -ne 0 ]; then
	printf "Script must be run as root. Try 'sudo ./install.sh'\n"
	exit 1
fi

git clone github

printf "Done!\n"