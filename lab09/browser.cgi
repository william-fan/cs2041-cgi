#!/bin/sh
echo Content-type: text/html
echo

host_address=`host $REMOTE_ADDR | sed 's/.* //' | sed 's/.$//'`

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>IBrowser IP, Host and User </title>
</head>
<body>
This web server is running on IP address: <b>$REMOTE_ADDR</b>
<p>
This web server is running on hostname: <b>$host_address</b>
<p>
This web server is <b>$HTTP_USER_AGENT</b>
</body>
</html>
eof
