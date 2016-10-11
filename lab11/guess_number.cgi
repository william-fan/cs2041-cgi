#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations

$max_number_to_guess = 99;

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Guess A Number</title>
    <link href="guess_number.css" rel="stylesheet">
</head>
<body>
<div class="guess_number_heading">
    Guess Number
</div>
eof

warningsToBrowser(1);

$number_to_guess = param('number_to_guess');
$guess = param('guess');

$game_over = 0;

if (defined $number_to_guess and defined $guess) {
    $guess =~ s/\D//g;
    $number_to_guess =~ s/\D//g;
    if ($guess == $number_to_guess) {
        print "<div class=\"guess_number_text\">You guessed right, it was $number_to_guess.</div>\n";
        $game_over = 1;
    } elsif ($guess < $number_to_guess) {
        print "<div class=\"guess_number_text\">Its higher than $guess.</div>\n";
    } else {
        print "<div class=\"guess_number_text\">Its lower than $guess.</div>\n";
    }
} else {
    $number_to_guess = 1 + int(rand $max_number_to_guess);
    print "<div class=\"guess_number_text\">I've  thought of number 0..$max_number_to_guess</div>\n";
}

if ($game_over) {
print <<eof;

    <form method="POST" action="">
        <div class="guess_number_input">
        <input type="submit" value="Play Again">
        </div>
    </form>
</div>
eof
} else {
print <<eof;

    <form method="POST" action="">
        <div class="guess_number_input">
        <input type="textfield" style="width:100%" name="guess">
        <input type="hidden" name="number_to_guess" value="$number_to_guess">
        </div>
    </form>

eof
}

print <<eof;
</body>
</html>
eof
