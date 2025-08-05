import os

exp_dir = os.path.dirname(os.path.abspath(__file__))

with open(f'{exp_dir}/example_workspace/scan_54/conf/config', 'r') as file:
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/scan_54/conf/config', 'w') as file:
    file.write(filedata)

with open(f'{exp_dir}/example_workspace/scan_54/conf/config_prep', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/scan_54/conf/config_prep', 'w') as file:
    file.write(filedata)

with open(f'{exp_dir}/example_workspace/scan_54/conf/config_disp', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/scan_54/conf/config_disp', 'w') as file:
    file.write(filedata)

with open(f'{exp_dir}/example_workspace/scan_54/conf/config_instr', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/scan_54/conf/config_instr', 'w') as file:
    file.write(filedata)

with open(f'{exp_dir}/example_workspace/esrf_exp_4/conf/config', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/esrf_exp_4/conf/config', 'w') as file:
    file.write(filedata)

with open(f'{exp_dir}/example_workspace/aps1ide_2075-2108/conf/config', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/aps1ide_2075-2108/conf/config', 'w') as file:
    file.write(filedata)

with open(f'{exp_dir}/example_workspace/P_63/conf/config', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('EXP_DIR', exp_dir)
with open(f'{exp_dir}/example_workspace/P_63/conf/config', 'w') as file:
    file.write(filedata)

