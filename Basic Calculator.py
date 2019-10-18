# coding=utf-8

print("Willkommen bei Deinem persönlichen Taschenrechner.")

a = 0
b = 0
operator = None
bedingung = True

while bedingung:

	operator = raw_input(
		"Welche Rechenart möchtest du durchführen? (' + ' - ' / ' * ') ").strip()

	if operator in ["+", "-", "/", "*"]:

		try:
			a = int(raw_input("Wie lautet die erste Zahl? ").strip())
			b = int(raw_input("Wie lautet die zweite Zahl? ").strip())
		except Exception as error:
			print("Es ist ein Fehler aufgetreten! Bitte prüfen Sie Ihre Eingabe")
			continue

	if operator == "+":
		result = a + b
		print("Ergebnis: " + str(result))

	elif operator == "-":
		result = a - b
		print("Ergebnis: " + str(result))

	elif operator == "/":
		result = a / b
		print("Ergebnis: " + str(result))

	elif operator == "*":
		result = a * b
		print("Ergebnis: " + str(result))

	decision = raw_input("Möchten Sie es erneut versuchen? Antworten Sie mit Ja oder Nein: ").strip()
	if decision == "Nein":
		bedingung = False