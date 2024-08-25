from function import *

def _safeEval(expr):
    # 避免对方输入恶意代码
    # 替换
    expr = expr.replace('^', '**')

    # 支持的运算
    operators = {
        ast.Add: lambda x, y: x + y,
        ast.Sub: lambda x, y: x - y,
        ast.Mult: lambda x, y: x * y,
        ast.Div: lambda x, y: x / y if y != 0 else "你不能将 0 作为除数",
        ast.Pow: lambda x, y: x ** y,
        ast.USub: lambda x: -x
    }

    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            right_val = _eval(node.right)
            if right_val == "你不能将 0 作为除数":
                return right_val
            return operators[type(node.op)](_eval(node.left), right_val)
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](_eval(node.operand))
        else:
            raise TypeError(node)
    try:
        result = _eval(ast.parse(expr, mode='eval').body)
    except:
        result = "无法解析算式"
    return result



def when_start():
    send("dqqbbpdxdpppbpq 已启动")
    send("该示例将计算对方发送的算式")

def when_update():
    ...

def when_get_message(inner):
    send(_safeEval(inner))

def when_stop():
    send("dqqbbpdxdpppbpq 已关闭")
