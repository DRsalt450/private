import bcrypt 
   
password = 'ahoj' 
bytes = password.encode("utf-8")
salt = bcrypt.gensalt(12) 

