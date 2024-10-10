def reconhece_numero(string):
  estado = 'q0'

  for char in string:
    if estado == 'q0':
      if char.isdigit():
        estado = 'q1'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q1':
      if char.isdigit():
        estado = 'q1'
      elif char == '.':
        estado = 'q2'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q2':
      if char.isdigit():
        estado = 'q3'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q3':
      if char.isdigit():
        estado = 'q3'
      else:
        estado = 'q_rejeita'
        break

  if estado in ['q1', 'q3']:
    return "Número válido!"
  else:
    return "Número inválido!"


#testes
print(reconhece_numero("123")) #valido (inteiro)
print(reconhece_numero("456.789")) #valido (flutuante)
print(reconhece_numero("12.34.56")) #invalido
print(reconhece_numero("abc")) #invalido
