def reconhece_placa_transito(string):
  estado = 'q0'

  for char in string:
    if estado == 'q0':
      if char.isalpha():
        estado = 'q1'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q1':
      if char.isalpha():
        estado = 'q2'
      else:
        estado = 'q_rejeita'
    elif estado == 'q2':
      if char.isalpha():
        estado = 'q3'
      else:
        estado = 'q_rejeita'
    elif estado == 'q3':
      if char == '-':
        estado = 'q4'
      else:
        estado = 'q_rejeita'
    elif estado == 'q4':
      if char.isdigit():
        estado = 'q5'
      else:
        estado = 'q_rejeita'
    elif estado == 'q5':
      if char.isdigit():
        estado = 'q6'
      else:
        estado = 'q_rejeita'
    elif estado == 'q6':
      if char.isdigit():
        estado = 'q7'
      else:
        estado = 'q_rejeita'

  if estado == 'q7':
    return "Placa Válida!"
  else:
    return "Placa Inválida!"
print(reconhece_placa_transito('mnw-0209'))