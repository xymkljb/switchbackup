#!/usr/bin/python
#This is a switch logfile export test
import pexpect,os,re
ipadd = ''
loginname = ''
passwd = ''
su = ''
cmd = 'telnet ' + ipadd
if __name__ == '__main__':
	main = pexpect.spawn(cmd)
	index = main.expect(['[Uu]sername:',pexpect.EOF,pexpect.TIMEOUT])
	if index == 0 :
		main.sendline(loginname)
		main.expect('[Pp]assword:')
		main.sendline(passwd)
		main.expect('>')
		main.sendline('su 15')
		main.expect('[Pp]assword:')
		main.sendline(su)	
		main.expect('>')
		main.sendline('sys')
		main.expect(r']')
		main.sendline('disp cu')
		f = file('config','w')
		p = re.compile(r'\x1b\[42D\s+\x1b\[42D\s*')
		while 1 :
			index = main.expect(['-* [Mm]ore -*',r']'])
			if index == 0 :
				text = re.sub(p,'',main.before)
				print text
				f.write(text)
				main.sendline(' ')
			else :
				f.close()
				break	
	else :
		print 'telnet login failed,due to TIMEOUT or EOF'
		main.close(force=True)


