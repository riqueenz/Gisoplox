# -*- coding: utf-8 -*-
from settings import local_data_files
import os
from datetime import date
import time


def versao():
    return "0.21.0129"


def Parametros():
    settings_file = ".gisoplox/settings.ini"
    if not os.path.exists(settings_file):
        local_data_files.create()
    configurar = open(settings_file)

    configurar.readline()
    icorte = configurar.readline()
    icorte = icorte.rstrip('\n')
    configurar.readline()
    configurar.readline()

    fcorte = configurar.readline()
    fcorte = fcorte.rstrip('\n')
    configurar.readline()
    configurar.readline()

    extencao = configurar.readline()
    extencao = extencao.rstrip('\n')
    extencao = extencao.replace(".", "")
    extencao = "." + extencao
    configurar.readline()
    configurar.readline()

    SmesaX = configurar.readline()
    SmesaX = SmesaX.rstrip('\n')
    mesaX = float(SmesaX)
    configurar.readline()
    configurar.readline()

    SmesaY = configurar.readline()
    SmesaY = SmesaY.rstrip('\n')
    mesaY = float(SmesaY)
    configurar.readline()
    configurar.readline()

    numerar = configurar.readline()
    numerar = numerar.rstrip('\n')
    numerar = int(numerar)
    configurar.readline()
    configurar.readline()

    colocarVelocidadeAvanco = configurar.readline()
    colocarVelocidadeAvanco = colocarVelocidadeAvanco.rstrip('\n')
    colocarVelocidadeAvanco = int(colocarVelocidadeAvanco)
    configurar.readline()
    configurar.readline()

    colocarVelocidadeAvancoRapido = configurar.readline()
    colocarVelocidadeAvancoRapido = colocarVelocidadeAvancoRapido.rstrip('\n')
    colocarVelocidadeAvancoRapido = int(colocarVelocidadeAvancoRapido)
    configurar.readline()
    configurar.readline()

    velocidadeAvancoRapido = configurar.readline()
    velocidadeAvancoRapido = velocidadeAvancoRapido.rstrip('\n')
    velocidadeAvancoRapido = float(velocidadeAvancoRapido)
    configurar.readline()
    configurar.readline()

    pastaPadLinux = configurar.readline()
    configurar.readline()
    configurar.readline()

    pastaPadWin = configurar.readline()
    pastaPadLinux = pastaPadLinux.rstrip('\n')
    pastaPadWin = pastaPadWin.rstrip('\n')
    configurar.close()

    return icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux


def NumerarLinhas(nomeDoArquivo):
    # Se a funçao escrever o programa com extençao e a referencia estiver sem
    if os.path.isdir(nomeDoArquivo) == False:
        if nomeDoArquivo != "":
            temExtencao = "." in nomeDoArquivo
            if temExtencao == False:
                nomeDoArquivo += Parametros()[2]
    # Incio do codigo
    linha = 0
    arquivo = open(nomeDoArquivo)
    linhaAtual = arquivo.readline()
    texto = ""
    tamanhoLinhaAtual = len(linhaAtual)
    while (tamanhoLinhaAtual > 0):
        linha = linha + 1
        texto = texto + "N" + str(linha) + " " + linhaAtual
        linhaAtual = arquivo.readline()
        tamanhoLinhaAtual = len(linhaAtual)
    escrever = open(nomeDoArquivo, "w")
    escrever.write(texto)
    escrever.close()


def ColocarVelocidadeAvanco(nomeDoArquivo, velocidade):
    # Se a funçao escrever o programa com extençao e a referencia estiver sem
    if os.path.isdir(nomeDoArquivo) == False:
        if nomeDoArquivo != "":
            temExtencao = "." in nomeDoArquivo
            if temExtencao == False:
                nomeDoArquivo += Parametros()[2]
    # Incio do codigo
    FA = str(" F" + str(int(velocidade)))
    arquivo = open(nomeDoArquivo)
    linha = arquivo.readline()
    texto = ""
    tamanhoLinha = len(linha)
    while (tamanhoLinha > 0):
        if linha[0:3] == "G01" or linha[0:3] == "G02" or linha[0:3] == "G03":
            linha = linha.rstrip('\n') + FA + '\n'
            texto = texto + linha
        else:
            texto = texto + linha
        linha = arquivo.readline()
        tamanhoLinha = len(linha)
    escrever = open(nomeDoArquivo, "w")
    escrever.write(texto)
    escrever.close()


def ColocarVelocidadeAvancoRapido(nomeDoArquivo, velocidade):
    # Se a funçao escrever o programa com extençao e a referencia estiver sem
    if os.path.isdir(nomeDoArquivo) == False:
        if nomeDoArquivo != "":
            temExtencao = "." in nomeDoArquivo
            if temExtencao == False:
                nomeDoArquivo += Parametros()[2]
    # Incio do codigo
    FA = str(" F" + str(int(velocidade)))
    arquivo = open(nomeDoArquivo)
    linha = arquivo.readline()
    texto = ""
    tamanhoLinha = len(linha)
    while (tamanhoLinha > 0):
        if linha[0:3] == "G00":
            linha = linha.rstrip('\n') + FA + '\n'
            texto = texto + linha
        else:
            texto = texto + linha
        linha = arquivo.readline()
        tamanhoLinha = len(linha)
    escrever = open(nomeDoArquivo, "w")
    escrever.write(texto)
    escrever.close()


def PassarMilimetro(fracao):
    # Se a entrada estiver vazia definir a string ZERO como valor
    if fracao == "":
        fracao = "0"

    # Trocador todos os separadores por -
    fracao = str(fracao)
    fracao = fracao.replace(' ', '-')
    fracao = fracao.replace('/', '-')
    fracao = fracao.replace('*', '-')
    fracao = fracao.replace('+', '-')
    fracao = fracao.replace(',', '.')
    fracao = fracao.replace('"', '')
    fracao = fracao.replace('\'', '')

    # Contar quantas vezes aparece -
    sep = fracao.count('-')
    if sep == 0:
        return float(fracao) * 25.4
    if sep == 1:
        numerador, divisor = fracao.split('-')
        return float(numerador) * 25.4 / float(divisor)
    if sep == 2:
        inteiro, numerador, divisor = fracao.split('-')
        decimal = float(numerador) / float(divisor)
        return (decimal + float(inteiro)) * 25.4


def Kerf(espessura):
    esp = float(espessura)
    arquivoKerf = str(os.getcwd()) + "/.gisoplox/oxyfuel_cutting_width.gisoplox"
    ler = open(arquivoKerf)

    espMin = 0
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    ler.close()


def KerfPlasma(espessura):
    esp = float(espessura)
    arquivoKerf = str(os.getcwd()) + "/.gisoplox/plasma_cutting_width.gisoplox"
    ler = open(arquivoKerf)

    espMin = 0
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    espMin = ler.readline()[0:-1]
    espMax = ler.readline()[0:-1]
    larg = ler.readline()[0:-1]
    vel = ler.readline()[0:-1]
    ler.readline()
    if esp > float(espMin) and esp <= float(espMax):
        kerf = float(larg) / 2.0
        return (kerf, vel)

    ler.close()


def escreverPrograma(programa, salvar):
    if salvar != "":
        temExtencao = "." in salvar
        if temExtencao == False:
            salvar += Parametros()[2]
        escrever = open(salvar, "w")
        escrever.write(programa)
        escrever.close()


def verificarHist():
    arquivo = str(os.getcwd()) + "/.gisoplox/history.gisoplox"
    # Funçao que verifica se o arquivo hist existe
    # Se nao existir um novo e criado
    if os.path.isfile(arquivo) == False:
        escrever = open(arquivo, "w")
        escrever.write("")
        escrever.close()
    arquivo2 = str(os.getcwd()) + "/.gisoplox/history_sheet.csv"
    if os.path.isfile(arquivo2) == False:
        escrever2 = open(arquivo2, "w")
        escrever2.write("")
        escrever2.close()


def lerHistLinha(linha):
    verificarHist()
    arquivo = str(os.getcwd()) + "/.gisoplox/history.gisoplox"
    ler = open(arquivo)
    a = 1
    while a < linha:
        ler.readline()
        a += 1
    texto = ler.readline().replace("\n", "")
    # Nome
    encontrado = texto.find("|")
    Nome = texto[0:encontrado]
    texto = texto[encontrado:-1]
    texto = texto[1:-1]
    # Peso unitario
    encontrado = texto.find("|")
    PesoUn = texto[0:encontrado]
    texto = texto[encontrado:-1]
    texto = texto[1:-1]
    # Peso total
    encontrado = texto.find("|")
    PesoTotal = texto[0:encontrado]
    texto = texto[encontrado:-1]
    texto = texto[1:-1]
    # Distancia
    encontrado = texto.find("|")
    Dist = texto[0:encontrado]
    texto = texto[encontrado:-1]
    texto = texto[1:-1]
    # Data
    encontrado = texto.find("|")
    Data = texto[0:encontrado]
    texto = texto[encontrado:-1]
    texto = texto[1:-1]
    # Hora
    encontrado = texto.find("|")
    Hora = texto[0:encontrado]
    texto = texto[encontrado:-1]
    texto = texto[1:-1]
    # Versao
    encontrado = texto.find("|")
    Versao = texto[0:encontrado]
    ler.close()
    return Nome, PesoUn, PesoTotal, Dist, Data, Hora, Versao


def escreverHist(Nome, PesoUn, PesoTotal, Dist, Versao):
    verificarHist()
    arquivo = str(os.getcwd()) + "/.gisoplox/history.gisoplox"
    ler = open(arquivo)
    texto = ler.read()
    ler.close()
    escrever = open(arquivo, "w")
    hora = time.strftime("%H:%M")
    data = (time.strftime("%d/%m/%y"))
    linha = str(Nome) + "|" + str(PesoUn) + "|" + str(PesoTotal) + "|" + str(Dist) + "|" + str(data) + "|" + str(
        hora) + "|" + str(Versao) + "||||||||||||||\n"
    texto = linha + texto
    escrever.write(texto)
    escrever.close()


# escreverHist("Teste", "20 kg", "32 kg", "12 metros", "1.160121")
# print lerHistLinha(1)

def escreverCSV(texto):
    verificarHist()
    arquivo = str(os.getcwd()) + "/.gisoplox/history_sheet.csv"
    ler = open(arquivo)
    conteudo = ler.read()
    ler.close()
    escrever = open(arquivo, "w")
    hora = time.strftime("%H:%M")
    data = (time.strftime("%d/%m/%y"))
    texto = str(data) + "," + str(hora) + "," + texto + conteudo
    escrever.write(texto)
    escrever.close()


# escreverHist("Nome", "PesoUn", "PesoTotal", "Dist")
# print lerHistLinha(1)

def converterDist(dist):
    dist = float(dist)
    if dist < 1000:
        a = str(int(dist)) + " mm"
        return a
    if 1000 <= dist < 2000:
        a = str(int(dist / 1000)) + " meter"
        return a
    if 2000 < dist < 1000000:
        a = str(int(dist / 1000)) + " meters"
        return a
    if dist >= 1000000:
        a = str(int(dist / 1000000)) + " km"
        return a


def lerEstat(unidade):
    verificarEstat()
    arquivo = ".gisoplox/metrics.gisoplox"
    ler = open(arquivo)

    def numData(dia, mes, ano):
        num = date(ano, mes, dia).toordinal()
        return num

    def converterPeso(peso):
        peso = float(peso)
        if peso <= 1:
            a = str(int(peso)) + " gram"
            return a
        if 1 < peso < 1000:
            a = str(int(peso)) + " grams"
            return a
        if 1000 <= peso < 1000000:
            a = str(int(peso / 1000)) + " kg"
            return a
        if 1000000 <= peso < 2000000:
            a = str(int(peso / 1000000)) + " tonne"
            return a
        if peso >= 2000000:
            a = str(int(peso / 1000000)) + " tonnes"
            return a

    def numParaEscrita(num):
        ano = date.fromordinal(int(num)).year
        mes = date.fromordinal(int(num)).month
        meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        mes = meses[mes - 1]
        dia = date.fromordinal(int(num)).day
        #dia = str(dia) + " de " + str(mes) + " de " + str(ano)
        dia = str(mes) + " " + str(dia) + "th, " + str(ano)
        return dia

    # Início da leitura do arquivo
    # Dados totais
    distTotal = ler.readline()
    distTotal = distTotal.replace("\n", "")
    if unidade == True:
        distTotal = converterDist(distTotal)
    # print distTotal
    pesoTotal = ler.readline()
    pesoTotal = pesoTotal.replace("\n", "")
    if unidade == True:
        pesoTotal = converterPeso(pesoTotal)
    # print pesoTotal
    prgTotal = ler.readline()
    prgTotal = prgTotal.replace("\n", "")
    # print prgTotal
    dataTotal = ler.readline().replace("\n", "")
    if unidade == True:
        diaTotal = numParaEscrita(dataTotal)
    if unidade == False:
        diaTotal = dataTotal

    # Dados zeraveis
    distZerado = ler.readline()
    distZerado = distZerado.replace("\n", "")
    if unidade == True:
        distZerado = converterDist(distZerado)
    # print distZerado
    pesoZerado = ler.readline()
    pesoZerado = pesoZerado.replace("\n", "")
    if unidade == True:
        pesoZerado = converterPeso(pesoZerado)
    # print pesoZerado
    prgZerado = ler.readline()
    prgZerado = prgZerado.replace("\n", "")
    # print prgZerado
    dataZerado = ler.readline().replace("\n", "")
    if unidade == True:
        diaZerado = numParaEscrita(dataZerado)
    if unidade == False:
        diaZerado = dataZerado

    return distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado


def adicionarEstat(dist, peso):
    verificarEstat()
    # Local do arquivo estat
    arquivo = ".gisoplox/metrics.gisoplox"

    # Lendo valores das variaveis
    distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado = lerEstat(False)

    # Transformando todas as variaveis para o tipo inteiro para evitar problemas
    dist = float(dist)
    peso = float(peso)
    dist = int(dist)
    peso = int(peso)
    distTotal = int(distTotal)
    pesoTotal = int(pesoTotal)
    prgTotal = int(prgTotal)
    diaTotal = int(diaTotal)
    distZerado = int(distZerado)
    pesoZerado = int(pesoZerado)
    prgZerado = int(prgZerado)
    diaZerado = int(diaZerado)

    # Incrementando variaveis
    distTotal += dist
    pesoTotal += peso
    prgTotal += 1
    distZerado += dist
    pesoZerado += peso
    prgZerado += 1

    # Escrevendo o texto das variaveis

    texto = str(distTotal) + "\n"
    texto += str(pesoTotal) + "\n"
    texto += str(prgTotal) + "\n"
    texto += str(diaTotal) + "\n"
    texto += str(distZerado) + "\n"
    texto += str(pesoZerado) + "\n"
    texto += str(prgZerado) + "\n"
    texto += str(diaZerado)

    # Escrevendo o texto no arquivo
    escrever = open(arquivo, "w")
    escrever.write(texto)
    escrever.close()


def zerarEstat():
    verificarEstat()
    # Local do arquivo estat
    arquivo = ".gisoplox/metrics.gisoplox"

    # Lendo valores das variaveis
    distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado = lerEstat(False)

    # Transformando todas as variaveis para o tipo inteiro para evitar problemas
    distTotal = int(distTotal)
    pesoTotal = int(pesoTotal)
    prgTotal = int(prgTotal)
    diaTotal = int(diaTotal)
    distZerado = int(distZerado)
    pesoZerado = int(pesoZerado)
    prgZerado = int(prgZerado)
    diaZerado = int(diaZerado)

    # Escrevendo o texto das variaveis
    texto = str(distTotal) + "\n"
    texto += str(pesoTotal) + "\n"
    texto += str(prgTotal) + "\n"
    texto += str(diaTotal) + "\n"
    texto += "0\n"
    texto += "0\n"
    texto += "0\n"
    diaZerado = int(date.today().toordinal())
    texto += str(diaZerado)

    # Escrevendo o texto no arquivo
    escrever = open(arquivo, "w")
    escrever.write(texto)
    escrever.close()


def criarEstat():
    # Local do arquivo estat
    arquivo = ".gisoplox/metrics.gisoplox"

    # Escrevendo o texto das variaveis
    texto = ""
    linha = 0
    while linha < 7:
        if 0 <= linha < 3 or 3 < linha:
            # print "ok"
            texto += "0\n"
        if linha == 3:
            texto += str(int(date.today().toordinal())) + "\n"
        linha += 1
    texto += str(int(date.today().toordinal()))

    # Escrevendo o texto no arquivo
    escrever = open(arquivo, "w")
    escrever.write(texto)
    escrever.close()


def verificarEstat():
    arquivo = str(os.getcwd()) + ".gisoplox/metrics.gisoplox"
    # Funçao que verifica se o arquivo estat existe
    # Se nao existir um novo e criado
    if os.path.isfile(arquivo) == False:
        criarEstat()


def Wildcard():
    extencao = Parametros()[2]
    wildcard = "Personalizado (*" + str(extencao) + ") |*" + str(extencao) + "|" \
                                                                             "Linux CNC / EMC2 (*.ngc)|*.ngc|" \
                                                                             "Texto (*.txt)|*.txt|" \
                                                                             "Arquivo CNC (*.cnc)|*.cnc|" \
                                                                             "Arquivo NC (*.nc)|*.nc|" \
                                                                             "Codigo G (*.gcode)|*.gcode|" \
                                                                             "Codigo G (*.gco)|*.gco|" \
                                                                             "Codigo G (*.g)|*.g|" \
                                                                             "Todos os arquivos (*.*)|*.*"
    return wildcard


########################################################### Pesos das peças cortados ##############################################################
def pesoRetangulo(esp, tx, ty, quantidade):
    esp = float(esp)
    tx = float(tx)
    ty = float(ty)
    quantidade = int(quantidade)
    densidade = 7.86 / 1000
    volume = esp * tx * ty
    pesoUnitario = volume * densidade
    pesoTotal = pesoUnitario * quantidade
    return pesoUnitario, pesoTotal


def pesoTrianguloRetangulo(esp, tx, ty, quantidade):
    esp = float(esp)
    tx = float(tx)
    ty = float(ty)
    quantidade = int(quantidade)
    densidade = 7.86 / 1000
    volume = esp * tx * ty / 2.0
    pesoUnitario = volume * densidade
    pesoTotal = pesoUnitario * quantidade
    return pesoUnitario, pesoTotal


def pesoCirculo(esp, diam, quantidade):
    esp = float(esp)
    diam = float(diam)
    quantidade = int(quantidade)
    densidade = 7.86 / 1000
    pi = 3.14159265359
    volume = esp * (pi * diam * diam / 4.0)
    pesoUnitario = volume * densidade
    pesoTotal = pesoUnitario * quantidade
    return pesoUnitario, pesoTotal


def pesoAnel(esp, diam, diamFuro, quantidade):
    esp = float(esp)
    diam = float(diam)
    diamFuro = float(diamFuro)
    quantidade = float(quantidade)
    densidade = 7.86 / 1000
    pi = 3.14159265359
    areaExt = pi * diam * diam / 4.0
    areaInt = pi * diamFuro * diamFuro / 4.0
    area = areaExt - areaInt
    volume = esp * area
    pesoUnitario = volume * densidade
    pesoTotal = pesoUnitario * quantidade
    return pesoUnitario, pesoTotal


def pesoRetanguloFuro(esp, tx, ty, furo, quantidade):
    esp = float(esp)
    tx = float(tx)
    ty = float(ty)
    furo = float(furo)
    pesoUnitarioRetangulo, pesoTotalRetangulo = pesoRetangulo(esp, tx, ty, quantidade)
    pesoUnitarioFuro, pesoTotalFuro = pesoCirculo(esp, furo, quantidade)

    pesoUnitario = float(pesoUnitarioRetangulo) - float(pesoUnitarioFuro)
    pesoTotal = float(pesoTotalRetangulo) - float(pesoTotalFuro)
    return pesoUnitario, pesoTotal


def pesoTrianguloPontasCortadas(esp, tx, ty, chanfroX, chanfroY, quantidade):
    esp = str(esp)
    tx = str(tx)
    ty = str(ty)
    chanfroX = str(chanfroX)
    chanfroY = str(chanfroY)
    tx = float(tx) + float(chanfroX)
    ty = float(ty) + float(chanfroY)
    pesoUnitarioGrande, pesoTotalGrande = pesoTrianguloRetangulo(esp, tx, ty, quantidade)
    pesoUnitarioPequeno, pesoTotalPequeno = pesoTrianguloRetangulo(esp, chanfroX, chanfroY, quantidade)
    pesoUnitario = pesoUnitarioGrande - pesoUnitarioPequeno - pesoUnitarioPequeno
    pesoTotal = pesoTotalGrande - pesoTotalPequeno - pesoTotalPequeno
    # pesoUnitario=1.0
    # pesoTotal=1.0
    return pesoUnitario, pesoTotal


def pesoRetanguloChanfrado(esp, tx, ty, chanfroXs, chanfroYs, chanfroXi, chanfroYi, quantidade):
    esp = float(esp)
    tx = float(tx)
    ty = float(ty)
    area = (tx * ty) - (chanfroXs * chanfroYs) - (chanfroXi * chanfroYi)
    quantidade = int(quantidade)
    densidade = 7.86 / 1000
    volume = esp * area
    pesoUnitario = volume * densidade
    pesoTotal = pesoUnitario * quantidade
    return pesoUnitario, pesoTotal


def pesoString(pesoEmGramas):
    peso = int(pesoEmGramas)
    if peso == 1:
        pesoString = "1 grama"
    elif 1 < peso < 1000:
        pesoString = str(int(peso) + 1) + " gramas"
    elif peso >= 1000:
        pesoString = str(int((peso / 1000) + 1)) + " kg"
    return pesoString
