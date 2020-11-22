while 1 :
  print ("welcom to university")
  print ("enter 'stu' for going to class student")
  print ("enter 'emp' for going to class employ")
  print ("enter 'teach' for going to class teacher")
  print ("enter 'ex' to exit")
  user_input = input(" :")
  if user_input == "ex" :
    print ("exit")
    break
elif user_input == "stu" :
    import class student
  elif user_input == "emp" :
    import class employ
  elif user_input == "teach" :
    import class teacher

  else :
    print("unknown")


lst = []
st1=student("mahsa","abdi",123,20,"dadeh")
st2=student("ali","hasani",234,18,"dadeh")
st3=student("hasan","karimi",456,19,"dadeh")
lst.append(st1.get_stu())
lst.append(st2.get_stu())
lst.append(st3.get_stu())
print(lst)
