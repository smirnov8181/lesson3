with open('referat.txt', 'r', encoding='utf-8') as referat:
	content = referat.read()
	words = (len(content.split()))
	print(words)

	
	content = content.replace('.', '!')
	print(content)



with open('referat2.txt', 'w', encoding='utf-8') as f:
	#content = referat.read()
	#content = (len(content.split()))
	#print(content)
    f.write(content)