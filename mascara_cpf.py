def mascara_cpf(cpf):
    estado = 'q0'
    formattedCPF = ''
    cpf = str(cpf)


    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return "CPF inválido"

    for i in range(len(cpf)):
        if not cpf[i].isdigit():
            return "CPF inválido"

        if estado in ['q0', 'q1', 'q2', 'q9', 'q10']:
            formattedCPF += 'x'
        else:
            formattedCPF += cpf[i]

        if estado == 'q0':
            estado = 'q1'
        elif estado == 'q1':
            estado = 'q2'
        elif estado == 'q2':
            estado = 'q3'
        elif estado == 'q3':
            estado = 'q4'
        elif estado == 'q4':
            estado = 'q5'
        elif estado == 'q5':
            estado = 'q6'
        elif estado == 'q6':
            estado = 'q7'
        elif estado == 'q7':
            estado = 'q8'
        elif estado == 'q8':
            estado = 'q9'
        elif estado == 'q9':
            estado = 'q10'
    print(cpf)
    return f'{formattedCPF[:3]}.{formattedCPF[3:6]}.{formattedCPF[6:9]}-{formattedCPF[9:]}'

print(mascara_cpf('12144088595'))

