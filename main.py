from controller import Combat_System
from UI import FoodOptionsApp

class Application:
    def Main(self):
        FoodOptionsApp().run()

    def Build(self):
        Controller_system = Combat_System()


MyApplication = Application()
MyApplication.Main()
MyApplication.Build()





