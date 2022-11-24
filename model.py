class Combat_Model:
    def __init__(self,stat_fight: bool):
        self.__stat_fight = stat_fight
        bool(stat_fight)


    def get_stat_fight(self):
        return self.__stat_fight

    def the_next_step(self):
        return str

    def fighter_data(self):
        q = fighter.get_weight()
        w = fighter.get_name()
        e = fighter.get_rapidity()
        r = fighter.get_strength()
        t = fighter.get_block_probability()
        y = fighter.get_chance_to_get_up_on_knockout()
        u = fighter.get_counterstrike_probability()
        i = fighter.get_current_breath()
        o = fighter.get_current_health()
        p = fighter.get_dexterity()
        a = fighter.get_evasion_probability()
        s = fighter.get_knockout()
        d = fighter.get_Max_Health()
        f = fighter.get_Maximum_breath()
        lst_fighter = [q,w,e,r,t,y,u,i,o,p,a,s,d,f]



class Hit:
    def __init__(self,damage: int,recommended_strength: int,breathing_rate: int):
        self.__damage = damage
        self.__recommended_strength = recommended_strength
        self.__breathing_rate = breathing_rate

    def get_damage(self):
        return self.__damage

    def get_recommended_strenghth(self):
        return self.__recommended_strength

    def get_breathing_rate(self):
        return self.__breathing_rate

class Fighter:
    def __init__(self,name:str,weight:int,strength:int,dexterity:int,rapidity:int,Max_Health:int,Maximum_breath:int,
                 block_probability: float,evasion_probability: float,counterstrike_probability: float,chance_to_get_up_on_knockout:float,
                 current_health:int,current_breath : int, knockout= bool):
        self.__name = name
        self.__weight = weight
        self.__strength = strength
        self.__dexterity = dexterity
        self.__rapidity = rapidity
        self.__Max_Health = Max_Health
        self.__Maximum_breath = Maximum_breath
        self.__block_probability = block_probability
        self.__evasion_probability = evasion_probability
        self.__counterstrike_probability = counterstrike_probability
        self.__chance_to_get_up_on_knockout = chance_to_get_up_on_knockout
        self.__current_health = current_health
        self.__current_breath = current_breath
        self.__knockout = knockout


    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_strength(self):
        return self.__strength

    def get_dexterity(self):
        return self.__dexterity

    def get_rapidity(self):
        return self.__rapidity

    def get_Max_Health(self):
        return self.__Max_Health

    def get_Maximum_breath(self):
        return self.__Maximum_breath

    def get_block_probability(self):
        return self.__block_probability

    def get_evasion_probability(self):
        return self.__evasion_probability

    def get_counterstrike_probability(self):
        return self.__counterstrike_probability

    def get_chance_to_get_up_on_knockout(self):
        return self.__chance_to_get_up_on_knockout

    def get_current_health(self):
        return self.__current_health

    def get_current_breath(self):
        return self.__current_breath

    def get_knockout(self):
        return self.__knockout


    def to_strike(self,damage=1,recommended_strength=1,breathing_rate=1):
        punch = Hit(damage=1,recommended_strength=1,breathing_rate=1)
        punch.get_breathing_rate()
        punch.get_recommended_strenghth()
        punch.get_damage()
        return str

    def up_from_knockout(self):
        return str

fighter = Fighter(name="1",weight=1,strength=1,dexterity=1,rapidity=1,Max_Health=1,
                  Maximum_breath=1,block_probability=0.1,evasion_probability=0.1,
                  counterstrike_probability=0.1,chance_to_get_up_on_knockout=0.1,
                  current_health=1,current_breath=1,knockout=True or False)

punch = Hit(damage=1,recommended_strength=1,breathing_rate=1)






