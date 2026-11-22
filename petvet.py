import json
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, simpledialog

PLIK = Path(_file_).with_name('petvet_dane.json')


def wczytaj_dane():
    if PLIK.exists():
        try:
            with open(PLIK, 'r', encoding='utf-8') as plik:
                return json.load(plik)
        except (json.JSONDecodeError, OSError):
            messagebox.showwarning('PETVET', 'Nie udalo sie odczytac pliku z danymi.')
    return {'opiekunowie': [], 'zwierzeta': [], 'wizyty': []}


def zapisz_dane():
    with open(PLIK, 'w', encoding='utf-8') as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=2)


def nowe_id(lista):
    return max((x['id'] for x in lista), default=0) + 1


def zapytaj(tekst):
    wynik = simpledialog.askstring('PETVET', tekst, parent=okno)
    if wynik is None:
        return None
    return wynik.strip()


def pokaz(tekst):
    pole_tekstu.config(state='normal')
    pole_tekstu.delete('1.0', tk.END)
    pole_tekstu.insert(tk.END, tekst)
    pole_tekstu.config(state='disabled')


def lista_opiekunow():
    return '\n'.join(f"{o['id']}. {o['imie']} {o['nazwisko']} (tel. {o['telefon']})"
                     for o in dane['opiekunowie'])


def lista_zwierzat():
    return '\n'.join(f"{z['id']}. {z['imie']} - {z['gatunek']} (opiekun ID: {z['opiekun_id']})"
                     for z in dane['zwierzeta'])


def znajdz(lista, identyfikator):
    return next((x for x in lista if str(x['id']) == str(identyfikator)), None)


def dodaj_opiekuna():
    imie = zapytaj('Imię opiekuna:')
    if not imie:
        return
    nazwisko = zapytaj('Nazwisko opiekuna:')
    if not nazwisko:
        return
    telefon = zapytaj('Numer telefonu:')
    if not telefon:
        return

    dane['opiekunowie'].append({
        'id': nowe_id(dane['opiekunowie']),
        'imie': imie, 'nazwisko': nazwisko, 'telefon': telefon
    })
    zapisz_dane()
    pokaz_baze()
    messagebox.showinfo('PETVET', 'Dodano opiekuna.')


def dodaj_zwierze():
    if not dane['opiekunowie']:
        messagebox.showwarning('PETVET', 'Najpierw dodaj opiekuna.')
        return

    identyfikator = zapytaj('Podaj ID opiekuna:\n\n' + lista_opiekunow())
    if identyfikator is None:
        return
    if not znajdz(dane['opiekunowie'], identyfikator):
        messagebox.showerror('Błąd', 'Nie ma takiego opiekuna.')
        return

    imie = zapytaj('Imię zwierzęcia:')
    if not imie:
        return
    gatunek = zapytaj('Gatunek (np. pies, kot):')
    if not gatunek:
        return
    rasa = zapytaj('Rasa zwierzęcia:')
    if rasa is None:
        return

    dane['zwierzeta'].append({
        'id': nowe_id(dane['zwierzeta']),
        'imie': imie, 'gatunek': gatunek, 'rasa': rasa,
        'opiekun_id': int(identyfikator)
    })
    zapisz_dane()
    pokaz_baze()
    messagebox.showinfo('PETVET', 'Dodano zwierzę.')


def umow_wizyte():
    if not dane['zwierzeta']:
        messagebox.showwarning('PETVET', 'Najpierw dodaj zwierzę.')
        return

    identyfikator = zapytaj('Podaj ID zwierzęcia:\n\n' + lista_zwierzat())
    if identyfikator is None:
        return
    if not znajdz(dane['zwierzeta'], identyfikator):
        messagebox.showerror('Błąd', 'Nie ma takiego zwierzęcia.')
        return

    lekarz = zapytaj('Lekarz (np. Lekarz 1 albo Lekarz 2):')
    if not lekarz:
        return
    termin = zapytaj('Termin wizyty (RRRR-MM-DD GG:MM):')
    if not termin:
        return
    try:
        data_wizyty = datetime.strptime(termin, '%Y-%m-%d %H:%M')
    except ValueError:
        messagebox.showerror('Błąd', 'Zły format daty. Przykład: 2026-12-03 14:30')
        return
    if data_wizyty < datetime.now():
        messagebox.showerror('Błąd', 'Termin nie może być w przeszłości.')
        return

    for wizyta in dane['wizyty']:
        if (wizyta['lekarz'].lower() == lekarz.lower()
                and wizyta['termin'] == termin
                and wizyta['status'] == 'zaplanowana'):
            messagebox.showerror('Błąd', 'Ten lekarz ma już wizytę o tej godzinie.')
            return

    powod = zapytaj('Powód wizyty:')
    if not powod:
        return
    dane['wizyty'].append({
        'id': nowe_id(dane['wizyty']),
        'zwierze_id': int(identyfikator),
        'lekarz': lekarz, 'termin': termin, 'powod': powod,
        'status': 'zaplanowana', 'diagnoza': '', 'zalecenia': '',
        'szczepienie': '', 'koszt': 0, 'platnosc': ''
    })
    zapisz_dane()
    pokaz_wizyty()
    messagebox.showinfo('PETVET', 'Wizyta została umówiona.')


def pokaz_baze():
    tekst = 'OPIEKUNOWIE\n' + (lista_opiekunow() or 'Brak danych')
    tekst += '\n\nZWIERZĘTA\n' + (lista_zwierzat() or 'Brak danych')
    pokaz(tekst)


def pokaz_wizyty():
    tekst = 'WIZYTY\n\n'
    if not dane['wizyty']:
        tekst += 'Brak wizyt.'
    for w in sorted(dane['wizyty'], key=lambda x: x['termin']):
        zwierze = znajdz(dane['zwierzeta'], w['zwierze_id'])
        imie = zwierze['imie'] if zwierze else 'Nieznane'
        tekst += f"ID: {w['id']} | {w['termin']} | {imie}\n"
        tekst += f"Lekarz: {w['lekarz']} | Status: {w['status']}\n"
        tekst += f"Powód: {w['powod']}\n"
        if w['status'] == 'zrealizowana':
            tekst += f"Koszt: {w['koszt']:.2f} zł | Płatność: {w['platnosc'] or 'brak'}\n"
        tekst += '\n'
    pokaz(tekst)


def zakoncz_wizyte():
    pokaz_wizyty()
    identyfikator = zapytaj('ID wizyty do zakończenia (sprawdź listę w oknie):')
    if identyfikator is None:
        return
    w = znajdz(dane['wizyty'], identyfikator)
    if not w or w['status'] != 'zaplanowana':
        messagebox.showerror('Błąd', 'Nie znaleziono zaplanowanej wizyty.')
        return

    diagnoza = zapytaj('Rozpoznanie / diagnoza:')
    if not diagnoza:
        return
    zalecenia = zapytaj('Zalecenia dla opiekuna:')
    if zalecenia is None:
        return
    szczepienie = zapytaj('Wykonane szczepienie (jeśli brak, zostaw puste):')
    if szczepienie is None:
        return
    kwota = zapytaj('Koszt wizyty w zł (np. 100):')
    if kwota is None:
        return
    try:
        koszt = float(kwota.replace(',', '.'))
        if koszt < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror('Błąd', 'Wpisz poprawną kwotę.')
        return

    w['status'] = 'zrealizowana'
    w['diagnoza'] = diagnoza
    w['zalecenia'] = zalecenia
    w['szczepienie'] = szczepienie
    w['koszt'] = koszt
    zapisz_dane()
    pokaz_wizyty()
    messagebox.showinfo('PETVET', 'Zapisano zakończoną wizytę.')


def odwolaj_wizyte():
    pokaz_wizyty()
    identyfikator = zapytaj('ID wizyty do odwołania:')
    if identyfikator is None:
        return
    w = znajdz(dane['wizyty'], identyfikator)
    if not w or w['status'] != 'zaplanowana':
        messagebox.showerror('Błąd', 'Można odwołać tylko zaplanowaną wizytę.')
        return
    w['status'] = 'odwołana'
    zapisz_dane()
    pokaz_wizyty()


def oplac_wizyte():
    pokaz_wizyty()
    identyfikator = zapytaj('ID wizyty do opłacenia:')
    if identyfikator is None:
        return
    w = znajdz(dane['wizyty'], identyfikator)
    if not w or w['status'] != 'zrealizowana':
        messagebox.showerror('Błąd', 'Ta wizyta nie została zrealizowana.')
        return
    if w['platnosc']:
        messagebox.showinfo('PETVET', 'Ta wizyta jest już opłacona.')
        return
    metoda = zapytaj('Metoda płatności: gotówka / karta')
    if metoda is None:
        return
    if metoda.lower() not in ('gotówka', 'gotowka', 'karta'):
        messagebox.showerror('Błąd', 'Wpisz gotówka albo karta.')
        return
    w['platnosc'] = 'gotówka' if metoda.lower() in ('gotówka', 'gotowka') else 'karta'
    zapisz_dane()
    pokaz_wizyty()
    messagebox.showinfo('PETVET', f"Zapisano płatność: {w['koszt']:.2f} zł")


def historia_zwierzecia():
    if not dane['zwierzeta']:
        messagebox.showwarning('PETVET', 'Brak zwierząt w bazie.')
        return
    identyfikator = zapytaj('Podaj ID zwierzęcia:\n\n' + lista_zwierzat())
    if identyfikator is None:
        return
    zwierze = znajdz(dane['zwierzeta'], identyfikator)
    if not zwierze:
        messagebox.showerror('Błąd', 'Nie ma takiego zwierzęcia.')
        return

    tekst = f"HISTORIA LECZENIA: {zwierze['imie']}\n\n"
    znaleziono = False
    for w in sorted(dane['wizyty'], key=lambda x: x['termin']):
        if w['zwierze_id'] == zwierze['id'] and w['status'] == 'zrealizowana':
            znaleziono = True
            tekst += f"Data: {w['termin']} | Lekarz: {w['lekarz']}\n"
            tekst += f"Powód: {w['powod']}\n"
            tekst += f"Diagnoza: {w['diagnoza']}\n"
            tekst += f"Zalecenia: {w['zalecenia']}\n"
            if w['szczepienie']:
                tekst += f"Szczepienie: {w['szczepienie']}\n"
            tekst += f"Koszt: {w['koszt']:.2f} zł\n\n"
    if not znaleziono:
        tekst += 'Brak zakończonych wizyt.'
    pokaz(tekst)


okno = tk.Tk()
okno.title('PETVET - przychodnia weterynaryjna')
okno.geometry('810x530')

dane = wczytaj_dane()

tk.Label(okno, text='PETVET', font=('Arial', 19, 'bold')).pack(pady=(12, 0))
tk.Label(okno, text='Prosty system obsługi przychodni weterynaryjnej').pack(pady=(0, 12))

ramka = tk.Frame(okno)
ramka.pack(fill='both', expand=True, padx=12, pady=6)

przyciski = tk.Frame(ramka)
przyciski.pack(side='left', fill='y', padx=(0, 12))

opcje = [
    ('Dodaj opiekuna', dodaj_opiekuna),
    ('Dodaj zwierzę', dodaj_zwierze),
    ('Pokaż opiekunów i zwierzęta', pokaz_baze),
    ('Umów wizytę', umow_wizyte),
    ('Pokaż wizyty', pokaz_wizyty),
    ('Zakończ wizytę', zakoncz_wizyte),
    ('Odwołaj wizytę', odwolaj_wizyte),
    ('Zapisz płatność', oplac_wizyte),
    ('Historia zwierzęcia', historia_zwierzecia),
]
for napis, funkcja in opcje:
    tk.Button(przyciski, text=napis, command=funkcja, width=27).pack(pady=3)

pole_tekstu = tk.Text(ramka, width=60, height=22, wrap='word', font=('Consolas', 10))
pole_tekstu.pack(side='left', fill='both', expand=True)
pole_tekstu.config(state='disabled')

pokaz_baze()
okno.mainloop()
