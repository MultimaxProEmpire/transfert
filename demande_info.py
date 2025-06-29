#!/usr/bin/env python3
import sys
import mysql.connector

def agi_read_variables():
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

agi_read_variables()

# Lecture numéro de téléphone
print('GET DATA bienvenue/entrez_numero 3000 10')
sys.stdout.flush()
numero = sys.stdin.readline().strip()

# Enregistrement en base
conn = mysql.connector.connect(user='root', password='pass', database='edutech')
cursor = conn.cursor()
cursor.execute("INSERT INTO prospects (telephone) VALUES (%s)", (numero,))
conn.commit()
conn.close()

# Message de fin
print('STREAM FILE bienvenue/merci_enregistrement ""')
print('HANGUP')
sys.stdout.flush()
