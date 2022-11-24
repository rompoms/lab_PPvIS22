from accessify import private, protected
from model import Combat_Model
from model import punch
import UI


class Combat_System:
    def __init__(self):
        combat_model = Combat_Model(stat_fight=True or False)
        Stat_Fight = combat_model.get_stat_fight()
        combat_model.fighter_data()# данные бойца
        damage = punch.get_damage() # данные удара, класс hit
        strenghth = punch.get_recommended_strenghth()# данные удара, класс hit
        rate = punch.get_breathing_rate()# данные удара, класс hit



    def on_metod_combat_model(self):
        combat_model.the_next_step()

    def on_run_the_fight(self):
        pass

    def on_save_setting(self):
        pass

    def on_set_fighter(self, number: int, ID: int):
        pass

    def on_choose_a_fighter(self,ID: int):
        pass

    def on_delete_fighter(self,ID: int):
        pass

    def on_save_a_fighter(self,ID: int, fighter: list):
        pass

    def on_create_a_fighter(self):
        pass

    def on_add_hit(self,ID_fighter: int, ID_hit: int):
        pass

    def on_hit_selected (ID: int):
        pass

    def on_delete_hit(self, ID: int):
        pass

    def on_save_the_hit(self,ID: int, damage,strenghth,rate):
        pass

    def on_create_a_hit(self):
        pass

    @protected
    @classmethod
    def _load_fighter(self,ID:int):
        return fighter
        pass

    @protected
    @classmethod
    def _save_fighter(self, fighter: list):
        return fighter
        pass

    @protected
    @classmethod
    def _delete_fighter(self, ID: int):
        pass

    @protected
    @classmethod
    def _load_hit(self,ID: int,damage,strenghth,rate):
        pass


    @protected
    @classmethod
    def _save_a_hit(self,fighter: list,damage,strenghth,rate):
        pass

    @protected
    @classmethod
    def _delete_hit(self, ID: int):
        pass



