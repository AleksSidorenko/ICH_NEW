
"""
17:08:22 От Teacher 23 Teacher 23 до Все:
	In Python sind *args und **kwargs spezielle Syntaxelemente, die in Funktionsdefinitionen verwendet werden, um eine flexible Anzahl von Argumenten zu akzeptieren.

	*args
	*args wird verwendet, um eine beliebige Anzahl von positional arguments (positionsbasierte Argumente) an eine Funktion zu übergeben.
	Es wird als Tupel innerhalb der Funktion behandelt.
	Beispiel:

	python
	def addiere(*args):
	    return sum(args)

17:08:43 От Teacher 23 Teacher 23 до Все:
	print(addiere(1, 2, 3))        # Ausgabe: 6
	print(addiere(4, 5, 6, 7, 8))  # Ausgabe: 30
	Erklärung:
	Die Funktion addiere nimmt beliebig viele Zahlen entgegen.
	Alle übergebenen Argumente werden in args als Tupel gespeichert (args = (1, 2, 3) im ersten Beispiel).
	Dies ist nützlich, wenn die Anzahl der Argumente nicht im Voraus bekannt ist.
	**kwargs
	**kwargs wird verwendet, um eine beliebige Anzahl von keyword arguments (Schlüssel-Wert-Paare) an eine Funktion zu übergeben.
	Es wird als Dictionary innerhalb der Funktion behandelt.
	Beispiel:

	python
	def benutzer_info(**kwargs):
	    for key, value in kwargs.items():
	        print(f"{key}: {value}")

	benutzer_info(name="Anna", alter=25, beruf="Ingenieurin")

17:08:49 От Teacher 23 Teacher 23 до Все:
	# Ausgabe:
	# name: Anna
	# alter: 25
	# beruf: Ingenieurin
	Erklärung:
	Die Funktion benutzer_info akzeptiert beliebige Schlüssel-Wert-Paare.
	Diese werden in kwargs als Dictionary gespeichert (kwargs = {'name': 'Anna', 'alter': 25, 'beruf': 'Ingenieurin'}).
	Kombination von *args und **kwargs
	Man kann beide zusammen verwenden, um sowohl positionsbasierte als auch Schlüssel-Wert-basierte Argumente zu akzeptieren.

	Beispiel:

	python
	def beispiel_funktion(a, b, *args, **kwargs):
	    print(f"a: {a}, b: {b}")
	    print(f"args: {args}")
	    print(f"kwargs: {kwargs}")

	beispiel_funktion(1, 2, 3, 4, x=5, y=6)
	# Ausgabe:
	# a: 1, b: 2
	# args: (3, 4)
	# kwargs: {'x': 5, 'y': 6}
	Erklärung:
	Die ersten beiden Argumente (a, b) sind normale positionsbasierte Argumente.
	Weitere positionsbasierte Argumente (3, 4) werden in args gespeichert.
	Schlüssel-Wert-Paare (x=5, y=6) landen in kwargs.
"""