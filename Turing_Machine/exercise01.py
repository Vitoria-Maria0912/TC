# @title {vertical-output: true }
cadeia1 = "aaabbab" # @param {type:"string"}
from automata.tm.dtm import DTM

# Construa a máquina aqui
dtm1 = DTM(
    states={'start','done'},
    input_symbols={'a', 'b'},
    tape_symbols={'a', 'b', '.','#'},
    transitions={
        'start': {
            '.' : ('done', '.', 'R'),
            'a' : ('start', '#', 'R'),
            'b' : ('start', 'b', 'R')
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)

if (all(n in dtm1.input_symbols for n in cadeia1)):
  gen1 = dtm1.read_input_stepwise(cadeia1)
  _,output1, configurations1 = dtm_configurations(gen1)
  print(f"Saída: {output1}")
  print("Configurações: ")
  for c in configurations1:
    print(f" {c}")
else:
  print("Cadeia inválida")

# Possíveis testes
#
#['00','ab','#b',True],
#['01','abaaa','#b###',True],
#['02','','',True],
#['03','bbbbb','bbbbb',True],
#['04','baabbabb','b##bb#bb',True],
#['05','b','b',True],
#['06','a','#',True],
#['06','aaaaa','#####',True],
#['07','baaaaa','b#####',True]
