# -*- coding: utf-8 -*-

import wx
import os
import math
import platform
import gettext
import Oxicorte
import Plasma
import Auxiliares
import wx
import wx.grid as gridlib

sistemaOperacional=platform.system()
#print sistemaOperacional
AbrirIntro="Nao"
versao= "Versão " + Auxiliares.versao()
    
###################################################### I - Frame Home Gisoplox ###############################################################################
class Gisoplox(wx.Frame):
    def __init__(self, *args, **kwds):
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("Gisoplox")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((350, 500))
        self.Bind(wx.EVT_CLOSE, self.FecharGisoplox)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP,  self.OnClick)
        #self.posCtrl = wx.TextCtrl(self, -1, "", pos=(40, 350))

        #Criando o menu        
        menuBar = wx.MenuBar()
        menu = wx.Menu()

        #Menu opções/Teste
        #m_teste = menu.Append(wx.ID_ANY, "&Teste\tAlt-T", "Teste")
        #self.Bind(wx.EVT_MENU, self.AbrirTrianguloPontasCortadas, m_teste)

        #Menu opções/Estatísticas
        m_estat = menu.Append(wx.ID_ANY, "&Estatísticas\tAlt-E", "Estatísticas do histórico de corte")
        self.Bind(wx.EVT_MENU, self.AbrirEstat, m_estat)

        #Menu opções/Histórico
        m_hist = menu.Append(wx.ID_ANY, "&Histórico\tAlt-H", "Histórico de programas gerados")
        self.Bind(wx.EVT_MENU, self.AbrirHist, m_hist)
        
        #Menu opções/configurações
        m_config = menu.Append(wx.ID_ANY, "&Configurações\tAlt-C", "Configurações de escrita do código")
        self.Bind(wx.EVT_MENU, self.AbrirConfigurar, m_config)

        #Menu opções/Parâmetros de corte
        SubMenuKerf = wx.Menu()
        menu.Append(wx.ID_ANY, '&Parâmetros de corte', SubMenuKerf)
        m_kerf = SubMenuKerf.Append(wx.ID_ANY, "&Oxicorte\tCtrl-O", "Parâmetros de corte para oxicorte")
        m_kerfPlasma = SubMenuKerf.Append(wx.ID_ANY, "&Plasma\tCtrl-P", "Parâmetros de corte para corte a plasma")
        self.Bind(wx.EVT_MENU, self.AbrirKerf, m_kerf)
        self.Bind(wx.EVT_MENU, self.AbrirKerfPlasma, m_kerfPlasma)

        #Menu opções/sair
        menu.AppendSeparator()
        m_sair = menu.Append(wx.ID_EXIT, "S&air\tAlt-S", "Fechar o programa")
        self.Bind(wx.EVT_MENU, self.FecharGisoplox, m_sair)
        menuBar.Append(menu, "&Opções")

        #Menu Ferramentas
        menu = wx.Menu()
        menuBar.Append(menu, "&Ferramentas")

        #Sub-menu Ferramentas/retângulos
        SubMenuRetangulos = wx.Menu()
        menu.Append(wx.ID_ANY, 'R&etângulos', SubMenuRetangulos)
        #Ferramentas/retângulos/retângulo
        m_rectange = SubMenuRetangulos.Append(wx.ID_ANY, "&Retângulo\tCtrl-R", "Abrir a ferramenta de gerar retângulos")
        self.Bind(wx.EVT_MENU, self.AbrirRectange, m_rectange)
        #Ferramentas/retângulos/retângulo com furo central
        m_RetanguloFuro = SubMenuRetangulos.Append(wx.ID_ANY, "&Retângulo com furo central", "Abrir a ferramenta de gerar retângulos com furo central")
        self.Bind(wx.EVT_MENU, self.AbrirRetanguloFuro, m_RetanguloFuro)
        #Ferramentas/retângulos/retângulo chanfrado
        m_RetanguloChanfrado = SubMenuRetangulos.Append(wx.ID_ANY, "&Retângulo chanfrado", "Abrir a ferramenta de gerar retângulos chanfrados")
        self.Bind(wx.EVT_MENU, self.AbrirRetanguloChanfrado, m_RetanguloChanfrado)

        #Sub-menu Ferramentas/circulos
        SubMenuCirculos = wx.Menu()
        menu.Append(wx.ID_ANY, 'C&írculos', SubMenuCirculos)
        #Ferramentas/circulos/anel
        m_circle = SubMenuCirculos.Append(wx.ID_ANY, "&Anel\tCtrl-A", "Abrir a ferramenta de gerar anéis")
        self.Bind(wx.EVT_MENU, self.AbrirCircle, m_circle)
        #Ferramentas/circulos/círculo
        m_circleSimple = SubMenuCirculos.Append(wx.ID_ANY, "&Círculo\tCtrl-C", "Abrir a ferramenta de gerar círculos")
        self.Bind(wx.EVT_MENU, self.AbrirCircleSimple, m_circleSimple)

        #Sub-menu Ferramentas/triangulos
        SubMenuTriangulos = wx.Menu()
        menu.Append(wx.ID_ANY, 'T&riângulos', SubMenuTriangulos)
        m_triangulo = SubMenuTriangulos.Append(wx.ID_ANY, "&T&riângulo retângulo\tCtrl-T", "Abrir a ferramenta de gerar triângulos retângulos")
        self.Bind(wx.EVT_MENU, self.AbrirTriangulo, m_triangulo)
        m_trianguloPontasCortadas = SubMenuTriangulos.Append(wx.ID_ANY, "&T&riângulo com pontas cortadas", "Abrir a ferramenta de gerar triângulos com pontas cortadas")
        self.Bind(wx.EVT_MENU, self.AbrirTrianguloPontasCortadas, m_trianguloPontasCortadas)

        #Menu ajuda
        menu = wx.Menu()
        menuBar.Append(menu, "&Ajuda")
        #Menu ajuda/Estatísticas
        m_estat = menu.Append(wx.ID_ANY, "&Estatísticas\tAlt-E", "Estatísticas do histórico de corte")
        self.Bind(wx.EVT_MENU, self.AbrirEstat, m_estat)
        #Menu ajuda/Histórico
        m_hist = menu.Append(wx.ID_ANY, "&Histórico\tAlt-H", "Histórico de programas gerados")
        self.Bind(wx.EVT_MENU, self.AbrirHist, m_hist)
        #Menu ajuda/Sobre
        m_about = menu.Append(wx.ID_ABOUT, "&Sobre", "Informações sobre este programa")
        self.Bind(wx.EVT_MENU, self.AbrirAbout, m_about)
        
        self.SetMenuBar(menuBar)
        self.statusbar = self.CreateStatusBar()

        #Desenhando a interfácie
        #label_1 = wx.StaticText(self, wx.ID_ANY, "COMANDOS:", pos=(10,310))
        #label_1 = wx.StaticText(self, wx.ID_ANY, "Início de corte:", pos=(10,330))

    def OnPaint(self, evt):
        self.dc = wx.PaintDC(self)
        self.dc.SetPen(wx.Pen("grey",style=wx.TRANSPARENT))
        #self.dc.SetBrush(wx.Brush((102,255,102), wx.SOLID))
        self.dc.SetBrush(wx.Brush("gray", wx.SOLID))
        self.dc.DrawRectangle(25,25,100, 150)
        self.dc.DrawCircle(250,100,75)
        self.dc.DrawPolygon(((25, 225), (25, 375), (125, 375)))
        del self.dc

    def OnClick(self, event):
        pos = event.GetPosition()
        if pos.x>25 and pos.x<125 and pos.y>25 and pos.y<175:
            #print "Retangulo"
            frame_FormatosRetangulares.Show()
            frame_Gisoplox.Hide()
        if pos.x>175 and pos.x<325 and pos.y>25 and pos.y<175:
            #print "Circulo"
            frame_FormatosCirculares.Show()
            frame_Gisoplox.Hide()
        if pos.x>25 and pos.x<125 and pos.y>225 and pos.y<375:
            #print "Triangulo"
            frame_FormatosTriangulares.Show()
            frame_Gisoplox.Hide()
        #self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))
        
    def FecharGisoplox(self, event):
        #print "Fechando..."
        frame_Kerf.Destroy()
        frame_KerfPlasma.Destroy()
        frame_FormatosRetangulares.Destroy()
        frame_FormatosCirculares.Destroy()
        frame_FormatosTriangulares.Destroy()
        frame_Estat.Destroy()
        frame_Hist.Destroy()
        frame_Configurar.Destroy()
        frame_About.Destroy()
        frame_Gisoplox.Destroy()
        frame_Rectange.Destroy()
        frame_Circle.Destroy()
        frame_Triangulo.Destroy()
        frame_RetanguloFuro.Destroy()
        frame_RetanguloChanfrado.Destroy()
        frame_CircleSimple.Destroy()
        frame_TrianguloPontasCortadas.Destroy()

    def AbrirFormatosRetangulares(self, event):
        frame_FormatosRetangulares.Show()
        frame_Gisoplox.Hide()

    def AbrirFormatosCirculares(self, event):
        frame_FormatosCirculares.Show()
        frame_Gisoplox.Hide()

    def AbrirFormatosTriangulares(self, event):
        frame_FormatosTriangulares.Show()
        frame_Gisoplox.Hide()

    def AbrirEstat(self, event):
        frame_Estat.Show()
        frame_Gisoplox.Hide()

    def AbrirTeste(self, event):
        frame_RetanguloFuro.Show()
        frame_Gisoplox.Hide()

    def AbrirHist(self, event):
        frame_Hist.Show()
        frame_Gisoplox.Hide()

    def AbrirConfigurar(self, event):
        frame_Configurar.Show()
        frame_Gisoplox.Hide()

    def AbrirKerf(self, event):
        frame_Kerf.Show()
        frame_Gisoplox.Hide()

    def AbrirAbout(self, event):
        frame_About.Show()
        #frame_Gisoplox.Hide()

    def AbrirKerfPlasma(self, event):
        frame_KerfPlasma.Show()
        frame_Gisoplox.Hide()

    def AbrirRectange(self, event):
        frame_Rectange.Show()
        frame_Gisoplox.Hide()

    def AbrirCircle(self, event):
        frame_Circle.Show()
        frame_Gisoplox.Hide()

    def AbrirCircleSimple(self, event):
        frame_CircleSimple.Show()
        frame_Gisoplox.Hide()

    def AbrirTriangulo(self, event):
        frame_Triangulo.Show()
        frame_Gisoplox.Hide()

    def AbrirRetanguloFuro(self, event):
        frame_RetanguloFuro.Show()
        frame_Gisoplox.Hide()

    def AbrirRetanguloChanfrado(self, event):
        frame_RetanguloChanfrado.Show()
        frame_Gisoplox.Hide()

    def AbrirTrianguloPontasCortadas(self, event):
        frame_TrianguloPontasCortadas.Show()
        frame_Gisoplox.Hide()

########################################################### F - Frame Home Gisoplox ############################################################################################
############################################################## I - Frame Intro #################################################################################################
class Intro(wx.Frame):
    def __init__(self, *args, **kwds):
        # Detalhes do frame
        kwds["style"] = wx.BORDER_SIMPLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("Gisoplox")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((620, 170))
        self.SetBackgroundColour(wx.WHITE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_CLOSE, self.FecharIntro)
        self.Bind(wx.EVT_BUTTON, self.FecharIntro)
        self.Bind(wx.EVT_MOTION,  self.FecharIntro)

    def FecharIntro(self, event):
        frame_Intro.Destroy()
        frame_Gisoplox.Show()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        fundo=wx.Pen("#660066",50)
        dc.SetPen(fundo)

        #Retangulo roxo
        dc.SetBrush(wx.Brush('#660066'))
        dc.DrawRectangle(0,0,540,170)
        roxo=wx.Pen("#660066",100)
        dc.SetPen(roxo)

        #Amarelo do fogo
        amarelo=wx.Pen("#ffff00",12)
        dc.SetPen(amarelo)
        dc.DrawLine(13,102,19,92)
        dc.DrawLine(19,92,11,86)
        dc.DrawLine(11,86,23,84)
        dc.DrawLine(23,84,16,64)
        dc.DrawLine(12,64,24,74)
        dc.DrawLine(24,74,19,57)
        dc.DrawLine(19,57,26,57)
        dc.DrawLine(11,63,11,81)
        dc.DrawLine(21,46,22,47)
        

        #Vermelho do fogo
        vermelho=wx.Pen("#cc0000",7)
        dc.SetPen(vermelho)
        dc.DrawLine(10,127,10,110)
        dc.DrawLine(10,110,17,118)
        dc.DrawLine(17,118,17,105)
        dc.DrawLine(17,105,21,113)
        dc.DrawLine(21,113,21,98)
        dc.DrawLine(21,98,27,106)
        dc.DrawLine(27,106,25,90)
        dc.DrawLine(25,90,33,97)
        dc.DrawLine(33,97,28,80)
        dc.DrawLine(28,80,33,75)
        dc.DrawLine(33,75,28,65)
        dc.DrawLine(28,65,38,52)
        dc.DrawLine(38,52,28,51)
        dc.DrawLine(28,51,32,34)
        dc.DrawLine(32,34,24,47)
        dc.DrawLine(24,47,26,18)
        dc.DrawLine(26,18,21,38)
        dc.DrawLine(21,38,17,28)
        dc.DrawLine(17,28,17,50)
        dc.DrawLine(17,50,9,37)
        dc.DrawLine(9,37,12,58)
        dc.DrawLine(12,58,4,60)
        dc.DrawLine(4,60,9,77)
        dc.DrawLine(9,77,2,83)
        dc.DrawLine(2,83,8,97)
        dc.DrawLine(8,97,4,108)
        dc.DrawLine(4,108,11,114)

        #Escrevendo gisoplox
        fonte = wx.Font(80, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
		wx.FONTWEIGHT_BOLD, False, 'Courier New')
        dc = wx.PaintDC(self)
        dc.SetFont(fonte)
        dc.SetTextForeground('WHITE')
        dc.DrawText('GISOPLOX', 40, 30)

        #Desenhando cotas
        cotas=wx.Pen("#ff0000",3)
        dc.SetPen(cotas)
        dc.DrawLine(572,167,588,167)
        dc.DrawLine(572,2,588,2)
        dc.DrawLine(580,2,580,167)

        #Cota Superior
        dc.DrawLine(580,3,576,18)
        dc.DrawLine(580,3,584,18)
        dc.DrawLine(576,18,584,18)

        #Cota inferior
        dc.DrawLine(580,166,576,153)
        dc.DrawLine(580,166,584,153)
        dc.DrawLine(576,153,584,153)

        #Triangulo
        dc.SetBrush(wx.Brush('#ff0000'))
        dc.DrawPolygon(((587, 97), (611, 97), (599, 70)))

############################################################## F - Frame Intro #################################################################################################
############################################################## I - Frame About ####################################################################################################
class About(wx.Frame):
    def __init__(self, *args, **kwds):
        # Detalhes do frame
        #kwds["style"] =  wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.SetTitle("Gisoplox")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((430, 280))
        self.SetBackgroundColour(wx.WHITE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_CLOSE, self.FecharAbout)

    def FecharAbout(self, event):
        print("Fechando...")
        #frame_Gisoplox.Show()
        frame_About.Destroy()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        esc=0.7

        fundo=wx.Pen("#660066",int(50*esc))
        dc.SetPen(fundo)

        #Retangulo roxo
        dc.SetBrush(wx.Brush('#660066'))
        dc.DrawRectangle(0,0,int(540*esc),int(170*esc))
        fundo=wx.Pen("#ffffff",int(50*esc))
        dc.SetPen(fundo)
        dc.DrawLine(0,int(200*esc),int(700*esc),int(200*esc))

        #Amarelo do fogo
        amarelo=wx.Pen("#ffff00",int(12*esc))
        dc.SetPen(amarelo)
        dc.DrawLine(int(13*esc),int(102*esc),int(19*esc),int(92*esc))
        dc.DrawLine(int(19*esc),int(92*esc),int(11*esc),int(86*esc))
        dc.DrawLine(int(11*esc),int(86*esc),int(23*esc),int(84*esc))
        dc.DrawLine(int(23*esc),int(84*esc),int(16*esc),int(64*esc))
        dc.DrawLine(int(12*esc),int(64*esc),int(24*esc),int(74*esc))
        dc.DrawLine(int(24*esc),int(74*esc),int(19*esc),int(57*esc))
        dc.DrawLine(int(19*esc),int(57*esc),int(26*esc),int(57*esc))
        dc.DrawLine(int(11*esc),int(63*esc),int(11*esc),int(81*esc))
        dc.DrawLine(int(21*esc),int(46*esc),int(22*esc),int(47*esc))
        

        #Vermelho do fogo
        vermelho=wx.Pen("#cc0000",int(7*esc))
        dc.SetPen(vermelho)
        dc.DrawLine(int(10*esc),int(127*esc),int(10*esc),int(110*esc))
        dc.DrawLine(int(10*esc),int(110*esc),int(17*esc),int(118*esc))
        dc.DrawLine(int(17*esc),int(118*esc),int(17*esc),int(105*esc))
        dc.DrawLine(int(17*esc),int(105*esc),int(21*esc),int(113*esc))
        dc.DrawLine(int(21*esc),int(113*esc),int(21*esc),int(98*esc))
        dc.DrawLine(int(21*esc),int(98*esc),int(27*esc),int(106*esc))
        dc.DrawLine(int(27*esc),int(106*esc),int(25*esc),int(90*esc))
        dc.DrawLine(int(25*esc),int(90*esc),int(33*esc),int(97*esc))
        dc.DrawLine(int(33*esc),int(97*esc),int(28*esc),int(80*esc))
        dc.DrawLine(int(28*esc),int(80*esc),int(33*esc),int(75*esc))
        dc.DrawLine(int(33*esc),int(75*esc),int(28*esc),int(65*esc))
        dc.DrawLine(int(28*esc),int(65*esc),int(38*esc),int(52*esc))
        dc.DrawLine(int(38*esc),int(52*esc),int(28*esc),int(51*esc))
        dc.DrawLine(int(28*esc),int(51*esc),int(32*esc),int(34*esc))
        dc.DrawLine(int(32*esc),int(34*esc),int(24*esc),int(47*esc))
        dc.DrawLine(int(24*esc),int(47*esc),int(26*esc),int(18*esc))
        dc.DrawLine(int(26*esc),int(18*esc),int(21*esc),int(38*esc))
        dc.DrawLine(int(21*esc),int(38*esc),int(17*esc),int(28*esc))
        dc.DrawLine(int(17*esc),int(28*esc),int(17*esc),int(50*esc))
        dc.DrawLine(int(17*esc),int(50*esc),int(9*esc),int(37*esc))
        dc.DrawLine(int(9*esc),int(37*esc),int(12*esc),int(58*esc))
        dc.DrawLine(int(12*esc),int(58*esc),int(4*esc),int(60*esc))
        dc.DrawLine(int(4*esc),int(60*esc),int(9*esc),int(77*esc))
        dc.DrawLine(int(9*esc),int(77*esc),int(2*esc),int(83*esc))
        dc.DrawLine(int(2*esc),int(83*esc),int(8*esc),int(97*esc))
        dc.DrawLine(int(8*esc),int(97*esc),int(4*esc),int(108*esc))
        dc.DrawLine(int(4*esc),int(108*esc),int(11*esc),int(114*esc))

        #Escrevendo gisoplox
        fonte = wx.Font(int(80*esc), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
		wx.FONTWEIGHT_BOLD, False, 'Courier New')
        dc = wx.PaintDC(self)
        dc.SetFont(fonte)
        dc.SetTextForeground('WHITE')
        dc.DrawText('GISOPLOX', int(40*esc), int(30*esc))

        #Desenhando cotas
        cotas=wx.Pen("#ff0000",int(3*esc))
        dc.SetPen(cotas)
        dc.DrawLine(int(572*esc),int(167*esc),int(588*esc),int(167*esc))
        dc.DrawLine(int(572*esc),int(2*esc),int(588*esc),int(2*esc))
        dc.DrawLine(int(580*esc),int(2*esc),int(580*esc),int(167*esc))

        #Cota Superior
        dc.DrawLine(int(580*esc),int(3*esc),int(576*esc),int(18*esc))
        dc.DrawLine(int(580*esc),int(3*esc),int(584*esc),int(18*esc))
        dc.DrawLine(int(576*esc),int(18*esc),int(584*esc),int(18*esc))

        #Cota inferior
        dc.DrawLine(int(580*esc),int(166*esc),int(576*esc),int(153*esc))
        dc.DrawLine(int(580*esc),int(166*esc),int(584*esc),int(153*esc))
        dc.DrawLine(int(576*esc),int(153*esc),int(584*esc),int(153*esc))

        #Triangulo
        dc.SetBrush(wx.Brush('#ff0000'))
        #dc.DrawPolygon((int(587*esc), int(97*esc)), (int(611*esc), int(97*esc)), (int(599*esc), int(70*esc)))

        #Escrevendo dados
        dc.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
		wx.FONTWEIGHT_BOLD, False, 'Courier New'))
        dc.SetTextForeground('#000000')
        dc.DrawText(versao, 130, 150)
        dc.DrawText("Autor: Henrique Enzweiler", 80, 180)
        dc.DrawText("e-mail: henriqueenzweiler@gmail.com", 20, 210)

        #Botao de fechar
        #self.botao_Gerar = wx.Button(self, id=-1, label='Fechar', pos=(170, 260))
        #self.Bind(wx.EVT_BUTTON, self.FecharAbout)

    def FecharAbout(self, event):
        frame_About.Hide()


###################################################### F - Frame About ###############################################################################
#########################################################  I - Frame FormatosRetangulares ####################################################################################
class FormatosRetangulares(wx.Frame):
    def __init__(self, *args, **kwds):
        if sistemaOperacional=="Linux":
            TXFrame=530
            TYFrame=450
            
        if sistemaOperacional=="Windows":
            TXFrame=530
            TYFrame=450
            
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("GISOPLOX - Formatos Retangulares")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TXFrame, TYFrame))
        self.Bind(wx.EVT_CLOSE, self.FecharFormatosRetangulares)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP,  self.OnClick)

        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

    def OnClick(self, event):
        pos = event.GetPosition()
        #print pos.x
        if 45<pos.x<245 and 55<pos.y<355:
            #print "Retangulo"
            frame_Rectange.Show()
            frame_FormatosRetangulares.Hide()
        if 285<pos.x<485 and 55<pos.y<355:
            #print "Retangulo"
            frame_RetanguloFuro.Show()
            frame_FormatosRetangulares.Hide()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        def desenharCirculo(diam, xc, yc):
            raio=diam/2.0
            x=-raio+0.01
            #print x
            while -raio<x<raio:
                y=math.sqrt(raio*raio-x*x)
                xf=x+1.0
                if xf<raio:
                    yf=math.sqrt(raio*raio-xf*xf)                
                dc.DrawLine(int(round(x+xc)),int(round(y+yc)),int(round(xf+xc)),int(round(yf+yc)))
                dc.DrawLine(int(round(x+xc)),int(round(-y+yc)),int(round(xf+xc)),int(round(-yf+yc)))
                dc.DrawLine(int(round(y+xc)),int(round(x+yc)),int(round(yf+xc)),int(round(xf+yc)))
                dc.DrawLine(int(round(y-xc)),int(round(x+yc)),int(round(yf-xc)),int(round(xf+yc)))
                x+=1.0

        #Desenhando o retângulo
        xi=45
        yi=55
        drx=200
        dry=300
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,drx,yi)
        dc.DrawLine(drx,yi,drx,dry)
        dc.DrawLine(drx,dry,xi,dry)
        dc.DrawLine(xi,dry,xi,yi)

        #Desenhando o retângulo com furo
        xi=285
        yi=55
        drx=200
        dry=300

        xc=387
        yc=200
        tam=130
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,drx,yi)
        dc.DrawLine(drx,yi,drx,dry)
        dc.DrawLine(drx,dry,xi,dry)
        dc.DrawLine(xi,dry,xi,yi)
        desenharCirculo(tam, xc, yc)

    #Comando do botão sair e X de fechar
    def FecharFormatosRetangulares(self, event):
        frame_FormatosRetangulares.Hide()
        frame_Gisoplox.Show()
######################################################### F - Frame FormatosRetangulares ####################################################################################
#########################################################  I - Frame FormatosCirculares ####################################################################################
class FormatosCirculares(wx.Frame):
    def __init__(self, *args, **kwds):
        if sistemaOperacional=="Linux":
            TXFrame=580
            TYFrame=350
            X1=20
            Y1=10
            DistEntreTextos=20
            DistEntreTitulos=30
            XSair=170
            YSair=360
            XZerar=70
            YZerar=YSair

            
        if sistemaOperacional=="Windows":
            TXFrame=600
            TYFrame=350
            X1=20
            Y1=10
            DistEntreTextos=20
            DistEntreTitulos=30
            XSair=170
            YSair=360
            XZerar=70
            YZerar=YSair
            
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("GISOPLOX - Formatos Circulares")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TXFrame, TYFrame))
        self.Bind(wx.EVT_CLOSE, self.FecharFormatosCirculares)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP,  self.OnClick)

        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

    def OnClick(self, event):
        pos = event.GetPosition()
        if pos.x>6 and pos.x<273 and pos.y>25 and pos.y<295:
            #print "Circulo"
            frame_Circle.Show()
            frame_FormatosCirculares.Hide()
        if pos.x>308 and pos.x<576 and pos.y>25 and pos.y<295:
            #print "Triangulo"
            frame_CircleSimple.Show()
            frame_FormatosCirculares.Hide()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o anel
        def desenharCirculo(diam, xc, yc):
            raio=diam/2.0
            x=-raio+0.01
            #print x
            while -raio<x<raio:
                y=math.sqrt(raio*raio-x*x)
                xf=x+1.0
                if xf<raio:
                    yf=math.sqrt(raio*raio-xf*xf)                
                dc.DrawLine(int(round(x+xc)),int(round(y+yc)),int(round(xf+xc)),int(round(yf+yc)))
                dc.DrawLine(int(round(x+xc)),int(round(-y+yc)),int(round(xf+xc)),int(round(-yf+yc)))
                dc.DrawLine(int(round(y+xc)),int(round(x+yc)),int(round(yf+xc)),int(round(xf+yc)))
                dc.DrawLine(int(round(y-xc)),int(round(x+yc)),int(round(yf-xc)),int(round(xf+yc)))
                x+=1.0
        desenharCirculo(264, 140, 160)
        desenharCirculo(140, 140, 160)
        desenharCirculo(264, 440, 160)

    #Comando do botão sair e X de fechar
    def FecharFormatosCirculares(self, event):
        frame_FormatosCirculares.Hide()
        frame_Gisoplox.Show()
######################################################### F - Frame FormatosCirculares ####################################################################################
#########################################################  I - Frame FormatosTriangulares ####################################################################################
class FormatosTriangulares(wx.Frame):
    def __init__(self, *args, **kwds):
        if sistemaOperacional=="Linux":
            TXFrame=520
            TYFrame=430
            X1=20
            Y1=10
            DistEntreTextos=20
            DistEntreTitulos=30
            XSair=170
            YSair=360
            XZerar=70
            YZerar=YSair

            
        if sistemaOperacional=="Windows":
            TXFrame=520
            TYFrame=430
            X1=20
            Y1=10
            DistEntreTextos=20
            DistEntreTitulos=30
            XSair=170
            YSair=360
            XZerar=70
            YZerar=YSair
            
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("GISOPLOX - Formatos Triangulares")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TXFrame, TYFrame))
        self.Bind(wx.EVT_CLOSE, self.FecharFormatosTriangulares)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP,  self.OnClick)

        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

    def OnClick(self, event):
        pos = event.GetPosition()

        if pos.x>45 and pos.x<245 and pos.y>45 and pos.y<345:
            #print "Triangulo"
            frame_Triangulo.Show()
            frame_FormatosTriangulares.Hide()
        if pos.x>285 and pos.x<485 and pos.y>45 and pos.y<345:
            #print "Triangulo com pontas cortadas"
            frame_TrianguloPontasCortadas.Show()
            frame_FormatosTriangulares.Hide()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o triângulo
        xi=45
        yi=45
        drx=200
        dry=300
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,drx,yi)
        dc.DrawLine(xi,dry,drx,yi)
        dc.DrawLine(xi,dry,xi,yi)

        #Desenhando o triângulo com pontas cortadas
        xi=285
        yi=45
        xLinha=60
        yLinha=50
        drx=200
        dry=300
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,xi,dry)
        dc.DrawLine(xi,dry,drx,dry)
        dc.DrawLine(drx,dry,drx,(dry-yLinha))
        dc.DrawLine(drx,(dry-yLinha),(xi+xLinha),yi)
        dc.DrawLine((xi+xLinha),yi,xi,yi)

    #Comando do botão sair e X de fechar
    def FecharFormatosTriangulares(self, event):
        frame_FormatosTriangulares.Hide()
        frame_Gisoplox.Show()
######################################################### F - Frame FormatosTriangulares ####################################################################################
######################################################### I - Frame estat ####################################################################################
class Estat(wx.Frame):
    def __init__(self, *args, **kwds):
        if sistemaOperacional=="Linux":
            TXFrame=310
            TYFrame=410
            X1=20
            Y1=10
            DistEntreTextos=20
            DistEntreTitulos=30
            XSair=170
            YSair=360
            XZerar=70
            YZerar=YSair

            
        if sistemaOperacional=="Windows":
            TXFrame=290
            TYFrame=440
            X1=20
            Y1=10
            DistEntreTextos=20
            DistEntreTitulos=30
            XSair=170
            YSair=360
            XZerar=70
            YZerar=YSair
            
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("GISOPLOX - estatísticas")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TXFrame, TYFrame))
        self.Bind(wx.EVT_MOTION,  self.OnMove)
        self.Bind(wx.EVT_CLOSE, self.FecharEstat)

        distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado = Auxiliares.lerEstat(True)
        #print distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado

        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

        #Desenhando a interfácie
        wx.StaticText(self, wx.ID_ANY, ("DADOS ESTATÍSTICOS DE CORTE:"), pos=(X1,Y1))
        Y=Y1+DistEntreTitulos
        wx.StaticText(self, wx.ID_ANY, ("DESDE A INSTALAÇÃO:"), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Distância de corte: "
        mensagem+=str(distTotal)
        self.texto_distTotal=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Peso total das peças: "
        mensagem+=str(pesoTotal)
        self.texto_pesoTotal=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Programas gerados: "
        mensagem+=str(prgTotal)
        self.texto_prgTotal=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Início da contagem: "
        mensagem+=str(diaTotal)
        self.texto_diaTotal=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTitulos
        wx.StaticText(self, wx.ID_ANY, ("DESDE QUE FOI ZERADO:"), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Distância de corte: "
        mensagem+=str(distZerado)
        self.texto_distZerado=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Peso total das peças: "
        mensagem+=str(pesoZerado)
        self.texto_pesoZerado=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Programas gerados: "
        mensagem+=str(prgZerado)
        self.texto_prgZerado=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTextos
        mensagem="Início da contagem: "
        mensagem+=str(diaZerado)
        self.texto_diaZerado=wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))
        Y+=DistEntreTitulos
        mensagem="Obs: Para gerar os dados estatísticos são\nlevados  em  consideração  os  programas\ngerados e não os cortados."
        mensagem+=" Para o cálculo\ndo peso o material  foi  considerado  aço."
        wx.StaticText(self, wx.ID_ANY, (mensagem), pos=(X1,Y))

        #Botão sair
        Botao_Sair = wx.Button(self, id=-1, label='Sair', pos=(XSair, YSair))
        self.Bind(wx.EVT_BUTTON, self.FecharEstat, Botao_Sair)
        #Botão zerar
        Botao_Zerar = wx.Button(self, id=-1, label='Zerar', pos=(XZerar, YZerar))
        self.Bind(wx.EVT_BUTTON, self.Zerar, Botao_Zerar)

    def Zerar(self, event):
        Auxiliares.zerarEstat()
        distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado = Auxiliares.lerEstat(True)
        mensagem="Distância de corte: "
        mensagem+=str(distTotal)
        self.texto_distTotal.SetLabel(mensagem)
        mensagem="Peso total das peças: "
        mensagem+=str(pesoTotal)
        self.texto_pesoTotal.SetLabel(mensagem)
        mensagem="Programas gerados: "
        mensagem+=str(prgTotal)
        self.texto_prgTotal.SetLabel(mensagem)
        mensagem="Início da contagem: "
        mensagem+=str(diaTotal)
        self.texto_diaTotal.SetLabel(mensagem)
        mensagem="Distância de corte: "
        mensagem+=str(distZerado)
        self.texto_distZerado.SetLabel(mensagem)
        mensagem="Peso total das peças: "
        mensagem+=str(pesoZerado)
        self.texto_pesoZerado.SetLabel(mensagem)
        mensagem="Programas gerados: "
        mensagem+=str(prgZerado)
        self.texto_prgZerado.SetLabel(mensagem)
        mensagem="Início da contagem: "
        mensagem+=str(diaZerado)
        self.texto_diaZerado.SetLabel(mensagem)
        #Mostrar aviso de sucesso
        dlg = wx.MessageDialog(parent=None, message="Dados estatícos zerados com sucesso!", caption="Dados estatícos zerados", style=wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnMove(self, event):
        distTotal, pesoTotal, prgTotal, diaTotal, distZerado, pesoZerado, prgZerado, diaZerado = Auxiliares.lerEstat(True)
        mensagem="Distância de corte: "
        mensagem+=str(distTotal)
        self.texto_distTotal.SetLabel(mensagem)
        mensagem="Peso total das peças: "
        mensagem+=str(pesoTotal)
        self.texto_pesoTotal.SetLabel(mensagem)
        mensagem="Programas gerados: "
        mensagem+=str(prgTotal)
        self.texto_prgTotal.SetLabel(mensagem)
        mensagem="Início da contagem: "
        mensagem+=str(diaTotal)
        self.texto_diaTotal.SetLabel(mensagem)
        mensagem="Distância de corte: "
        mensagem+=str(distZerado)
        self.texto_distZerado.SetLabel(mensagem)
        mensagem="Peso total das peças: "
        mensagem+=str(pesoZerado)
        self.texto_pesoZerado.SetLabel(mensagem)
        mensagem="Programas gerados: "
        mensagem+=str(prgZerado)
        self.texto_prgZerado.SetLabel(mensagem)
        mensagem="Início da contagem: "
        mensagem+=str(diaZerado)
        self.texto_diaZerado.SetLabel(mensagem)     

    #Comando do botão sair e X de fechar
    def FecharEstat(self, event):
        frame_Estat.Hide()
        frame_Gisoplox.Show()
######################################################### F - Frame estat ####################################################################################
######################################################### I - Frame hist ####################################################################################
class Hist(wx.Frame):
    def __init__(self, *args, **kwds):
        if sistemaOperacional=="Linux":
            TXFrame=820
            TYFrame=450
            Col1=250
            Col2=100
            Col3=80
            Col4=90
            Col5=70
            Col6=50
            Col7=80

            
        if sistemaOperacional=="Windows":
            TXFrame=820
            TYFrame=450
            Col1=250
            Col2=100
            Col3=80
            Col4=90
            Col5=70
            Col6=50
            Col7=80
            
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("GISOPLOX - histórico")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TXFrame, TYFrame))
        self.Bind(wx.EVT_CLOSE, self.FecharHist)
        mostrarProgramas=1000

        #Criando o menu        
        menuBar = wx.MenuBar()
        menu = wx.Menu()

        #Menu opções/Atualizar
        m_atualizar = menu.Append(wx.ID_ANY, "&Atualizar")
        self.Bind(wx.EVT_MENU, self.Atualizar, m_atualizar)

        #Menu opções/sair
        menu.AppendSeparator()
        m_sair = menu.Append(wx.ID_EXIT, "S&air\tAlt-S", "Fechar o programa")
        self.Bind(wx.EVT_MENU, self.FecharHist, m_sair)
        menuBar.Append(menu, "&Opções")

        #Menu Atualizar
        menu = wx.Menu()
        m_atualizar=menuBar.Append(menu, "&Atualizar")
        m_atualizar = menu.Append(wx.ID_ANY, "&Atualizar")
        self.Bind(wx.EVT_MENU, self.Atualizar, m_atualizar)
        
        self.SetMenuBar(menuBar)
        self.statusbar = self.CreateStatusBar()
        
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        self.myGrid = gridlib.Grid(panel)
        self.myGrid.CreateGrid(mostrarProgramas, 7)
        self.myGrid.SetColSize(0, Col1)
        self.myGrid.SetColSize(1, Col2)
        self.myGrid.SetColSize(2, Col3)
        self.myGrid.SetColSize(3, Col4)
        self.myGrid.SetColSize(4, Col5)
        self.myGrid.SetColSize(5, Col6)
        self.myGrid.SetColSize(6, Col7)

        # get the cell attribute for the top left row
        editor = self.myGrid.GetCellEditor(0,0)
        attr = gridlib.GridCellAttr()
        attr.SetReadOnly(True)

        #Nao permitir ediçao
        self.myGrid.EnableEditing(False)

        self.myGrid.SetColLabelValue(0, "Nome do programa")
        self.myGrid.SetColLabelValue(1, "Peso Unitario")
        self.myGrid.SetColLabelValue(2, "Peso Total")
        self.myGrid.SetColLabelValue(3, "Distância")
        self.myGrid.SetColLabelValue(4, "Data")
        self.myGrid.SetColLabelValue(5, "Hora")
        self.myGrid.SetColLabelValue(6, "Versão")

        #Escrevendo os programas
        a=0
        while a<mostrarProgramas:
            Nome, PesoUn, PesoTotal, Dist, Data, Hora, Versao = Auxiliares.lerHistLinha(a+1)
            self.myGrid.SetCellValue(a, 0, Nome)
            self.myGrid.SetCellValue(a, 1, PesoUn)
            self.myGrid.SetCellValue(a, 2, PesoTotal)
            self.myGrid.SetCellValue(a, 3, Dist)
            self.myGrid.SetCellValue(a, 4, Data)
            self.myGrid.SetCellValue(a, 5, Hora)
            self.myGrid.SetCellValue(a, 6, Versao)
            a+=1

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)

    def Atualizar(self, event):
        mostrarProgramas=1000
        a=0
        while a<mostrarProgramas:
            Nome, PesoUn, PesoTotal, Dist, Data, Hora, Versao = Auxiliares.lerHistLinha(a+1)
            self.myGrid.SetCellValue(a, 0, Nome)
            self.myGrid.SetCellValue(a, 1, PesoUn)
            self.myGrid.SetCellValue(a, 2, PesoTotal)
            self.myGrid.SetCellValue(a, 3, Dist)
            self.myGrid.SetCellValue(a, 4, Data)
            self.myGrid.SetCellValue(a, 5, Hora)
            self.myGrid.SetCellValue(a, 6, Versao)
            a+=1

    def FecharHist(self, event):
        frame_Hist.Hide()
        frame_Gisoplox.Show()
######################################################### F - Frame Hist ####################################################################################
###################################################### CONFIG I ##########################################################################################
icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
SmesaX = str(int(mesaX))
SmesaY = str(int(mesaY))

class Configurar(wx.Frame):
    def __init__(self, *args, **kwds):
        if sistemaOperacional=="Linux":
            TXFrame=390
            TYFrame=530
            X1=10
            Y1=10
            posIcorteY=30
            posMesa1X=70
            posMesa1Y=80
            X2=110
            X3=175
            X4=265
            X5=125
            X6=170
            X7=230
            X8=285
            X9=230
            X10=265
            X11=320
            XCancelar=200
            XAplicar=290
            XOxi=50
            XPlas=180
            Y0=10
            Y1=65
            Y2=90
            Y3=120
            Y4=140
            Y5=160
            Y6=180
            Y7=220
            Y8=260
            YTextConfigurar=300
            YOxi=320
            YTextPastaSalvar=370
            XCampoPastaSalvar=X1
            YCampoPastaSalvar=390
            YBotaoPastaSalvar=YCampoPastaSalvar
            TamXCampoPastaSalvar=275
            XBotaoPastaSalvar=290
            YCancelar=450
            TamAjuCodX=300
            TamAjuCodY=20
            T1X=50
            T1Y=30
            
        if sistemaOperacional=="Windows":
            TXFrame=330
            TYFrame=500
            X1=10
            Y1=10
            posIcorteY=30
            posMesa1X=60
            posMesa1Y=80
            X2=95
            X3=175
            X4=250
            X5=115
            X6=170
            X7=220
            X8=275
            X9=180
            X10=200
            X11=255
            XCancelar=130
            XAplicar=220
            XOxi=X1
            XPlas=140
            Y0=10
            Y1=65
            Y2=90
            Y3=120
            Y4=140
            Y5=160
            Y6=180
            Y7=210
            Y8=240
            YTextConfigurar=270
            YOxi=290
            YTextPastaSalvar=330
            XCampoPastaSalvar=X1
            YCampoPastaSalvar=350
            YBotaoPastaSalvar=380
            TamXCampoPastaSalvar=295
            XBotaoPastaSalvar=220
            YCancelar=430
            TamAjuCodX=300
            TamAjuCodY=20
            T1X=50
            T1Y=20
            
        # Detalhes do frame
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("GISOPLOX - Configurar")
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TXFrame, TYFrame))
        self.Bind(wx.EVT_CLOSE, self.FecharConfig)

        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

        #Desenhando a interfácie
        label_1 = wx.StaticText(self, wx.ID_ANY, ("COMANDOS:"), pos=(X1,Y0))
        label_1 = wx.StaticText(self, wx.ID_ANY, ("Início de corte:"), pos=(X1,posIcorteY))
        self.campo_de_texto_Icorte=wx.TextCtrl(self, wx.ID_ANY, icorte, pos=(X2,posIcorteY), size=(T1X,T1Y))

        label_1 = wx.StaticText(self, wx.ID_ANY, ("Fim de corte:"), pos=(X3,posIcorteY))
        self.campo_de_texto_Fcorte=wx.TextCtrl(self, wx.ID_ANY, fcorte, pos=(X4,posIcorteY), size=(T1X,T1Y))

        label_1 = wx.StaticText(self, wx.ID_ANY, ("TAMANHO DA MESA / LIMITES DE CORTE:"), pos=(X1,Y1))
        label_1 = wx.StaticText(self, wx.ID_ANY, ("Limite X:"), pos=(X1,Y2))
        self.campo_de_texto_mesaX=wx.TextCtrl(self, wx.ID_ANY, SmesaX, pos=(posMesa1X,Y2), size=(T1X,T1Y))
        label_1 = wx.StaticText(self, wx.ID_ANY, ("mm"), pos=(X5,Y2))
        label_1 = wx.StaticText(self, wx.ID_ANY, ("Limite Y:"), pos=(X6,Y2))
        self.campo_de_texto_mesaY=wx.TextCtrl(self, wx.ID_ANY, SmesaY, pos=(X7,Y2), size=(T1X,T1Y))
        label_1 = wx.StaticText(self, wx.ID_ANY, ("mm"), pos=(X8,Y2))

        label_1 = wx.StaticText(self, wx.ID_ANY, ('AJUSTES DO CÓDIGO:'), pos=(X1,Y3), size=(TamAjuCodX,TamAjuCodY))

        #Usar 1 para SIM e 0 para não
        self.checarNumerarLinhas = wx.CheckBox(self, -1, 'Numerar linhas', (X1, Y4))
        if numerar == 1:
            self.checarNumerarLinhas.SetValue(True)
        if numerar == 0:
            self.checarNumerarLinhas.SetValue(False)
            
        self.checarColocarVelocidadeAvanco = wx.CheckBox(self, -1, 'Colocar velocidade de avanço', (X1, Y5))
        if colocarVelocidadeAvanco == 1:
            self.checarColocarVelocidadeAvanco.SetValue(True)
        if colocarVelocidadeAvanco == 0:
            self.checarColocarVelocidadeAvanco.SetValue(False)

        self.checarColocarVelocidadeAvancoRapido = wx.CheckBox(self, -1, 'Colocar velocidade de avanço rápido', (X1, Y6))
        if colocarVelocidadeAvancoRapido == 1:
            self.checarColocarVelocidadeAvancoRapido.SetValue(True)
        if colocarVelocidadeAvancoRapido == 0:
            self.checarColocarVelocidadeAvancoRapido.SetValue(False)
        
        label_1 = wx.StaticText(self, wx.ID_ANY, ("EXTENÇÃO DO ARQUIVO CNC:"), pos=(X1,Y7))
        self.campo_de_texto_extencao=wx.TextCtrl(self, wx.ID_ANY, extencao, pos=(X9,Y7), size=(T1X,T1Y))

        label_1 = wx.StaticText(self, wx.ID_ANY, ("VELOCIDADE DO AVANÇO RÁPIDO:"), pos=(X1,Y8))
        self.campo_de_texto_velocidadeAvancoRapido=wx.TextCtrl(self, wx.ID_ANY, SmesaX, pos=(X10,Y8), size=(T1X,T1Y))
        label_1 = wx.StaticText(self, wx.ID_ANY, ("mm/min"), pos=(X11,Y8))

        #Botões Oxicorte e Plasma
        label_1 = wx.StaticText(self, wx.ID_ANY, ("CONFIGURAR PARÂMETROS DE CORTE:"), pos=(X1,YTextConfigurar))
        
        Botao_ConfigOxi = wx.Button(self, id=-1, label='Oxicorte', pos=(XOxi, YOxi))
        self.Bind(wx.EVT_BUTTON, self.MostrarKerf, Botao_ConfigOxi)
        
        Botao_ConfigPlas = wx.Button(self, id=-1, label='Plasma', pos=(XPlas, YOxi))
        self.Bind(wx.EVT_BUTTON, self.MostrarKerfPlasma, Botao_ConfigPlas)

        #Pasta salvar padrão
        #pastaPad="CNC/"
        label_1 = wx.StaticText(self, wx.ID_ANY, ('PASTA "SALVAR PADRÃO:"'), pos=(X1,YTextPastaSalvar))

        if sistemaOperacional=="Windows":
            textoPastaPad = pastaPadWin
            texto = 'Alterar pasta'
        if sistemaOperacional=="Linux":
            textoPastaPad = pastaPadLinux
            texto = 'Alterar'
        self.campo_de_texto_PastaSalvarPadrao=wx.TextCtrl(self, wx.ID_ANY, textoPastaPad, pos=(XCampoPastaSalvar,YCampoPastaSalvar), size=(TamXCampoPastaSalvar,T1Y), style=(wx.TE_READONLY))
        
        Botao_Alterar = wx.Button(self, id=-1, label=texto, pos=(XBotaoPastaSalvar, YBotaoPastaSalvar))
        self.Bind(wx.EVT_BUTTON, self.AlterarSalvarPad, Botao_Alterar)

        #Botões Cancelar e Aplicar        
        Botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XCancelar, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharConfig, Botao_Cancelar)
        
        Botao_Aplicar = wx.Button(self, id=-1, label='Aplicar', pos=(XAplicar, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.AplicarConfig, Botao_Aplicar)

        

        #Comando do botão aplicar
    def AplicarConfig(self, event):
        pastaPadWin=Auxiliares.Parametros()[9]
        pastaPadLinux=Auxiliares.Parametros()[10]
        icorte = self.campo_de_texto_Icorte.GetValue()
        fcorte = self.campo_de_texto_Fcorte.GetValue()
        extencao = self.campo_de_texto_extencao.GetValue()
        SmesaX = self.campo_de_texto_mesaX.GetValue()
        SmesaY = self.campo_de_texto_mesaY.GetValue()
        numerar = self.checarNumerarLinhas.GetValue()
        textoPastaPad = self.campo_de_texto_PastaSalvarPadrao.GetValue()
        if sistemaOperacional=="Windows":
            pastaPadWin = textoPastaPad
        if sistemaOperacional=="Linux":
            pastaPadLinux = textoPastaPad
        if numerar == True:
            numerar = 1
        if numerar == False:
            numerar = 0
        colocarVelocidadeAvanco = self.checarColocarVelocidadeAvanco.GetValue()
        if colocarVelocidadeAvanco == True:
            colocarVelocidadeAvanco = 1
        if colocarVelocidadeAvanco == False:
            colocarVelocidadeAvanco = 0
        colocarVelocidadeAvancoRapido = self.checarColocarVelocidadeAvancoRapido.GetValue()
        if colocarVelocidadeAvancoRapido == True:
            colocarVelocidadeAvancoRapido = 1
        if colocarVelocidadeAvancoRapido == False:
            colocarVelocidadeAvancoRapido = 0
        velocidadeAvancoRapido = self.campo_de_texto_velocidadeAvancoRapido.GetValue()

        #Garantindo extencao .txt
        extencao = extencao.replace(".", "")
        extencao = "." + extencao

        texto = "icorte" + '\n' + icorte + '\n' + '\n'
        texto = texto + "fcorte" + '\n' + fcorte + '\n' + '\n'
        texto = texto + "extencao" + '\n' + extencao + '\n' + '\n'
        texto = texto + "tamanho da mesa X (mm)" + '\n' + SmesaX + '\n' + '\n'
        texto = texto + "tamanho da mesa Y (mm)" + '\n' + SmesaY + '\n' + '\n'
        texto = texto + "numerar linhas (0-nao, 1-sim)" + '\n' + str(numerar) + '\n' + '\n'
        texto = texto + "colocar velocidade de avaco (0-nao, 1-sim)" + '\n' + str(colocarVelocidadeAvanco) + '\n' + '\n'
        texto = texto + "colocar velocidade de avaco rapido(0-nao, 1-sim)" + '\n' + str(colocarVelocidadeAvancoRapido) + '\n' + '\n'
        texto = texto + "velocidade de avanco rapido(mm/min)" + '\n' + velocidadeAvancoRapido + '\n' + '\n'
        texto = texto + 'pasta salvar padrao "Linux"' + '\n' + pastaPadLinux + '\n' + '\n'
        texto = texto + 'pasta salvar padrao "Windows"' + '\n' + pastaPadWin
        arquivoDeConfig = str(os.getcwd()) + "/.gisoplox/settings.ini"
        escrever = open(arquivoDeConfig, "w")
        escrever.write(texto)
        escrever.close()

        #Mostrar aviso de sucesso
        dlg = wx.MessageDialog(parent=None, message="Configurações salvas com sucesso", caption="Configurações salvas", style=wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    #Comando do botão cancelar e X de fechar
    def FecharConfig(self, event):
        frame_Configurar.Hide()
        frame_Gisoplox.Show()

    #Comando do botão "Oxicorte"
    def MostrarKerf(self, event):
        frame_Kerf.Show()
        frame_Configurar.Hide()

    #Comando do botão "Plasma"
    def MostrarKerfPlasma(self, event):
        frame_KerfPlasma.Show()
        frame_Configurar.Hide()

    #Comando do botão "Alterar" pasta Salvar padrão
    def AlterarSalvarPad(self, event):
        dialog = wx.DirDialog(None, "Escolha uma pasta:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            salvarPad=dialog.GetPath()
            self.campo_de_texto_PastaSalvarPadrao.SetValue(salvarPad)
            #print salvarPad
        dialog.Destroy()

###################################################### CONFIG F ##########################################################################################

###################################################### KERF I ##########################################################################################
arquivoDeKerf = ".gisoplox/oxyfuel_cutting_width.gisoplox"
kerf = open(arquivoDeKerf)

#Bloco 1
espMin1 = "0"
espMax1 = kerf.readline()
kerf1 = kerf.readline()
vel1 = kerf.readline()
kerf.readline()

#Bloco 2
espMin2 = kerf.readline()
espMax2 = kerf.readline()
kerf2 = kerf.readline()
vel2 = kerf.readline()
kerf.readline()

#Bloco 3
espMin3 = kerf.readline()
espMax3 = kerf.readline()
kerf3 = kerf.readline()
vel3 = kerf.readline()
kerf.readline()

#Bloco 4
espMin4 = kerf.readline()
espMax4 = kerf.readline()
kerf4 = kerf.readline()
vel4 = kerf.readline()
kerf.readline()

#Bloco 5
espMin5 = kerf.readline()
espMax5 = kerf.readline()
kerf5 = kerf.readline()
vel5 = kerf.readline()
kerf.readline()

#Bloco 6
espMin6 = kerf.readline()
espMax6 = kerf.readline()
kerf6 = kerf.readline()
vel6 = kerf.readline()
kerf.readline()

#Bloco 7
espMin7 = kerf.readline()
espMax7 = kerf.readline()
kerf7 = kerf.readline()
vel7 = kerf.readline()
kerf.readline()

#Bloco 8
espMin8 = kerf.readline()
espMax8 = kerf.readline()
kerf8 = kerf.readline()
vel8 = kerf.readline()
kerf.readline()

#Bloco 9
espMin9 = kerf.readline()
espMax9 = kerf.readline()
kerf9 = kerf.readline()
vel9 = kerf.readline()
kerf.readline()

#Bloco 10
espMin10 = kerf.readline()
espMax10 = kerf.readline()
kerf10 = kerf.readline()
vel10 = kerf.readline()
kerf.readline()

#Retirando a quebra de linha das strings
espMax1=espMax1.rstrip('\n')
espMax2=espMax2.rstrip('\n')
espMax3=espMax3.rstrip('\n')
espMax4=espMax4.rstrip('\n')
espMax5=espMax5.rstrip('\n')
espMax6=espMax6.rstrip('\n')
espMax7=espMax7.rstrip('\n')
espMax8=espMax8.rstrip('\n')
espMax9=espMax9.rstrip('\n')
espMax10=espMax10.rstrip('\n')

espMin1=espMin1.rstrip('\n')
espMin2=espMin2.rstrip('\n')
espMin3=espMin3.rstrip('\n')
espMin4=espMin4.rstrip('\n')
espMin5=espMin5.rstrip('\n')
espMin6=espMin6.rstrip('\n')
espMin7=espMin7.rstrip('\n')
espMin8=espMin8.rstrip('\n')
espMin9=espMin9.rstrip('\n')
espMin10=espMin10.rstrip('\n')

kerf1=kerf1.rstrip('\n')
kerf2=kerf2.rstrip('\n')
kerf3=kerf3.rstrip('\n')
kerf4=kerf4.rstrip('\n')
kerf5=kerf5.rstrip('\n')
kerf6=kerf6.rstrip('\n')
kerf7=kerf7.rstrip('\n')
kerf8=kerf8.rstrip('\n')
kerf9=kerf9.rstrip('\n')
kerf10=kerf10.rstrip('\n')

vel1=vel1.rstrip('\n')
vel2=vel2.rstrip('\n')
vel3=vel3.rstrip('\n')
vel4=vel4.rstrip('\n')
vel5=vel5.rstrip('\n')
vel6=vel6.rstrip('\n')
vel7=vel7.rstrip('\n')
vel8=vel8.rstrip('\n')
vel9=vel9.rstrip('\n')
vel10=vel10.rstrip('\n')

class Kerf(wx.Frame):
    def __init__(self, *args, **kwds):
        # Detalhes do frame
        if sistemaOperacional=="Linux":
            TX=440
            TY=460
            Y=40
            Ydist=30
            X1=20
            T1X=40
            T1Y=20
            X2=65
            X3=80
            X4=180
            X5=300
            T2X=60
            T2Y=20
            T3X=60
            T3Y=20
            XBC=205
            XBA=310

        if sistemaOperacional=="Windows":
            TX=420
            TY=320
            Y=30
            Ydist=20
            X1=20
            T1X=25
            T1Y=20
            X2=50
            X3=60
            X4=150
            X5=300
            T2X=60
            T2Y=20
            T3X=60
            T3Y=20
            XBC=185
            XBA=290
        
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(("GISOPLOX - Parâmetros de corte - Oxicorte"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_MOTION,  self.OnMove)
        self.Bind(wx.EVT_CLOSE, self.FecharKerf)
        self.style=wx.CAPTION
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

        #Desenhando a interfácie
        wx.StaticText(self, wx.ID_ANY, ("Espessura (mm)"), pos=(15,10))
        wx.StaticText(self, wx.ID_ANY, ("Largura de corte (mm)"), pos=(120,10))
        wx.StaticText(self, wx.ID_ANY, ("Velocidade (mm/min)"), pos=(270,10))

        #Desenhando a tabela
        
        
        #Espaço 1
        self.campo_espMin1 = wx.TextCtrl(self, wx.ID_ANY, espMin1, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin1.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax1 = wx.TextCtrl(self, wx.ID_ANY, espMax1, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf1 = wx.TextCtrl(self, wx.ID_ANY, kerf1, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel1 = wx.TextCtrl(self, wx.ID_ANY, vel1, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 2
        self.campo_espMin2 = wx.TextCtrl(self, wx.ID_ANY, espMin2, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin2.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax2 = wx.TextCtrl(self, wx.ID_ANY, espMax2, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf2 = wx.TextCtrl(self, wx.ID_ANY, kerf2, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel2 = wx.TextCtrl(self, wx.ID_ANY, vel2, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 3
        self.campo_espMin3 = wx.TextCtrl(self, wx.ID_ANY, espMin3, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin3.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax3 = wx.TextCtrl(self, wx.ID_ANY, espMax3, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf3 = wx.TextCtrl(self, wx.ID_ANY, kerf3, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel3 = wx.TextCtrl(self, wx.ID_ANY, vel3, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 4
        self.campo_espMin4 = wx.TextCtrl(self, wx.ID_ANY, espMin4, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin4.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax4 = wx.TextCtrl(self, wx.ID_ANY, espMax4, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf4 = wx.TextCtrl(self, wx.ID_ANY, kerf4, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel4 = wx.TextCtrl(self, wx.ID_ANY, vel4, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 5
        self.campo_espMin5 = wx.TextCtrl(self, wx.ID_ANY, espMin5, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin5.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax5 = wx.TextCtrl(self, wx.ID_ANY, espMax5, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf5 = wx.TextCtrl(self, wx.ID_ANY, kerf5, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel5 = wx.TextCtrl(self, wx.ID_ANY, vel5, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 6
        self.campo_espMin6 = wx.TextCtrl(self, wx.ID_ANY, espMin6, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin6.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax6 = wx.TextCtrl(self, wx.ID_ANY, espMax6, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf6 = wx.TextCtrl(self, wx.ID_ANY, kerf6, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel6 = wx.TextCtrl(self, wx.ID_ANY, vel6, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 7
        self.campo_espMin7 = wx.TextCtrl(self, wx.ID_ANY, espMin7, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin7.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax7 = wx.TextCtrl(self, wx.ID_ANY, espMax7, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf7 = wx.TextCtrl(self, wx.ID_ANY, kerf7, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel7 = wx.TextCtrl(self, wx.ID_ANY, vel7, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 8
        self.campo_espMin8 = wx.TextCtrl(self, wx.ID_ANY, espMin8, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin8.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax8 = wx.TextCtrl(self, wx.ID_ANY, espMax8, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf8 = wx.TextCtrl(self, wx.ID_ANY, kerf8, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel8 = wx.TextCtrl(self, wx.ID_ANY, vel8, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 9
        self.campo_espMin9 = wx.TextCtrl(self, wx.ID_ANY, espMin9, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin9.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax9 = wx.TextCtrl(self, wx.ID_ANY, espMax9, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf9 = wx.TextCtrl(self, wx.ID_ANY, kerf9, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel9 = wx.TextCtrl(self, wx.ID_ANY, vel9, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 10
        self.campo_espMin10 = wx.TextCtrl(self, wx.ID_ANY, espMin10, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMin10.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMax10 = wx.TextCtrl(self, wx.ID_ANY, espMax10, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerf10 = wx.TextCtrl(self, wx.ID_ANY, kerf10, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_vel10 = wx.TextCtrl(self, wx.ID_ANY, vel10, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+50
        #Botão Cancelar
        Botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, Y))
        self.Bind(wx.EVT_BUTTON, self.FecharKerf, Botao_Cancelar)

        #Botao Aplicar
        Botao_Aplicar = wx.Button(self, id=-1, label='Aplicar', pos=(XBA, Y))
        self.Bind(wx.EVT_BUTTON, self.AplicarKerf, Botao_Aplicar)

        #Comando do botão cancelar
    def FecharKerf(self, event):
        frame_Gisoplox.Show()
        frame_Kerf.Hide()

        #Comando do botão aplicar
    def AplicarKerf(self, event):
        #Pegar o valor dos campos de texto
        espMax1=self.campo_espMax1.GetValue()
        espMax2=self.campo_espMax2.GetValue()
        espMax3=self.campo_espMax3.GetValue()
        espMax4=self.campo_espMax4.GetValue()
        espMax5=self.campo_espMax5.GetValue()
        espMax6=self.campo_espMax6.GetValue()
        espMax7=self.campo_espMax7.GetValue()
        espMax8=self.campo_espMax8.GetValue()
        espMax9=self.campo_espMax9.GetValue()
        espMax10=self.campo_espMax10.GetValue()

        espMin1=self.campo_espMin1.GetValue()
        espMin2=self.campo_espMin2.GetValue()
        espMin3=self.campo_espMin3.GetValue()
        espMin4=self.campo_espMin4.GetValue()
        espMin5=self.campo_espMin5.GetValue()
        espMin6=self.campo_espMin6.GetValue()
        espMin7=self.campo_espMin7.GetValue()
        espMin8=self.campo_espMin8.GetValue()
        espMin9=self.campo_espMin9.GetValue()
        espMin10=self.campo_espMin10.GetValue()

        kerf1=self.campo_kerf1.GetValue()
        kerf2=self.campo_kerf2.GetValue()
        kerf3=self.campo_kerf3.GetValue()
        kerf4=self.campo_kerf4.GetValue()
        kerf5=self.campo_kerf5.GetValue()
        kerf6=self.campo_kerf6.GetValue()
        kerf7=self.campo_kerf7.GetValue()
        kerf8=self.campo_kerf8.GetValue()
        kerf9=self.campo_kerf9.GetValue()
        kerf10=self.campo_kerf10.GetValue()

        vel1=self.campo_vel1.GetValue()
        vel2=self.campo_vel2.GetValue()
        vel3=self.campo_vel3.GetValue()
        vel4=self.campo_vel4.GetValue()
        vel5=self.campo_vel5.GetValue()
        vel6=self.campo_vel6.GetValue()
        vel7=self.campo_vel7.GetValue()
        vel8=self.campo_vel8.GetValue()
        vel9=self.campo_vel9.GetValue()
        vel10=self.campo_vel10.GetValue()

        #Trocar vírgulas por pontos
        espMax1=espMax1.replace(',', '.')
        espMax2=espMax2.replace(',', '.')
        espMax3=espMax3.replace(',', '.')
        espMax4=espMax4.replace(',', '.')
        espMax5=espMax5.replace(',', '.')
        espMax6=espMax6.replace(',', '.')
        espMax7=espMax7.replace(',', '.')
        espMax8=espMax8.replace(',', '.')
        espMax9=espMax9.replace(',', '.')
        espMax10=espMax10.replace(',', '.')

        espMin1=espMin1.replace(',', '.')
        espMin2=espMin2.replace(',', '.')
        espMin3=espMin3.replace(',', '.')
        espMin4=espMin4.replace(',', '.')
        espMin5=espMin5.replace(',', '.')
        espMin6=espMin6.replace(',', '.')
        espMin7=espMin7.replace(',', '.')
        espMin8=espMin8.replace(',', '.')
        espMin9=espMin9.replace(',', '.')
        espMin10=espMin10.replace(',', '.')

        kerf1=kerf1.replace(',', '.')
        kerf2=kerf2.replace(',', '.')
        kerf3=kerf3.replace(',', '.')
        kerf4=kerf4.replace(',', '.')
        kerf5=kerf5.replace(',', '.')
        kerf6=kerf6.replace(',', '.')
        kerf7=kerf7.replace(',', '.')
        kerf8=kerf8.replace(',', '.')
        kerf9=kerf9.replace(',', '.')
        kerf10=kerf10.replace(',', '.')

        vel1=vel1.replace(',', '.')
        vel2=vel2.replace(',', '.')
        vel3=vel3.replace(',', '.')
        vel4=vel4.replace(',', '.')
        vel5=vel5.replace(',', '.')
        vel6=vel6.replace(',', '.')
        vel7=vel7.replace(',', '.')
        vel8=vel8.replace(',', '.')
        vel9=vel9.replace(',', '.')
        vel10=vel10.replace(',', '.')

        #Tirar espaços se houver
        espMax1=espMax1.replace(' ', '')
        espMax2=espMax2.replace(' ', '')
        espMax3=espMax3.replace(' ', '')
        espMax4=espMax4.replace(' ', '')
        espMax5=espMax5.replace(' ', '')
        espMax6=espMax6.replace(' ', '')
        espMax7=espMax7.replace(' ', '')
        espMax8=espMax8.replace(' ', '')
        espMax9=espMax9.replace(' ', '')
        espMax10=espMax10.replace(' ', '')

        espMin1=espMin1.replace(' ', '')
        espMin2=espMin2.replace(' ', '')
        espMin3=espMin3.replace(' ', '')
        espMin4=espMin4.replace(' ', '')
        espMin5=espMin5.replace(' ', '')
        espMin6=espMin6.replace(' ', '')
        espMin7=espMin7.replace(' ', '')
        espMin8=espMin8.replace(' ', '')
        espMin9=espMin9.replace(' ', '')
        espMin10=espMin10.replace(' ', '')

        kerf1=kerf1.replace(' ', '')
        kerf2=kerf2.replace(' ', '')
        kerf3=kerf3.replace(' ', '')
        kerf4=kerf4.replace(' ', '')
        kerf5=kerf5.replace(' ', '')
        kerf6=kerf6.replace(' ', '')
        kerf7=kerf7.replace(' ', '')
        kerf8=kerf8.replace(' ', '')
        kerf9=kerf9.replace(' ', '')
        kerf10=kerf10.replace(' ', '')

        vel1=vel1.replace(' ', '')
        vel2=vel2.replace(' ', '')
        vel3=vel3.replace(' ', '')
        vel4=vel4.replace(' ', '')
        vel5=vel5.replace(' ', '')
        vel6=vel6.replace(' ', '')
        vel7=vel7.replace(' ', '')
        vel8=vel8.replace(' ', '')
        vel9=vel9.replace(' ', '')
        vel10=vel10.replace(' ', '')

        
        #Procurar erros de preenchimento
        erros=0
        if espMax1.replace('.', '').isdigit() == False or espMax2.replace('.', '').isdigit() == False or espMax3.replace('.', '').isdigit() == False or espMax4.replace('.', '').isdigit() == False or espMax5.replace('.', '').isdigit() == False or espMax6.replace('.', '').isdigit() == False or espMax7.replace('.', '').isdigit() == False or espMax8.replace('.', '').isdigit() == False or espMax9.replace('.', '').isdigit() == False or espMax10.replace('.', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar apenas números! \nHá um erro em uma das espessuras!", caption="Atenção", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        if kerf1.replace('.', '').isdigit() == False or kerf2.replace('.', '').isdigit() == False or kerf3.replace('.', '').isdigit() == False or kerf4.replace('.', '').isdigit() == False or kerf5.replace('.', '').isdigit() == False or kerf6.replace('.', '').isdigit() == False or kerf7.replace('.', '').isdigit() == False or kerf8.replace('.', '').isdigit() == False or kerf9.replace('.', '').isdigit() == False or kerf10.replace('.', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar apenas números! \nHá um erro em uma das larguras de corte!", caption="Atenção", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        if vel1.replace('.', '').isdigit() == False or vel2.replace('.', '').isdigit() == False or vel3.replace('.', '').isdigit() == False or vel4.replace('.', '').isdigit() == False or vel5.replace('.', '').isdigit() == False or vel6.replace('.', '').isdigit() == False or vel7.replace('.', '').isdigit() == False or vel8.replace('.', '').isdigit() == False or vel9.replace('.', '').isdigit() == False or vel10.replace('.', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar apenas números! \nHá um erro em uma das velocidades!", caption="Atenção", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Verificando se as minimas estão em ordem crescente    
        if float(espMax2) <= float(espMax1) or float(espMax3) <= float(espMax2) or float(espMax4) <= float(espMax3) or float(espMax5) <= float(espMax4) or float(espMax6) <= float(espMax5) or float(espMax7) <= float(espMax6) or float(espMax8) <= float(espMax7) or float(espMax9) <= float(espMax8) or float(espMax10) <= float(espMax9):
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar os dados em ordem crescente!", caption="Dados incoerentes", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Escrever as novas configurações no arquivo
        if erros == 0:
            texto = espMax1
            texto = texto + "\n" + kerf1
            texto = texto + "\n" + vel1 + "\n"
            texto = texto + "\n" + espMin2
            texto = texto + "\n" + espMax2
            texto = texto + "\n" + kerf2
            texto = texto + "\n" + vel2 + "\n"
            texto = texto + "\n" + espMin3
            texto = texto + "\n" + espMax3
            texto = texto + "\n" + kerf3
            texto = texto + "\n" + vel3 + "\n"
            texto = texto + "\n" + espMin4
            texto = texto + "\n" + espMax4
            texto = texto + "\n" + kerf4
            texto = texto + "\n" + vel4 + "\n"
            texto = texto + "\n" + espMin5
            texto = texto + "\n" + espMax5
            texto = texto + "\n" + kerf5
            texto = texto + "\n" + vel5 + "\n"
            texto = texto + "\n" + espMin6
            texto = texto + "\n" + espMax6
            texto = texto + "\n" + kerf6
            texto = texto + "\n" + vel6 + "\n"
            texto = texto + "\n" + espMin7
            texto = texto + "\n" + espMax7
            texto = texto + "\n" + kerf7
            texto = texto + "\n" + vel7 + "\n"
            texto = texto + "\n" + espMin8
            texto = texto + "\n" + espMax8
            texto = texto + "\n" + kerf8
            texto = texto + "\n" + vel8 + "\n"
            texto = texto + "\n" + espMin9
            texto = texto + "\n" + espMax9
            texto = texto + "\n" + kerf9
            texto = texto + "\n" + vel9 + "\n"
            texto = texto + "\n" + espMin10
            texto = texto + "\n" + espMax10
            texto = texto + "\n" + kerf10
            texto = texto + "\n" + vel10
            escrever = open(arquivoDeKerf, "w")
            escrever.write(texto)
            escrever.close()

            #Mostrar aviso de sucesso
            dlg = wx.MessageDialog(parent=None, message="Configurações salvas com sucesso", caption="Configurações salvas", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        
    def OnMove(self, event):

        #Atualizar campos
        espMin1 = self.campo_espMax1.GetValue()
        self.campo_espMin2.SetValue(espMin1)
        espMin2 = self.campo_espMax2.GetValue()
        self.campo_espMin3.SetValue(espMin2)
        espMin3 = self.campo_espMax3.GetValue()
        self.campo_espMin4.SetValue(espMin3)
        espMin4 = self.campo_espMax4.GetValue()
        self.campo_espMin5.SetValue(espMin4)
        espMin5 = self.campo_espMax5.GetValue()
        self.campo_espMin6.SetValue(espMin5)
        espMin6 = self.campo_espMax6.GetValue()
        self.campo_espMin7.SetValue(espMin6)
        espMin7 = self.campo_espMax7.GetValue()
        self.campo_espMin8.SetValue(espMin7)
        espMin8 = self.campo_espMax8.GetValue()
        self.campo_espMin9.SetValue(espMin8)
        espMin9 = self.campo_espMax9.GetValue()
        self.campo_espMin10.SetValue(espMin9)
        espMin10 = self.campo_espMax10.GetValue()
###################################################### kerfPlasma F ##########################################################################################
###################################################### kerf PLASMA I ##########################################################################################
arquivoDekerfPlasma = str(os.getcwd()) + "/.gisoplox/plasma_cutting_width.gisoplox"
kerfPlasma = open(arquivoDekerfPlasma)

#Bloco 1
espMinPlasma1 = "0"
espMaxPlasma1 = kerfPlasma.readline()
kerfPlasma1 = kerfPlasma.readline()
velPlasma1 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 2
espMinPlasma2 = kerfPlasma.readline()
espMaxPlasma2 = kerfPlasma.readline()
kerfPlasma2 = kerfPlasma.readline()
velPlasma2 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 3
espMinPlasma3 = kerfPlasma.readline()
espMaxPlasma3 = kerfPlasma.readline()
kerfPlasma3 = kerfPlasma.readline()
velPlasma3 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 4
espMinPlasma4 = kerfPlasma.readline()
espMaxPlasma4 = kerfPlasma.readline()
kerfPlasma4 = kerfPlasma.readline()
velPlasma4 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 5
espMinPlasma5 = kerfPlasma.readline()
espMaxPlasma5 = kerfPlasma.readline()
kerfPlasma5 = kerfPlasma.readline()
velPlasma5 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 6
espMinPlasma6 = kerfPlasma.readline()
espMaxPlasma6 = kerfPlasma.readline()
kerfPlasma6 = kerfPlasma.readline()
velPlasma6 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 7
espMinPlasma7 = kerfPlasma.readline()
espMaxPlasma7 = kerfPlasma.readline()
kerfPlasma7 = kerfPlasma.readline()
velPlasma7 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 8
espMinPlasma8 = kerfPlasma.readline()
espMaxPlasma8 = kerfPlasma.readline()
kerfPlasma8 = kerfPlasma.readline()
velPlasma8 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 9
espMinPlasma9 = kerfPlasma.readline()
espMaxPlasma9 = kerfPlasma.readline()
kerfPlasma9 = kerfPlasma.readline()
velPlasma9 = kerfPlasma.readline()
kerfPlasma.readline()

#Bloco 10
espMinPlasma10 = kerfPlasma.readline()
espMaxPlasma10 = kerfPlasma.readline()
kerfPlasma10 = kerfPlasma.readline()
velPlasma10 = kerfPlasma.readline()
kerfPlasma.readline()

#Retirando a quebra de linha das strings
espMaxPlasma1=espMaxPlasma1.rstrip('\n')
espMaxPlasma2=espMaxPlasma2.rstrip('\n')
espMaxPlasma3=espMaxPlasma3.rstrip('\n')
espMaxPlasma4=espMaxPlasma4.rstrip('\n')
espMaxPlasma5=espMaxPlasma5.rstrip('\n')
espMaxPlasma6=espMaxPlasma6.rstrip('\n')
espMaxPlasma7=espMaxPlasma7.rstrip('\n')
espMaxPlasma8=espMaxPlasma8.rstrip('\n')
espMaxPlasma9=espMaxPlasma9.rstrip('\n')
espMaxPlasma10=espMaxPlasma10.rstrip('\n')

espMinPlasma1=espMinPlasma1.rstrip('\n')
espMinPlasma2=espMinPlasma2.rstrip('\n')
espMinPlasma3=espMinPlasma3.rstrip('\n')
espMinPlasma4=espMinPlasma4.rstrip('\n')
espMinPlasma5=espMinPlasma5.rstrip('\n')
espMinPlasma6=espMinPlasma6.rstrip('\n')
espMinPlasma7=espMinPlasma7.rstrip('\n')
espMinPlasma8=espMinPlasma8.rstrip('\n')
espMinPlasma9=espMinPlasma9.rstrip('\n')
espMinPlasma10=espMinPlasma10.rstrip('\n')

kerfPlasma1=kerfPlasma1.rstrip('\n')
kerfPlasma2=kerfPlasma2.rstrip('\n')
kerfPlasma3=kerfPlasma3.rstrip('\n')
kerfPlasma4=kerfPlasma4.rstrip('\n')
kerfPlasma5=kerfPlasma5.rstrip('\n')
kerfPlasma6=kerfPlasma6.rstrip('\n')
kerfPlasma7=kerfPlasma7.rstrip('\n')
kerfPlasma8=kerfPlasma8.rstrip('\n')
kerfPlasma9=kerfPlasma9.rstrip('\n')
kerfPlasma10=kerfPlasma10.rstrip('\n')

velPlasma1=velPlasma1.rstrip('\n')
velPlasma2=velPlasma2.rstrip('\n')
velPlasma3=velPlasma3.rstrip('\n')
velPlasma4=velPlasma4.rstrip('\n')
velPlasma5=velPlasma5.rstrip('\n')
velPlasma6=velPlasma6.rstrip('\n')
velPlasma7=velPlasma7.rstrip('\n')
velPlasma8=velPlasma8.rstrip('\n')
velPlasma9=velPlasma9.rstrip('\n')
velPlasma10=velPlasma10.rstrip('\n')

class KerfPlasma(wx.Frame):
    def __init__(self, *args, **kwds):
        # Detalhes do frame
        if sistemaOperacional=="Linux":
            TX=440
            TY=460
            Y=40
            Ydist=30
            X1=20
            T1X=40
            T1Y=20
            X2=65
            X3=80
            X4=180
            X5=300
            T2X=60
            T2Y=20
            T3X=60
            T3Y=20
            XBC=205
            XBA=310

        if sistemaOperacional=="Windows":
            TX=420
            TY=320
            Y=30
            Ydist=20
            X1=20
            T1X=25
            T1Y=20
            X2=50
            X3=60
            X4=150
            X5=300
            T2X=60
            T2Y=20
            T3X=60
            T3Y=20
            XBC=185
            XBA=290
        
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(("GISOPLOX - Parâmetros de corte - Plasma"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_MOTION,  self.OnMove)
        self.Bind(wx.EVT_CLOSE, self.FecharkerfPlasma)
        self.style=wx.CAPTION
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)

        #Desenhando a interfácie
        wx.StaticText(self, wx.ID_ANY, ("Espessura (mm)"), pos=(15,10))
        wx.StaticText(self, wx.ID_ANY, ("Largura de corte (mm)"), pos=(120,10))
        wx.StaticText(self, wx.ID_ANY, ("Velocidade (mm/min)"), pos=(270,10))

        #Desenhando a tabela
        
        
        #Espaço 1
        self.campo_espMinPlasma1 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma1, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma1.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma1 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma1, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma1 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma1, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma1 = wx.TextCtrl(self, wx.ID_ANY, velPlasma1, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 2
        self.campo_espMinPlasma2 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma2, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma2.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma2 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma2, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma2 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma2, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma2 = wx.TextCtrl(self, wx.ID_ANY, velPlasma2, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 3
        self.campo_espMinPlasma3 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma3, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma3.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma3 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma3, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma3 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma3, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma3 = wx.TextCtrl(self, wx.ID_ANY, velPlasma3, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 4
        self.campo_espMinPlasma4 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma4, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma4.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma4 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma4, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma4 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma4, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma4 = wx.TextCtrl(self, wx.ID_ANY, velPlasma4, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 5
        self.campo_espMinPlasma5 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma5, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma5.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma5 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma5, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma5 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma5, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma5 = wx.TextCtrl(self, wx.ID_ANY, velPlasma5, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 6
        self.campo_espMinPlasma6 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma6, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma6.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma6 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma6, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma6 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma6, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma6 = wx.TextCtrl(self, wx.ID_ANY, velPlasma6, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 7
        self.campo_espMinPlasma7 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma7, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma7.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma7 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma7, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma7 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma7, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma7 = wx.TextCtrl(self, wx.ID_ANY, velPlasma7, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 8
        self.campo_espMinPlasma8 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma8, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma8.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma8 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma8, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma8 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma8, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma8 = wx.TextCtrl(self, wx.ID_ANY, velPlasma8, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 9
        self.campo_espMinPlasma9 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma9, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma9.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma9 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma9, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma9 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma9, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma9 = wx.TextCtrl(self, wx.ID_ANY, velPlasma9, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+Ydist
        #Espaço 10
        self.campo_espMinPlasma10 = wx.TextCtrl(self, wx.ID_ANY, espMinPlasma10, pos=(X1,Y), size=(T1X,T1Y))
        self.campo_espMinPlasma10.Enable(False)
        wx.StaticText(self, wx.ID_ANY, ("-"), pos=(X2,Y))
        self.campo_espMaxPlasma10 = wx.TextCtrl(self, wx.ID_ANY, espMaxPlasma10, pos=(X3,Y), size=(T1X,T1Y))
        self.campo_kerfPlasma10 = wx.TextCtrl(self, wx.ID_ANY, kerfPlasma10, pos=(X4,Y), size=(T2X,T2Y))
        self.campo_velPlasma10 = wx.TextCtrl(self, wx.ID_ANY, velPlasma10, pos=(X5,Y), size=(T3X,T3Y))

        Y=Y+50
        #Botão Cancelar
        Botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, Y))
        self.Bind(wx.EVT_BUTTON, self.FecharkerfPlasma, Botao_Cancelar)

        #Botao Aplicar
        Botao_Aplicar = wx.Button(self, id=-1, label='Aplicar', pos=(XBA, Y))
        self.Bind(wx.EVT_BUTTON, self.AplicarkerfPlasma, Botao_Aplicar)

        #Comando do botão cancelar
    def FecharkerfPlasma(self, event):
        frame_Gisoplox.Show()
        frame_KerfPlasma.Hide()

        #Comando do botão aplicar
    def AplicarkerfPlasma(self, event):
        #Pegar o valor dos campos de textoPlasma
        espMaxPlasma1=self.campo_espMaxPlasma1.GetValue()
        espMaxPlasma2=self.campo_espMaxPlasma2.GetValue()
        espMaxPlasma3=self.campo_espMaxPlasma3.GetValue()
        espMaxPlasma4=self.campo_espMaxPlasma4.GetValue()
        espMaxPlasma5=self.campo_espMaxPlasma5.GetValue()
        espMaxPlasma6=self.campo_espMaxPlasma6.GetValue()
        espMaxPlasma7=self.campo_espMaxPlasma7.GetValue()
        espMaxPlasma8=self.campo_espMaxPlasma8.GetValue()
        espMaxPlasma9=self.campo_espMaxPlasma9.GetValue()
        espMaxPlasma10=self.campo_espMaxPlasma10.GetValue()

        espMinPlasma1=self.campo_espMinPlasma1.GetValue()
        espMinPlasma2=self.campo_espMinPlasma2.GetValue()
        espMinPlasma3=self.campo_espMinPlasma3.GetValue()
        espMinPlasma4=self.campo_espMinPlasma4.GetValue()
        espMinPlasma5=self.campo_espMinPlasma5.GetValue()
        espMinPlasma6=self.campo_espMinPlasma6.GetValue()
        espMinPlasma7=self.campo_espMinPlasma7.GetValue()
        espMinPlasma8=self.campo_espMinPlasma8.GetValue()
        espMinPlasma9=self.campo_espMinPlasma9.GetValue()
        espMinPlasma10=self.campo_espMinPlasma10.GetValue()

        kerfPlasma1=self.campo_kerfPlasma1.GetValue()
        kerfPlasma2=self.campo_kerfPlasma2.GetValue()
        kerfPlasma3=self.campo_kerfPlasma3.GetValue()
        kerfPlasma4=self.campo_kerfPlasma4.GetValue()
        kerfPlasma5=self.campo_kerfPlasma5.GetValue()
        kerfPlasma6=self.campo_kerfPlasma6.GetValue()
        kerfPlasma7=self.campo_kerfPlasma7.GetValue()
        kerfPlasma8=self.campo_kerfPlasma8.GetValue()
        kerfPlasma9=self.campo_kerfPlasma9.GetValue()
        kerfPlasma10=self.campo_kerfPlasma10.GetValue()

        velPlasma1=self.campo_velPlasma1.GetValue()
        velPlasma2=self.campo_velPlasma2.GetValue()
        velPlasma3=self.campo_velPlasma3.GetValue()
        velPlasma4=self.campo_velPlasma4.GetValue()
        velPlasma5=self.campo_velPlasma5.GetValue()
        velPlasma6=self.campo_velPlasma6.GetValue()
        velPlasma7=self.campo_velPlasma7.GetValue()
        velPlasma8=self.campo_velPlasma8.GetValue()
        velPlasma9=self.campo_velPlasma9.GetValue()
        velPlasma10=self.campo_velPlasma10.GetValue()

        #Trocar vírgulas por pontos
        espMaxPlasma1=espMaxPlasma1.replace(',', '.')
        espMaxPlasma2=espMaxPlasma2.replace(',', '.')
        espMaxPlasma3=espMaxPlasma3.replace(',', '.')
        espMaxPlasma4=espMaxPlasma4.replace(',', '.')
        espMaxPlasma5=espMaxPlasma5.replace(',', '.')
        espMaxPlasma6=espMaxPlasma6.replace(',', '.')
        espMaxPlasma7=espMaxPlasma7.replace(',', '.')
        espMaxPlasma8=espMaxPlasma8.replace(',', '.')
        espMaxPlasma9=espMaxPlasma9.replace(',', '.')
        espMaxPlasma10=espMaxPlasma10.replace(',', '.')

        espMinPlasma1=espMinPlasma1.replace(',', '.')
        espMinPlasma2=espMinPlasma2.replace(',', '.')
        espMinPlasma3=espMinPlasma3.replace(',', '.')
        espMinPlasma4=espMinPlasma4.replace(',', '.')
        espMinPlasma5=espMinPlasma5.replace(',', '.')
        espMinPlasma6=espMinPlasma6.replace(',', '.')
        espMinPlasma7=espMinPlasma7.replace(',', '.')
        espMinPlasma8=espMinPlasma8.replace(',', '.')
        espMinPlasma9=espMinPlasma9.replace(',', '.')
        espMinPlasma10=espMinPlasma10.replace(',', '.')

        kerfPlasma1=kerfPlasma1.replace(',', '.')
        kerfPlasma2=kerfPlasma2.replace(',', '.')
        kerfPlasma3=kerfPlasma3.replace(',', '.')
        kerfPlasma4=kerfPlasma4.replace(',', '.')
        kerfPlasma5=kerfPlasma5.replace(',', '.')
        kerfPlasma6=kerfPlasma6.replace(',', '.')
        kerfPlasma7=kerfPlasma7.replace(',', '.')
        kerfPlasma8=kerfPlasma8.replace(',', '.')
        kerfPlasma9=kerfPlasma9.replace(',', '.')
        kerfPlasma10=kerfPlasma10.replace(',', '.')

        velPlasma1=velPlasma1.replace(',', '.')
        velPlasma2=velPlasma2.replace(',', '.')
        velPlasma3=velPlasma3.replace(',', '.')
        velPlasma4=velPlasma4.replace(',', '.')
        velPlasma5=velPlasma5.replace(',', '.')
        velPlasma6=velPlasma6.replace(',', '.')
        velPlasma7=velPlasma7.replace(',', '.')
        velPlasma8=velPlasma8.replace(',', '.')
        velPlasma9=velPlasma9.replace(',', '.')
        velPlasma10=velPlasma10.replace(',', '.')

        #Tirar espaços se houver
        espMaxPlasma1=espMaxPlasma1.replace(' ', '')
        espMaxPlasma2=espMaxPlasma2.replace(' ', '')
        espMaxPlasma3=espMaxPlasma3.replace(' ', '')
        espMaxPlasma4=espMaxPlasma4.replace(' ', '')
        espMaxPlasma5=espMaxPlasma5.replace(' ', '')
        espMaxPlasma6=espMaxPlasma6.replace(' ', '')
        espMaxPlasma7=espMaxPlasma7.replace(' ', '')
        espMaxPlasma8=espMaxPlasma8.replace(' ', '')
        espMaxPlasma9=espMaxPlasma9.replace(' ', '')
        espMaxPlasma10=espMaxPlasma10.replace(' ', '')

        espMinPlasma1=espMinPlasma1.replace(' ', '')
        espMinPlasma2=espMinPlasma2.replace(' ', '')
        espMinPlasma3=espMinPlasma3.replace(' ', '')
        espMinPlasma4=espMinPlasma4.replace(' ', '')
        espMinPlasma5=espMinPlasma5.replace(' ', '')
        espMinPlasma6=espMinPlasma6.replace(' ', '')
        espMinPlasma7=espMinPlasma7.replace(' ', '')
        espMinPlasma8=espMinPlasma8.replace(' ', '')
        espMinPlasma9=espMinPlasma9.replace(' ', '')
        espMinPlasma10=espMinPlasma10.replace(' ', '')

        kerfPlasma1=kerfPlasma1.replace(' ', '')
        kerfPlasma2=kerfPlasma2.replace(' ', '')
        kerfPlasma3=kerfPlasma3.replace(' ', '')
        kerfPlasma4=kerfPlasma4.replace(' ', '')
        kerfPlasma5=kerfPlasma5.replace(' ', '')
        kerfPlasma6=kerfPlasma6.replace(' ', '')
        kerfPlasma7=kerfPlasma7.replace(' ', '')
        kerfPlasma8=kerfPlasma8.replace(' ', '')
        kerfPlasma9=kerfPlasma9.replace(' ', '')
        kerfPlasma10=kerfPlasma10.replace(' ', '')

        velPlasma1=velPlasma1.replace(' ', '')
        velPlasma2=velPlasma2.replace(' ', '')
        velPlasma3=velPlasma3.replace(' ', '')
        velPlasma4=velPlasma4.replace(' ', '')
        velPlasma5=velPlasma5.replace(' ', '')
        velPlasma6=velPlasma6.replace(' ', '')
        velPlasma7=velPlasma7.replace(' ', '')
        velPlasma8=velPlasma8.replace(' ', '')
        velPlasma9=velPlasma9.replace(' ', '')
        velPlasma10=velPlasma10.replace(' ', '')

        
        #Procurar erros de preenchimento
        erros=0
        if espMaxPlasma1.replace('.', '').isdigit() == False or espMaxPlasma2.replace('.', '').isdigit() == False or espMaxPlasma3.replace('.', '').isdigit() == False or espMaxPlasma4.replace('.', '').isdigit() == False or espMaxPlasma5.replace('.', '').isdigit() == False or espMaxPlasma6.replace('.', '').isdigit() == False or espMaxPlasma7.replace('.', '').isdigit() == False or espMaxPlasma8.replace('.', '').isdigit() == False or espMaxPlasma9.replace('.', '').isdigit() == False or espMaxPlasma10.replace('.', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar apenas números! \nHá um erro em uma das espessuras!", caption="Atenção", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        if kerfPlasma1.replace('.', '').isdigit() == False or kerfPlasma2.replace('.', '').isdigit() == False or kerfPlasma3.replace('.', '').isdigit() == False or kerfPlasma4.replace('.', '').isdigit() == False or kerfPlasma5.replace('.', '').isdigit() == False or kerfPlasma6.replace('.', '').isdigit() == False or kerfPlasma7.replace('.', '').isdigit() == False or kerfPlasma8.replace('.', '').isdigit() == False or kerfPlasma9.replace('.', '').isdigit() == False or kerfPlasma10.replace('.', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar apenas números! \nHá um erro em uma das larguras de corte!", caption="Atenção", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        if velPlasma1.replace('.', '').isdigit() == False or velPlasma2.replace('.', '').isdigit() == False or velPlasma3.replace('.', '').isdigit() == False or velPlasma4.replace('.', '').isdigit() == False or velPlasma5.replace('.', '').isdigit() == False or velPlasma6.replace('.', '').isdigit() == False or velPlasma7.replace('.', '').isdigit() == False or velPlasma8.replace('.', '').isdigit() == False or velPlasma9.replace('.', '').isdigit() == False or velPlasma10.replace('.', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar apenas números! \nHá um erro em uma das velPlasmaocidades!", caption="Atenção", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Verificando se as minimas estão em ordem crescente    
        if float(espMaxPlasma2) <= float(espMaxPlasma1) or float(espMaxPlasma3) <= float(espMaxPlasma2) or float(espMaxPlasma4) <= float(espMaxPlasma3) or float(espMaxPlasma5) <= float(espMaxPlasma4) or float(espMaxPlasma6) <= float(espMaxPlasma5) or float(espMaxPlasma7) <= float(espMaxPlasma6) or float(espMaxPlasma8) <= float(espMaxPlasma7) or float(espMaxPlasma9) <= float(espMaxPlasma8) or float(espMaxPlasma10) <= float(espMaxPlasma9):
            dlg = wx.MessageDialog(parent=None, message="Você deve digitar os dados em ordem crescente!", caption="Dados incoerentes", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Escrever as novas configurações no arquivo
        if erros == 0:
            textoPlasma = espMaxPlasma1
            textoPlasma = textoPlasma + "\n" + kerfPlasma1
            textoPlasma = textoPlasma + "\n" + velPlasma1 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma2
            textoPlasma = textoPlasma + "\n" + espMaxPlasma2
            textoPlasma = textoPlasma + "\n" + kerfPlasma2
            textoPlasma = textoPlasma + "\n" + velPlasma2 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma3
            textoPlasma = textoPlasma + "\n" + espMaxPlasma3
            textoPlasma = textoPlasma + "\n" + kerfPlasma3
            textoPlasma = textoPlasma + "\n" + velPlasma3 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma4
            textoPlasma = textoPlasma + "\n" + espMaxPlasma4
            textoPlasma = textoPlasma + "\n" + kerfPlasma4
            textoPlasma = textoPlasma + "\n" + velPlasma4 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma5
            textoPlasma = textoPlasma + "\n" + espMaxPlasma5
            textoPlasma = textoPlasma + "\n" + kerfPlasma5
            textoPlasma = textoPlasma + "\n" + velPlasma5 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma6
            textoPlasma = textoPlasma + "\n" + espMaxPlasma6
            textoPlasma = textoPlasma + "\n" + kerfPlasma6
            textoPlasma = textoPlasma + "\n" + velPlasma6 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma7
            textoPlasma = textoPlasma + "\n" + espMaxPlasma7
            textoPlasma = textoPlasma + "\n" + kerfPlasma7
            textoPlasma = textoPlasma + "\n" + velPlasma7 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma8
            textoPlasma = textoPlasma + "\n" + espMaxPlasma8
            textoPlasma = textoPlasma + "\n" + kerfPlasma8
            textoPlasma = textoPlasma + "\n" + velPlasma8 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma9
            textoPlasma = textoPlasma + "\n" + espMaxPlasma9
            textoPlasma = textoPlasma + "\n" + kerfPlasma9
            textoPlasma = textoPlasma + "\n" + velPlasma9 + "\n"
            textoPlasma = textoPlasma + "\n" + espMinPlasma10
            textoPlasma = textoPlasma + "\n" + espMaxPlasma10
            textoPlasma = textoPlasma + "\n" + kerfPlasma10
            textoPlasma = textoPlasma + "\n" + velPlasma10
            escrever = open(arquivoDekerfPlasma, "w")
            escrever.write(textoPlasma)
            escrever.close()

            #Mostrar aviso de sucesso
            dlg = wx.MessageDialog(parent=None, message="Configurações salvas com sucesso", caption="Configurações salvas", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        
    def OnMove(self, event):

        #Atualizar campos
        espMinPlasma1 = self.campo_espMaxPlasma1.GetValue()
        self.campo_espMinPlasma2.SetValue(espMinPlasma1)
        espMinPlasma2 = self.campo_espMaxPlasma2.GetValue()
        self.campo_espMinPlasma3.SetValue(espMinPlasma2)
        espMinPlasma3 = self.campo_espMaxPlasma3.GetValue()
        self.campo_espMinPlasma4.SetValue(espMinPlasma3)
        espMinPlasma4 = self.campo_espMaxPlasma4.GetValue()
        self.campo_espMinPlasma5.SetValue(espMinPlasma4)
        espMinPlasma5 = self.campo_espMaxPlasma5.GetValue()
        self.campo_espMinPlasma6.SetValue(espMinPlasma5)
        espMinPlasma6 = self.campo_espMaxPlasma6.GetValue()
        self.campo_espMinPlasma7.SetValue(espMinPlasma6)
        espMinPlasma7 = self.campo_espMaxPlasma7.GetValue()
        self.campo_espMinPlasma8.SetValue(espMinPlasma7)
        espMinPlasma8 = self.campo_espMaxPlasma8.GetValue()
        self.campo_espMinPlasma9.SetValue(espMinPlasma8)
        espMinPlasma9 = self.campo_espMaxPlasma9.GetValue()
        self.campo_espMinPlasma10.SetValue(espMinPlasma9)
        espMinPlasma10 = self.campo_espMaxPlasma10.GetValue()
###################################################### kerf PLASMA F ##########################################################################################
########################################################### I - Rectange ##############################################################################
class OrectangeFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            TX=600
            TY=480
            X1=160
            X2=18
            X3=310
            X4=380
            X5=430
            X6=480
            X7=310
            X8=390
            X9=445
            X10=425
            X11=460
            X12=435
            X13=497
            X14=508
            XBC=400
            XBA=490
            T1X=50
            T2X=30
            T3X=60
            Y1=20
            Y2=200
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358

            

            YCX=30
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"
            
        if sistemaOperacional=="Windows":
            TX=600
            TY=480
            X1=160
            X2=28
            X3=310
            X4=370
            X5=420
            X6=470
            X7=310
            X8=380
            X9=425
            X10=405
            X11=430
            X12=420
            X13=484
            X14=495
            XBC=380
            XBA=470
            T1X=40
            T2X=20
            T3X=60
            Y1=28
            Y2=200
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=370
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=288
            YCancelar=348
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

            YCX=20
            
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Retângulo"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_CLOSE, self.FecharRectange)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        #self.currentDirectory = os.getcwd()
        #Desenho e cotas
        self.campo_de_texto_TamanhoX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X1,Y1), size=(T1X,YCX))
        self.campo_de_texto_TamanhoY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X2,Y2), size=(T1X,YCX))

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X3,Y3))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y3), size=(T1X,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X5, Y3))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X6, Y3))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X7,Y4))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X8,Y4), size=(T1X,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X9,Y4))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X3,Y5))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X10,Y5), size=(T2X,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X11,Y5))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X3,Y6))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X12,Y6), size=(T3X,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X13,Y6))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X14,Y6), size=(T3X,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharRectange, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

        #self.Bind(wx.EVT_MOTION,  self.OnMove)        
        #self.posCtrl = wx.TextCtrl(self, -1, "", pos=(406, 322))

    def OnMove(self, event):
        pos = event.GetPosition()
        #self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o retângulo
        xi=85
        yi=65
        drx=200
        dry=300
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,drx,yi)
        dc.DrawLine(drx,yi,drx,dry)
        dc.DrawLine(drx,dry,xi,dry)
        dc.DrawLine(xi,dry,xi,yi)

        #Desenhando as cotas
        dc.SetPen(cota)
        tamLinha=20
        dist=4
        flechaX=12
        flechaY=4
        mLinha=int(tamLinha/2)
        
        #Cota superior
        dc.DrawLine(xi,yi-dist,xi,yi-dist-tamLinha)
        dc.DrawLine(drx,yi-dist,drx,yi-dist-tamLinha)
        dc.DrawLine(xi,yi-dist-mLinha,drx,yi-dist-mLinha)

        #Flecha superior esquerda
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha+flechaY)

        #Flecha superior direita
        dc.DrawLine(drx,yi-dist-mLinha,drx-flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(drx,yi-dist-mLinha,drx-flechaX,yi-dist-mLinha+flechaY)

        #Cota lateral
        dc.DrawLine(xi-dist,yi,xi-dist-tamLinha,yi)
        dc.DrawLine(xi-dist,dry,xi-dist-tamLinha,dry)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha,dry)

        #Flecha lateral superior
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha-flechaY,yi+flechaX)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha+flechaY,yi+flechaX)

        #Flecha lateral inferior
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha-flechaY,dry-flechaX)
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha+flechaY,dry-flechaX)

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Criando variavel "salvar" vazia para poder fazer comparações
        salvar=""

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            print(Kerf)
            pecasGeradas, programa, distCorte=Plasma.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        #print salvar

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and erros==0:
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)
        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def FecharRectange(self, event):
        frame_Gisoplox.Show()
        #print "Fechando..."
        frame_Rectange.Hide()
########################################################### F - Rectange ##############################################################################
########################################################### I - Circle ##############################################################################
class OcircleFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            X1=300
            X2=117
            X3=315
            X4=135
            TX1=40
            TX2=40
            X5=310
            X6=380
            X7=420
            X8=470
            X9=310
            X10=390
            X11=435
            X12=X9
            X13=423
            X14=445
            X15=X12
            X16=433
            X17=494
            X18=505
            X19=380
            X20=470
            X21=40

            XCX1=40
            XCX2=20
            XCX3=60
            YCX=30

            Y1=22
            Y2=134
            Y3=17
            Y4=127
            Y5=70
            Y6=107
            Y7=144
            Y8=181
            Y9=228
            Y10=350

            T1X=40
            T2X=20
            T3X=60
            XTextoProcesso=X5
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=380
            YSalvarPad=288
            YCancelar=348
            XBC=380
            XBA=470

            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

        if sistemaOperacional=="Windows":
            X1=300
            X2=117
            X3=317
            X4=135
            TX1=40
            TX2=40
            X5=310
            X6=370
            X7=420
            X8=470
            X9=310
            X10=380
            X11=425
            X12=X9
            X13=405
            X14=430
            X15=X12
            X16=420
            X17=484
            X18=495
            X19=380
            X20=470
            X21=40

            XCX1=40
            XCX2=20
            XCX3=60
            YCX=20

            Y1=25
            Y2=135
            Y3=25
            Y4=135
            Y5=70
            Y6=107
            Y7=144
            Y8=181
            Y9=228
            Y10=350

            T1X=40
            T2X=20
            T3X=60
            XTextoProcesso=X5
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=380
            YSalvarPad=288
            YCancelar=348
            XBC=380
            XBA=470

            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Anel"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((600, 480))
        self.Bind(wx.EVT_CLOSE, self.FecharCircle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        #Campos de texto das cotas
        simbDimExt = wx.StaticText(self, wx.ID_ANY, "Ø", pos=(X1,Y1))
        simbDimInt = wx.StaticText(self, wx.ID_ANY, "Ø", pos=(X2,Y2))
        #fonteDiam = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        fonteDiam = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        simbDimExt.SetFont(fonteDiam)
        simbDimInt.SetFont(fonteDiam)
        self.campo_de_texto_DiamExt=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X3,Y3), size=(TX1,YCX))
        self.campo_de_texto_DiamInt=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y4), size=(TX2,YCX))

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X5,Y5))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X6,Y5), size=(XCX1,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X7, 70))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X8, Y5))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X9,Y6))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X10,Y6), size=(XCX1,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X11,Y6))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X12,Y7))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X13,Y7), size=(XCX2,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X14,Y7))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X15,181))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X16,Y8), size=(XCX3,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X17,Y8))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X18,Y8), size=(XCX3,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharCircle, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

        self.Bind(wx.EVT_MOTION,  self.OnMove)        
        #self.posCtrl = wx.TextCtrl(self, -1, "", pos=(X21, Y10))

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o anel
        def desenharCirculo(diam, xc, yc):
            raio=diam/2.0
            x=-raio+0.01
            #print x
            while -raio<x<raio:
                y=math.sqrt(raio*raio-x*x)
                xf=x+1.0
                if xf<raio:
                    yf=math.sqrt(raio*raio-xf*xf)                
                dc.DrawLine(int(round(x+xc)),int(round(y+yc)),int(round(xf+xc)),int(round(yf+yc)))
                dc.DrawLine(int(round(x+xc)),int(round(-y+yc)),int(round(xf+xc)),int(round(-yf+yc)))
                dc.DrawLine(int(round(y+xc)),int(round(x+yc)),int(round(yf+xc)),int(round(xf+yc)))
                dc.DrawLine(int(round(y-xc)),int(round(x+yc)),int(round(yf-xc)),int(round(xf+yc)))
                x+=1.0
        desenharCirculo(264, 140, 160)
        desenharCirculo(140, 140, 160)

        #Desenhando as cotas
        #Cota diam externo
        dc.SetPen(cota)
        Xi=247
        Yi=83
        Xm=288
        Ym=49
        Xf=360
        Xvf1=7
        Yvf1=9
        Xvf2=10
        Yvf2=5

        Xf1=Xi+Xvf1
        Yf1=Yi-Yvf1
        Xf2=Xi+Xvf2
        Yf2=Yi-Yvf2
        
        dc.DrawLine(Xi,Yi,Xm,Ym)
        dc.DrawLine(Xm,Ym,Xf,Ym)
        dc.DrawLine(Xi,Yi,Xf1,Yf1) #Lado esq flecha
        dc.DrawLine(Xi,Yi,Xf2,Yf2) #Lado dir flecha

        #Cota diam interno
        XiCotaInterna=71
        XfCotaInterna=209
        XvCotaInterna=11
        YCotaInterna=160
        YvCotaInterna=3
        dc.DrawLine(XiCotaInterna,YCotaInterna,XfCotaInterna,YCotaInterna)
        dc.DrawLine(XfCotaInterna-XvCotaInterna,YCotaInterna-YvCotaInterna,XfCotaInterna,YCotaInterna) #Cota esq superior
        dc.DrawLine(XfCotaInterna-XvCotaInterna,YCotaInterna+YvCotaInterna-1,XfCotaInterna,YCotaInterna) #Cota esq inferior
        dc.DrawLine(XiCotaInterna,YCotaInterna,XiCotaInterna+XvCotaInterna,YCotaInterna-YvCotaInterna) #Cota dir superior
        dc.DrawLine(XiCotaInterna,YCotaInterna,XiCotaInterna+XvCotaInterna,YCotaInterna+YvCotaInterna-1) #Cota dir inferior

    def OnMove(self, event):
        pos = event.GetPosition()
        #self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        diam1=self.campo_de_texto_DiamExt.GetValue()
        diam2=self.campo_de_texto_DiamInt.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
        diam1=diam1.replace(',', '.')
        diam2=diam2.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=str(espessura)
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0
        Esp=float(espessura)

        #Erro: A espessura digitada é inválida
        if str(espessura).replace('.', '').replace('/', '').replace('"', '').replace('-', '').replace(' ', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="A espessura digitada é inválida!\nDigite apenas números!", caption="Espessura inválida", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura digitada é inválida
        if str(espessura).replace('.', '').replace('/', '').replace('"', '').replace('-', '').replace(' ', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="A espessura digitada é inválida!\nDigite apenas números!", caption="Espessura inválida", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Diametro externo não for preenchido
        if diam1=="" or diam1.replace('.', '').isdigit() == False:
            if diam1=="":
                dlg = wx.MessageDialog(parent=None, message="O diâmetro externo não foi digitado!", caption="Verifique o diâmetro externo digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1
            if diam1!="":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no diâmetro externo informado!\nDigite apenas números.", caption="Verifique o diâmetro externo digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: Diametro interno não for preenchido
        if diam2=="" or diam2.replace('.', '').isdigit() == False:
            if diam2=="":
                dlg = wx.MessageDialog(parent=None, message="O diâmetro interno não foi digitado!\n\nCaso queira gerar o código de uma peça sem furo\nabra a página principal do GISOPLOX e no menu\nescolha as seguintes opções:\n\n>>Ferramentas/Círculos/Círculo", caption="Verifique o diâmetro interno digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1
            if diam2!="":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no diâmetro interno informado!\nDigite apenas números.", caption="Verifique o diâmetro interno digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: Diametro externo e' menor que o interno
        if diam1.replace('.', '').isdigit() == True and diam2.replace('.', '').isdigit() == True:
            if float(diam1) < float(diam2):
                dlg = wx.MessageDialog(parent=None, message="O diâmetro externo digitado é menor que o diâmetro interno!", caption="Verifique os diâmetros digitados", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: Diametro externo e' igual que o interno
        if diam1.replace('.', '').isdigit() == True and diam2.replace('.', '').isdigit() == True:
            if float(diam1) == float(diam2):
                dlg = wx.MessageDialog(parent=None, message="O diâmetro externo digitado é igual ao diâmetro interno!", caption="Verifique os diâmetros digitados", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!\nDigite apenas números.", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calculando peso em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoAnel(Esp, diam1, diam2, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)
        
        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        intdiam1=int(round(float(diam1), 0))
        intdiam2=int(round(float(diam2), 0))
        nomePadrao=espi + "XD" + str(intdiam1) + "XD" + str(intdiam2) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()


        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(diam1)+'","'+str(diam2)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'",anel,"'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='diam1,diam2,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)      

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        diam1=self.campo_de_texto_DiamExt.GetValue()
        diam2=self.campo_de_texto_DiamInt.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
        diam1=diam1.replace(',', '.')
        diam2=diam2.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=str(espessura)
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0
        Esp=float(espessura)

        #Erro: A espessura digitada é inválida
        if str(espessura).replace('.', '').replace('/', '').replace('"', '').replace('-', '').replace(' ', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="A espessura digitada é inválida!\nDigite apenas números!", caption="Espessura inválida", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura digitada é inválida
        if str(espessura).replace('.', '').replace('/', '').replace('"', '').replace('-', '').replace(' ', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="A espessura digitada é inválida!\nDigite apenas números!", caption="Espessura inválida", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Diametro externo não for preenchido
        if diam1=="" or diam1.replace('.', '').isdigit() == False:
            if diam1=="":
                dlg = wx.MessageDialog(parent=None, message="O diâmetro externo não foi digitado!", caption="Verifique o diâmetro externo digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1
            if diam1!="":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no diâmetro externo informado!\nDigite apenas números.", caption="Verifique o diâmetro externo digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: Diametro interno não for preenchido
        if diam2=="" or diam2.replace('.', '').isdigit() == False:
            if diam2=="":
                dlg = wx.MessageDialog(parent=None, message="O diâmetro interno não foi digitado!\n\nCaso queira gerar o código de uma peça sem furo\nabra a página principal do GISOPLOX e no menu\nescolha as seguintes opções:\n\n>>Ferramentas/Círculos/Círculo", caption="Verifique o diâmetro interno digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1
            if diam2!="":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no diâmetro interno informado!\nDigite apenas números.", caption="Verifique o diâmetro interno digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: Diametro externo e' menor que o interno
        if diam1.replace('.', '').isdigit() == True and diam2.replace('.', '').isdigit() == True:
            if float(diam1) < float(diam2):
                dlg = wx.MessageDialog(parent=None, message="O diâmetro externo digitado é menor que o diâmetro interno!", caption="Verifique os diâmetros digitados", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: Diametro externo e' igual que o interno
        if diam1.replace('.', '').isdigit() == True and diam2.replace('.', '').isdigit() == True:
            if float(diam1) == float(diam2):
                dlg = wx.MessageDialog(parent=None, message="O diâmetro externo digitado é igual ao diâmetro interno!", caption="Verifique os diâmetros digitados", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!\nDigite apenas números.", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.Circulo(diam1, diam2, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calculando peso em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoAnel(Esp, diam1, diam2, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        intdiam1=int(round(float(diam1), 0))
        intdiam2=int(round(float(diam2), 0))
        nomePadrao=espi + "XD" + str(intdiam1) + "XD" + str(intdiam2) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        #print salvar

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and erros==0:
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

         #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(diam1)+'","'+str(diam2)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'",anel,"'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='diam1,diam2,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def FecharCircle(self, event):
        frame_Gisoplox.Show()
        frame_Circle.Hide()
########################################################### F - Circle ##############################################################################
########################################################### I - CircleSimple ##############################################################################
class CircleSimple(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            X1=300
            X2=117
            X3=315
            X4=135
            TX1=40
            TX2=40
            X5=310
            X6=380
            X7=420
            X8=470
            X9=310
            X10=390
            X11=435
            X12=X9
            X13=423
            X14=445
            X15=X12
            X16=433
            X17=494
            X18=505
            X19=380
            X20=470
            X21=40

            XCX1=40
            XCX2=20
            XCX3=60
            YCX=30

            Y1=22
            Y2=134
            Y3=17
            Y4=127
            Y5=70
            Y6=107
            Y7=144
            Y8=181
            Y9=228
            Y10=350

            T1X=40
            T2X=20
            T3X=60
            XTextoProcesso=X5
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=380
            YSalvarPad=288
            YCancelar=348
            XBC=380
            XBA=470

            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

        if sistemaOperacional=="Windows":
            X1=300
            X2=117
            X3=317
            X4=135
            TX1=40
            TX2=40
            X5=310
            X6=370
            X7=420
            X8=470
            X9=310
            X10=380
            X11=425
            X12=X9
            X13=405
            X14=430
            X15=X12
            X16=420
            X17=484
            X18=495
            X19=380
            X20=470
            X21=40

            XCX1=40
            XCX2=20
            XCX3=60
            YCX=25

            Y1=25
            Y2=130
            Y3=25
            Y4=130
            Y5=70
            Y6=107
            Y7=144
            Y8=181
            Y9=228
            Y10=350

            T1X=40
            T2X=20
            T3X=60
            XTextoProcesso=X5
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=380
            YSalvarPad=288
            YCancelar=348
            XBC=380
            XBA=470

            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Círculo simples"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((600, 480))
        self.Bind(wx.EVT_CLOSE, self.FecharCircleSimple)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        #Campos de texto das cotas
        simbDimExt = wx.StaticText(self, wx.ID_ANY, "Ø", pos=(X2,Y2))
        fonteDiam = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        simbDimExt.SetFont(fonteDiam)
        self.campo_de_texto_DiamExt=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y4), size=(TX2,YCX))

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X5,Y5))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X6,Y5), size=(XCX1,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X7, 70))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X8, Y5))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X9,Y6))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X10,Y6), size=(XCX1,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X11,Y6))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X12,Y7))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X13,Y7), size=(XCX2,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X14,Y7))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X15,181))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X16,Y8), size=(XCX3,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X17,Y8))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X18,Y8), size=(XCX3,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharCircleSimple, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

        self.Bind(wx.EVT_MOTION,  self.OnMove)        
        #self.posCtrl = wx.TextCtrl(self, -1, "", pos=(X21, Y10))

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o anel
        def desenharCirculo(diam, xc, yc):
            raio=diam/2.0
            x=-raio+0.01
            #print x
            while -raio<x<raio:
                y=math.sqrt(raio*raio-x*x)
                xf=x+1.0
                if xf<raio:
                    yf=math.sqrt(raio*raio-xf*xf)                
                dc.DrawLine(int(round(x+xc)),int(round(y+yc)),int(round(xf+xc)),int(round(yf+yc)))
                dc.DrawLine(int(round(x+xc)),int(round(-y+yc)),int(round(xf+xc)),int(round(-yf+yc)))
                dc.DrawLine(int(round(y+xc)),int(round(x+yc)),int(round(yf+xc)),int(round(xf+yc)))
                dc.DrawLine(int(round(y-xc)),int(round(x+yc)),int(round(yf-xc)),int(round(xf+yc)))
                x+=1.0
        desenharCirculo(264, 140, 160)
        #desenharCirculo(140, 140, 160)

        #Desenhando as cotas
        #Cota diam externo
        dc.SetPen(cota)
        Xi=247
        Yi=83
        Xm=288
        Ym=49
        Xf=360
        Xvf1=7
        Yvf1=9
        Xvf2=10
        Yvf2=5

        Xf1=Xi+Xvf1
        Yf1=Yi-Yvf1
        Xf2=Xi+Xvf2
        Yf2=Yi-Yvf2

        #Cota diam interno
        XiCotaInterna=7
        XfCotaInterna=271
        XvCotaInterna=13
        YCotaInterna=160
        YvCotaInterna=5
        dc.DrawLine(XiCotaInterna,YCotaInterna,XfCotaInterna,YCotaInterna)
        dc.DrawLine(XfCotaInterna-XvCotaInterna,YCotaInterna-YvCotaInterna,XfCotaInterna,YCotaInterna) #Cota esq superior
        dc.DrawLine(XfCotaInterna-XvCotaInterna,YCotaInterna+YvCotaInterna-1,XfCotaInterna,YCotaInterna) #Cota esq inferior
        dc.DrawLine(XiCotaInterna,YCotaInterna,XiCotaInterna+XvCotaInterna,YCotaInterna-YvCotaInterna) #Cota dir superior
        dc.DrawLine(XiCotaInterna,YCotaInterna,XiCotaInterna+XvCotaInterna,YCotaInterna+YvCotaInterna-1) #Cota dir inferior

    def OnMove(self, event):
        pos = event.GetPosition()
        #self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        diam=self.campo_de_texto_DiamExt.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        espi=espessura.replace('.', ',')
        processo=self.lista_Processo.GetValue()
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
        diam1=diam.replace(',', '.')
        diam=diam1
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0
        Esp=float(espessura)

        #Erro: A espessura digitada é inválida
        if str(espessura).replace('.', '').replace('/', '').replace('"', '').replace('-', '').replace(' ', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="A espessura digitada é inválida!\nDigite apenas números!", caption="Espessura inválida", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Diametro externo não for preenchido
        if diam=="" or diam.replace('.', '').isdigit() == False:
            if diam=="":
                dlg = wx.MessageDialog(parent=None, message="O diâmetro não foi digitado!", caption="Verifique o diâmetro digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1
            if diam!="":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no diâmetro externo informado!\nDigite apenas números.", caption="Verifique o diâmetro externo digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!\nDigite apenas números.", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Colocar unidade na espessura milimetrica
        if self.radio_esp_pol.GetValue() == False:
            espi+=" mm "

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.CirculoSimples(diam, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.CirculoSimples(diam, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoCirculo(Esp, diam, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)
        
        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        intdiam=int(round(float(diam), 0))
        nomePadrao=espi + "X D" + str(intdiam) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(diam1)+'","","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'",circulo,"'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='diam1,,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        diam=self.campo_de_texto_DiamExt.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        espi=espessura.replace('.', ',')
        processo=self.lista_Processo.GetValue()
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
        diam1=diam.replace(',', '.')
        diam=diam1
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0
        Esp=float(espessura)

        #Erro: A espessura digitada é inválida
        if str(espessura).replace('.', '').replace('/', '').replace('"', '').replace('-', '').replace(' ', '').isdigit() == False:
            dlg = wx.MessageDialog(parent=None, message="A espessura digitada é inválida!\nDigite apenas números!", caption="Espessura inválida", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Diametro externo não for preenchido
        if diam=="" or diam.replace('.', '').isdigit() == False:
            if diam=="":
                dlg = wx.MessageDialog(parent=None, message="O diâmetro não foi digitado!", caption="Verifique o diâmetro digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1
            if diam!="":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no diâmetro externo informado!\nDigite apenas números.", caption="Verifique o diâmetro externo digitado", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
                erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!\nDigite apenas números.", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Colocar unidade na espessura milimetrica
        if self.radio_esp_pol.GetValue() == False:
            espi+=" mm "

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.CirculoSimples(diam, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.CirculoSimples(diam, entrada, chapaX, chapaY, pecas, Kerf)
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoCirculo(Esp, diam, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        intdiam=int(round(float(diam), 0))
        nomePadrao=espi + "X D" + str(intdiam) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        #print salvar

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and erros==0:
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(diam1)+'","","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'",circulo,"'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='diam1,,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def FecharCircleSimple(self, event):
        frame_Gisoplox.Show()
        frame_CircleSimple.Hide()
########################################################### F - CircleSimple ##############################################################################
########################################################### I - Triangulo ##############################################################################
class FrameTriangulo(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            TX=600
            TY=480
            X1=160
            X2=18
            X3=310
            X4=380
            X5=430
            X6=480
            X7=310
            X8=390
            X9=445
            X10=425
            X11=460
            X12=435
            X13=497
            X14=508
            XBC=400
            XBA=490
            T1X=50
            T2X=30
            T3X=60
            Y1=38
            Y2=210
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358

            

            YCX=30
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"
            
        if sistemaOperacional=="Windows":
            TX=600
            TY=480
            X1=160
            X2=28
            X3=310
            X4=370
            X5=420
            X6=470
            X7=310
            X8=380
            X9=425
            X10=405
            X11=430
            X12=420
            X13=484
            X14=495
            XBC=380
            XBA=470
            T1X=40
            T2X=20
            T3X=60
            Y1=43
            Y2=230
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=370
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=288
            YCancelar=348
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

            YCX=25
            
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Triângulo retângulo"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_CLOSE, self.FecharTriangulo)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.currentDirectory = os.getcwd()
        self.currentDirectory = self.currentDirectory + "/CNC"

        #Desenho e cotas
        self.campo_de_texto_TamanhoX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X1,Y1), size=(T1X,YCX))
        self.campo_de_texto_TamanhoY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X2,Y2), size=(T1X,YCX))

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X3,Y3))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y3), size=(T1X,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X5, Y3))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X6, Y3))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X7,Y4))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X8,Y4), size=(T1X,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X9,Y4))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X3,Y5))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X10,Y5), size=(T2X,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X11,Y5))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X3,Y6))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X12,Y6), size=(T3X,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X13,Y6))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X14,Y6), size=(T3X,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharTriangulo, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

        #self.Bind(wx.EVT_MOTION,  self.OnMove)        
        #self.posCtrl = wx.TextCtrl(self, -1, "", pos=(406, 322))

    def OnMove(self, event):
        pos = event.GetPosition()
        #self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o triângulo
        xi=85
        yi=85
        drx=200
        dry=300
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,drx,yi)
        dc.DrawLine(xi,dry,drx,yi)
        dc.DrawLine(xi,dry,xi,yi)

        #Desenhando as cotas
        dc.SetPen(cota)
        tamLinha=20
        dist=4
        flechaX=12
        flechaY=4
        mLinha=int(tamLinha/2)
        
        #Cota superior
        dc.DrawLine(xi,yi-dist,xi,yi-dist-tamLinha)
        dc.DrawLine(drx,yi-dist,drx,yi-dist-tamLinha)
        dc.DrawLine(xi,yi-dist-mLinha,drx,yi-dist-mLinha)

        #Flecha superior esquerda
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha+flechaY)

        #Flecha superior direita
        dc.DrawLine(drx,yi-dist-mLinha,drx-flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(drx,yi-dist-mLinha,drx-flechaX,yi-dist-mLinha+flechaY)

        #Cota lateral
        dc.DrawLine(xi-dist,yi,xi-dist-tamLinha,yi)
        dc.DrawLine(xi-dist,dry,xi-dist-tamLinha,dry)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha,dry)

        #Flecha lateral superior
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha-flechaY,yi+flechaX)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha+flechaY,yi+flechaX)

        #Flecha lateral inferior
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha-flechaY,dry-flechaX)
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha+flechaY,dry-flechaX)

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Criando variavel "salvar" vazia para poder fazer comparações
        salvar=""

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoTrianguloRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","triangulo retangulo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.TrianguloRetangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoTrianguloRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        #print salvar

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and erros==0:
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

         #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","triangulo retangulo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def FecharTriangulo(self, event):
        frame_Gisoplox.Show()
        frame_Triangulo.Hide()

###################################################################### F - Triangulo ###########################################################################
########################################################### I - Triangulo com pontas cortadas ##############################################################################
class FrameTrianguloPontasCortadas(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            TX=600
            TY=480
            X1=160
            X2=18
            X3=310
            X4=380
            X5=430
            X6=480
            X7=310
            X8=390
            X9=445
            X10=425
            X11=460
            X12=435
            X13=497
            X14=508
            XBC=400
            XBA=490
            T1X=50
            T2X=30
            T3X=60
            Y1=38
            Y2=210
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358
            XtamX=160
            YtamX=390
            XchanfX=90
            YchanfX=35
            XchanfY=300
            YchanfY=345

            YCX=30
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"
            
        if sistemaOperacional=="Windows":
            TX=600
            TY=480
            X1=160
            X2=28
            X3=310
            X4=370
            X5=420
            X6=470
            X7=310
            X8=380
            X9=425
            X10=405
            X11=430
            X12=420
            X13=484
            X14=495
            XBC=380
            XBA=470
            T1X=40
            T2X=20
            T3X=60
            Y1=43
            Y2=230
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358
            XtamX=160
            YtamX=395
            XchanfX=95
            YchanfX=40
            XchanfY=315
            YchanfY=350
            
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

            YCX=25
            
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Triângulo com pontas cortadas"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_CLOSE, self.FecharTrianguloPontasCortadas)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.currentDirectory = os.getcwd()
        self.currentDirectory = self.currentDirectory + "/CNC"

        #Desenho e cotas
        self.campo_de_texto_TamanhoX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(XtamX,YtamX), size=(T1X,YCX))
        self.campo_de_texto_ChanfroX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(XchanfX,YchanfX), size=(T1X,YCX))
        self.campo_de_texto_ChanfroY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(XchanfY,YchanfY), size=(T1X,YCX))
        self.campo_de_texto_TamanhoY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X2,Y2), size=(T1X,YCX))

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X3,Y3))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y3), size=(T1X,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X5, Y3))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X6, Y3))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X7,Y4))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X8,Y4), size=(T1X,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X9,Y4))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X3,Y5))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X10,Y5), size=(T2X,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X11,Y5))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X3,Y6))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X12,Y6), size=(T3X,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X13,Y6))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X14,Y6), size=(T3X,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharTrianguloPontasCortadas, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

        #self.Bind(wx.EVT_MOTION,  self.OnMove)        
        #self.posCtrl = wx.TextCtrl(self, -1, "", pos=(406, 322))

    def OnMove(self, event):
        pos = event.GetPosition()
        #self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        #Desenhando o triângulo
        xi=85
        yi=85
        xLinha=60
        yLinha=50
        drx=200
        dry=300
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,xi,dry)
        dc.DrawLine(xi,dry,drx,dry)
        dc.DrawLine(drx,dry,drx,(dry-yLinha))
        dc.DrawLine(drx,(dry-yLinha),(xi+xLinha),yi)
        dc.DrawLine((xi+xLinha),yi,xi,yi)

        #Desenhando as cotas
        dc.SetPen(cota)
        tamLinha=20
        dist=4
        flechaX=12
        flechaY=4
        mLinha=int(tamLinha/2)
        
        #Cota superior
        dc.DrawLine(xi,yi-dist,xi,yi-dist-tamLinha)
        dc.DrawLine((xi+xLinha),yi-dist,(xi+xLinha),yi-dist-tamLinha)
        dc.DrawLine(xi,yi-dist-mLinha,(xi+xLinha),yi-dist-mLinha)

        #Flecha superior esquerda
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha+flechaY)

        #Flecha superior direita
        dc.DrawLine((xi+xLinha),yi-dist-mLinha,(xi+xLinha)-flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine((xi+xLinha),yi-dist-mLinha,(xi+xLinha)-flechaX,yi-dist-mLinha+flechaY)

        #Cota inferior
        tamLinhaInf=45
        mLinhaInf=35
        dc.DrawLine(xi,dry+dist,xi,dry+dist+tamLinhaInf)
        dc.DrawLine(drx,dry+dist,drx,dry+dist+tamLinhaInf)
        dc.DrawLine(xi,dry+dist+mLinhaInf,drx,dry+dist+mLinhaInf)

        #Flecha inferior esquerda
        dc.DrawLine(xi,dry+mLinhaInf+dist,xi+flechaX,dry+mLinhaInf-flechaY+dist)
        dc.DrawLine(xi,dry+mLinhaInf+dist,xi+flechaX,dry+mLinhaInf+flechaY+dist)

        #Flecha inferior direita
        dc.DrawLine(drx,dry+mLinhaInf+dist,drx-flechaX,dry+mLinhaInf-flechaY+dist)
        dc.DrawLine(drx,dry+mLinhaInf+dist,drx-flechaX,dry+mLinhaInf+flechaY+dist)       

        #Cota lateral
        dc.DrawLine(xi-dist,yi,xi-dist-tamLinha,yi)
        dc.DrawLine(xi-dist,dry,xi-dist-tamLinha,dry)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha,dry)

        #Flecha lateral superior
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha-flechaY,yi+flechaX)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha+flechaY,yi+flechaX)

        #Flecha lateral inferior
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha-flechaY,dry-flechaX)
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha+flechaY,dry-flechaX)

        #Cota lateral chanfro Y
        xi=293
        xf=370
        yi=335
        yf=dry
        mLinha=-70
        dc.DrawLine(xi-dist,yi,xf,yi)
        dc.DrawLine(xi-dist,yf,xf,yf)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha,dry)

        #Flecha lateral superior chanfro Y
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha-flechaY,yi+flechaX)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha+flechaY,yi+flechaX)

        #Flecha lateral inferior chanfro Y
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha-flechaY,dry-flechaX)
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha+flechaY,dry-flechaX)

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        chanfroX=self.campo_de_texto_ChanfroX.GetValue()
        chanfroY=self.campo_de_texto_ChanfroY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Criando variavel "salvar" vazia para poder fazer comparações
        salvar=""

        #Trocar pontos por vírgula
        txd=txd.replace(',', '.')
        tyd=tyd.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')
        chanfroX=chanfroX.replace(',', '.')
        chanfroY=chanfroY.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            elif txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        if chanfroX.replace('.', '').isdigit() == False or chanfroY.replace('.', '').isdigit() == False:
            if chanfroX == "" or chanfroY == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            elif chanfroX != "" or chanfroY != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Chanfro digitado maior que lado
        if float(chanfroX)>float(txd)*0.93:
            dlg = wx.MessageDialog(parent=None, message="O chanfro grande demais para a medida do lado!", caption="Verifique as medidas", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        if float(chanfroY)>float(tyd)*0.93:
            dlg = wx.MessageDialog(parent=None, message="O chanfro grande demais para a medida do lado!", caption="Verifique as medidas", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.TrianguloPontasCortadas(txd, tyd, chanfroX, chanfroY, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.TrianguloPontasCortadas(txd, tyd, chanfroX, chanfroY, entrada, chapaX, chapaY, pecas, Kerf)
            #pass

        pecasFaltantes=int(float(pecas))-int(pecasGeradas)

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoTrianguloPontasCortadas(espessura, txd, tyd, chanfroX, chanfroY, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(chanfroX)+'","'+str(chanfroY)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","triangulo com pontas cortadas","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,chfX,chfY,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        chanfroX=self.campo_de_texto_ChanfroX.GetValue()
        chanfroY=self.campo_de_texto_ChanfroY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Criando variavel "salvar" vazia para poder fazer comparações
        salvar=""

        #Trocar pontos por vírgula
        txd=txd.replace(',', '.')
        tyd=tyd.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')
        entrada=entrada.replace(',', '.')
        chapaX=chapaX.replace(',', '.')
        chapaY=chapaY.replace(',', '.')
        chanfroX=chanfroX.replace(',', '.')
        chanfroY=chanfroY.replace(',', '.')

        #Se o tamanho da chapa for deixado em branco definir como ZERO
        if chapaX == "":
            chapaX=0
        if chapaY == "":
            chapaY=0

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            elif txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        if chanfroX.replace('.', '').isdigit() == False or chanfroY.replace('.', '').isdigit() == False:
            if chanfroX == "" or chanfroY == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            elif chanfroX != "" or chanfroY != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Chanfro digitado maior que lado
        if float(chanfroX)>float(txd)*0.93:
            dlg = wx.MessageDialog(parent=None, message="O chanfro grande demais para a medida do lado!", caption="Verifique as medidas", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        if float(chanfroY)>float(tyd)*0.93:
            dlg = wx.MessageDialog(parent=None, message="O chanfro grande demais para a medida do lado!", caption="Verifique as medidas", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.TrianguloPontasCortadas(txd, tyd, chanfroX, chanfroY, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.TrianguloPontasCortadas(txd, tyd, chanfroX, chanfroY, entrada, chapaX, chapaY, pecas, Kerf)
            #pass

        pecasFaltantes=int(float(pecas))-int(pecasGeradas)

        #Calculando o peso das peças em gramas
        pesoUnitario, pesoTotal=Auxiliares.pesoTrianguloPontasCortadas(espessura, txd, tyd, chanfroX, chanfroY, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(chanfroX)+'","'+str(chanfroY)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","triangulo com pontas cortadas","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,chfX,chfY,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)
       

    def FecharTrianguloPontasCortadas(self, event):
        frame_Gisoplox.Show()
        frame_TrianguloPontasCortadas.Hide()

#################################################### F - Triangulo com pontas cortadas #####################################################################
########################################################### I - RetanguloFuro ##############################################################################
class FrameRetanguloFuro(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            TX=600
            TY=480
            X1=160
            X2=18
            X3=310
            X4=380
            X5=430
            X6=480
            X7=310
            X8=390
            X9=445
            X10=425
            X11=460
            X12=435
            X13=497
            X14=508
            XBC=400
            XBA=490
            T1X=50
            T2X=30
            T3X=60
            Y1=20
            Y2=200
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoFuro=155
            YTextoFuro=183
            XFuro=173
            YFuro=178
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358

            

            YCX=30
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"
            
        if sistemaOperacional=="Windows":
            TX=600
            TY=480
            X1=160
            X2=28
            X3=310
            X4=370
            X5=420
            X6=470
            X7=310
            X8=380
            X9=425
            X10=405
            X11=430
            X12=420
            X13=484
            X14=495
            XBC=380
            XBA=470
            T1X=40
            T2X=20
            T3X=60
            Y1=28
            Y2=200
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoFuro=155
            YTextoFuro=183
            XFuro=173
            YFuro=185
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

            YCX=20
            
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Retângulo com furo central"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_CLOSE, self.FecharRetanguloFuro)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        #self.currentDirectory = os.getcwd()
        #Desenho e cotas
        self.campo_de_texto_TamanhoX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X1,Y1), size=(T1X,YCX))
        self.campo_de_texto_TamanhoY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X2,Y2), size=(T1X,YCX))
        self.campo_de_texto_Furo=wx.TextCtrl(self, wx.ID_ANY, "", pos=(XFuro,YFuro), size=(T1X,YCX))
        texto = wx.StaticText(self, wx.ID_ANY, _("Ø"), pos=(XTextoFuro,YTextoFuro))
        fonteDiam = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        texto.SetFont(fonteDiam)

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X3,Y3))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y3), size=(T1X,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X5, Y3))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X6, Y3))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X7,Y4))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X8,Y4), size=(T1X,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X9,Y4))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X3,Y5))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X10,Y5), size=(T2X,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X11,Y5))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X3,Y6))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X12,Y6), size=(T3X,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X13,Y6))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X14,Y6), size=(T3X,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharRetanguloFuro, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        dc.SetPen(pen)

        def desenharCirculo(diam, xc, yc):
            raio=diam/2.0
            x=-raio+0.01
            #print x
            while -raio<x<raio:
                y=math.sqrt(raio*raio-x*x)
                xf=x+1.0
                if xf<raio:
                    yf=math.sqrt(raio*raio-xf*xf)                
                dc.DrawLine(int(round(x+xc)),int(round(y+yc)),int(round(xf+xc)),int(round(yf+yc)))
                dc.DrawLine(int(round(x+xc)),int(round(-y+yc)),int(round(xf+xc)),int(round(-yf+yc)))
                dc.DrawLine(int(round(y+xc)),int(round(x+yc)),int(round(yf+xc)),int(round(xf+yc)))
                dc.DrawLine(int(round(y-xc)),int(round(x+yc)),int(round(yf-xc)),int(round(xf+yc)))
                x+=1.0
        
        #Desenhando o retângulo
        xi=85
        yi=65
        drx=200
        dry=300

        xc=187
        yc=210
        tam=130
        drx=drx+xi
        dry=dry+yi
        dc.DrawLine(xi,yi,drx,yi)
        dc.DrawLine(drx,yi,drx,dry)
        dc.DrawLine(drx,dry,xi,dry)
        dc.DrawLine(xi,dry,xi,yi)
        desenharCirculo(tam, xc, yc)

        #Desenhando as cotas do retangulo
        dc.SetPen(cota)
        tamLinha=20
        dist=4
        flechaX=12
        flechaY=4
        mLinha=int(tamLinha/2)

        #Cota diam interno
        XiCotaInterna=125
        XfCotaInterna=250
        XvCotaInterna=13
        YCotaInterna=yc
        YvCotaInterna=5
        dc.DrawLine(XiCotaInterna,YCotaInterna,XfCotaInterna,YCotaInterna)
        dc.DrawLine(XfCotaInterna-XvCotaInterna,YCotaInterna-YvCotaInterna,XfCotaInterna,YCotaInterna) #Cota esq superior
        dc.DrawLine(XfCotaInterna-XvCotaInterna,YCotaInterna+YvCotaInterna-1,XfCotaInterna,YCotaInterna) #Cota esq inferior
        dc.DrawLine(XiCotaInterna,YCotaInterna,XiCotaInterna+XvCotaInterna,YCotaInterna-YvCotaInterna) #Cota dir superior
        dc.DrawLine(XiCotaInterna,YCotaInterna,XiCotaInterna+XvCotaInterna,YCotaInterna+YvCotaInterna-1) #Cota dir inferior
        
        #Cota superior
        dc.DrawLine(xi,yi-dist,xi,yi-dist-tamLinha)
        dc.DrawLine(drx,yi-dist,drx,yi-dist-tamLinha)
        dc.DrawLine(xi,yi-dist-mLinha,drx,yi-dist-mLinha)

        #Flecha superior esquerda
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha+flechaY)

        #Flecha superior direita
        dc.DrawLine(drx,yi-dist-mLinha,drx-flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(drx,yi-dist-mLinha,drx-flechaX,yi-dist-mLinha+flechaY)

        #Cota lateral
        dc.DrawLine(xi-dist,yi,xi-dist-tamLinha,yi)
        dc.DrawLine(xi-dist,dry,xi-dist-tamLinha,dry)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha,dry)

        #Flecha lateral superior
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha-flechaY,yi+flechaX)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha+flechaY,yi+flechaX)

        #Flecha lateral inferior
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha-flechaY,dry-flechaX)
        dc.DrawLine(xi-dist-mLinha,dry,xi-dist-mLinha+flechaY,dry-flechaX)

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        furo=self.campo_de_texto_Furo.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Criando variavel "salvar" vazia para poder fazer comparações
        salvar=""

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False or furo.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "" or furo== "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "" or furo != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: O diametro do furo é muito grande para esta peça
        if (((float(furo)+4.0)<float(txd))==False) or (((float(furo)+4.0)<float(txd))==False):
            dlg = wx.MessageDialog(parent=None, message="O diâmetro do furo é muito grande para as medidas externas!", caption="Verifique as cotas", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetanguloFuro(espessura, txd, tyd, furo, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        intfuro=int(round(float(furo), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "XD" + str(intfuro) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(furo)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo com furo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,DiamFuro,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)

        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        furo=self.campo_de_texto_Furo.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False or furo.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "" or furo== "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "" or furo != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: O diametro do furo é muito grande para esta peça
        if (((float(furo)+4.0)<float(txd))==False) or (((float(furo)+4.0)<float(txd))==False):
            dlg = wx.MessageDialog(parent=None, message="O diâmetro do furo é muito grande para as medidas externas!", caption="Verifique as cotas", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.RetanguloFuro(txd, tyd, furo, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetanguloFuro(espessura, txd, tyd, furo, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        intfuro=int(round(float(furo), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "XD" + str(intfuro) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        #print salvar

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and erros==0:
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(furo)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo com furo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,DiamFuro,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)
        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def FecharRetanguloFuro(self, event):
        frame_Gisoplox.Show()
        #print "Fechando..."
        frame_RetanguloFuro.Hide()
########################################################### F - RetanguloFuro ##############################################################################
########################################################### I - RetanguloChanfrado ##############################################################################
class FrameRetanguloChanfrado(wx.Frame):
    def __init__(self, *args, **kwds):
        #Configurar Frame
        if sistemaOperacional=="Linux":
            TX=600
            TY=480
            X1=160
            X2=18
            X3=310
            X4=380
            X5=430
            X6=480
            X7=310
            X8=390
            X9=445
            X10=425
            X11=460
            X12=435
            X13=497
            X14=508
            XBC=400
            XBA=490
            T1X=50
            T2X=30
            T3X=60
            Y1=20
            Y2=200
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=380
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=298
            YCancelar=358

            

            YCX=30
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                self.currentDirectory = Auxiliares.Parametros()[10]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"
            
        if sistemaOperacional=="Windows":
            TX=600
            TY=480
            X1=160
            X2=28
            X3=310
            X4=370
            X5=420
            X6=470
            X7=310
            X8=380
            X9=425
            X10=405
            X11=430
            X12=420
            X13=484
            X14=495
            XBC=380
            XBA=470
            T1X=40
            T2X=20
            T3X=60
            Y1=28
            Y2=200
            Y3=70
            Y4=107
            Y5=144
            Y6=181
            XTextoProcesso=X7
            XRadioOxicorte=370
            YRadioOxicorte=220
            XSalvarPad=400
            YSalvarPad=288
            YCancelar=348
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                self.currentDirectory = Auxiliares.Parametros()[9]
            else:
                self.currentDirectory = os.getcwd() + "/CNC"

            YCX=20
            
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("GISOPLOX - Retângulo chanfrado"))
        self.SetIcon(wx.Icon('Gisoplox.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        if sistemaOperacional=="Windows":
            self.SetBackgroundColour(wx.WHITE)
        self.SetSize((TX, TY))
        self.Bind(wx.EVT_CLOSE, self.FecharRetanguloChanfrado)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        #self.currentDirectory = os.getcwd()
        #Desenho e cotas
        xi=85
        yi=65
        drx=200
        dry=300
        chanfroS=25
        chanfroI=43
        meioXS=drx-chanfroS-chanfroS
        meioXI=drx-chanfroI-chanfroI
        meioY=dry-chanfroS-chanfroI
        corretorX=0
        corretorY=10
        XchanfroXI=140
        YchanfroXI=385

        #Campos de texto
        self.campo_de_texto_TamanhoX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X1,Y1), size=(T1X,YCX))
        self.campo_de_texto_TamanhoY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X2,Y2), size=(T1X,YCX))
        self.campo_de_texto_ChanfroXS=wx.TextCtrl(self, wx.ID_ANY, "", pos=(xi+chanfroS+meioXS-corretorX,yi+chanfroS+corretorY), size=(T1X,YCX))
        self.campo_de_texto_ChanfroYS=wx.TextCtrl(self, wx.ID_ANY, "", pos=(xi+chanfroS+corretorX+corretorX,yi+2), size=(T1X,YCX))
        self.campo_de_texto_ChanfroYI=wx.TextCtrl(self, wx.ID_ANY, "", pos=(xi+drx+15,yi+dry-chanfroI+corretorY), size=(T1X,YCX))
        self.campo_de_texto_ChanfroXI=wx.TextCtrl(self, wx.ID_ANY, "", pos=(XchanfroXI,YchanfroXI), size=(T1X,YCX))

        #Restante da interface     
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Espessura:"), pos=(X3,Y3))
        self.campo_de_texto_Espessura=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X4,Y3), size=(T1X,YCX))
        self.radio_esp_mm = wx.RadioButton(self, label='mm', pos=(X5, Y3))
        self.radio_esp_pol = wx.RadioButton(self, label='polegada', pos=(X6, Y3))
        self.radio_esp_pol.SetValue(True)
        
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Quantidade:"), pos=(X7,Y4))
        self.campo_de_texto_Quantidade=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X8,Y4), size=(T1X,YCX))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("peças"), pos=(X9,Y4))

        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Entrada de corte:"), pos=(X3,Y5))
        self.campo_de_texto_Entrada=wx.TextCtrl(self, wx.ID_ANY, "5", pos=(X10,Y5), size=(T2X,YCX))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("mm"), pos=(X11,Y5))
        
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Tamanho da chapa:"), pos=(X3,Y6))
        self.campo_de_texto_ChapaX=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X12,Y6), size=(T3X,YCX))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("X"), pos=(X13,Y6))
        self.campo_de_texto_ChapaY=wx.TextCtrl(self, wx.ID_ANY, "", pos=(X14,Y6), size=(T3X,YCX))

        #Escolher entre oxicorte e plasma
        wx.StaticText(self, wx.ID_ANY, _("Processo:"), pos=(XTextoProcesso,YRadioOxicorte))
        processo = ['Oxicorte', 'Plasma']
        #processo = ['Oxicorte']
        self.lista_Processo=wx.ComboBox(self, -1, pos=(XRadioOxicorte, YRadioOxicorte), size=(150, -1), choices=processo, style=wx.CB_READONLY)

        #Botão salvar padrão
        self.botao_SalvarPad = wx.Button(self, id=-1, label='         Salvar Padrão         ', pos=(XSalvarPad, YSalvarPad))
        self.Bind(wx.EVT_BUTTON, self.SalvarPad, self.botao_SalvarPad)
        #Botão cancelar
        self.botao_Cancelar = wx.Button(self, id=-1, label='Cancelar', pos=(XBC, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.FecharRetanguloChanfrado, self.botao_Cancelar)
        #Botão salvar
        self.botao_Gerar = wx.Button(self, id=-1, label='Salvar', pos=(XBA, YCancelar))
        self.Bind(wx.EVT_BUTTON, self.GerarCodigo, self.botao_Gerar)

        #achar coordenada
        self.Bind(wx.EVT_MOTION,  self.OnMove)        
        self.posCtrl = wx.TextCtrl(self, -1, "", pos=(406, 322))

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen=wx.Pen('black',2)
        cota=wx.Pen('red',2)
        cotaAzul=wx.Pen('blue',2)
        cotaVerde=wx.Pen('green',2)
        dc.SetPen(pen)

        #Desenhando o retângulo
        xi=85
        yi=65
        drx=200
        dry=300
        chanfroS=25
        chanfroI=43
        meioXS=drx-chanfroS-chanfroS
        meioXI=drx-chanfroI-chanfroI
        meioY=dry-chanfroS-chanfroI
        dc.DrawLine(xi,yi+chanfroS,xi+chanfroS,yi)
        dc.DrawLine(xi+chanfroS,yi,xi+chanfroS+meioXS,yi)
        dc.DrawLine(xi+chanfroS+meioXS,yi,xi+chanfroS+meioXS+chanfroS,yi+chanfroS)
        dc.DrawLine(xi+chanfroS+meioXS+chanfroS,yi+chanfroS,xi+chanfroS+meioXS+chanfroS,yi+chanfroS+meioY)
        dc.DrawLine(xi+chanfroS+meioXS+chanfroS,yi+chanfroS+meioY,xi+chanfroS+meioXS+chanfroS-chanfroI,yi+chanfroS+meioY+chanfroI)
        dc.DrawLine(xi+chanfroS+meioXS+chanfroS-chanfroI,yi+chanfroS+meioY+chanfroI,xi+chanfroS+meioXS+chanfroS-chanfroI-meioXI,yi+chanfroS+meioY+chanfroI)
        dc.DrawLine(xi+chanfroI,yi+chanfroS+meioY+chanfroI,xi,yi+chanfroS+meioY)
        dc.DrawLine(xi,yi+chanfroS+meioY,xi,yi+chanfroS)

        #Desenhando as cotas
        dc.SetPen(cota)
        tamLinha=20
        dist=4
        flechaX=12
        flechaY=4
        mLinha=int(tamLinha/2)
        
        #Cota superior
        dc.DrawLine(xi,yi-dist,xi,yi-dist-tamLinha)
        dc.DrawLine(drx+xi,yi-dist,drx+xi,yi-dist-tamLinha)
        dc.DrawLine(xi,yi-dist-mLinha,drx+xi,yi-dist-mLinha)

        #Flecha superior esquerda
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha-flechaY)
        dc.DrawLine(xi,yi-dist-mLinha,xi+flechaX,yi-dist-mLinha+flechaY)

        #Flecha superior direita
        dc.DrawLine(drx+xi,yi-dist-mLinha,drx-flechaX+xi,yi-dist-mLinha-flechaY)
        dc.DrawLine(drx+xi,yi-dist-mLinha,drx-flechaX+xi,yi-dist-mLinha+flechaY)

        #Cota lateral
        dc.DrawLine(xi-dist,yi,xi-dist-tamLinha,yi)
        dc.DrawLine(xi-dist,dry+yi,xi-dist-tamLinha,dry+yi)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha,dry+yi)

        #Flecha lateral superior
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha-flechaY,yi+flechaX)
        dc.DrawLine(xi-dist-mLinha,yi,xi-dist-mLinha+flechaY,yi+flechaX)

        #Flecha lateral inferior
        dc.DrawLine(xi-dist-mLinha,dry+yi,xi-dist-mLinha-flechaY,dry-flechaX+yi)
        dc.DrawLine(xi-dist-mLinha,dry+yi,xi-dist-mLinha+flechaY,dry-flechaX+yi)

        #Cota chanfroX Superior
        dc.SetPen(cotaAzul)
        baixar=30
        dc.DrawLine(xi+chanfroS+meioXS,yi+dist,xi+chanfroS+meioXS,yi+chanfroS+dist+dist+baixar)
        dc.DrawLine(xi+chanfroS+meioXS+chanfroS,yi+dist+chanfroS,xi+chanfroS+meioXS+chanfroS,yi+chanfroS+dist+dist+baixar)
        dc.DrawLine(xi+chanfroS+meioXS-flechaX-dist,yi+chanfroS+dist+baixar,xi+chanfroS+meioXS+chanfroS+flechaX+dist,yi+chanfroS+dist+baixar)

        #Flecha chanfroX direita superior
        dc.DrawLine(xi+chanfroS+meioXS+chanfroS,yi+dist+chanfroS+baixar,xi+chanfroS+meioXS+chanfroS+flechaX,yi+dist+chanfroS-flechaY+baixar)
        dc.DrawLine(xi+chanfroS+meioXS+chanfroS,yi+dist+chanfroS+baixar,xi+chanfroS+meioXS+chanfroS+flechaX,yi+dist+chanfroS+flechaY+baixar)

        #Flecha chanfroX esquerda superior
        dc.DrawLine(xi+chanfroS+meioXS,yi+dist+chanfroS+baixar,xi+chanfroS+meioXS-flechaX,yi+dist+chanfroS-flechaY+baixar)
        dc.DrawLine(xi+chanfroS+meioXS,yi+dist+chanfroS+baixar,xi+chanfroS+meioXS-flechaX,yi+dist+chanfroS+flechaY+baixar)

        #Cota chanfroY Superior
        deslocar=40
        dc.DrawLine(xi+dist,yi+chanfroS,xi+chanfroS+dist+dist+deslocar,yi+chanfroS)
        dc.DrawLine(xi+chanfroS+deslocar,yi,xi+chanfroS+dist+dist+deslocar,yi)
        dc.DrawLine(xi+chanfroS+dist+deslocar,yi-flechaX-dist,xi+chanfroS+dist+deslocar,yi+chanfroS+flechaX+dist)

        #Flecha chanfro Y superior inferior
        dc.DrawLine(xi+chanfroS+dist+deslocar+flechaY,yi+chanfroS+flechaX,xi+chanfroS+dist+deslocar,yi+chanfroS)
        dc.DrawLine(xi+chanfroS+dist+deslocar-flechaY,yi+chanfroS+flechaX,xi+chanfroS+dist+deslocar,yi+chanfroS)

        #Flecha chanfro Y superior superior
        dc.DrawLine(xi+chanfroS+dist+deslocar,yi,xi+chanfroS+dist+deslocar-flechaY,yi-flechaX)
        dc.DrawLine(xi+chanfroS+dist+deslocar,yi,xi+chanfroS+dist+deslocar+flechaY,yi-flechaX)

        #Cotas chanfro Inferior
        dc.SetPen(cotaVerde)
        deslocar=60
        dc.DrawLine(xi+meioXI+chanfroI+dist, yi+dry, xi+meioXI+chanfroI+dist+chanfroI+deslocar, yi+dry)
        dc.DrawLine(xi+drx+dist, yi+dry-chanfroI, xi+drx+dist+deslocar, yi+dry-chanfroI)
        dc.DrawLine(xi+meioXI+chanfroI+dist+chanfroI+deslocar-5,yi+dry-chanfroI-flechaX,xi+meioXI+chanfroI+dist+chanfroI+deslocar-5,yi+dry+flechaX)
        #Flecha chanfro Y inferior inferior
        dc.DrawLine(xi+meioXI+chanfroI+dist+chanfroI+deslocar-5,yi+dry,xi+meioXI+chanfroI+dist+chanfroI+deslocar-5-flechaY,yi+dry+flechaX)
        dc.DrawLine(xi+meioXI+chanfroI+dist+chanfroI+deslocar-5,yi+dry,xi+meioXI+chanfroI+dist+chanfroI+deslocar-5+flechaY,yi+dry+flechaX)
        #Flecha chanfro Y inferior superior
        X1=343
        Y1=320
        dc.DrawLine(X1,Y1,X1+4,Y1-11)
        dc.DrawLine(X1,Y1,X1-4,Y1-11)

        #Conta chanfro X inferior
        X1 = 85
        X2 = 127
        X3 = 180
        Y1 = 327
        Y2 = 415
        Y3 = 367
        Y4 = 410
        dc.DrawLine(X1,Y1,X1,Y2)
        dc.DrawLine(X2,Y3,X2,Y2)
        dc.DrawLine(X1-13,Y4,X3,Y4)
        #Cota esquerda
        dc.DrawLine(X1,Y4,X1-12,Y4-5)
        dc.DrawLine(X1,Y4,X1-12,Y4+4)
        #Cota direita
        dc.DrawLine(X2,Y4,X2+12,Y4-5)
        dc.DrawLine(X2,Y4,X2+12,Y4+4)

    def GerarCodigo(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Criando variavel "salvar" vazia para poder fazer comparações
        salvar=""

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            pecasGeradas, programa, distCorte=Plasma.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Mostrar diálogo salvar como... se não for encontrado nenhum erro
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if erros == 0:
            dlg = wx.FileDialog( self, message="Salvar o código em ...", defaultDir=self.currentDirectory, defaultFile=nomePadrao, wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                salvar = dlg.GetPath()
            dlg.Destroy()

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and salvar!="":
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Mostrar aviso quando o usuário presiona "cancelar"
        if salvar=="":
            dlg = wx.MessageDialog(parent=None, message="GERAÇÃO DE PROGRAMA CANCELADO!\n\nO procedimento de geração do programa foi cancelado por ação do usuário!", caption='Procedimento cancelado!', style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def SalvarPad(self, event):
        #Pegando o valor dos campos de texto
        txd=self.campo_de_texto_TamanhoX.GetValue()
        tyd=self.campo_de_texto_TamanhoY.GetValue()
        entrada=self.campo_de_texto_Entrada.GetValue()
        chapaX=self.campo_de_texto_ChapaX.GetValue()
        chapaY=self.campo_de_texto_ChapaY.GetValue()
        pecas=self.campo_de_texto_Quantidade.GetValue()
        espessura=self.campo_de_texto_Espessura.GetValue()
        processo=self.lista_Processo.GetValue()
        espi=espessura.replace('.', ',')
        espi=espi.replace('/', '-')
        espi=espi.replace('\\', '-')
        espi=espi.replace('\'', '')
        espi=espi.replace('"', '')

        #Trocar pontos por vírgula
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

        #Transformando a espessura em mm
        if self.radio_esp_pol.GetValue() == True:
            espessura=Auxiliares.PassarMilimetro(espessura)
            espi=espi + " POL "

        '''#Informando o usuário sobre erros de preenchimento'''
        erros=0

        #Erro: Nenhuma unidade para a espessura
        if self.radio_esp_pol.GetValue() == False and self.radio_esp_mm.GetValue() == False:
            dlg = wx.MessageDialog(parent=None, message="Você deve selecionar uma unidade para a espessura (mm ou polegada)!", caption="Escolha uma unidade", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1

        #Erro: O número de peças não foi informado
        if pecas.isdigit() == False or pecas == "":
            if pecas == "":
                dlg = wx.MessageDialog(parent=None, message="O número de peças não foi informado!", caption="Digite o número de peças", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if pecas != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação no número de peças informado!", caption="Digite o número de peças novamente", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: A espessura das peças não foi informada
        if espi == "" or espi == " POL ":
            dlg = wx.MessageDialog(parent=None, message="A espessura não foi informada!", caption="Digite a espessura", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros=erros + 1
            
        #Erro: Encontrar erros de preenchimento nas cotas
        if txd.replace('.', '').isdigit() == False or tyd.replace('.', '').isdigit() == False:
            if txd == "" or tyd == "":
                dlg = wx.MessageDialog(parent=None, message="Há cotas sem nenhuma medida informada!", caption="Digite a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if txd != "" or tyd != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação nas cotas!", caption="Digite novamente a medida das cotas", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Encontrar erros de preenchimento na entrada de corte
        if entrada.isdigit() == False:
            if entrada == "":
                dlg = wx.MessageDialog(parent=None, message="A medida de entrada de corte não foi informada!", caption="Digite uma medida de entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if entrada != "":
                dlg = wx.MessageDialog(parent=None, message="Há erros de digitação na entrada de corte!", caption="Digite novamente a entrada de corte", style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            erros=erros + 1

        #Erro: Nenhum processo de corte foi selecionado
        if processo=="":
            dlg = wx.MessageDialog(parent=None, message="Processo de corte não selecionado!\n\nSelecione um processo disponível na lista!", caption="Processo não selecionado", style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
            erros+=1

        #Pegar os parâmetros
        icorte, fcorte, extencao, mesaX, mesaY, numerar, colocarVelocidadeAvanco, colocarVelocidadeAvancoRapido, velocidadeAvancoRapido, pastaPadWin, pastaPadLinux = Auxiliares.Parametros()
        if processo=="Oxicorte":
            Kerf, avanco = Auxiliares.Kerf(espessura)
        if processo=="Plasma":
            Kerf, avanco = Auxiliares.KerfPlasma(espessura)

        #Para não colocar a os avanços definir velocidades como ZERO
        if colocarVelocidadeAvanco == 0:
            avanco=0
        if colocarVelocidadeAvancoRapido == 0:
            velocidadeAvancoRapido=0

        #Chamando a funcao que gera o codigo
        if processo=="Oxicorte":
            pecasGeradas, programa, distCorte=Oxicorte.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
        if processo=="Plasma":
            print(Kerf)
            pecasGeradas, programa, distCorte=Plasma.Retangulo(txd, tyd, entrada, chapaX, chapaY, pecas, Kerf)
            #pass
        pecasFaltantes=int(pecas)-int(pecasGeradas)

        #Calcular o peso em gramas
        pesoUnitario, pesoTotal = Auxiliares.pesoRetangulo(espessura, txd, tyd, pecasGeradas)

        #Adicionar os dados ao arquivo estat
        Auxiliares.adicionarEstat(distCorte, pesoTotal)

        #Se pasta padrão for encontrada salvar programa
        inttxd=int(round(float(txd), 0))
        inttyd=int(round(float(tyd), 0))
        nomePadrao=espi + "X" + str(inttxd) + "X" + str(inttyd) + "-" + str(int(pecasGeradas)) + "P"
        wildcard=Auxiliares.Wildcard()
        if sistemaOperacional=="Linux":
            if os.path.isdir(Auxiliares.Parametros()[10])==True:
                salvar=Auxiliares.Parametros()[10]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        if sistemaOperacional=="Windows":
            if os.path.isdir(Auxiliares.Parametros()[9])==True:
                salvar=Auxiliares.Parametros()[9]
            else:
                erros+=1
                mensagem='A Pasta "Salvar padrão" não foi encontrada!\n\n'
                mensagem+='Possíveis soluções:\n'
                mensagem+='1) Se essa pasta estiver em um pen-drive verifique se:\nO PEN-DRIVE ESTÁ CONECTADO AO COMPUTADOR!'
                mensagem+='\n2) Tente reconfigurar a pasta "Salvar padrão" nas configurações'
                dlg = wx.MessageDialog(parent=None, message=mensagem, caption='Pasta "Salvar padrão" não encontrada!', style=wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
        salvar+="/" + nomePadrao
        #print salvar

        #Se não houve espaço para colocar todas as peças na chapa, mostrar aviso
        if pecasFaltantes!=0:
            mensagem="Não há espaço suficiente na chapa para\ncortar a quantidade de peças informadas!\n"
            mensagem+="A quantidade máxima suportada de peças\npara este tamanho de chapa foi gerada!\n\n"
            mensagem+="Informações sobre o programa gerado:\n"
            mensagem+="\nQuantidade pretendida de peças: " + str(pecas) + " pçs"
            mensagem+="\nQuantidade de peças que faltaram:" + str(pecasFaltantes) + " pçs"
            mensagem+="\nQuantidade de peças geradas: " + str(pecasGeradas) + " pçs"
            mensagem+="\nTamanho da chapa: " + str(chapaX) + " X " + str(chapaY) + " mm"
            titulo="Espaço insuficiente | Faltaram: " + str(pecasFaltantes) + " peças"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption=titulo, style=wx.OK|wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            dlg.Destroy()
        

        #Mostrar aviso de sucesso
        if pecasFaltantes==0 and erros==0:
            mensagem="O seu código foi gerado com sucesso!\n\n"
            mensagem+="Peso unitário: "+Auxiliares.pesoString(pesoUnitario)
            mensagem+="\nPeso total: "+Auxiliares.pesoString(pesoTotal)
            mensagem+="\nDistância de corte: "+Auxiliares.converterDist(distCorte)
            mensagem+="\nObs: Peso para peças de aço"
            dlg = wx.MessageDialog(parent=None, message=mensagem, caption="Gódigo salvo", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        #Adicionar dados ao historico
        if erros==0:
            SpesoUnitario=Auxiliares.pesoString(pesoUnitario)
            SpesoTotal=Auxiliares.pesoString(pesoTotal)
            SdistCorte=Auxiliares.converterDist(distCorte)
            Auxiliares.escreverHist(nomePadrao, SpesoUnitario, SpesoTotal, SdistCorte, Auxiliares.versao())

        ferramenta=str(txd)+'","'+str(tyd)+'","'+str(entrada)+'","'+str(chapaX)+'","'+str(chapaY)+'","'+str(pecas)+'","'+str(Kerf)
        linha='"'+str(nomePadrao)+'","'+str(ferramenta)+'","'+str(pecasFaltantes)+'","'+str(pecasGeradas)+'","'+str(SpesoUnitario)+'","'+str(SpesoTotal)+'","'+str(SdistCorte)+'","'+Auxiliares.versao()+'","'+str(erros)+'","retangulo","'+str(processo)+'"\n'
        Auxiliares.escreverCSV(linha)

        LegFerramenta='txd,tyd,entrada,chapaX,chapaY,pecas,Kerf'
        Leglinha='nomePadrao,'+LegFerramenta+',pecasFaltantes,pecasGeradas,SpesoUnitario,SpesoTotal,SdistCorte,versao,erros,formato,processo\n'
        Auxiliares.escreverCSV(Leglinha)
        

        #Chamando a função que cria o arquivo
        if erros==0:
            Auxiliares.escreverPrograma(programa, salvar)
        if (avanco>0):
            Auxiliares.ColocarVelocidadeAvanco(salvar, avanco)
        if(velocidadeAvancoRapido>0):
            Auxiliares.ColocarVelocidadeAvancoRapido(salvar, velocidadeAvancoRapido)
        if(numerar==1):
            Auxiliares.NumerarLinhas(salvar)

    def FecharRetanguloChanfrado(self, event):
        frame_Gisoplox.Show()
        #print "Fechando..."
        frame_RetanguloChanfrado.Hide()
########################################################### F - RetanguloChanfrado ##############################################################################

if __name__ == "__main__":
    gettext.install("GisoploxApp")

    GisoploxApp = wx.App(0)
    #Frame Gisoplox Home
    frame_Gisoplox = Gisoplox(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Gisoplox)
    #Frame Gisoplox About
    frame_About = About(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_About)
    #Frame Formatos Retangulares
    frame_FormatosRetangulares = FormatosRetangulares(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_FormatosRetangulares)
    #Frame Formatos Circulares
    frame_FormatosCirculares = FormatosCirculares(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_FormatosCirculares)    
    #Frame Formatos Triangulares
    frame_FormatosTriangulares = FormatosTriangulares(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_FormatosTriangulares)
    #Frame Estat
    frame_Estat = Estat(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Estat)
    #Frame Hist
    frame_Hist = Hist(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Hist)
    #Frame configurar
    frame_Configurar = Configurar(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Configurar)
    #Frame Retângulo
    frame_Rectange = OrectangeFrame(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Rectange)
    #Frame Círculo
    frame_Circle = OcircleFrame(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Circle)
    #Frame círculo simples
    frame_CircleSimple = CircleSimple(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_CircleSimple)
    #Frame Triângulo retângulo
    frame_TrianguloPontasCortadas = FrameTrianguloPontasCortadas(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_TrianguloPontasCortadas)
    #Frame Retângulo com furo
    frame_RetanguloFuro = FrameRetanguloFuro(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_RetanguloFuro)
    #Frame Retângulo com chanfros
    frame_RetanguloChanfrado = FrameRetanguloChanfrado(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_RetanguloChanfrado)
    #Frame Triângulo com pontas cortadas
    frame_Triangulo = FrameTriangulo(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Triangulo)
    #Frame Kerf
    frame_Kerf = Kerf(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_Kerf)
    #Frame Kerf Plasma
    frame_KerfPlasma = KerfPlasma(None, wx.ID_ANY, "")
    GisoploxApp.SetTopWindow(frame_KerfPlasma)
    if AbrirIntro == "Sim":
        #Frame Intro
        frame_Intro = Intro(None, wx.ID_ANY, "")
        GisoploxApp.SetTopWindow(frame_Intro)
        frame_Intro.Show()
    if AbrirIntro != "Sim":
        frame_Gisoplox.Show()
    #Colocar em loop
    GisoploxApp.MainLoop()
