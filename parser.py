from colorama import Fore, Back, Style
var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_input = input("Enter string : ")
g_input = input("Enter Grammar in this format ((S=AB , A=aA|a , B=bB|b)) and (S as Start): \n") 

grammar = {}
for i in range(0,len(g_input)):
	if g_input[i] == "=" :
		temp_j = False
		j = i
		while temp_j == False:
			j+=1
			try :
				if g_input[j] == " ":
					temp_j = True
			except Exception :
				temp_j = True
		temp_g = False
		k = i
		while temp_g == False:
			k+=1
			try :
				if g_input[k] == "|":
					temp_g = True
			except Exception :
				temp_g = True
		if i == 1:
			grammar[g_input[i-1]] = (g_input[i+1:j] ,'')
		else : 
			grammar[g_input[i-1]] = (g_input[i+1:k] , g_input[k+1:j])
#putting grammar in a DICT
#print("Grammar :" ,grammar)

prefix = ['']
for i in range(0,len(s_input)):
	for j in range(0,len(s_input)+1):
		if i<j :
			prefix.append(s_input[i:j])
#creating a list that contains prefixes of stirng
print("Prefixes =",prefix)

def var_check(g):
	for i in g:
		for j in var:
			if j == i:
				return True , g.index(j)
	else : 
		return False , len(g)

def parser(g):
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
			for p in prefix:
				if p == root[:v_c_1]:
					prefix_check = True
				#second step: check if the first part befor first variable 
				#of grammar is equal to one of prefixes or not
			if prefix_check == True:  
				try:
					for c in range(0,len(g[root[v_c_1]])):
						queue.append(root[:v_c_1]+(g[root[v_c_1]])[c]+root[v_c_1+1:])  #placing grammar child instead of it (first left variable)
				except KeyError:
					pass
		else : #without child
			if root == s_input:
				return True 
	return parse_check # return false if while didn't work

print(Fore.BLUE + Back.LIGHTCYAN_EX + "Checking",end="")
for i in range(20):
	print(".",end="")
print(Style.RESET_ALL + "")

if parser(grammar) == True:
	print()
	print("+The Grammar contains string.\n")
else :
	print()
	print("-The Grammar Doesn't contain string.\n")
