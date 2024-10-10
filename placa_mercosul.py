def valida_placa_mercosul(placa):
    estado = 'q0'
    placa = placa.upper()


    # Verifica se a placa tem exatamente 7 caracteres
    if len(placa) != 7:
        return "Placa inválida"

    for i in range(len(placa)):
        char = placa[i]

        if estado == 'q0' or estado == 'q1' or estado == 'q2':
            if char.isalpha():
                estado = f'q{i+1}'
            else:
                return "Placa inválida"

        elif estado == 'q3':
            if char.isdigit():
                estado = 'q4'
            else:
                return "Placa inválida"


        elif estado == 'q4':
            if char.isalpha():
                estado = 'q5'
            else:
                return "Placa inválida"


        elif estado == 'q5' or estado == 'q6':
            if char.isdigit():
                estado = f'q{i+1}'
            else:
                return "Placa inválida"


    if estado == 'q7':
        return "Placa válida"
    else:
        return "Placa inválida"


print(valida_placa_mercosul("ABC1D23"))  # Placa válida
print(valida_placa_mercosul("AB123CD"))  # Placa inválida

