#!/usr/bin/env python3
import sys
import mysql.connector

def agi_read_variables():
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

agi_read_variables()

# Lecture identifiant
print('GET DATA bienvenue/entrez_identifiant 3000 8')
sys.stdout.flush()
identifiant = sys.stdin.readline().strip()

# Récupération des cours
conn = mysql.connector.connect(user='root', password='pass', database='edutech')
cursor = conn.cursor()
cursor.execute("SELECT cours FROM programmes WHERE etudiant_id = %s", (identifiant,))
cours = cursor.fetchall()
conn.close()

# Lecture des cours
if cours:
    for c in cours:
        print(f'SAY PHRASE "{c[0]}" ""')  # ou STREAM FILE si audio
else:
    print('STREAM FILE bienvenue/pas_de_cours ""')

print('HANGUP')
sys.stdout.flush()


