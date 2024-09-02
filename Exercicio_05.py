def identificar_interruptores():
    
    interruptores = {'Interruptor 1': 'desligado', 'Interruptor 2': 'desligado', 'Interruptor 3': 'desligado'}
    lampadas = {'Lâmpada 1': 'desligada', 'Lâmpada 2': 'desligada', 'Lâmpada 3': 'desligada'}
    
    
    interruptores['Interruptor 1'] = 'ligado' #liguei o Interruptor 1 
    print('-' * 40)
    print("Ligando o Interruptor 1")
    
    
    lampadas['Lâmpada 2'] = 'acesa'  # A lâmpada controlada pelo Interruptor 1 = lampada 2 acessa
    print('-' * 40)
    print("A lâmpada 2 está acesa e é controlada pelo Interruptor 1.")
    
    
    interruptores['Interruptor 1'] = 'desligado' #desligando o interruptor 1
    interruptores['Interruptor 2'] = 'ligado' #ligando o interruptor 2
    print('-' * 40)
    print("Desligando o Interruptor 1 e ligando o Interruptor 2")
    
    
    lampadas['Lâmpada 3'] = 'acesa'  # A lâmpada controlada pelo Interruptor 2 = lampada acessa 3
    print('-' * 40)
    print("A lâmpada 3 está acesa e é controlada pelo Interruptor 2.")
    
    # verificando qual o estado da que sobrou 
    for lampada, estado in lampadas.items():
        if estado == 'desligada':
            print('-' * 40)
            print(f"A lâmpada {lampada} está desligada e é controlada pelo Interruptor 3.")
            print('-' * 40)

identificar_interruptores()

'''Resumindo: testaria um interruptor e decoraria qual lampada ficou ligada, 
apagaria ele e ligaria o outro, decorando também qual ficou ligada e deduzindo 
pela lógica que a que sobrou é a do interruptor que não foi testado e ficou desligado '''


