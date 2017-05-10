from colorama import Fore, Back, Style
var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"
s_input = "am" #input("Enter string : ")
g_input = "S=AB , A=aA|a , B=bBC|b , C=c" #input("Enter Grammar in this format ((S=AB , A=aA|a , B=bB|b)) (S =>Start): \n")
print()
print(Fore.BLUE + "Checking",end="")
for i in range(20):
	print(".",end="")
print(Style.RESET_ALL + "\n")


grammar = {}
for i in range(0,len(g_input)):

	if g_input[i] == "=" :
		temp_g = False
		j = i
		while temp_g == False:
			j+=1
			try :
				if g_input[j] == " ":
					temp_g = True
			except Exception :
				temp_g = True
		temp_g = False
		k = i
		while temp_g == False:
			k+=1
			try :
				if g_input[k] == "|":
					temp_g = True
			except Exception :
				temp_g = True
		if i==1:
			grammar[g_input[i-1]] = (g_input[i+1:j] ,)
		else : 
			grammar[g_input[i-1]] = (g_input[i+1:k] , g_input[k+1:j])


print("Grammar =" ,grammar)
#putting grammar in a dict 

prefix = ["&"]
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

'''def alpha_check(g):
	for i in alphabet:
		if i == g:
			return True
	else : 
		return False'''


#Grammar = {'C': ('c', ''), 'A': ('aA', 'a'), 'S': ('AB',), 'B': ('bBC', 'b')}
#Prefixes = ['&', 'a', 'ab', 'b']

def parser(g):
	queue = ["S"]
	temp = False
	while temp == False:
		try : 
			t_root_var = queue[0]
			t_root_var = queue.pop(0)
		except Exception:
			break
		for p in prefix :
			if (p == t_root_var[:(var_check(t_root_var))[1]] ) or ((var_check(t_root_var))[1] == 0):
				#print(t_root_var)
				#print(t_root_var[:(var_check(t_root_var))[1]])
				for child in g[t_root_var[var_check(t_root_var)[1]:var_check(t_root_var)[1]+1]]:
					print(child)
					v_c_0 = var_check(t_root_var)[0]
					v_c_1 = var_check(t_root_var)[1]
					tmp = v_c_1+1
					if v_c_0 == True :
						if (v_c_1 == 0 ) and (var_check(t_root_var[tmp:])[1] == 0):
							queue.append(child)
						elif (v_c_1 == 0 ) and (var_check(t_root_var[tmp:])[1] > 0):
							queue.append(child+ t_root_var[tmp:])
						elif (v_c_1 != 0 ) and (var_check(t_root_var[tmp:])[1] == 0):
							queue.append(t_root_var[:tmp] + child)
						elif (v_c_1 != 0 ) and (var_check(t_root_var[tmp:])[1] > 0):
							queue.append(t_root_var[:tmp] + child + t_root_var[tmp:])
					else :
						temp = True
			else :
				temp = False
	return temp

if parser(grammar) == True:
	print()
	print("+The Grammar contains string.\n")
else :
	print()
	print("-The Grammar Don't contain string.\n")
