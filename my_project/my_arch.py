import sys
sys.path.append('../')
from pycore.tikzeng import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    # Detail branch
    to_Conv_color('detail1_attn', s_filer="CBAM", n_filer='', height=32, depth=32, width=1, color=5),
    to_Conv_color('detail1', s_filer="I/2", n_filer='', offset='(1,0,0)',to='(detail1_attn-east)', height=32, depth=32, width=2),
    to_Conv_color('detail2', s_filer="I/4", n_filer='', offset='(2.5,0,0)' , to='(detail1-east)', height=20, depth=20, width=4),
    to_connection('detail1', 'detail2'),
    to_Conv_color('detail3', s_filer="I/8", n_filer='', offset='(2,0,0)', to='(detail2-east)', height=12, depth=12, width=6),
    to_connection('detail2', 'detail3'),
    # semantic branch
    to_Conv_color('semantic1', s_filer='I/2', n_filer='', offset='(0,-8,0)', to='(detail1_attn-south)', height=32, depth=32, width=2, color=1),
    to_Conv_color('semantic2', s_filer='I/4', n_filer='', offset='(2.5,0,0)', to='(semantic1-east)', height=20, depth=20, width=4, color=1),
    to_connection('semantic1', 'semantic2'),
    to_Conv_color('semantic3', s_filer='I/8', n_filer='', offset='(2,0,0)', to='(semantic2-east)', height=12, depth=12, width=6, color=1),
    to_connection('semantic2', 'semantic3'),
    to_Conv_color('semantic4', s_filer='I/16', n_filer='', offset='(2,0,0)', to='(semantic3-east)', height=8, depth=8, width=10, color=1),
    to_connection('semantic3', 'semantic4'),
    to_Conv_color('semantic5', s_filer='I/32', n_filer='', offset='(2,0,0)', to='(semantic4-east)', height=4, depth=4, width=16, color=1),
    to_connection('semantic4', 'semantic5'),
    # aggregation layer
    to_Conv_color('aggregation', s_filer="Aggregation", n_filer='', offset='(4,6,0)', to='(semantic5-east)', height=12, depth=12, width=6, color=2),
    to_connection2('detail3', 'aggregation', 2.75, 'up'),
    to_connection2('semantic5', 'aggregation', 3, 'down'),
    # input
    to_Conv_color('input', s_filer='projected view', n_filer='', offset='(-30,0,0)', to='(aggregation-west)', height=32, depth=100, width=1, color=3),
    # CAM
    to_Conv_color('CAM', s_filer='CAM', n_filer='', offset='(2.5,0,0)', to='(input-east)', height=32, depth=100, width=4, color=4),
    to_connection('input', 'CAM'),
    to_connection3('CAM', 'detail1_attn', 6),
    to_connection3('CAM', 'semantic1', 6),
    # output
    to_Conv_color('output', s_filer='result', n_filer='', offset='(5,0,0)', to='(aggregation-east)', height=32, depth=100, width=1, color=3),
    to_connection('aggregation', 'output'),
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__=='__main__':
    main()
