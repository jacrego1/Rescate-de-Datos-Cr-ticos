# Reto de Algoritmos — Rescate de Datos Críticos

Planificador en Python que calcula un cronograma básico para recuperar y validar datos tras un incidente, respetando dependencias y la restricción de recuperar un solo servidor a la vez.

## Objetivo
Recuperar y validar los datos críticos de dos servidores dentro de 120 minutos y, después, dejar listo el informe a dirección, la comunicación a clientes, la coordinación con legal y el plan de contingencia.

## Tareas y duraciones (min)
A 15, B 20, C 10, D 5, E 30, F 25, G 15, H 10, I 20, J 15, K 25.

## Dependencias
```
Inicio → {A, B, C}
A + C → D
B + D → E → F
E + F → G
G → {H, I, J, K}
```

## Estructura
```
.
├── README.md
└── main.py
```
