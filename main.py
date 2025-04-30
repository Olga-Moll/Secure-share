import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from cryptography.fernet import Fernet
import os

# Schlüssel aus Passwort generieren (vereinfachte Version)
def passwort_zu_schluessel(passwort):
    return Fernet.generate_key()  # später verbessern mit Hash aus Passwort

# Datei verschlüsseln
def datei_verschluesseln():
    dateipfad = filedialog.askopenfilename()
    if not dateipfad:
        return

    passwort = simpledialog.askstring("Passwort eingeben", "Gib ein Passwort zur Verschlüsselung ein:", show="*")
    if not passwort:
        return

    # Schlüssel erzeugen (noch ohne echten Passwort-Hash – vereinfacht)
    schluessel = Fernet.generate_key()
    f = Fernet(schluessel)

    # Datei lesen
    with open(dateipfad, 'rb') as datei:
        daten = datei.read()

    # Datei verschlüsseln
    verschluesselt = f.encrypt(daten)

    # Neue Datei speichern
    neuer_pfad = dateipfad + ".enc"
    with open(neuer_pfad, 'wb') as datei:
        datei.write(verschluesselt)

    # Schlüssel anzeigen (z. B. später in Passwort ableiten)
    messagebox.showinfo("Fertig", f"Datei verschlüsselt als:\n{neuer_pfad}\n\n🔑 Schlüssel:\n{schluessel.decode()}")

# Fenster erstellen
fenster = tk.Tk()
fenster.title("SecureShare – Datei verschlüsseln")
fenster.geometry("400x200")

# Button
verschluesseln_button = tk.Button(fenster, text="Datei verschlüsseln", command=datei_verschluesseln)
verschluesseln_button.pack(pady=40)

fenster.mainloop()
