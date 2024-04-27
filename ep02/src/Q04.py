from automata.tm.mntm import MNTM

mntm4 = MNTM(
    states={'start', 'done'},
    input_symbols={'a', 'b', '#'},
    tape_symbols={'a', 'b', '#', '.'},
    n_tapes=2,
    transitions={
      'start': {
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'},
)
