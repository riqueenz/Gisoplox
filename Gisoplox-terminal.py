# -*- coding: utf-8 -*-
import os
import platform
import Auxiliares
import Oxicorte
import Plasma

sistemaOperacional=platform.system()
###########################################
def limparTela():
    if sistemaOperacional=="Windows":
        os.system('cls')
    else:
        os.system('clear')
###########################################
def formatos(processo):
    print "Processo escolhido: "+str(processo)
    print "\nFerramentas disponíveis:"
    print "1-Retângulo"
    print "2-Circulo"
    print "3-Triângulo retângulo"
    print "4-Retângulo com furo central"
    ferramenta=raw_input("\nFerramenta:")
    erros=True

    ####Mensagem de sucesso
    def mensagemSucesso(pecas, pecasFaltantes, pecasGeradas, chapaX, chapaY):
        limparTela()
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            print mensagem

        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço\n\n"
            print mensagem

    ####Gerar codigo da ferramenta escolhida
    if ferramenta=="1":
        erros=False
        #retangulo

        #Perguntar dados ao usuario
        limparTela()
        cliente=raw_input("Cliente:")
        cliente=cliente.upper()
        espi=raw_input("Espessura:")
        txd=raw_input("Tamanho X:")
        tyd=raw_input("Tamanho Y:")
        entrada=raw_input("Entrada:")
        chapaX=raw_input("Tamanho da chapa em X:")
        chapaY=raw_input("Tamanho da chapa em Y:")
        pecas=raw_input("Quantidade:")

        #Transformando espessura
        espi=espi.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')
        espessura=espi
        espessura=espessura.replace(' ', '')
        espessura=espessura.replace('m', '')

        #Trocar vírgula por ponto
        txd=txd.replace(',', '.')
        tyd=tyd.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0
        if entrada == "":
            entrada=5

        #Transformando a espessura em mm
        if espi.find("m") == -1:
            espessura=Auxiliares.PassarMilimetro(espessura)

        #Pegar os parâmetros
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)
        
        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Nome do arquivo
        nomePadrao=cliente + " " + espi + "X" + str(int(txd)) + "X" + str(int(tyd)) + "-" + str(int(pecasGeradas)) + "P"
        print nomePadrao

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo","'+str(processo)+'","Terminal"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo,Terminal\n'
        Auxiliares.escreverCSV(Leglinha) 
        
    elif ferramenta=="2":
        erros=False
        #circulo
        #Perguntar dados ao usuario
        limparTela()
        cliente=raw_input("Cliente:")
        cliente=cliente.upper()
        espi=raw_input("Espessura:")
        diam1=raw_input("Diâmetro 1:")
        diam2=raw_input("Diâmetro 2:")
        entrada=raw_input("Entrada:")
        chapaX=raw_input("Tamanho da chapa em X:")
        chapaY=raw_input("Tamanho da chapa em Y:")
        pecas=raw_input("Quantidade:")

        #Transformando espessura
        espi=espi.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')
        espessura=espi
        espessura=espessura.replace(' ', '')
        espessura=espessura.replace('m', '')

        #Trocar vírgula por ponto
        diam1=diam1.replace(',', '.')
        diam2=diam2.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if diam1 == "":
            diam1=0
        if diam2 == "":
            diam2=0
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0
        if entrada == "":
            entrada=5

        #Definir o maior diametro como diam1
        if diam2>diam1:
            maior=diam2
            menor=diam1
            diam2=maior
            diam1=menor

        #Se nao tiver furo o diametro e' u'nico
        if diam2==0:
            diam=diam1

        #Transformando a espessura em mm
        if espi.find("m") == -1:
            espessura=Auxiliares.PassarMilimetro(espessura)

        #Pegar os parâmetros
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)
        
        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte" and diam2>0:
            pecasGeradas, programa, distCorte=Oxicorte.Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma" and diam2>0:
            pecasGeradas, programa, distCorte=Plasma.Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Oxicorte" and diam2==0:
            pecasGeradas, programa, distCorte=Oxicorte.CirculoSimples(diam, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma" and diam2==0:
            pecasGeradas, programa, distCorte=Plasma.CirculoSimples(diam, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Nome do arquivo
        if diam2>0:
            nomePadrao=cliente + " " + espi + "XD" + str(int(diam1)) + "XD" + str(int(diam2)) + "-" + str(int(pecasGeradas)) + "P"
        if diam2==0:
            nomePadrao=cliente + " " + espi + "X D" + str(int(diam)) + "-" + str(int(pecasGeradas)) + "P"
        
        print nomePadrao

        #Calcular o peso em gramas
        if diam2>0:
            pesoUnitario, pesoTotal=Auxiliares.pesoAnel(espessura, diam1, diam2, pecasGeradas)
        if diam2==0:
            pesoUnitario, pesoTotal=Auxiliares.pesoCirculo(espessura, diam, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Adicionar dados ao historico
        if erros==False and diam2>0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        if erros==False and diam2==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        if diam2>0:
            ferramenta=str(diam1)+'","'+str(diam2)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
            linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'",anel,"'+str(processo)+'","Terminal"\n'
            Auxiliares.escreverCSV(linha)
            LegFerramenta='diam1,diam2,entrada,chapaX,chapaY,pecas,Kerf'
            Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo,Terminal\n'
            Auxiliares.escreverCSV(Leglinha)

        if diam2==0:
            ferramenta=str(diam1)+'","","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
            linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'",circulo,"'+str(processo)+'","Terminal"\n'
            Auxiliares.escreverCSV(linha)
            LegFerramenta='diam1,,entrada,chapaX,chapaY,pecas,Kerf'
            Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo,Terminal\n'
            Auxiliares.escreverCSV(Leglinha)

        
    elif ferramenta=="3":
        erros=False
        #"triangulo-retangulo"
        #Perguntar dados ao usuario
        limparTela()
        cliente=raw_input("Cliente:")
        cliente=cliente.upper()
        espi=raw_input("Espessura:")
        txd=raw_input("Tamanho X:")
        tyd=raw_input("Tamanho Y:")
        entrada=raw_input("Entrada:")
        chapaX=raw_input("Tamanho da chapa em X:")
        chapaY=raw_input("Tamanho da chapa em Y:")
        pecas=raw_input("Quantidade:")

        #Transformando espessura
        espi=espi.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')
        espessura=espi
        espessura=espessura.replace(' ', '')
        espessura=espessura.replace('m', '')

        #Trocar vírgula por ponto
        txd=txd.replace(',', '.')
        tyd=tyd.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0
        if entrada == "":
            entrada=5

        #Transformando a espessura em mm
        if espi.find("m") == -1:
            espessura=Auxiliares.PassarMilimetro(espessura)

        #Pegar os parâmetros
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)
        
        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Nome do arquivo
        nomePadrao=cliente + " " + espi + "X" + str(int(txd)) + "X" + str(int(tyd)) + "-" + str(int(pecasGeradas)) + "P"
        print nomePadrao

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoTrianguloRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Adicionar dados ao historico
        if erros==False:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","triangulo retangulo","'+str(processo)+'","Terminal"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo,Terminal\n'
        Auxiliares.escreverCSV(Leglinha)

    elif ferramenta=="4":
        erros=False
        ##Retângulo com furo central
        #Perguntar dados ao usuario
        limparTela()
        cliente=raw_input("Cliente:")
        cliente=cliente.upper()
        espi=raw_input("Espessura:")
        txd=raw_input("Tamanho X:")
        tyd=raw_input("Tamanho Y:")
        furo=raw_input("Furo:")
        entrada=raw_input("Entrada:")
        chapaX=raw_input("Tamanho da chapa em X:")
        chapaY=raw_input("Tamanho da chapa em Y:")
        pecas=raw_input("Quantidade:")

        #Transformando espessura
        espi=espi.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')
        espessura=espi
        espessura=espessura.replace(' ', '')
        espessura=espessura.replace('m', '')

        #Trocar vírgula por ponto
        txd=txd.replace(',', '.')
        tyd=tyd.replace(',', '.')
        furo=furo.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0
        if entrada == "":
            entrada=5

        #Transformando a espessura em mm
        if espi.find("m") == -1:
            espessura=Auxiliares.PassarMilimetro(espessura)

        #Pegar os parâmetros
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)
        
        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Nome do arquivo
        nomePadrao=cliente + " " + espi + "X" + str(int(txd)) + "X" + str(int(tyd)) + "XD" + str(int(furo)) + "-" + str(int(pecasGeradas)) + "P"
        print nomePadrao

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetanguloFuro(espessura, txd, tyd, furo, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(furo)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo com furo","'+str(processo)+'","Terminal"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,DiamFuro,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo,Terminal\n'
        Auxiliares.escreverCSV(Leglinha)
    else:
        #Se uma ferramenta invalida for escolhida reiniciar codigo
        limparTela()
        print 'Ferramenta "'+str(ferramenta)+'" não reconhecida!'
        print 'Por favor digite o número da ferramenta novamente\n'
        formatos(processo)

    ####Para não colocar a os avanços definir velocidades como ZERO
    icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
    if colocarVelocidadeAvanco == 0:
        avanco=0
    if colocarVelocidadeAvancoRapido == 0:
        velocidadeAvancoRapido=0

    ####Chamando a função que cria o arquivo
    def salvarPrograma(programa, salvar, avanco, velocidadeAvancoRapido, numerar):
        Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    if erros==False:
        salvar="CNC/"+str(nomePadrao)
        salvarPrograma(programa, salvar, avanco, velocidadeAvancoRapido, numerar)
        #Se a pasta padrao existir salvar nela
        if os.path.isdir(Auxiliares.Parametros()[10])==True:
            pastaPad=Auxiliares.Parametros()[10]
            salvar=pastaPad+"/"+str(nomePadrao)
            salvarPrograma(programa, salvar, avanco, velocidadeAvancoRapido, numerar)
        if os.path.isdir(Auxiliares.Parametros()[9])==True:
            pastaPad=Auxiliares.Parametros()[9]
            salvar=pastaPad+"/"+str(nomePadrao)
            salvarPrograma(programa, salvar, avanco, velocidadeAvancoRapido, numerar)
        mensagemSucesso(pecas, pecasFaltantes, pecasGeradas, chapaX, chapaY)
###########################################
def GisoploxTexto():
    print 'Gisoplox -- Linha de comando\n'
    print 'Escolha um processo de corte:'
    print '1-Oxicorte'
    print '2-Plasma\n'
    processo=raw_input("Processo:")
    processo=processo.upper()

    erro=False
    if processo=="1":
        processo="Oxicorte"
    elif processo=="2":
        processo="Plasma"
    elif processo=="O":
        processo="Oxicorte"
    elif processo=="P":
        processo="Plasma"
    elif processo=="OXICORTE":
        processo="Oxicorte"
    elif processo=="PLASMA":
        processo="Plasma"
    elif processo=="OXI":
        processo="Oxicorte"
    elif processo=="PLAS":
        processo="Plasma"
    elif processo=="PLA":
        processo="Plasma"
    else:
        limparTela()
        print 'Processo "'+str(processo)+'" não reconhecido!'
        print 'Por favor digite o número do processo novamente\n'
        GisoploxTexto()
        erro=True

    if erro==False:
        limparTela()
        formatos(processo)

############################## Iniciar o programa ###################################
limparTela()
GisoploxTexto()
