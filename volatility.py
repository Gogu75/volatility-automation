#!/usr/bin/python3
import sys
import os
import time

print("###Volatility Script###")

#get image name
os.system("volatility imageinfo -f " + sys.argv[1]) 


print("Entrez l'image du profil : ")
profil = input()

#profil = "Win2003SP0x86"

#list of all volatility commands
liste = ["atoms", "atomscan", "auditpol", "bioskbd", "cachedump", "callacks", "clipboard", "cmdline", "cmdscan", "netscan","dlllist", "driverirp", "drivermodule", "driverscan", "envars", "eventhooks", "filescan", "gahti", "gditimers", "gdt", "getservicesids", "getsids", "handles", "hashdump", "hibinfo", "hivelist", "idt", "iehistory", "joblinks", "kdbgscan", "kpcrscan", "ldrmodules", "lsadump", "machoinfo", "malfind", "mbrparser", "messagehooks", "mftparser", "modscan", "modules", "mutantscan", "objtypescan", "privs", "pslist", "psscan", "pstree", "psxview", "sessions", "shellbags", "shimcache", "sockets", "ssdt", "strings", "svcscan", "symlinkscan", "thrdscan", "threads", "timeliner", "timers", "unloadedmodules", "userassist", "userhandles", "vadinfo", "vadtree", "vadwalk", "windows", "wndscan"]

#loop on all commands and redirect the output to a text file
for i in liste:
	print("[+]",i,"Dump")
	print("Attendez")
	os.system("volatility --profile=" + str(profil) + " -f " + sys.argv[1] + " --output-file=" + i + "-dmp.txt " + i)

time.sleep(5)