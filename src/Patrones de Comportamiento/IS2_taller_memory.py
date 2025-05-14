

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        return memento

    def undo(self, index=0):
        if index < len(self.history):
            memento = self.history[-(index + 1)]
            self.file = memento.file
            self.content = memento.content

class FileWriterCaretaker:


	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n\n")


	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")
# Test
writer = FileWriterUtility("GFG.txt")
caretaker = FileWriterCaretaker()

writer.write("Primera entrada\n")
caretaker.save(writer)
writer.write("Segunda entrada\n")
caretaker.save(writer)
writer.write("Tercera entrada\n")

print("Contenido antes de undo:", writer.content)
caretaker.undo(writer, 1)  # Recuperar el estado anterior al más reciente
print("Contenido después de undo:", writer.content)
