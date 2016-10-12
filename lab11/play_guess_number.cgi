#!/usr/bin/perl -w
use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>A Guessing Game Player</title>
</head>
<body>
eof
warningsToBrowser(1);
$guess = param("guess") || 50;
$low_limit = param("low_limit") || 1;
$high_limit = param("high_limit") || 100;
if (defined param("higher")) {
    if ($high_limit == -1) {
        $guess = 0;
    } else {
        $low_limit = $guess+1;
        $guess = int(($high_limit + $low_limit)/2);
    }
} elsif (defined param("lower")) {
    if ($high_limit == 2 || $high_limit == -1) {
        $high_limit = -1;
        $guess = 0;
    } else {
        $high_limit = $guess-1;
        $guess = int(($high_limit + $low_limit)/2);
    }
}

if (defined param("correct")) {
    print <<eof;
    <form method="POST" action="">
    I win!!!!
    <input type="submit" value="Play Again">
    </form>
    </body>
    </html>
eof
} else {
    print <<eof;
    <form method="POST" action="">
    My guess is: $guess
    <input type="submit" name="higher" value="Higher?">
    <input type="submit" name="correct" value="Correct?">
    <input type="submit" name="lower" value="Lower?">
    <input type="hidden" name="high_limit" value="$high_limit">
    <input type="hidden" name="guess" value="$guess">
    <input type="hidden" name="low_limit" value="$low_limit">
    </form>
    </body>
    </html>
eof
}
