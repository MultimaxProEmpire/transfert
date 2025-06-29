#!/usr/bin/env python3
import sys
import mysql.connector

def agi_read_variables():
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

agi_read_variables()

# Lecture code transaction
print('GET DATA bienvenue/code_transaction 3000 10')
sys.stdout.flush()
code = sys.stdin.readline().strip()

# Vérification
conn = mysql.connector.connect(user='root', password='pass', database='edutech')
cursor = conn.cursor()
cursor.execute("SELECT statut FROM paiements WHERE code = %s", (code,))
result = cursor.fetchone()

if result and result[0] != "validee":
    cursor.execute("UPDATE paiements SET statut = 'validee' WHERE code = %s", (code,))
    conn.commit()
    print('STREAM FILE bienvenue/paiement_valide ""')
else:
    print('STREAM FILE bienvenue/code_invalide ""')

conn.close()
print('HANGUP')
sys.stdout.flush()
