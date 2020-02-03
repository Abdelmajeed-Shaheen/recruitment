def main():
	skills = ["Python","C++","Javascript","HTML","CSS","Asp.Net","Java"]
	cv = {'name':'','age':'','expe':'','skills':[]}

	name = input("What's your name?")
	cv['name'] = name
	age = input("How old are you?")
	cv['age'] = age
	expe = input("How many years of experience do you have?")
	cv['expe'] = expe

	num = 1
	for skill in skills:
		print(str(num)+". "+skill)
		num = num+1
	firstskill = input("Choose a skill from above by entering its number:")
	cv['skills'].append(skills[int(firstskill)-1])
	secskill = input("Choose another skill from above by entering its number:")
	cv['skills'].append(skills[int(secskill)-1])

	if (int(cv['age'])>25)and(int(cv['age'])<40)and(int(cv['expe'])>5)and(skills[6] in cv['skills']):
		print ("You have been accepted,"+ cv['name'])
	else:
		print ("You have been rejected,"+ cv['name'])





if __name__ == '__main__':
	main()
