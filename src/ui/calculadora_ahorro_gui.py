from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import sys
sys.path.append('src')

from core.ahorro import AhorroProgramado, ErrorMetaMayorACero, ErrorPlazoMayorACero, ErrorAbonoSuperaMeta, ErrorMesExtraFueraDelRango, ErrorAbonoExtraMenorAcero

 
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
 
        btn = Button(text="Calcular")
        btn.bind(on_press=self.calcular_ahorro)
        self.layout.add_widget(btn)
 
        self.resultado = Label(text="")
        self.layout.add_widget(self.resultado)
 
        return self.layout
 
    def calcular_ahorro(self, sender):
        ...
 
 
 
if __name__ == "__main__":
    AhorroProgramadoApp().run()