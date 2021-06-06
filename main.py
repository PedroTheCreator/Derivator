import PySimpleGUI as sg
sg.theme('lightblue')   
layout = [  
    
  [sg.Text('')],  
  [sg.Image('./images/Custo_fixo.png',size=(150,80))],
  [sg.Text('')],  

  [sg.Text('Aluguel mensal', size=(25, 1)), sg.InputText()],
  [sg.Text('Folha de pagamento mensal', size=(25, 1)), sg.InputText()],
  [sg.Text('Energia mensal', size=(25, 1)), sg.InputText()],
  [sg.Text('Água mensal',size=(25, 1)), sg.InputText()],
  [sg.Text('Internet mensal',size=(25, 1)), sg.InputText()],
  

  [sg.Text('Teste',justification='c')],  
  [sg.Image('./images/Custo_variavel.png',size=(200  ,80))],
  [sg.Text('')], 

  [sg.Text('Preço unitário',size=(25, 1)), sg.InputText()],
  [sg.Text('Unidades em um lote',size=(25, 1)), sg.InputText()],
  [sg.Text('Lotes produzidos por mês',size=(25, 2)), sg.InputText()],
  [sg.Text('Custo de embalagem por unidade',size=(25, 1)), sg.InputText()],
  [sg.Text('Custo de embalagem por lote',size=(25, 1)), sg.InputText()],
  [sg.OK(button_text="Calcular")],
  [sg.Output(size=(80,3))],
]

window = sg.Window('Derivator',layout, icon="./images/icon.ico")
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Fechar'):
      break
    valores = []
    for i in values:
      valores.append(values[i])
    for i in range(0,len(valores)):
      valores[i] = str(valores[i].replace(",","."))
    try:
      custo_fixo = (float(valores[0])+float(valores[1])+float(valores[2])+float(valores[3])+float(valores[4]))
      p = float(valores[5])
      g = float(valores[6])
      x = float(valores[7])
      Eu = float(valores[8])
      Eg = float(valores[9])
      Custo_variavel = p*g*x**2 + Eu*g*x + Eg*g + custo_fixo
      Custo_marginal = 2*(p*g*x) + Eu*g 
      print("Custo total: R${}\nCusto Marginal: R${}".format(Custo_variavel, Custo_marginal))
      #print("Custo fixo = {}".format(custo_fixo))
    except ValueError:
      sg.popup("Ops, você precisa inserir valores númericos em todos os campos.",title="Erro!")
      print("Ops, insira os dados corretamente.")
    
window.close()