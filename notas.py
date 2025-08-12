
#  Elabore um programa em Python que leia as duas notas de prova (P1 e P2) e 
# duas notas de trabalho (T1 e T2) e posteriormente exiba a mensagem ‘Aprovado’ 
# ou ‘Não aprovado’ dependendo dos valores obtidos, conforme as regras de cálculo definidas a seguir:
#  Média de provas: MP = (P1 + P2)/2
#  Média de trabalhos: MT = (T1 + T2)/2
#  Média final: MF = 0,6MP + 0,4MTSe MF ≥ 6,0 → aprovado
#  Se MF < 6,0 → não aprovado
#  Usar funções
#  Situação
MP = float(input("digite a nota da Média de provas:"))
MT = float(input("digite a nota da Média de trabalhos:"))
MF = (MP+MT)/2
print(f"media final: {MF:.1f}")
if MF <=6:
 print ("aprovado")
else:
 print("reprovado")
 