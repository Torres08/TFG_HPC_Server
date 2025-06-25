---
marp: true
theme: beam
footer: '**Seguridad y Proteccion de Sistemas Informaticos** '
paginate: true
---

<!-- _class: title -->
# Practica OpenSSL & RSA
Torres Ramos, Juan Luis
ETSIIT - UGR
2022-06-19


---
# Introduccion
`¿Qué se va a hacer en esta demo?`

1. Generar claves públicas y privadas para el emisor y receptor.
2. Firmar y cifrar un PDF usando AES, con la clave simétrica, cifrada con RSA.
3. Descifrar y verificar la autenticidad del documento por el receptor.

Cifrados usados:

- Asimétrico: RSA para la clave simétrica.
- Simétrico: AES con derivación de clave mediante PBKDF2 y sal

