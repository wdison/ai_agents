from mcp.server.fastmcp import Context

def add(a: float, b: float, ctx: Context) -> float:
    """returns a + b."""
    print(f"Adicionando {a} e {b}")
    ctx.log(level="info", message=f"Chamando metodo de soma para {a} e {b}")
    return a + b

def subtract(a: float, b: float, ctx: Context) -> float:
    """returns a - b."""
    print(f"Subtraindo {a} e {b}")
    ctx.log(level="info", message=f"Chamando metodo de subtração para {a} e {b}")
    # Porque o log do contexto não é enviado para o cliente

    return a - b

def multiply(a: float, b: float, ctx: Context) -> float:
    """returns a * b."""
    print(f"Multiplicando {a} e {b}")
    ctx.log(level="info", message=f"Chamando metodo de multiplicação para {a} e {b}")
    return a * b

def divide(a: float, b: float, ctx: Context) -> float:
    """returns a / b."""
    print(f"Dividindo {a} e {b}")
    ctx.log(level="info", message=f"Chamando metodo de divisão para {a} e {b}")
    return a / b