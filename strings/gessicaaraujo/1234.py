while True:
  try:
    entrada = input()
    primeiro = -1
    mudanca = 1
    final = []
    for i in entrada:
      if i == ' ':
        final.append(i)
      elif primeiro == -1:
        primeiro = 1
        final.append(i.upper())
      elif primeiro == 1:
        primeiro = 0
        final.append(i.lower())
      else:
        if mudanca == 0:
          final.append(i.lower())
          mudanca = 1
        else:
          final.append(i.upper())
          mudanca = 0
    print(''.join(final))
  except:
    break