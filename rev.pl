#!/usr/bin/perl

##
## Reverse all command line arguments
## Use perl
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

use strict;
use warnings;

my $string = "";

if (@ARGV != 0) {
  $string = shift;
  foreach my $i (1..@ARGV) {
    $string = $string . " " . shift;
  }
} else {
  $string = "";
}

$string = reverse $string;

print "$string\n";
