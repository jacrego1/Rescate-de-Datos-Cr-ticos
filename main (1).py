dur = {
    "A": 15,
    "B": 20,
    "C": 10,
    "D": 5,
    "E": 30,
    "F": 25,
    "G": 15,
    "H": 10,
    "I": 20,
    "J": 15,
    "K": 25
}

deps = {
    "A": [],
    "B": [],
    "C": [],
    "D": ["A", "C"],
    "E": ["B", "D"],
    "F": ["E"],
    "G": ["E", "F"],
    "H": ["G"],
    "I": ["G"],
    "J": ["G"],
    "K": ["G"]
}

start = {}
finish = {}
orden = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

for t in orden:
    if len(deps[t]) == 0:
        start[t] = 0
    else:
        m = 0
        for prev in deps[t]:
            if finish.get(prev, 0) > m:
                m = finish[prev]
        start[t] = m
    finish[t] = start[t] + dur[t]

print("CRONOGRAMA (minutos desde el inicio):")
for t in orden:
    print(f"- {t}: inicio {start[t]}  fin {finish[t]}  (duración {dur[t]} min)")

total = max(finish.values())
print("\nTiempo total del plan:", total, "minutos")

if total <= 120:
    print("Cumple la ventana de 120 minutos.")
else:
    print("No cumple los 120 minutos. Revisa dependencias y duraciones.")
