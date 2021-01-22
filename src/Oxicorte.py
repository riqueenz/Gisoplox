# -*- coding: cp1252 -*-
import Auxiliares
from math import sqrt
from math import tan
from math import atan
from math import degrees
from math import radians
icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()

def calcularHipotenusa(catX, catY):
    catX=float(catX)
    catY=float(catY)
    hip=sqrt((catX*catX)+(catY*catY))
    return hip

def distCirculoRaio(raio):
    pi=3.14159265359
    dist=2*pi*float(raio)
    return dist
###################################################################################################################################
def Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, kerf):

    #Garantir que as variaveis sao do tipo float
    txd=float(txd)
    tyd=float(tyd)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<txd:
        chapaX=txd+1
    if chapaY<tyd:
        chapaY=tyd+1

    #Calculo de tamanhos
    lcorte=kerf+kerf
    tx=txd+kerf
    txf=txd+lcorte
    ty=tyd+kerf
    tyf=tyd+lcorte
    mover=tx+kerf+entrada
    mover=round(mover, 4)
    mover2=mover+mover-kerf-entrada
    gx=1
    gy=0
    divX=txd+lcorte
    mx=chapaX/divX
    l=0
    pecasFeitas=0

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    divX=txd+lcorte
    mx=chapaX/divX
    mx=int(mx)

    divY=tyd+lcorte
    my=chapaY/divY
    my=int(my)
    seq=0

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        if (pecasFeitas==0) or seq==1:
            #Gerar primeira peça
            programa=programa + "G00 X" + str(txf) + " Y-" + str(entrada) + '\n'
            programa=programa + str(icorte) + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 Y" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=float(txf)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            programa=programa + "G01 X" + str(txf) + '\n'
            distCorte+=float(txf)
            tyfEentrada=tyf + entrada
            programa=programa + "G01 Y-" + str(tyfEentrada) + '\n'
            distCorte+=float(tyfEentrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)

            if mx==2:
                seq=4

            if mx==1:
                seq=5
    
            pecasFeitas=1
            gx=gx+1
            mov=1

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1) or (seq==2 and gy<my):
            #Gerar segunda peça
            programa=programa + "G00 X" + str(kerf) + " Y" + str(entrada) + '\n'
            programa=programa + icorte + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 X" + str(tx) + '\n'
            distCorte+=float(tx)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=0

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==0) or (seq==3 and gy<my):            
            #Gerar demais peças da primeira linha
            programa=programa + "G00 X" + str(mover) + " Y-" + str(tyf) + '\n'
            programa=programa + icorte + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 X" + str(tx) + '\n'
            distCorte+=float(tx)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my) or (seq==4 and gy<my):
            #Gerar ultima peça da primeira linha
            tyEkerf=ty+kerf
            if mx==2:
                programa=programa + "G00 X" + str(kerf) + " Y" + str(entrada) + '\n'
            else:
                programa=programa + "G00 X" + str(mover) + " Y-" + str(tyEkerf) + '\n'
            programa=programa + icorte + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 X" + str(tx) + '\n'
            distCorte+=float(tx)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)

            if mx==2:
                seq=5

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1

        elif (pecasFeitas<pecas and gx==1 and gy<my) or (seq==5 and gy<my):
            #Gerar primeira peça das demais linhas
            if mx==1:
                if gy==0:
                    programa=programa + "G00 X-" + str(txf) + " Y" + str(tyf+kerf+entrada) + '\n'
                    gy+=2
                else:
                    programa=programa + "G00 X-" + str(txf-entrada) + " Y" + str(tyf+kerf) + '\n'
                    gy+=1
            else:
                mover1peca2linha=(txf*(mx-2))+kerf-entrada+txf
                programa=programa + "G00 X-" + str(mover1peca2linha) + " Y" + str(kerf) + '\n'
            programa=programa + icorte + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=float(ty)
            programa=programa + "G01 X" + str(txf) + '\n'
            distCorte+=float(txf)
            programa=programa + "G01 Y-" + str(ty) + '\n'
            distCorte+=float(ty)
            programa=programa + "G01 X-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)
            if mx==1:
                pass
            else:
                programa=programa + "G00 X" + str(mover) + '\n'

            if mx==2:
                seq=7

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx<mx and gy<my) or (seq==6 and gy<my):
            #Gerar demais peças das demais linhas
            programa=programa + icorte + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=float(ty)
            txEentrada=tx+entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)
            programa=programa + "G00 X" + str(mover2) + " Y-" + str(ty) + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and gy<my) or (seq==7 and gy<my):
            #Gerar ultima peça das demais linhas
            programa=programa + icorte + '\n'
            #distCorte+=float(icorte)
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=float(ty)
            txEentrada=tx+entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            #distCorte+=float(fcorte)

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
        elif (gy==my or pecasFeitas==pecas):
            break
        else:
            break
  
    programa=programa + "M02"
        
    return pecasFeitas, programa, distCorte
#############################################################################################################################################
def Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, kerf):

    #Garantir que as variaveis sao do tipo float
    diam1=float(diam1)
    diam2=float(diam2)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0

    #Definir o maior diâmetro como externo
    if (diam1>=diam2):
        diamExt=float(diam1)
        diamInt=float(diam2)

    if (diam1<diam2):
        diamExt=float(diam2)
        diamInt=float(diam1)
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<diamExt:
        chapaX=diamExt+1
    if chapaY<diamExt:
        chapaY=diamExt+1

    #Calculo de tamanhos
    lcorte=kerf+kerf
    gx=1
    gy=0
    l=0
    pecasFeitas=0
    raioExt=diamExt/2
    raioExtKerf=raioExt + kerf
    raioInt=diamInt/2
    raioIntKerf=raioInt - kerf
    entradaKerf=entrada + kerf
    mov=0

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    div=diamExt+lcorte+entrada
    mx=chapaX/div
    my=chapaY/div
    mx=int(mx)
    my=int(my)
    seq=0

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        if (pecasFeitas==0 and mov==0):
            #Gerar primeira peça
            #print "Gerar primeira peça"

            
            programa=programa + "G00 X" + str(raioExtKerf+raioIntKerf-entradaKerf) + " Y" + str(raioExtKerf+entradaKerf) + '\n'
            
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I-" + str(raioIntKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(raioIntKerf-entradaKerf) + ' Y-' + str(raioExtKerf+entradaKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G02 X0.0000 Y0.0000 I0.0000 J" + str(raioExtKerf) + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 Y-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'
    
            pecasFeitas=1
            gx=gx+1
            mov=1

            if (mx==2):
                mov=2

            if mx==1:
                #gy+=1
                seq=1

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1):
            #Movimentar para a segunda peça
            programa=programa + "G00 X" + str(raioExtKerf+raioExtKerf+raioIntKerf+kerf) + ' Y' + str(raioExtKerf+entradaKerf) + '\n'
            #print "Movimentar para a segunda peça"
            mov=2

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==2):
            #Gerar segunda peça
            #print "Gerar segunda peça"

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I-" + str(raioIntKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(raioExtKerf+raioIntKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'

            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=2

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==2):
            #Movimentar para as demais peças da primeira linha
            #print "Movimentar para as demais peças da primeira linha"
            programa=programa + "G00 X" + str(diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + '\n'
            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==1):            
            #Gerar demais peças da primeira linha
            #print "Gerar demais peças da primeira linha"
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I-" + str(raioIntKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(raioExtKerf+raioIntKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'


            pecasFeitas=pecasFeitas+1
            mov=2
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my and mov==2):
            #Movimentar para as últimas peças da primeira linha
            #print "Movimentar para as últimas peças da primeira linha"
            if mx==2:
                programa=programa + "G00 X" + str(raioExtKerf-diamExt-lcorte-lcorte-entradaKerf+diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + " Y" + str(raioExtKerf+entradaKerf) + '\n'
            else:
                programa=programa + "G00 X" + str(diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + '\n'
            mov=1


        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my and mov==1):
            #Gerar ultima peça da primeira linha
            #print "Gerar ultima peça da primeira linha"
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I-" + str(raioIntKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(raioExtKerf+raioIntKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'


            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
            mov=3

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==3):
            #Movimentar para a primeira peça das demais linhas
            #print "Movimentar para a primeira peça das demais linhas"
            programa=programa + "G00 X-" + str(((mx-2)*(diamExt+lcorte+lcorte+entradaKerf))+raioExt+lcorte) + " Y" + str(raioExt+lcorte+entradaKerf+raioExtKerf+raioIntKerf-entradaKerf) + '\n'            
            mov=4

        elif (gy<my and seq==1):
            #print "Movimentar seq=1"
            if mx==1:
                programa+="G00 X0.0  Y"+str(raioExtKerf+raioExtKerf+entrada+kerf+raioExtKerf+raioIntKerf)+"\n"
            else:
                programa+="G00 X"+str(entrada+raioExtKerf)+" Y"+str(raioExtKerf+raioExtKerf+raioIntKerf)+"\n"
            seq=2
            gy+=1

        elif (gy<my and seq==4):
            #print "Movimentar seq=4"
            programa+="G00 X0.0  Y"+str(raioExtKerf+raioExtKerf+entrada+kerf+raioExtKerf+raioIntKerf)+"\n"
            seq=2
            gy+=1


        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==4) or (seq==2 and gy<my):
            #Gerar primeira peça das demais linhas
            #print "Gerar primeira peça das demais linhas"

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I0.0 J-" + str(raioIntKerf) + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 Y-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 Y-" + str(raioExtKerf+raioIntKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G02 X0.0000 Y0.0000 I0.0 J" + str(raioExtKerf) + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 Y-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'


            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=3

            if mx==1:
                seq=4

        elif (pecasFeitas<pecas and gx<mx and gy<my and mov==3):
            #Movimentar para as demais peças das demais linhas
            #print "Movimentar para as demais peças das demais linhas"
            if (gx!=2):
                programa=programa + "G00 X" + str(diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + '\n' 
            if (gx==2):
                programa=programa + "G00 X" + str(raioExtKerf-diamExt-lcorte-lcorte-entradaKerf+diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + " Y" + str(raioExtKerf+entradaKerf) + '\n'
            mov=4

        elif (pecasFeitas<pecas and gx<mx and gy<my and mov==4):
            #Gerar demais peças das demais linhas
            #print "Gerar demais peças das demais linhas"
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I-" + str(raioIntKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(raioExtKerf+raioIntKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=3

        elif (pecasFeitas<pecas and gx==mx and gy<my and mov==3):
            #Movimentar para a ultima peça das demais linhas
            #print "Movimentar para a ultima peça das demais linhas"
            if mx==2:
                #print gy
                #gy+=1
                programa=programa + "G00 X" + str(raioExtKerf-diamExt-lcorte-lcorte-entradaKerf+diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + " Y" + str(raioExtKerf+entradaKerf) + '\n'
            else:
                programa=programa + "G00 X" + str(diamExt+lcorte+lcorte+entradaKerf+raioExtKerf+raioIntKerf) + '\n'
            mov=4

        elif (pecasFeitas<pecas and gx==mx and gy<my and mov==4):
            #Gerar ultima peça das demais linhas
            #print "Gerar ultima peça das demais linhas"
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I-" + str(raioIntKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioIntKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(raioExtKerf+raioIntKerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
            mov=3

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==3):
            #Mover para a próxima linha
            #print "Mover para a próxima linha"
            programa=programa + "G00 X-" + str(((mx-2)*(diamExt+lcorte+lcorte+entradaKerf))+raioExt+lcorte) + " Y" + str(raioExt+lcorte+entradaKerf+raioExtKerf+raioIntKerf-entradaKerf) + '\n'
            mov=4
            
        elif (gy>=my or pecasFeitas==pecas):
            break
        else:
            break

    #print programa
    programa=programa + "M02"
    return pecasFeitas, programa, distCorte
#pecasFeitas, prg, distCorte = Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, kerf)
#pecasFeitas, prg, distCorte = Circulo("200", "100", "5", "0", "0", "25", "1.3")
#Auxiliares.escreverPrograma(prg, "/home/henrique/linuxcnc/nc_files/a.ngc")

#############################################################################################################################################
def CirculoSimples(diam1, entrada, chapaX, chapaY, pecas, kerf):
    #Garantir que as variaveis sao do tipo float
    diam1=float(diam1)
    diamExt=float(diam1)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<diamExt:
        chapaX=diamExt+1
    if chapaY<diamExt:
        chapaY=diamExt+1

    #Calculo de tamanhos
    lcorte=kerf+kerf
    gx=1
    gy=0
    l=0
    pecasFeitas=0
    raioExt=diamExt/2
    raioExtKerf=raioExt + kerf
    entradaKerf=entrada + kerf
    mov=0

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    div=diamExt+lcorte+entrada
    mx=chapaX/div
    my=chapaY/div
    mx=int(mx)
    my=int(my)
    seq=0

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        if (pecasFeitas==0 and mov==0):
            #Gerar primeira peça
            #print "Gerar primeira peça"
            programa=programa + "G00 X" + str(raioExtKerf) + " Y-" + str(entradaKerf) + '\n'

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G02 X0.0000 Y0.0000 I0.0000" + " J" + str(raioExtKerf) + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 Y-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'
    
            pecasFeitas=1
            gx=gx+1
            mov=1

            if (mx==2):
                seq=21

            if mx==1:
                #gy+=1
                seq=11

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1) or (gy<my and seq==21):
            #Movimentar para a segunda peça
            programa=programa + "G00 X" + str(raioExtKerf+kerf) + ' Y' + str(entradaKerf+raioExtKerf) + '\n'
            #programa+="teste\n"
            #print "Movimentar para a segunda peça"
            mov=2
            if mx==2:
                seq=0

        elif (gy<my and seq==11):
            #Movimentar para a primeira peça da próxima linha quando mx=1
            programa=programa + 'G00 X0.0 Y' + str(entradaKerf+raioExtKerf+raioExtKerf+kerf) + '\n'
            #programa+="teste\n"
            #print "Movimentar para a primeira peça da próxima linha quando mx=1"
            gy+=1
            seq=12

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==2):
            #Gerar segunda peça
            #print "Gerar segunda peça"

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'

            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=2

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==2):
            #Movimentar para as demais peças da primeira linha
            #print "Movimentar para as demais peças da primeira linha"
            programa=programa + "G00 X" + str(diamExt+kerf+kerf+kerf+entradaKerf) + '\n'
            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==1):            
            #Gerar demais peças da primeira linha
            #print "Gerar demais peças da primeira linha"

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'


            pecasFeitas=pecasFeitas+1
            mov=2
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my and mov==2):
            #Movimentar para as últimas peças da primeira linha
            #print "Movimentar para as últimas peças da primeira linha"
            if mx==2:
                pass
            else:
                programa=programa + "G00 X" + str(diamExt+kerf+kerf+kerf+entradaKerf) + '\n'
            mov=1


        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my and mov==1):
            #Gerar ultima peça da primeira linha
            #print "Gerar ultima peça da primeira linha"

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'


            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
            mov=3

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==3):
            #Movimentar para a primeira peça das demais linhas
            #print "Movimentar para a primeira peça das demais linhas"
            programa=programa + "G00 X-" + str(((mx-1)*(diamExt+kerf+kerf+kerf+entradaKerf))-(entradaKerf+raioExtKerf)) + " Y" + str(raioExtKerf+kerf) + '\n'            
            mov=4

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==4) or (gy<my and seq==12):
            #Gerar primeira peça das demais linhas
            #print "Gerar primeira peça das demais linhas"

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G02 X0.0000 Y0.0000 I0.0000" + " J" + str(raioExtKerf) + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 Y-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'

            if mx==1:
                seq=11


            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=3

        elif (pecasFeitas<pecas and gx<mx and gy<my and mov==3):
            #Movimentar para as demais peças das demais linhas
            #print "Movimentar para as demais peças das demais linhas"
            if (gx!=2):
                programa=programa + "G00 X" + str(diamExt+kerf+kerf+kerf+entradaKerf) + '\n'
            
            if (gx==2):
                programa=programa + "G00 X" + str(raioExtKerf+kerf) + ' Y' + str(entradaKerf+raioExtKerf) + '\n'
            mov=4

        elif (pecasFeitas<pecas and gx<mx and gy<my and mov==4):
            #Gerar demais peças das demais linhas
            #print "Gerar demais peças das demais linhas"
            
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=3

        elif (pecasFeitas<pecas and gx==mx and gy<my and mov==3):
            #Movimentar para a ultima peça das demais linhas
            #print "Movimentar para a ultima peça das demais linhas"
            if mx==2:
                pass
            else:
                programa=programa + "G00 X" + str(diamExt+kerf+kerf+kerf+entradaKerf) + '\n'
            mov=4

        elif (pecasFeitas<pecas and gx==mx and gy<my and mov==4):
            #Gerar ultima peça das demais linhas
            #print "Gerar ultima peça das demais linhas"
            if mx==2:
                programa=programa + "G00 X" + str(raioExtKerf+kerf) + ' Y' + str(entradaKerf+raioExtKerf) + '\n'

            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 X" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + "G03 X0.0000 Y0.0000 I" + str(raioExtKerf) + " J0.0000" + '\n'
            distCorte+=distCirculoRaio(raioExtKerf)
            programa=programa + "G01 X-" + str(entradaKerf) + '\n'
            distCorte+=entradaKerf
            programa=programa + fcorte + '\n'

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
            mov=3

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==3):
            #Mover para a próxima linha
            #print "Mover para a próxima linha"
            programa=programa + "G00 X-" + str(((mx-1)*(diamExt+kerf+kerf+kerf+entradaKerf))-(entradaKerf+raioExtKerf)) + " Y" + str(raioExtKerf+kerf) + '\n' 
            mov=4
            
        elif (gy>=my or pecasFeitas==pecas):
            break
        else:
            break

    #print programa
    programa=programa + "M02"
    return pecasFeitas, programa, distCorte
#pecasFeitas, prg, distCorte = CirculoSimples(diam1, entrada, chapaX, chapaY, pecas, kerf)
#pecasFeitas, prg, distCorte = CirculoSimples("100", "5", "0", "0", "25", "1.5")
#Auxiliares.escreverPrograma(prg, "/home/henrique/linuxcnc/nc_files/a.ngc")

#############################################################################################################################################
def TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, kerf):
#Adaptado para plasma
    #Garantir que as variaveis sao do tipo float
    txd=float(txd)
    tyd=float(tyd)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<txd:
        chapaX=txd+1
    if chapaY<tyd:
        chapaY=tyd+1

    #Calculo de tamanhos
    lcorte=kerf+kerf
    tx=txd+kerf
    txf=txd+lcorte
    ty=tyd+kerf
    tyf=tyd+lcorte
    mover=tx+kerf+entrada
    mover2=mover+mover-kerf-entrada
    gx=1
    gy=0
    divX=txd+lcorte
    mx=chapaX/divX
    l=0
    pecasFeitas=0

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    divX=txd+lcorte+lcorte
    mx=chapaX/divX
    mx=(float(int(mx))*2.0)
    mx=int(mx)

    divY=tyd+lcorte+lcorte
    my=chapaY/divY
    my=int(my)

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        
        if (pecasFeitas==0):
            #Gerar primeira peça            
            programa=programa + "G00 X" + str(txf) + " Y-" + str(entrada) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa=programa + "G01 X" + str(txf) + " Y-" + str(tyf) + '\n'
            distCorte+=calcularHipotenusa(txf, tyf)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + fcorte + '\n'

            impar=True    
            pecasFeitas=1
            gx=1
            mov=1

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1):
            #Movimentar para a segunda peça

            programa=programa + "G00 X" + str(kerf) + " Y" + str(entrada) + '\n'
            
            mov=0

        elif (pecasFeitas<pecas and gx+1<mx and l==0 and mov==0 and impar==True):
            #Gerar demais peças ímpares da primeira linha

            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=1
            impar=False


        elif (pecasFeitas<pecas and gx+1<mx and l==0 and gy<my and mov==1 and impar==False):            
            #Movimento - peças impares para pares da primeira linha
            
            programa=programa + "G00 X" + str(tx+kerf+kerf) + " Y-" + str(ty+kerf) + '\n'

            mov=0

        elif (pecasFeitas<pecas and gx+1<mx and l==0 and gy<my and mov==0 and impar==False):            
            #Geração das demais peças pares da primeira linha

            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + "G01 X-" + str(txf) + " Y" + str(tyf) + '\n'
            distCorte+=calcularHipotenusa(txf, tyf)
            programa+= "G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=1
            impar=True
            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==1 and impar==True):            
            #Movimento - peças pares para impares da primeira linha
            
            programa=programa + "G00 X" + str(tx+kerf+kerf+entrada) + " Y-" + str(ty+kerf) + '\n'

            mov=0

        elif (pecasFeitas<pecas and gx<=mx and l==0 and mov==0 and impar==True):
            #Gerar últimas peças ímpares da primeira linha
            
            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=1
            gy+=1
            mov=3
            impar=False
            l=1

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==3 and impar==False):            
            #Movimento entre linhas - primeira peça das demais linhas

            mover=float((mx-1))*lcorte
            mover+=float((mx-2))*float(txd)*0.5
            mover-=float(kerf)
            programa=programa + "G00 X-" + str(mover) + " Y" + str(lcorte) + '\n'

            mov=0

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==0 and impar==False):            
            #Geração da primeira peça par das demais linhas

            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=ty
            programa=programa + "G01 X" + str(tx) + " Y-" + str(ty) + '\n'
            distCorte+=calcularHipotenusa(tx, ty)
            programa=programa + "G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + fcorte + '\n'

            mov=2
            gx+=1
            l=3
            pecasFeitas+=1
            impar=True

        elif (pecasFeitas<pecas and gx==2 and l==3 and gy<my and mov==2 and impar==True):            
            #Movimento - movimentação para a primeira peça ímpar das demais linhas

            programa=programa + "G01 X" + str(entrada+lcorte) + '\n'

            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==3 and gy<my and mov==1 and impar==True):            
            #Geração das demais peças impares das demais linhas

            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + fcorte + '\n'

            mov=2
            gx+=1
            l=3
            pecasFeitas+=1
            impar=False

        elif (pecasFeitas<pecas and gx<=mx and l==3 and gy<my and mov==2 and impar==False):            
            #Movimento - peças impares para pares das demais linhas


            programa=programa + "G00 X" + str(tx+lcorte) + " Y-" + str(ty+kerf) + '\n'

            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==3 and gy<my and mov==1 and impar==False):            
            #Geração das peças pares das demais linhas

            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + "G01 X-" + str(txf) + " Y" + str(tyf) + '\n'
            distCorte+=calcularHipotenusa(txf, tyf)
            programa+= "G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + fcorte + '\n'

            mov=2
            gx+=1
            l=3
            pecasFeitas+=1
            impar=True

        elif (pecasFeitas<pecas and gx<=mx and gx!= 2 and l==3 and gy<my and mov==2 and impar==True):            
            #Movimento - peças pares para ímpares das demais linhas

            programa=programa + "G00 X" + str(tx+kerf+kerf+entrada) + " Y-" + str(ty+kerf) + '\n'

            mov=1

        elif (pecasFeitas<pecas and gx==mx and l==3 and gy<my and mov==1 and impar==True):            
            #Geração da última peça das demais linhas

            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=txf
            programa=programa + fcorte + '\n'

            mov=3
            gx=1
            gy+=1
            l=3
            pecasFeitas+=1
            impar=False

        elif (gy==my or pecasFeitas==pecas):
            break
        else:
            break

    programa=programa + "M02"
    #Retornar a quantidade de peças feitas e o programa
    return pecasFeitas, programa, distCorte

#TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, kerf)
#pula, prg, pula = TrianguloRetangulo("100", "200", "5", "500", "0", "15", "1.2")
#Auxiliares.escreverPrograma(prg, "/home/henrique/linuxcnc/nc_files/a.ngc")
#############################################################################################################################################

def RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, kerf):
#Para adaptar
    #Garantir que as variaveis sao do tipo float
    txd=float(txd)
    tyd=float(tyd)
    furo=float(furo)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<txd:
        chapaX=txd+1
    if chapaY<tyd:
        chapaY=tyd+1

    #Calculo de tamanhos
    furo=float(furo)-kerf
    raio=float(furo)/2.0
    lcorte=kerf+kerf
    tx=txd+kerf
    mtx=float(tx)/2.0
    txf=txd+lcorte
    mtxf=float(txf)/2.0
    ty=tyd+kerf
    mty=float(ty)/2.0
    tyf=tyd+lcorte
    mtyf=float(tyf)/2.0
    mover=tx+kerf+entrada
    mover2=mover+mover-kerf-entrada
    gx=1
    gy=0
    divX=txd+lcorte
    mx=chapaX/divX
    l=0
    pecasFeitas=0

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    divX=txd+lcorte
    mx=chapaX/divX
    mx=int(mx)

    divY=tyd+lcorte
    my=chapaY/divY
    my=int(my)
    seq=0

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        if (pecasFeitas==0) or seq==1:
            #Gerar primeira peça
            programa=programa + "G00 X" + str(mtxf+raio-entrada) + " Y" + str(mtyf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa+= "G00 X" + str(mtxf-raio+entrada) + " Y-" + str(mtyf+entrada) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + "G01 X-" + str(txf) + '\n'
            distCorte+=float(txf)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            programa=programa + "G01 X" + str(txf) + '\n'
            distCorte+=float(txf)
            tyfEentrada=tyf + entrada
            programa=programa + "G01 Y-" + str(tyfEentrada) + '\n'
            distCorte+=float(tyfEentrada)
            programa=programa + fcorte + '\n'

            if mx==2:
                seq=4

            if mx==1:
                seq=5
    
            pecasFeitas=1
            gx=gx+1
            mov=1

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1) or (seq==2 and gy<my):
            #Gerar segunda peça
            programa=programa + "G00 X" + str(mtxf+raio-entrada+kerf) + " Y" + str(mtyf+entrada) + '\n'
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(mtxf+raio-entrada) + " Y-" + str(mtyf) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(tx) + '\n'
            distCorte+=float(tx)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=0

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==0) or (seq==3 and gy<my):            
            #Gerar demais peças da primeira linha
            programa=programa + "G00 X" + str(mtxf+raio+txf) + " Y-" + str(mtyf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(mtxf+raio-entrada) + " Y-" + str(mtyf) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(tx) + '\n'
            distCorte+=float(tx)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my) or (seq==4 and gy<my):
            #Gerar ultima peça da primeira linha
            tyEkerf=ty+kerf
            if mx==2:
                programa=programa + "G00 X" + str(mtxf+raio-entrada+kerf) + " Y" + str(mtyf+entrada) + '\n'
            else:
                programa=programa + "G00 X" + str(mtxf+raio+txf) + " Y-" + str(mtyf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(mtxf+raio-entrada) + " Y-" + str(mtyf) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(tx) + '\n'
            distCorte+=float(tx)
            programa=programa + "G01 Y" + str(tyf) + '\n'
            distCorte+=float(tyf)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'

            if mx==2:
                seq=5

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1

        elif (pecasFeitas<pecas and gx==1 and gy<my) or (seq==5 and gy<my):
            #Gerar primeira peça das demais linhas
            if mx==1:
                if gy==0:
                    programa=programa + "G00 X" + str(mtxf+raio-entrada-txf) + " Y" + str(tyfEentrada+mtyf+kerf) + '\n'
                    gy+=2
                else:
                    programa=programa + "G00 X" + str(mtxf+raio-txf) + " Y" + str(tyf+mtyf) + '\n'
                    gy+=1
            else:
                programa=programa + "G00 X-" + str((txf*(mx-1))-mtxf-raio+kerf) + " Y" + str(mtyf+kerf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X-" + str(mtxf+raio-entrada) + " Y-" + str(mtyf) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=float(ty)
            programa=programa + "G01 X" + str(txf) + '\n'
            distCorte+=float(txf)
            programa=programa + "G01 Y-" + str(ty) + '\n'
            distCorte+=float(ty)
            programa=programa + "G01 X-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'
            if mx==1:
                pass
            else:
                if (pecasFeitas<pecas and gx<mx and gy<my):
                    programa=programa + "G00 X" + str(kerf+mtxf+raio) + " Y" + str(mtyf) + '\n'

            if mx==2:
                seq=7

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx<mx and gy<my) or (seq==6 and gy<my):
            #Gerar demais peças das demais linhas
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X" + str(tx-mtxf-raio+entrada) + " Y-" + str(mtyf) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=float(ty)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'
            if (pecasFeitas<pecas and gx<mx and gy<my) or (pecasFeitas<pecas and gx==mx and gy<my):
                programa=programa + "G00 X" + str(mtxf+raio+txf) + " Y-" + str(mtyf-kerf) + '\n'             

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and gy<my) or (seq==7 and gy<my):
            #Gerar ultima peça das demais linhas
            programa=programa + str(icorte) + '\n'
            programa+="G01 X" + str(entrada) + '\n'
            distCorte+=entrada
            programa+="G03 X0.000 Y0.000 I-" + str(raio) + " J0.000\n"
            distCorte+=distCirculoRaio(raio)
            programa+="G01 X-" + str(entrada) + '\n'
            distCorte+=entrada
            programa=programa + str(fcorte) + '\n'

            programa=programa + "G00 X" + str(tx-mtxf-raio+entrada) + " Y-" + str(mtyf) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 Y" + str(ty) + '\n'
            distCorte+=float(ty)
            txEentrada=tx + entrada
            programa=programa + "G01 X-" + str(txEentrada) + '\n'
            distCorte+=float(txEentrada)
            programa=programa + fcorte + '\n'

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
        elif (gy==my or pecasFeitas==pecas):
            break
        else:
            break
  
    programa=programa + "M02"
        
    return pecasFeitas, programa, distCorte

#pecasFeitas, prg, distCorte = RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, kerf)
#pecasFeitas, prg, distCorte = RetanguloFuro("246", "305", "120", "3", "0", "0", "8", "1.5")
#Auxiliares.escreverPrograma(prg, "/home/henrique/linuxcnc/nc_files/a.ngc")
###################################################################################################################################
def TrianguloPontasCortadas(txd, tyd, chfXd, chfYd, entrada, chapaX, chapaY, pecas, kerf):
    #Garantir que as variaveis sao do tipo float
    txd=float(txd)
    tyd=float(tyd)
    chfXd=float(chfXd)
    chfYd=float(chfYd)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<txd:
        chapaX=txd+1
    if chapaY<tyd:
        chapaY=tyd+1

    #Calculo de tamanhos
    lcorte=kerf+kerf
    tx=txd+kerf
    txf=txd+lcorte
    ty=tyd+kerf
    tyf=tyd+lcorte
    chanfroX=chfXd+kerf
    chanfroY=chfYd+kerf
    mover=tx+kerf+entrada
    mover2=mover+mover-kerf-entrada
    gx=1
    gy=0
    divX=txd+lcorte
    mx=chapaX/divX
    l=0
    pecasFeitas=0

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    divX=txf+1
    mx=chapaX/divX
    
    mx=(float(int(mx))*2.0)
    mx=int(mx)

    divY=tyf+lcorte+kerf+chanfroY+((tyf-chanfroY)*(chanfroX/(txf-chanfroX)))
    my=chapaY/divY
    my=int(my)
    direita=False
    esquerda=True
    
    #Verificar se mx/2 é par
    resA=float(mx)/4.0
    resB=int(mx)/4
    if float(resA)==float(resB):
        mxPar=True
    else:
        mxPar=False

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        
        if (pecasFeitas==0):
            #Gerar primeira peça
            #print "Gerar primeira peça"
            programa+= "G00 X" + str(txf) + " Y-" + str(entrada) + '\n'
            programa+= str(icorte) + '\n'
            programa+= "G01 Y" + str(entrada) + '\n'
            distCorte+=entrada
            programa+= "G01 X-" + str(txf) + '\n'
            distCorte+=txf
            programa+= "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa+="G01 X" + str(chanfroX) + '\n'
            distCorte+=chanfroX
            programa+= "G01 X" + str((txf-chanfroX)) + " Y-" + str((tyf-chanfroY)) + '\n'
            distCorte+=calcularHipotenusa((txf-chanfroX), (tyf-chanfroY))
            programa+= "G01 Y-" + str(chanfroY+entrada) + '\n'
            distCorte+=chanfroY+entrada
            programa+= fcorte + '\n'

            impar=True
            pecasFeitas=1
            gx=1
            mov=1

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1):
            #Movimentar para a segunda peça
            #print "Movimentar para a segunda peça"
            programa+= "G00 X-" + str(txf-chanfroX) + " Y" + str(tyf+entrada) + '\n'
            
            mov=0

        elif (pecasFeitas<pecas and gx+1<mx and l==0 and mov==0 and impar==True):
            #Gerar demais peças ímpares da primeira linha
            #print "Gerar demais peças ímpares da primeira linha"
            #print direita
            #print esquerda
            if direita==False:
                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X-" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                if gx==1:
                    programa+= "G01 Y" + str(chanfroY) + '\n'
                    distCorte+=chanfroY
                else:
                    programa+= fcorte + '\n'
                    programa+= "G00 Y" + str(chanfroY) + '\n'
                    programa+= icorte + '\n'
                programa+= "G01 X" + str(txf) + '\n'
                distCorte+=txf
                programa+= "G01 Y-" + str(tyf) + '\n'
                distCorte+=tyf
                programa+= "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX            
                programa+= fcorte + '\n'
                esquerda=False

            if direita==True:
                programa=programa + icorte + '\n'
                programa+= "G01 X" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa=programa + fcorte + '\n'

                mover=(tyf-chanfroY)-(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G00 X" + str((txf-chanfroX-chanfroX)) + " Y" + str(mover) + '\n'

                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                programa+= "G01 Y" + str(chanfroY) + '\n'
                distCorte+=chanfroY
                programa+= "G01 X-" + str(txf) + '\n'
                distCorte+=txf
                
                programa=programa + fcorte + '\n'
                esquerda==True

            if esquerda==True:
                direita=False
            if esquerda==False:
                direita=True

            #print direita
            #print esquerda
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=1
            impar=False


        elif (pecasFeitas<pecas and gx+1<mx and l==0 and gy<my and mov==1 and impar==False):            
            #Movimento - peças impares para pares da primeira linha
            #print "Movimento - peças impares para pares da primeira linha"
            mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
            mover=round(mover, 4)
            if direita==True:
                programa=programa + "G00 X" + str(chanfroX) + " Y-" + str(mover+chanfroY) + '\n'
            if direita==False:
                mover=tyf+chanfroY+((tyf-chanfroY)*(chanfroX/(txf-chanfroX)))
                mover=round(mover, 4)
                programa=programa + "G00 X" + str(txf) + " Y-" + str(mover) + '\n'


            mov=0

        elif (pecasFeitas<pecas and gx+1<mx and l==0 and gy<my and mov==0 and impar==False):            
            #Geração das demais peças pares da primeira linha
            #print "Geração das demais peças pares da primeira linha"
            #print direita
            #print esquerda
            
            if direita==False:
                programa=programa + icorte + '\n'
                programa+= "G01 X" + str(txf) + '\n'
                distCorte+=txf
                programa+= "G01 Y" + str(chanfroY) + '\n'
                distCorte+=chanfroY
                programa+= "G01 X-" + str((txf-chanfroX)) + " Y" + str((tyf-chanfroY)) + '\n'
                distCorte+=calcularHipotenusa((txf-chanfroX), (tyf-chanfroY))
                programa+= "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa=programa + fcorte + '\n'
                esquerda=False

            if direita==True:
                programa=programa + icorte + '\n'
                programa+= "G01 X" + str(txf) + '\n'
                distCorte+=txf
                programa=programa + "G01 Y" + str(tyf) + '\n'
                distCorte+=tyf
                programa=programa + "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa+= "G01 X-" + str((txf-chanfroX)) + " Y-" + str((tyf-chanfroY)) + '\n'
                distCorte+=calcularHipotenusa((txf-chanfroX), (tyf-chanfroY))
                programa=programa + fcorte + '\n'
                esquerda=True

            #print direita
            #print esquerda
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=1
            impar=True
            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==1 and impar==True):            
            #Movimento - peças pares para impares da primeira linha
            #print "Movimento - peças pares para impares da primeira linha"          
            #programa=programa + "G00 X" + str(tx+kerf+kerf+entrada) + " Y-" + str(ty+kerf) + '\n'
            if direita==True:
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+="G00 Y" + str(mover) + '\n'
            if direita==False:
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+="G00 X" + str(chanfroX) + '\n'

            mov=0

        elif (pecasFeitas<pecas and gx<=mx and l==0 and mov==0 and impar==True):
            #Gerar últimas peças ímpares da primeira linha
            #print "Gerar últimas peças ímpares da primeira linha"
            if mxPar==False:
                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X-" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                if gx==1:
                    programa+= "G01 Y" + str(chanfroY) + '\n'
                else:
                    programa+= fcorte + '\n'
                    programa+= "G00 Y" + str(chanfroY) + '\n'
                    programa+= icorte + '\n'
                programa+= "G01 X" + str(txf) + '\n'
                distCorte+=txf
                programa+= "G01 Y-" + str(tyf) + '\n'
                distCorte+=tyf
                programa+= "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX            
                programa+= fcorte + '\n'
            if mxPar==True:
                programa=programa + icorte + '\n'
                programa+= "G01 X" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa=programa + fcorte + '\n'

                mover=(tyf-chanfroY)-(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)

                programa+= "G00 X" + str((txf-chanfroX-chanfroX)) + " Y" + str(mover) + '\n'

                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                programa+= "G01 Y" + str(chanfroY) + '\n'
                distCorte+=chanfroY
                programa+= "G01 X-" + str(txf) + '\n'
                distCorte+=txf
                
                programa=programa + fcorte + '\n'

                
            pecasFeitas=pecasFeitas+1
            gx=1
            gy+=1
            mov=3
            impar=False
            l=1

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==3 and impar==False):            
            #Movimento entre linhas - primeira peça das demais linhas
            #print "Movimento entre linhas - primeira peça das demais linhas"
            if mxPar==False:
                mover=float(((mx/2)*txf)-chanfroX)
                mover=round(mover, 4)
                programa+="G00 X-" + str(mover) + " Y" + str(tyf) + '\n'
            if mxPar==True:
                mover=float(((mx/2)-1)*txf)
                mover=round(mover, 4)
                programa+="G00 X-" + str(mover) + '\n'

            mov=0

        elif (pecasFeitas<pecas and gx==1 and gy<my and mov==0 and impar==False):            
            #Geração da primeira peça par das demais linhas
            #print "Geração da primeira peça par das demais linhas"
            programa+= str(icorte) + '\n'
            programa+= "G01 Y" + str(tyf) + '\n'
            distCorte+=tyf
            programa+="G01 X" + str(chanfroX) + '\n'
            distCorte+=chanfroX
            programa+= "G01 X" + str((txf-chanfroX)) + " Y-" + str((tyf-chanfroY)) + '\n'
            distCorte+=calcularHipotenusa((txf-chanfroX), (tyf-chanfroY))
            programa+= "G01 Y-" + str(chanfroY) + '\n'
            distCorte+=chanfroY
            programa+= fcorte + '\n'

            impar=True
            direita=False
            esquerda=True

            mov=2
            gx+=1
            l=3
            pecasFeitas+=1
            impar=True

        elif (pecasFeitas<pecas and gx==2 and l==3 and gy<my and mov==2 and impar==True):            
            #Movimento - movimentação para a primeira peça ímpar das demais linhas
            #print "Movimento - movimentação para a primeira peça ímpar das demais linhas"
            programa+= "G00 X-" + str(txf-chanfroX) + " Y" + str(tyf) + '\n'

            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==3 and gy<my and mov==1 and impar==True):            
            #Geração das demais peças impares das demais linhas
            #print "Geração das demais peças impares das demais linhas"
            #print direita
            #print esquerda
            #print "aqui"
            #print gx
            if direita==False:
                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X-" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                if gx==2:
                    programa+= "G01 Y" + str(chanfroY) + '\n'
                    distCorte+=chanfroY
                else:
                    programa+= fcorte + '\n'
                    programa+= "G00 Y" + str(chanfroY) + '\n'
                    programa+= icorte + '\n'
                programa+= "G01 X" + str(txf) + '\n'
                distCorte+=txf
                programa+= "G01 Y-" + str(tyf) + '\n'
                distCorte+=tyf
                programa+= "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX            
                programa+= fcorte + '\n'
                esquerda=False

            if direita==True:
                programa=programa + icorte + '\n'
                programa+= "G01 X" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa=programa + fcorte + '\n'

                mover=(tyf-chanfroY)-(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G00 X" + str((txf-chanfroX-chanfroX)) + " Y" + str(mover) + '\n'

                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                programa+= "G01 Y" + str(chanfroY) + '\n'
                distCorte+=chanfroY
                programa+= "G01 X-" + str(txf) + '\n'
                distCorte+=txf
                
                programa=programa + fcorte + '\n'
                esquerda==True

            if esquerda==True:
                direita=False
            if esquerda==False:
                direita=True

            #print direita
            #print esquerda

            mov=2
            gx+=1
            l=3
            pecasFeitas+=1
            impar=False

        elif (pecasFeitas<pecas and gx<=mx and l==3 and gy<my and mov==2 and impar==False):            
            #Movimento - peças impares para pares das demais linhas
            #print "Movimento - peças impares para pares das demais linhas"
            mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
            mover=round(mover, 4)
            if direita==True:
                programa=programa + "G00 X" + str(chanfroX+txf) + " Y-" + str(mover+chanfroY) + '\n'
            if direita==False:
                mover=tyf+chanfroY+((tyf-chanfroY)*(chanfroX/(txf-chanfroX)))
                mover=round(mover, 4)
                programa=programa + "G00 X" + str(txf+txf) + " Y-" + str(mover) + '\n'

            mov=1

        elif (pecasFeitas<pecas and gx<mx and l==3 and gy<my and mov==1 and impar==False):            
            #Geração das peças pares das demais linhas
            #print "Geração das peças pares das demais linhas"
            if direita==False:
                programa=programa + icorte + '\n'
                programa+= "G01 Y" + str(chanfroY) + '\n'
                distCorte+=chanfroY
                programa+= "G01 X-" + str((txf-chanfroX)) + " Y" + str((tyf-chanfroY)) + '\n'
                distCorte+=calcularHipotenusa((txf-chanfroX), (tyf-chanfroY))
                programa+= "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa=programa + fcorte + '\n'
                esquerda=False

            if direita==True:
                programa=programa + icorte + '\n'
                programa=programa + "G01 Y" + str(tyf) + '\n'
                distCorte+=tyf
                programa=programa + "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa+= "G01 X-" + str((txf-chanfroX)) + " Y-" + str((tyf-chanfroY)) + '\n'
                distCorte+=calcularHipotenusa((txf-chanfroX), (tyf-chanfroY))
                programa=programa + fcorte + '\n'
                esquerda=True

            #print direita
            #print esquerda
            
            mov=2
            gx+=1
            l=3
            pecasFeitas+=1
            impar=True

        elif (pecasFeitas<pecas and gx<=mx and gx!= 2 and l==3 and gy<my and mov==2 and impar==True):            
            #Movimento - peças pares para ímpares das demais linhas
            #print "Movimento - peças pares para ímpares das demais linhas"
            if direita==True:
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+="G00 Y" + str(mover) + '\n'
            if direita==False:
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+="G00 X" + str(chanfroX) + '\n'

            mov=1

        elif (pecasFeitas<pecas and gx==mx and l==3 and gy<my and mov==1 and impar==True):            
            #Geração da última peça das demais linhas
            #print "Geração da última peça das demais linhas"
            if mxPar==False:
                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X-" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                if gx==2:
                    programa+= "G01 Y" + str(chanfroY) + '\n'
                else:
                    programa+= fcorte + '\n'
                    programa+= "G00 Y" + str(chanfroY) + '\n'
                    programa+= icorte + '\n'
                programa+= "G01 X" + str(txf) + '\n'
                distCorte+=txf
                programa+= "G01 Y-" + str(tyf) + '\n'
                distCorte+=tyf
                programa+= "G01 X-" + str(chanfroX) + '\n'
                distCorte+=chanfroX            
                programa+= fcorte + '\n'

            if mxPar==True:
                programa=programa + icorte + '\n'
                programa+= "G01 X" + str(chanfroX) + '\n'
                distCorte+=chanfroX
                programa=programa + fcorte + '\n'

                mover=(tyf-chanfroY)-(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G00 X" + str((txf-chanfroX-chanfroX)) + " Y" + str(mover) + '\n'

                programa+= icorte + '\n'
                mover=(tyf-chanfroY)*(chanfroX/(txf-chanfroX))
                mover=round(mover, 4)
                programa+= "G01 X" + str(chanfroX) + " Y" + str(mover) + '\n'
                distCorte+=calcularHipotenusa(chanfroX, mover)
                programa+= "G01 Y" + str(chanfroY) + '\n'
                distCorte+=chanfroY
                programa+= "G01 X-" + str(txf) + '\n'
                distCorte+=txf

            mov=3
            gx=1
            gy+=1
            l=3
            pecasFeitas+=1
            impar=False

        elif (gy==my or pecasFeitas==pecas):
            break
        else:
            break

    programa=programa + "M02"
    #Retornar a quantidade de peças feitas e o programa
    return pecasFeitas, programa, distCorte

#pula, prg, pula = TrianguloPontasCortadas(txd, tyd, chfXd, chfYd, entrada, chapaX, chapaY, pecas, kerf)
#pula, prg, pula = TrianguloPontasCortadas("150", "250", "10", "15", "5", "0", "0", "142", "1.5")
#Auxiliares.escreverPrograma(prg, "/home/henrique/linuxcnc/nc_files/a.ngc")
#################################################################################################################################
###################################################################################################################################
def RetanguloChanfrado(txd, tyd, chanfroXs, chanfroYs, chanfroXi, chanfroYi, entrada, chapaX, chapaY, pecas, kerf):

    #Garantir que as variaveis sao do tipo float
    txd=float(txd)
    tyd=float(tyd)
    chanfroXs=float(chanfroXs)
    chanfroYs=float(chanfroYs)
    chanfroXi=float(chanfroXi)
    chanfroYi=float(chanfroYi)
    entrada=float(entrada)
    chapaX=float(chapaX)
    chapaY=float(chapaY)
    pecas=float(pecas)
    kerf=float(kerf)
    distCorte=0.0

    #Valor das linhas com compensação
    def adicional(a, b, kerf):
        calc1=atan(float(b)/float(a))
        calc1=calc1/2.0
        calc2=tan(calc1)*kerf
        return calc2

    #linhas normais
    addXs=adicional(chanfroXs, chanfroYs, kerf)
    ktxs=txd+addXs+addXs-chanfroXs-chanfroXs
    ktxs=("%.4f" % ktxs)
    
    addYs=adicional(chanfroYs, chanfroXs, kerf)
    addYi=adicional(chanfroYi, chanfroXi, kerf)
    kty=tyd+addYs+addYi-chanfroYs-chanfroYi
    kty=("%.4f" % kty)
    
    addXi=adicional(chanfroXi, chanfroYi, kerf)
    ktxi=txd+addXi+addXi-chanfroXi-chanfroXi
    ktxi=("%.4f" % ktxi)
    
    #linhas dos chanfros
    kcxs=chanfroXs+kerf-addXs
    kcxs=("%.4f" % kcxs)
    kcys=chanfroYs+kerf-addYs
    kcys=("%.4f" % kcys)
    kcxi=chanfroXi+kerf-addXi
    kcxi=("%.4f" % kcxi)
    kcyi=chanfroYi+kerf-addYi
    kcyi=("%.4f" % kcyi)
    def mostrarValores():
        print("ktxs:" + str(ktxs))
        print("ktxi:" + str(ktxi))
        print("kty:" + str(kty))
        print()
        print("kcxs:" + str(kcxs))
        print("kcys:" + str(kcys))
        print("kcxi:" + str(kcxi))
        print("kcyi:" + str(kcyi))
    #mostrarValores()
    
    #Ajustar chapa
    if chapaX == 0:
        chapaX=mesaX
    if chapaY == 0:
        chapaY=mesaY
    if chapaX<txd:
        chapaX=txd+1
    if chapaY<tyd:
        chapaY=tyd+1

    #Calculo de tamanhos
    lcorte=kerf+kerf
    tx=txd+kerf
    txf=txd+lcorte
    ty=tyd+kerf
    tyf=tyd+lcorte
    mover=tx+kerf+entrada
    mover=round(mover, 4)
    mover2=mover+mover-kerf-entrada
    gx=1
    gy=0
    divX=txd+lcorte
    mx=chapaX/divX
    l=0
    pecasFeitas=0
    linhaPar=False

    #Introducao do programa
    programa="G21" + '\n' + "G91" + '\n'

    #Calculo de pecas por linha
    divX=float(kcxs)+float(ktxs)+float(kcxs)
    mx=chapaX/divX
    mx=int(mx)

    divY=float(kcyi)+float(kty)+float(kcys)
    my=chapaY/divY
    my=int(my)
    seq=0

    #Inicio do loop de geraçao das peças
    while pecasFeitas<pecas:
        if (pecasFeitas==0) or seq==1:
            #Gerar primeira peça
            distX=float(ktxi)+float(kcxi)
            distX=("%.4f" % distX)
            programa=programa + "G00 X" + str(distX) + " Y-" + str(entrada) + '\n'
            programa=programa + str(icorte) + '\n'
            programa=programa + "G01 Y" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + "G01 X-" + str(ktxi) + '\n'
            distCorte+=float(ktxi)
            programa=programa + "G01 X-" + str(kcxi) + ' Y' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 Y" + str(kty) + '\n'
            distCorte+=float(kty)
            programa=programa + "G01 X" + str(kcxs) + ' Y' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 X" + str(ktxs) + '\n'
            distCorte+=float(ktxs)
            programa=programa + "G01 X" + str(kcxs) + ' Y-' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 Y-" + str(kty) + '\n'
            distCorte+=float(kty)
            programa=programa + "G01 X-" + str(kcxi) + ' Y-' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'

            if mx==2:
                seq=4

            if mx==1:
                linhaPar=False
                seq=5
                gy=1
    
            pecasFeitas=1
            gx=gx+1
            mov=1

        elif (pecasFeitas==1 and gx<mx and l==0 and mov==1) or (seq==2 and gy<my):
            #Gerar segunda peça
            distY=float(entrada)+float(kcyi)
            distY=("%.4f" % distY)
            programa=programa + "G00 X" + str(kcxi) + " Y" + str(distY) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(kcxi) + ' Y-' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 X" + str(ktxi) + '\n'
            distCorte+=float(ktxi)
            programa=programa + "G01 X" + str(kcxi) + ' Y' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 Y" + str(kty) + '\n'
            distCorte+=float(kty)
            programa=programa + "G01 X-" + str(kcxs) + ' Y' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 X-" + str(ktxs) + '\n'
            distCorte+=float(ktxs)
            programa=programa + "G01 X-" + str(kcxs) + ' Y-' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            mov=0

        elif (pecasFeitas<pecas and gx<mx and l==0 and gy<my and mov==0) or (seq==3 and gy<my):            
            #Gerar demais peças da primeira linha
            distX=float(kcxs)+float(ktxs)+float(kcxs)
            distX=("%.4f" % distX)
            distY=float(kty)-float(entrada)
            distY=("%.4f" % distY)
            programa=programa + "G00 X" + str(distX) + " Y-" + str(distY) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(kcxi) + ' Y-' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 X" + str(ktxi) + '\n'
            distCorte+=float(ktxi)
            programa=programa + "G01 X" + str(kcxi) + ' Y' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 Y" + str(kty) + '\n'
            distCorte+=float(kty)
            programa=programa + "G01 X-" + str(kcxs) + ' Y' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 X-" + str(ktxs) + '\n'
            distCorte+=float(ktxs)
            programa=programa + "G01 X-" + str(kcxs) + ' Y-' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx==mx and l==0 and gy<my) or (seq==4 and gy<my):
            #Gerar ultima peça da primeira linha
            tyEkerf=ty+kerf
            if mx==2:
                distY=float(entrada)+float(kcyi)
                distY=("%.4f" % distY)
                programa=programa + "G00 X" + str(kcxi) + " Y" + str(distY) + '\n'
            else:
                distX=float(kcxs)+float(ktxs)+float(kcxs)
                distX=("%.4f" % distX)
                distY=float(kty)-float(entrada)
                distY=("%.4f" % distY)
                programa=programa + "G00 X" + str(distX) + " Y-" + str(distY) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(kcxi) + ' Y-' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 X" + str(ktxi) + '\n'
            distCorte+=float(ktxi)
            programa=programa + "G01 X" + str(kcxi) + ' Y' + str(kcyi) + '\n'
            distCorte+=calcularHipotenusa(kcxi, kcyi)
            programa=programa + "G01 Y" + str(kty) + '\n'
            distCorte+=float(kty)
            programa=programa + "G01 X-" + str(kcxs) + ' Y' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 X-" + str(ktxs) + '\n'
            distCorte+=float(ktxs)
            programa=programa + "G01 X-" + str(kcxs) + ' Y-' + str(kcys) + '\n'
            distCorte+=calcularHipotenusa(kcxs, kcys)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'

            if mx==2:
                seq=5

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
            linhaPar=True

        elif (pecasFeitas<pecas and gx==1 and gy<my) or (seq==5 and gy<my):
            #Gerar primeira peça das demais linhas
            if linhaPar==False and mx==1:
                linhaPar=True
            elif linhaPar==True and mx==1:
                linhaPar=False
            if linhaPar==False:
                nktxs=("%.4f" % float(ktxs))
                nktxi=("%.4f" % float(ktxi))
                nkty=("%.4f" % float(kty))
                nkcxs=("%.4f" % float(kcxs))
                nkcys=("%.4f" % float(kcys))
                nkcxi=("%.4f" % float(kcxi))
                nkcyi=("%.4f" % float(kcyi))
            if linhaPar==True:
                nktxs=("%.4f" % float(ktxi))
                nktxi=("%.4f" % float(ktxs))
                nkty=("%.4f" % float(kty))
                nkcxs=("%.4f" % float(kcxi))
                nkcys=("%.4f" % float(kcyi))
                nkcxi=("%.4f" % float(kcxs))
                nkcyi=("%.4f" % float(kcys))
                
            if mx==1:
                distX=float(nkcxs)+float(nktxs)+float(nkcxs)-float(nkcxs)-float(nkcxi)-float(entrada)
                distX=("%.4f" % distX)
                distY=float(kcys)+float(kty)+float(kcyi)
                
                if gy==1:
                    distX=float(distX)+float(entrada)
                    distY+=float(entrada)
                distY=("%.4f" % distY)
                programa=programa + "G00 X-" + str(distX) + " Y" + str(distY) + '\n'
            else:
                distX=float(kcxs)+float(ktxs)+float(kcxs)
                distX=(distX*(mx-2))+float(nkcxi)+float(nktxi)
                distX=("%.4f" % distX)
                distY=float(nkcyi)+float(entrada)
                distY=("%.4f" % distY)
                programa=programa + "G00 X-" + str(distX) + " Y" + str(distY) + '\n'
            programa=programa + icorte + '\n'
            programa=programa + "G01 X-" + str(nkcxi) + ' Y' + str(nkcyi) + '\n'
            distCorte+=calcularHipotenusa(nkcxi, nkcyi)
            programa=programa + "G01 Y" + str(nkty) + '\n'
            distCorte+=float(nkty)
            programa=programa + "G01 X" + str(nkcxs) + ' Y' + str(nkcys) + '\n'
            distCorte+=calcularHipotenusa(nkcxs, nkcys)
            programa=programa + "G01 X" + str(nktxs) + '\n'
            distCorte+=float(nktxs)
            programa=programa + "G01 X" + str(nkcxs) + ' Y-' + str(nkcys) + '\n'
            distCorte+=calcularHipotenusa(nkcxs, nkcys)
            programa=programa + "G01 Y-" + str(nkty) + '\n'
            distCorte+=float(nkty)
            programa=programa + "G01 X-" + str(nkcxi) + ' Y-' + str(nkcyi) + '\n'
            distCorte+=calcularHipotenusa(nkcxi, nkcyi)
            programa=programa + "G01 X-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'
            if mx==1:
                pass
            else:
                distX=float(entrada)+float(nkcxi)
                distX=("%.4f" % distX)
                programa=programa + "G00 X" + str(distX) + ' Y' + str(nkcyi) + '\n'

            if mx==2:
                seq=7

            if seq==5:
                gy+=1
                

            pecasFeitas=pecasFeitas+1
            gx=gx+1

        elif (pecasFeitas<pecas and gx<mx and gy<my) or (seq==6 and gy<my):
            #Gerar demais peças das demais linhas
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(nkcxi) + ' Y-' + str(nkcyi) + '\n'
            distCorte+=calcularHipotenusa(nkcxi, nkcyi)
            programa=programa + "G01 X" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'

            distX=float(nktxi)-float(entrada)
            distX=("%.4f" % distX)            
            programa=programa + "G00 X" + str(distX) + '\n'

            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(nkcxi) + ' Y' + str(nkcyi) + '\n'
            distCorte+=calcularHipotenusa(nkcxi, nkcyi)
            programa=programa + "G01 Y" + str(nkty) + '\n'
            distCorte+=float(nkty)
            programa=programa + "G01 X-" + str(nkcxs) + ' Y' + str(nkcys) + '\n'
            distCorte+=calcularHipotenusa(nkcxs, nkcys)
            programa=programa + "G01 X-" + str(nktxs) + '\n'
            distCorte+=float(nktxs)
            programa=programa + "G01 X-" + str(nkcxs) + ' Y-' + str(nkcys) + '\n'
            distCorte+=calcularHipotenusa(nkcxs, nkcys)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'
            
            pecasFeitas=pecasFeitas+1
            gx=gx+1
            if pecasFeitas<pecas:
                distX=float(kcxs)+float(ktxs)+float(kcxs)
                distX=("%.4f" % distX)
                distY=float(kty)-float(entrada)
                distY=("%.4f" % distY)
                programa=programa + "G00 X" + str(distX) + " Y-" + str(distY) + '\n'

        elif (pecasFeitas<pecas and gx==mx and gy<my) or (seq==7 and gy<my):
            #Gerar ultima peça das demais linhas
            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(nkcxi) + ' Y-' + str(nkcyi) + '\n'
            distCorte+=calcularHipotenusa(nkcxi, nkcyi)
            programa=programa + "G01 X" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'

            distX=float(nktxi)-float(entrada)
            distX=("%.4f" % distX)            
            programa=programa + "G00 X" + str(distX) + '\n'

            programa=programa + icorte + '\n'
            programa=programa + "G01 X" + str(nkcxi) + ' Y' + str(nkcyi) + '\n'
            distCorte+=calcularHipotenusa(nkcxi, nkcyi)
            programa=programa + "G01 Y" + str(nkty) + '\n'
            distCorte+=float(nkty)
            programa=programa + "G01 X-" + str(nkcxs) + ' Y' + str(nkcys) + '\n'
            distCorte+=calcularHipotenusa(nkcxs, nkcys)
            programa=programa + "G01 X-" + str(nktxs) + '\n'
            distCorte+=float(nktxs)
            programa=programa + "G01 X-" + str(nkcxs) + ' Y-' + str(nkcys) + '\n'
            distCorte+=calcularHipotenusa(nkcxs, nkcys)
            programa=programa + "G01 Y-" + str(entrada) + '\n'
            distCorte+=float(entrada)
            programa=programa + fcorte + '\n'

            if linhaPar==False:
                linhaPar=True
            else:
                linhaPar=False

            pecasFeitas=pecasFeitas+1
            l=l+1
            gy=gy+1
            gx=1
        elif (gy==my or pecasFeitas==pecas):
            break
        else:
            break
  
    programa=programa + "M02"
        
    return pecasFeitas, programa, distCorte

#pula, prg, pula = RetanguloChanfrado(txd, tyd, chanfroXs, chanfroYs, chanfroXi, chanfroYi, entrada, chapaX, chapaY, pecas, kerf)
#pula, prg, pula = RetanguloChanfrado("130", "270", "6", "11", "9", "13", "5", "669", "0", "23", "1.8")
#Auxiliares.escreverPrograma(prg, 'C:\\Users\\rique\\Desktop\\cnc\\teste.nc')
#############################################################################################################################################
