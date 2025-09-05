## MÉDIA DE PRODUÇÃO DE CARNE  BOVINA POR REGIÃO BRASILEIRA:

r_sul= float(input('Qual a produção anual em toneladas de carne bovina na região Sul?'))
r_centro_oeste = float(input('Qual a produção anual em toneladas de carne bovina na região Centro-oeste ?'))
r_nordeste = float(input('Qual a produção anual em toneladas de carne bovina na região nordeste?'))
r_sudeste = float(input('Qual a produção anual em toneladas de carne bovina na região Sudeste?'))
r_nnorte = float(input('Qual a produção anual em toneladas de carne bovina na região Norte?'))

med_toon = (r_sul + r_centro_oeste + r_nordeste + r_sudeste + r_nnorte)  / 5

print(f"A media anual de produção bovina eh de:{med_toon} toneladas por região brasileira")
