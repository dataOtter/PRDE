#!/bin/csh -f

set TARGET=`ifconfig | grep 'inet addr' | grep 'Mask:255.255' | sed 's/ *//' | sed -e 's/inet addr://' | sed -e 's/ .*//'`

echo "Assuming local IP is $TARGET"

echo "Making a new /etc/mysql/mysql.conf.d/mysqld.cnf"
cat /etc/mysql/mysql.conf.d/mysqld.cnf.TEMPLATE | sed -e "s/IP_ADDRESS/$TARGET/g" > /etc/mysql/mysql.conf.d/mysqld.cnf
echo "Restarting mysqld: systemctl restart mysql"
systemctl restart mysql

echo "Making a new /etc/nginx/sites-available/testproject"
cat /etc/nginx/sites-available/testproject.TEMPLATE | sed -e "s/IP_ADDRESS/$TARGET/g" > /etc/nginx/sites-available/testproject

echo "Making a new /home/user/PRDE/testproject/constants.py"
cat /home/user/PRDE/testproject/constants.TEMPLATE.py | sed -e "s/IP_ADDRESS/$TARGET/g" > /home/user/PRDE/testproject/constants.py
chown user:user /home/user/PRDE/testproject/constants.py

echo "Restarting testproject: systemctl restart testproject"
systemctl restart testproject
sleep 5
echo "Restarting nginx: systemctl restart nginx"
systemctl restart nginx


