#!/usr/bin/perl

##
## Reverse single command line argument with perl
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

use strict;
use warnings;

my $string;

if (@ARGV != 0) {
  $string = shift;
} else {
  $string = "";
}

$string = reverse $string;

print "$string\n";
