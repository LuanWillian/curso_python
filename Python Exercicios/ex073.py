times = ('BotaFogo','Bragantino','Gremio','Palmeiras','Flamengo','Fortaleza','Fluminense'
         'Atletico Paranaese','Camaram','São Paulo','Cuiaba','Internacional','Corrhinthias','Santos'
         'Cruzeiro','Bahia','Vasco','Goiania','Curitiba','America-MG','Chapecoence','America-RN')
print('')
print(times)
print('')
print(f'Os 5 primeiros times: {times[:5]}')
print('')
print(f'Os 4 ultimos times: {times[16:]}')
print('')
print(f'Os times em orndem alfabetica: {sorted(times)}')
print('')
print(f'Chapecoence estar na {times.index("Chapecoence")+1}ª Posiçao' )