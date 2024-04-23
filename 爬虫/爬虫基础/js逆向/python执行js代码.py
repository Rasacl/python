"""
1. 安装pyexecjs库：pip install pyexecjs
"""

import execjs

js_code = '''
function add(a , b){
    return a + b
}

function work(){
    return 'fdsfrwefrfrf'
}
'''

# 第一步 编译
ctx = execjs.compile(js_code)
# 调用
print(ctx.call('add', 1, 2))
print(ctx.call('work'))