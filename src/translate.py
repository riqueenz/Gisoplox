import locale
language = locale.getlocale()[0]
language = 'pt_BR'

def translate(text):
    #print(language)
    if language == 'pt_BR':
        if text == "Test":
            text = "Teste"
        if text == "Tools":
            text = "Ferramentas"
        if text == "Metrics":
            text = "Estatísticas"
        if text == "Cutting history metrics":
            text = "Métricas históricas"
        if text == "History":
            text = "Histórico"
        if text == "History of generated CNC files":
            text = "Histórico de peças cortadas"
        if text == "History":
            text = "Histórico"
        if text == "History of generated CNC files":
            text = "Histórico de peças cortadas"
        if text == "Version":
            text = "Versão"    
        if text == "Author":
            text = "Autor"    
        if text == "Settings":
            text = "Configurações"
        if text == "Code writing settings":
            text = "Configurações de escrita de programa"
        if text == "Cutting settings":
            text = "Configurações de corte"
        if text == "Oxyfuel":
            text = "Oxicorte"
        if text == "Plasma cutting settings":
            text = "Configurações de corte plasma" 
        if text == "Close":
            text = "Fechar"
        if text == "Close the software":
            text = "Fechar o software"
        if text == "Options":
            text = "Opções"
        if text == 'R&ectangles':
            text = 'R&etângulos'
        if text == "Rectangle":
            text = "Retângulo"    
        if text == "Opens the rectangles generating tool":
            text = "Abre a ferramenta de geração de retângulos"
        if text == "Rectangle with center hole":
            text = "Retângulo com furo no centro"
        if text == "Opens the tool for generating rectangles with a central hole":
            text = "Abre a ferramenta para geração de retângulos com furo no centro"
        if text == "Rectangle with chamfer corners":
            text = "Retângulo com pontas chanfradas"
        if text == 'C&ircles':
            text = 'C&írculos' 
        if text == "Donut":
            text = "Círculo com furo no centro"
        if text == "Circle":
            text = "Círculo"
        if text == 'T&riangles':
            text = 'T&riângulos'
        if text == "Right triangle":
            text = "Triângulo reto"
        if text == "Triangle with ends cut":
            text = "Triângulo com pontas cortadas"
        if text == "Help":
            text = "Ajuda"
        if text == "About":
            text = "Sobre"
        if text == "About this software":
            text = "Sobre este software"
        if text == "Reset":
            text = "Zerar"
        if text == "Update":
            text = "Atualizar"
            
        if text == "CUTTING DATA:":
            text = "DADOS ESTATÍSTICOS DE CORTE:" 
        if text == "SINCE THE INSTALLATION:":
            text = "DESDE A INSTALAÇÃO:"
        if text == "Cutting distance: ":
            text = "Distância de corte: "
        if text == "Total weight of parts: ":
            text = "Peso total das peças: "
        if text == "Generated CNC files: ":
            text = "Programas gerados: "
        if text == "Starting date: ":
            text = "Início da contagem: "
        if text == "SINCE IT WAS RESET:":
            text = "DESDE QUE FOI ZERADO:"
        if text == "Note: To calculate the weight we consider\n that all the pieces were made of steel":
            text = "Obs: Para gerar os dados estatísticos são\nlevados  em  consideração  os  programas\ngerados e não os cortados."
        if text == "Data reset successfully!":
            text = "Dados estatícos zerados com sucesso!"
        if text == "Data reset":
            text = "Dados estatícos zerados"
        if text == "metrics":
            text = "estatícas"
            
        if text == "Thickness:":
            text = "Espessura"
        if text == "inch":
            text = "polegada"
        if text == "Quantity:":
            text = "Quantidade:"
        if text == "parts":
            text = "peças"
        if text == "Cut entry distance:":
            text = "Entrada de corte:"
        if text == "Sheet metal size:":
            text = "Tamanho da chapa:"
        if text == "Process:":
            text = "Processo:"
        if text == "Save":
            text = "Salvar"
        if text == "         Standard Save         ":
            text = "         Salvar Padrão         "
            
        if text == "COMMANDS:":
            text = "COMANDOS:"
        if text == "Cutting start:":
            text = "Início de corte:"
        if text == "End of cut:":
            text = "Fim de corte:"
        if text == "TABLE SIZE / CUT LIMITS:":
            text = "TAMANHO DA MESA / LIMITES DE CORTE:"
        if text == "Limit X:":
            text = "Limite X:"
        if text == "Limit Y:":
            text = "Limite Y:"
        if text == 'CODE SETTINGS:':
            text = 'AJUSTES DO CÓDIGO:'
        if text == 'Number lines':
            text = 'Numerar linhas'
        if text == 'Set feed speed':
            text = 'Colocar velocidade de avanço'
        if text == 'Set positioning speed':
            text = 'Colocar velocidade de avanço rápido'
        if text == "CNC FILE EXTENSION:":
            text = "EXTENÇÃO DO ARQUIVO CNC:"
        if text == "POSITIONING SPEED:":
            text = "VELOCIDADE DO AVANÇO RÁPIDO:"
        if text == "CONFIGURE CUTTING PARAMETERS:":
            text = "CONFIGURAR PARÂMETROS DE CORTE:"
        if text == '"STANDARD SAVE" FOLDER':
            text = 'PASTA "SALVAR PADRÃO:"'
        if text == 'Change':
            text = 'Alterar'
        if text == 'Apply':
            text = 'Aplicar'
        if text == "Choose a folder:":
            text = "Escolha uma pasta:"
        if text == "Settings saved successfully":
            text = "Configurações salvas com sucesso"
        if text == "Settings saved":
            text = "Configurações salvas"
            
        if text == "Thickness (mm)":
            text = "Espessura (mm)"
        if text == "Cutting width (mm)":
            text = "Largura de corte (mm)"
        if text == "Speed (mm/min)":
            text = "Velocidade (mm/min)"

    return text
