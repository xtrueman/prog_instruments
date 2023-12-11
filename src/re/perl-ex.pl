#!/usr/bin/perl -wT

use LWP::Simple;
$_=get "http://www.astronomynow.com";
push(@res, "http://$2")
   while m{SRC\s*=\s*(["'])http://(.*?)\1\s*(.*?)>}igs

