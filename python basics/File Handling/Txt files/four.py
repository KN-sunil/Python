#w-write mode writes the data if data is there means it overrides,if file not exists it creates the file

fp=open("emp.txt","w")

fp.write("hello everyone welcome to prostack academy")
fp.write(    "learning python ")
fp.close()
