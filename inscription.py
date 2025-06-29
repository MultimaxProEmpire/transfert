#!/usr/bin/env python3
import sys
import mysql.connector
import uuid

def agi_read_variables():
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

agi_read_variables()

# Lecture numéro
print('GET DATA bienvenue/entrez_numero 3000 10')
sys.stdout.flush()
numero = sys.stdin.readline().strip()

# Connexion DB
conn = mysql.connector.connect(user='root', password='pass', database='edutech')
cursor = conn.cursor()

# Vérification
cursor.execute("SELECT id FROM etudiants WHERE telephone = %s", (numero,))
if cursor.fetchone():
    print('STREAM FILE bienvenue/deja_inscrit ""')
else:
    identifiant = str(uuid.uuid4())[:8]  # ID court
    cursor.execute("INSERT INTO etudiants (telephone, identifiant) VALUES (%s, %s)", (numero, identifiant))
    conn.commit()
    print(f'SAY ALPHA "{identifiant}" ""')  # Épeler ID

conn.close()
print('HANGUP')
sys.stdout.flush()
