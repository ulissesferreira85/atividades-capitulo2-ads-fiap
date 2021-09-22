segunda = int(input("Informe quantos votos teve a SEGUNDA-FEIRA: "))
terca = int(input("Informe quantos votos teve a TERÇA-FEIRA: "))
quarta = int(input("Informe quantos votos teve a QUARTA-FEIRA: "))
quinta = int(input("Informe quantos votos teve a QUINTA-FEIRA: "))
sexta = int(input("Informe quantos votos teve a SEXTA-FEIRA: "))

if segunda>terca>quarta>quinta>sexta:
    print(f"Segunda-feira {segunda} voto(s), terça-feira {terca} voto(s), quarta-feira {quarta} voto(s), quinta-feira {quinta} voto(s) e sexta-feira {sexta} voto(s)")
    print("Segunda-feira foi escolhida!")
elif terca>segunda>quarta>quinta>sexta:
    print(f"Segunda-feira {segunda} voto(s), terça-feira {terca} voto(s), quarta-feira {quarta} voto(s), quinta-feira {quinta} voto(s) e sexta-feira {sexta} voto(s)")
    print("Terça-feira foi escolhida!")
elif quarta>segunda>terca>quinta>sexta:
    print(f"Segunda-feira {segunda} voto(s), terça-feira {terca} voto(s), quarta-feira {quarta} voto(s), quinta-feira {quinta} voto(s) e sexta-feira {sexta} voto(s)")
    print("Quarta-feira foi escolhida!")
elif quinta>segunda>terca>quarta>sexta:
    print(f"Segunda-feira {segunda} voto(s), terça-feira {terca} voto(s), quarta-feira {quarta} voto(s), quinta-feira {quinta} voto(s) e sexta-feira {sexta} voto(s)")
    print("Quinta-feira foi escolhida!")
elif sexta>segunda>terca>quarta>quinta:
    print(f"Segunda-feira {segunda} voto(s), terça-feira {terca} voto(s), quarta-feira {quarta} voto(s), quinta-feira {quinta} voto(s) e sexta-feira {sexta} voto(s)")
    print("Sexta-feira foi escolhida!")
else:
    print(f"Segunda-feira {segunda} voto(s), terça-feira {terca} voto(s), quarta-feira {quarta} voto(s), quinta-feira {quinta} voto(s) e sexta-feira {sexta} voto(s)")
    print("Houve empate!")