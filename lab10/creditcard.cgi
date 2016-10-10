#!/usr/bin/perl -w
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)
use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html("Credit Card Validation"), "\n";
warningsToBrowser(1);
$credit_card = param("credit_card");
$credit_card =~ s/\</&lt;/g;
$credit_card =~ s/\>/&gt;/g;
$close = param("close");
$valid = 0;
print start_form, "\n";
print "<h2>Credit Card Validation</h2>\n";
if (defined $close) {
    print "Thank you for using the Credit Card Validator.\n";
} elsif (defined $credit_card) {
    $string = validate($credit_card);
    if ($valid == 1) {
        print "This page checks whether a potential credit card number satisfies the Luhn Formula.<p>\n";
        print "<b><span style=\"color: red\">$string</span></b><p>";
        print "Try again:\n", textfield('credit_card'), "\n";
        print submit(value => Validate)," ", reset(reset => Reset), " ", submit(close => Close), "\n";
    } else {
        print "This page checks whether a potential credit card number satisfies the Luhn Formula.<p>\n";
        print "$string<p>";
        print "Another card number:\n", textfield(-name=>'credit_card', -value=>'', -override=>1), "\n";
        print submit(value => Validate)," ", reset(reset => Reset), " ", submit(close => Close), "\n";
    }
} else {
    print "This page checks whether a potential credit card number satisfies the Luhn Formula.<p>\n";
    print "Enter credit card number:\n", textfield('credit_card'), "\n";
    print submit(submit => Validate)," ", reset(reset => Reset), " ", submit(close => Close), "\n";
}
print end_form, "\n";
print end_html;
exit 0;

sub validate { 
    $temp = $_[0];
    $temp =~ s/-//g;
    $total = 0;
    if ($temp =~ /[0-9]{16}/) {
        $digits = reverse $temp;
        @numbers = split //, $digits;
        for ($count = 0; $count != length $digits; $count+=2) {
            $double = $numbers[$count+1]*2;       
            if ($double > 9) {
                $double -= 9;
            }
            if ($count != length $digits) {
                $total += $double;
            }
            $total += $numbers[$count];;
        }
        if ($total % 10 == 0) {
            $valid = 0;
            return "$_[0] is valid\n";
        } else {
            $valid = 1;
            return "$_[0] is invalid\n";
        }
    } else {
        $valid = 1;
        return "$_[0] is invalid - does not contain exactly 16 digits\n";
    }
}