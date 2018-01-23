##
## Reverse single command line argument with perl
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##


#!/usr/bin/perl
use strict;
use warnings;
my $string = shift;
$string = reverse $string;
print "$string";
