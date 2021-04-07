#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Long;
use POSIX;
use Cwd;
my $dir = getcwd;
=head1 Parameters

    -i  [str]   Input protein chain file
    -l  [str]   Input DNA chain file
    -c  [str]   The class of complex, "SS" means "Complex with single-starnd DNA", "DD" means "Complex with duplex DNA", "MISC" means "Complex with miscellaneous DNA".
    -o  [str]   Output file(binding affinity).
=cut
my $predbaout ="../code/PreDBA.out";
my $predpy="../code/PreDBA.py";
my ($chainname,$DNAchainname,$choosevalue,$endOut);
GetOptions(
    "i:s"=>\$chainname,
    "l:s"=>\$DNAchainname,
    "c:s"=>\$choosevalue,
    "o:s"=>\$endOut
    );
print "Begin to predict!\nPlease wait, this may take several minutes...\n";
system("nohup python -u $predpy $chainname $DNAchainname $choosevalue $endOut > $predbaout 2>&1");
$|=1;
open(FILEIP, $endOut);  
while(<FILEIP>)
{       
    chomp ;  
    s/00000//ig;
    print "Prediction end!\n";
    print "Predicted value of binding affinity is $_ kcal/mol.\n";
}
close (FILEIP);
