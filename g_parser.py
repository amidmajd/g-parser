from colorama import Fore, Back, Style
import sys

def grammar_parse(g):
	grammar = {}
	for i in range(0,len(g)):
		if g[i] == "=" :
			temp_j = False
			j = i
			while temp_j == False:
				j+=1
				try :
					if g[j] == " ":
						temp_j = True
				except Exception :
					temp_j = True
			temp_g = False
			k = i
			while temp_g == False:
				k+=1
				try :
					if g[k] == "|":
						temp_g = True
				except Exception :
					temp_g = True
			if i == 1:
				grammar[g[i-1]] = (g[i+1:j] ,'')
			else :
				grammar[g[i-1]] = (g[i+1:k] , g[k+1:j])
	grammar_check(grammar)  #checking if grammar is not right
	return grammar
	#putting grammar in a DICT

def prefixes(s):
	prefix = ['']
	for i in range(0,len(s)):
		for j in range(0,len(s)+1):
			if i<j :
				prefix.append(s[i:j])
	#creating a list that contains prefixes of stirng
	return prefix

def grammar_check(g):
	try:
		for k,v in g.items():
			if k != 'S':
				for tmp_v in v:
					assert tmp_v.isupper() != True
	except AssertionError :
		print(Fore.LIGHTRED_EX + "\n======>> Grammar Error <<======")
		sys.exit()


def var_check(g):
	var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in g:
		for j in var:
			if j == i:
				return True , g.index(j)
	else :
		return False , len(g)

def parser(g,s):
	grammar = grammar_parse(g)
	queue = ["S"]
	parse_check = False
	while parse_check == False:
		try:
			root = queue.pop(0)
		except Exception:
			return False
		#if the queue has been empty shows end of check
		v_c_0 = var_check(root)[0]
		v_c_1 = var_check(root)[1]
		if v_c_0 == True: #first step : check for variable
			prefix_check = False
			prefix = prefixes(s)
			for p in prefix:
				if p == root[:v_c_1]:
					prefix_check = True
				#second step: check if the first part befor first variable
				#of grammar is equal to one of prefixes or not
			if prefix_check == True:
				try:
					for c in range(0,len(grammar[root[v_c_1]])):
						queue.append(root[:v_c_1]+(grammar[root[v_c_1]])[c]+root[v_c_1+1:])  #placing grammar child instead of it (first left variable)
				except KeyError:
					pass
		else : #without child
			if root == s_input:
				return True
	return parse_check # return false if while didn't work



s_input = input("Enter string : ")
g_input = input("Enter Grammar in this format ((S=AB , A=aA|a , B=bB|b)) , (S as Start): \n")

print()
print(Fore.BLUE + Back.LIGHTCYAN_EX + "Checking",end="")
for i in range(20):
	print(".",end="")
print(Style.RESET_ALL + "")

if parser(g_input,s_input) == True:
	print(Fore.LIGHTGREEN_EX + "\n+The Grammar contains string.\n")
else :
	print(Fore.RED + "\n-The Grammar Doesn't contain string.\n")