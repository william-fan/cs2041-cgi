#!/usr/bin/perl -w
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)
use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html("Credit Card Validation"), "\n";
warningsToBrowser(1);
$credit_card = param("credit_card");
if (defined $credit_card) {
    print validate($credit_card);
}
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
            print("$_[0] is valid\n");
        } else {
            print("$_[0] is invalid\n");
        }
    } else {
        print("$_[0] is invalid - does not contain exactly 16 digits\n");
    }

}