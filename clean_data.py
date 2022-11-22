f = open('train.csv', 'r')
save_f = open('clean_train.csv', 'w')

for line in f.readlines():
	print(line.replace(';',','))
	save_f.write(line.replace(';',','))

save_f.close()