import cx_Freeze

executables = [cx_Freeze.Executable('Menu.py')]

cx_Freeze.setup(
    name="CaipiHead",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['imagens', 'sons', 'Fonte']}},

    executables = executables
)