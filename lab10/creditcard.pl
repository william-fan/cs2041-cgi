#!/usr/bin/perl -w
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)

foreach $arg (@ARGV) {
    $temp = $arg;
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
            print("$arg is valid\n");
        } else {
            print("$arg is invalid\n");
        }
    } else {
        print("$arg is invalid - does not contain exactly 16 digits\n");
    }

}