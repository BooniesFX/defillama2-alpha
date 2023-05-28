from defillama2alpha import DefiLlama
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.4f}'.format
obj = DefiLlama()
gmx_arbitrum_tvl = obj.get_protocol_curr_tvl_by_chain("gmx")['arbitrum']

print(gmx_arbitrum_tvl)