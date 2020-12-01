#!/usr/bin/perl

$wordfile = $ARGV[0];

%cmu = {};
open CMU, "cmudict.txt" or die ("Can't open cmudict.txt");
while (<CMU>) {
    chomp;
    /^(.*?)\s+(.*?)$/;
    $word = $1;
    $pron = $2;
    $cmu{$word} = $pron;
}
close CMU;


open(DIC,">$wordfile.dic") or die("can't open $senfile.dic for output!\n");
%done = {};
open SENT, $wordfile or die ("Can't open $wordfile");
while (<SENT>) {
    chomp;
    @f = split(/\s+/);
    for ($i=0; $i<=$#f; $i++) {
	if ($f[$i] !~ /\</) {
	    if (!exists $done{$f[$i]}) {
		print DIC $f[$i]."\t".$cmu{$f[$i]}."\n";
	    }
	}
    }
}
close SENT;
close DIC;

if ($VERBOSE>0) { print STDERR "Lexicon complete at ",scalar localtime(),"\n"; }

