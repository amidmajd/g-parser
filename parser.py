from colorama import Fore, Back, Style
var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"
s_input = "abbc" #input("Enter string : ")
g_input = "S=AB , A=aA|a , B=bBC|b , C=c" #input("Enter Grammar in this format ((S=AB , A=aA|a , B=bB|b)) (S =>Start): \n")
print()
print(Fore.BLUE + "Checking",end="")
for i in range(20):
	print(".",end="")
print(Style.RESET_ALL + "\n")

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


print("Grammar =" ,grammar)
#putting grammar in a dict 

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
		if v_c_0 == True:
			prefix_check = False
			for p in prefix:
				if p == root[:v_c_1]:
					prefix_check = True
			if prefix_check == True:
				for c in range(0,len(g[root[v_c_1]])):
					queue.append(root[:v_c_1]+(g[root[v_c_1]])[c]+root[v_c_1+1:])
		else : #without child
			if root == s_input:
				return True # return true if equal statement was true
	return parse_check # return false if while didn't work




if parser(grammar) == True:
	print()
	print("+The Grammar contains string.\n")
else :
	print()
	print("-The Grammar Doesn't contain string.\n")
