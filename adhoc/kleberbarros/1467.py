while True:
  try:
    v = input().split()
    v = [int(i) for i in v]
    a = v[0]
    b = v[1]
    c = v[2]

    if(a == b == c):
      print("*")
    elif(a == b):
        print("C")
    elif(a == c):
        print("B")
    else:
      print("A")
  except EOFError:
    break