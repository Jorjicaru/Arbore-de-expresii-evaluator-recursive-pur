from dataclasses import dataclass
from hypothesis import given, strategies as st

#arbore
@dataclass(frozen=True)
class Value:
    value: int 

    def eval(self):
        return self.value

@dataclass(frozen=True)
class Op:
    operator: object
    stanga: object
    dreapta: object

    def eval(self):
        return self.operator(self.stanga.eval(), self.dreapta.eval())

#functii
def adunare(x, y): 
    return x + y

def scadere(x, y): 
    return x - y

def inmultire(x, y): 
    return x * y

def impartire(x, y): 
    return x / y



#testare cu hypothesis
@given(x=st.integers(), y=st.integers())     #generare de numere intregi
def test_inmultire(x, y):
    expr1 = Op(inmultire, Value(x), Value(y))
    expr2 = Op(inmultire, Value(y), Value(x))
    assert expr1.eval() == expr2.eval()     #true = continue / false = eroare

@given(x=st.integers(), y=st.integers())
def test_adunare_comutativa(x, y):
    expr1 = Op(adunare, Value(x), Value(y))
    expr2 = Op(adunare, Value(y), Value(x))
    assert expr1.eval() == expr2.eval()

@given(x=st.integers())
def test_scadere_proprie(x):
    expr = Op(scadere, Value(x), Value(x))
    assert expr.eval() == 0

@given(x=st.integers())
def test_impartire_unu(x):
    expr = Op(impartire, Value(x), Value(1))
    assert expr.eval() == float(x)


test_inmultire()
test_adunare_comutativa()
test_scadere_proprie()
test_impartire_unu()

print("✅ Toate testele (Inmultire, Adunare, Scadere, Impartire) au trecut cu succes!")

#test manual
v1 = Value(10)
v2 = Value(5)

print(f"Valoarea lui v1 este: {v1.eval()}")
print(f"Valoarea lui v2 este: {v2.eval()}")

expr = Op(adunare, v1, v2)
print(f"Rezultatul adunarii este: {expr.eval()}")

