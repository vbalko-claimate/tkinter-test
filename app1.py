from tkinter import *
from random import *

# nastavení kontroly kliknutím na jednu ze čtyř možnotí
def kontrola (event):
    # získání widgetu, na kterém byla vyvolána událost
    vyber = event.widget
    
    # vyhodnocení, zda je text z tlačítka stejný jako správná odpověď
    if vyber.cget ("text") == odpovedi_1[poz[index]]:
        # když ano, zobrazí se vyhodnocení
        vyhodnoceni.config (text="SPRÁVNĚ, pokračuj v generování",bg = "light blue",fg = "green", font = ("Arial", 10, "bold"))
        # nastavení umístění popisku
        vyhodnoceni.pack(padx=10, pady=10, side=TOP, anchor="nw") 
    else:
        # když ne, zobrazí se vyhodnocení
        vyhodnoceni.config (text="ŠPATNĚ, zkus to znovu",bg = "light blue",fg = "red", font = ("Arial", 10, "bold"))
        # nastavení umístění popisku
        vyhodnoceni.pack(padx=10, pady=10, side=TOP, anchor="nw")

def konec(event):
    hlokno.destroy ()
    

def generovani(event):
    global index
    global poz
    # definice seznamu pozic
    poz=[]
    # generování, dokud nebudou všechna čísla unikátní
    while len(poz) < 4:
        rand_num = randint(0, len(otazky_1) - 1)
        if rand_num not in poz:
            poz.append(rand_num)
    # generování výběru otázky (z těch čtyř)
    index = randint(0,3) 
    # přiřazení otázky
    otazka.config (text=otazky_1[poz[index]])       
    # nastavení umístění popisku
    otazka.pack(padx=10, pady=10, side=TOP, anchor="nw")

    for i in range (4):
        # přiřazení otázky pozici [i] do popisku tlačítka v cyklu, takže čtyřikrát
        moznosti[i].config(text =odpovedi_1[poz[i]])
        # zobrazení otázky v popisku tlačítka
        moznosti[i].pack(padx=10, pady=10, side=TOP, anchor="nw")
    # vymazání vyhodnocení při generování otázky
    vyhodnoceni.pack_forget()
        
    
# vytvoření a nastavení parametrů pro okno
hlokno = Tk()
hlokno.geometry ("600x600")
hlokno.title ("TECHNOLOGIE")
hlokno.config (background = "light blue")

nadpis_1 = Label (text="Tato výuková aplikace by měla sloužit žákům pro zopakování základních pojmů v rámci odborného předmětu Technologie.", bg = "light blue",fg = "grey", font = ("Arial", 10, "italic"), wraplength=500, anchor="w")
nadpis_1.pack (padx=10, pady=10, side=TOP, anchor="n")

popis_1 = Label (text="Vygeneruj otázku a vyber správnou odpověď.", bg = "light blue",fg = "blue", font = ("Arial", 10, "bold"))
popis_1.pack (padx=10, pady=10, side=TOP, anchor="nw")

# otevření souboru pro čtení
with open("TEC_OT_1.txt","r",encoding='utf-8') as otazky_1:
        # načtení souboru do proměnné obsah
	obsah = otazky_1.read()
	# rozdělení řetězce do seznamu dle řádků
	otazky_1 = obsah.splitlines () 
# otevření souboru pro čtení
with open("TEC_OD_1.txt","r",encoding='utf-8') as odpovedi_1:
	# načtení souboru do proměnné obsah
	obsah = odpovedi_1.read()
        # rozdělení řetězce do seznamu dle řádků
	odpovedi_1 = obsah.splitlines ()

tlac_GE = Button (hlokno, text="VYGENERUJ OTÁZKU")
tlac_GE.pack(padx=10, pady=10, side=TOP, anchor="nw")
tlac_GE.bind ('<Button-1>',generovani)

# definice seznamu (prázdný seznam), do kterého se vloží čtyři tlačítka
moznosti = []
# cyklus pro vytvoření čtyř tlačítek
for i in range(4):
    tlvolba = Button (hlokno, text="")
    # vyvolání funkce kontrola po stisku tlačítka
    tlvolba.bind("<Button-1>",kontrola)
    # přidání tlačítka do seznamu
    moznosti.append (tlvolba) 

# vytvoření popisku pro nadpis
nadpis_1 = Label ()
# vytvoření popisku pro zadání
otazka = Label (bg = "light blue",fg = "black", font = ("Arial", 10, "bold"))
# vytvoření popisku pro vyhodnocení
vyhodnoceni = Label ()

zapati_1 = Label (text="Druhá verze této výukové aplikace bude zaměřená na možnost výběru tématu, následné spuštění v novém okně a generování otázek pouze ze zvoleného tématu.", bg = "light blue",fg = "white", font = ("Arial", 10, "italic"), wraplength=500, anchor="w")
zapati_1.pack (padx=10, pady=10, side=BOTTOM, anchor="n")


# vytvoření tlačítka KONEC
tlac_KO = Button (hlokno, text="KONEC")
# zobrazení a umístění tlačítka KONEC
tlac_KO.pack(padx=10, pady=10, side=BOTTOM, anchor="se") 
tlac_KO.bind ('<Button-1>',konec)


hlokno.mainloop ()
