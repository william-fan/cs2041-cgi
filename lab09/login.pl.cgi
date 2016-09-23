#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
if (-t STDOUT){
	print "username: ";
	$username = <STDIN>;
	print "password: ";
	$password = <STDIN>;
	chomp(($username, $password));
} else {
	print header, start_html('Login Page');
	warningsToBrowser(1);

	$username = param('username') || '';
	$password = param('password') || '';
}
if ($username && $password) {
    if (-d "accounts/$username"){
		if (-f "accounts/$username/password"){
			open (F, "<", "accounts/$username/password") or die "$0: can't open accounts/$username/password: $!\n";
			$line = <F>;
			chomp($line);
			if ($password eq $line){
				print "$username authenticated.";
			} else {
				print "Incorrect password!";
			}
		} else {
			print "Incorrect password!";
		}
	} else {
		print "Unknown username!";
	}
} elsif ($username && !$password) {
	print start_form, "\n";
    #print "Username:\n", textfield('username'), "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
	print hidden('username' => $username);
    print end_form, "\n";
} elsif (!$username && $password) {
	print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    #print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
	print hidden('password' => $password);
    print end_form, "\n";
	
} else {
    print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
}
if (-t STDOUT){
} else {
	print end_html;
}
exit(0);
