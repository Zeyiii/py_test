def limitKWFunc(name,*age,city='shenzhen',job):  #name为位置参数  后面为命名关键字参数
	for x in age:
		print(x)
	print(name,city,job)
	pass

info = {'job':'programmer'}
limitKWFunc('zeyiii',1,4,5,6,7,**info)
limitKWFunc('zeyiii',1,2,job='programmer')

#参数组合  
#顺序：
#必选参数、默认参数(按顺序提供默认参数,不按顺序提供部分默认参数时，需要把参数名写上，类似于命名关键字)
#、可变参数(list)、命名关键字参数(dict)和关键字参数(dict)  
def comblineFunc(name,address,weight=65,*age,city='shenzhen',job,**kw):
	for x in age:
		print (x)
	for i in kw:
		print(i,kw[i])
	print(name,address,weight,city,job)
comblineFunc('zeyiii','shende',21,4,5,6,job='programmer',qwer='qwe',asdf='asd')
li=[1,2,3,4]
dic={'job':'programmer','qwer':'qwe','asdf':'asd'}
comblineFunc('zeyiii','shende',*li,**dic)
li2=['zeyiii','shunde',1,2,3,4]
comblineFunc(*li2,**dic)

#尾递归！！！！！！尾递归优化   尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环