# import libraries
import matplotlib.pyplot as plt
import pandas as pd
from cadCAD import configs
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

plt.show()

exec_mode = ExecutionMode()
# Run Cad^2

first_config = configs  # only contains config1
single_proc_ctx = ExecutionContext(context=exec_mode.single_proc)
run = Executor(exec_context=single_proc_ctx, configs=first_config)


raw_result = run.execute()
df = pd.DataFrame(raw_result)
df.set_index(['run', 'timestep', 'substep'])

df.plot('timestep', ['box_A', 'box_B'], grid=True,
        colormap='RdYlGn',
        xticks=list(df['timestep'].drop_duplicates()),
        yticks=list(range(1 + (df['box_A'] + df['box_B']).max())))
