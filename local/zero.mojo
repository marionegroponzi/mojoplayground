from python import Python, PythonObject

def zero() -> PythonObject:
    torch = Python.import_module("torch")
    return torch.zeros(1)

def main():
    print(zero())

