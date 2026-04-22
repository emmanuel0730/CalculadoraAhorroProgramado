from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

import sys
sys.path.append('src')

from model.ahorro import AhorroProgramado, Ahorro

Window.clearcolor = (0.97, 0.97, 0.97, 1)


class AhorroProgramadoApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=24,
            spacing=10
        )

        # Título
        self.layout.add_widget(Label(
            text=" Ahorro Programado",
            font_size=22,
            bold=True,
            color=(0.13, 0.13, 0.13, 1),
            size_hint_y=None,
            height=48
        ))

        # Campos
        self._add_field("Meta ($):", "meta")
        self._add_field("Plazo (meses):", "plazo")
        self._add_field("Abono extra ($):", "extra")
        self._add_field("Mes del abono extra:", "mes_extra")

        # Resultado
        self.resultado = Label(
            text="Ingresa los valores y presiona Calcular",
            font_size=14,
            color=(0.4, 0.4, 0.4, 1),
            size_hint_y=None,
            height=40
        )
        self.layout.add_widget(self.resultado)

        # Botón
        btn = Button(
            text="Calcular",
            size_hint_y=None,
            height=46,
            background_color=(0.20, 0.60, 0.45, 1),
            color=(1, 1, 1, 1),
            font_size=15,
            bold=True
        )
        btn.bind(on_press=self.calcular_ahorro)
        self.layout.add_widget(btn)

        return self.layout

    def _add_field(self, label_text, attr_name):
        self.layout.add_widget(Label(
            text=label_text,
            font_size=13,
            color=(0.35, 0.35, 0.35, 1),
            size_hint_y=None,
            height=24,
            halign="left",
            text_size=(Window.width - 48, None)
        ))
        inp = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
            font_size=14,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.13, 0.13, 0.13, 1),
            cursor_color=(0.20, 0.60, 0.45, 1),
            padding=[10, 10]
        )
        setattr(self, attr_name, inp)
        self.layout.add_widget(inp)

    def calcular_ahorro(self, *_):
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
            self.resultado.text = f"Cuota mensual: ${round(cuota, 2):,.2f}"
            self.resultado.color = (0.10, 0.50, 0.35, 1)
        except ValueError:
            self.resultado.text = "Por favor, ingrese valores válidos."
            self.resultado.color = (0.8, 0.2, 0.2, 1)
        except Exception as err:
            self.mostrar_error(str(err))

    def mostrar_error(self, err):
        contenido = GridLayout(cols=1, padding=12, spacing=10)
        contenido.add_widget(Label(
            text=err,
            color=(1, 1, 1, 1),
            font_size=20
        ))
        cerrar = Button(
            text="Cerrar",
            size_hint_y=None,
            height=38,
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        contenido.add_widget(cerrar)
        popup = Popup(
            title="Error",
            content=contenido,
            size_hint=(0.8, 0.35)
        )
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
            float(self.meta.text)
        except ValueError:
            raise Exception("La meta debe ser un número válido.")

        try:
            plazo = int(self.plazo.text)
        except ValueError:
            raise Exception("El plazo debe ser un número entero.")

        try:
            extra = float(self.extra.text)
        except ValueError:
            raise Exception("El abono extra debe ser un número válido.")

        try:
            mes_extra = int(self.mes_extra.text)
        except ValueError:
            raise Exception("El mes del abono extra debe ser un número entero.")

        if extra == 0:
            if mes_extra != 0:
                raise Exception("Si el abono extra es 0, el mes también debe ser 0.")
        else:
            if mes_extra <= 0 or mes_extra > plazo:
                raise Exception(f"El mes del abono extra debe estar entre 1 y {plazo}.")


if __name__ == "__main__":
    AhorroProgramadoApp().run()