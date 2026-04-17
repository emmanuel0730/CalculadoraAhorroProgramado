from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append('src')

from model.ahorro import AhorroProgramado, Ahorro


class AhorroProgramadoApp(App):

    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.layout.add_widget(Label(text="Meta ($):"))
        self.meta = TextInput(multiline=False)
        self.layout.add_widget(self.meta)

        self.layout.add_widget(Label(text="Plazo (meses):"))
        self.plazo = TextInput(multiline=False)
        self.layout.add_widget(self.plazo)

        self.layout.add_widget(Label(text="Abono extra ($):"))
        self.extra = TextInput(multiline=False)
        self.layout.add_widget(self.extra)

        self.layout.add_widget(Label(text="Mes del abono extra:"))
        self.mes_extra = TextInput(multiline=False)
        self.layout.add_widget(self.mes_extra)

        self.resultado = Label(text="Resultado:")
        self.layout.add_widget(self.resultado)

        btn = Button(text="Calcular")
        self.layout.add_widget(btn)
        btn.bind(on_press=self.calcular_ahorro)

        return self.layout

    def calcular_ahorro(self, value):
        try:
           
            self.validar()


            cuota = AhorroProgramado().calcular_ahorro(
                Ahorro(
                    meta=float(self.meta.text),
                    plazo=int(self.plazo.text),
                    extra=float(self.extra.text),
                    mes_extra=int(self.mes_extra.text)
                )
            )

            self.resultado.text = f"Cuota mensual: ${str(round(cuota, 2))}"

        except ValueError:
            self.resultado.text = "Por favor, ingrese valores válidos."
        except Exception as err:
            self.mostrar_error(str(err))

    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)

        popup = Popup(title="Error", content=contenido)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

    def validar(self):
       
        if not self.meta.text.strip():
            raise Exception("La meta no puede estar vacía.")
        if not self.plazo.text.strip():
            raise Exception("El plazo no puede estar vacío.")
        if not self.extra.text.strip():
            raise Exception("El abono extra no puede estar vacío.")
        if not self.mes_extra.text.strip():
            raise Exception("El mes del abono extra no puede estar vacío.")

        
        try:
            meta = float(self.meta.text)
            if meta < 0:
                raise Exception("La meta debe ser mayor a cero.")
        except ValueError:
            raise Exception("La meta debe ser un número válido.")

        try:
            plazo = int(self.plazo.text)
            if plazo <= 0:
                raise Exception("El plazo debe ser mayor a cero.")
        except ValueError:
            raise Exception("El plazo debe ser un número entero.")

        try:
            extra = float(self.extra.text)
            if extra < 0:
                raise Exception("El abono extra no puede ser negativo.")
        except ValueError:
            raise Exception("El abono extra debe ser un número válido.")

        try:
            mes_extra = int(self.mes_extra.text)
            plazo = int(self.plazo.text)
            extra = float(self.extra.text)

   
            if extra == 0:
                if mes_extra != 0:
                    raise Exception("Si el abono extra es 0, el mes también debe ser 0.")
            else:
       
                if mes_extra <= 0 or mes_extra > plazo:
                    raise Exception(f"El mes del abono extra debe estar entre 1 y {plazo}.")

        except ValueError:
            raise Exception("El mes del abono extra debe ser un número entero.")


if __name__ == "__main__":
    AhorroProgramadoApp().run()