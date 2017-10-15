class Weapon2:
    def __init__(self, file):
        """ Initializes this Weapon with default values for tags and f as file.

        @param File file: a file to write to. generate_weapon needs this. 
                          added in the weapon itself so that its functions 
                          don't need a file parameter.
        """
        self.file = file
        self.name = ""
        self.flavorType, self.flavorType_true = "", False
        self.tip, self.tip_true = "", False
        self.title = ""
        self.short = ""
        self.desc = ""
        self.tooltip = ""
        self.ion, self.ion_true = 0, False
        self.damage, self.damage_true = 0, False
        self.sysDamage, self.sysDamage_true = 0, False
        self.persDamage, self.persDamage_true = 0, False
        self.fireChance, self.fireChance_true = 0, False
        self.breachChance, self.breachChance_true = 0, False
        self.stunChance, self.stunChance_true = 0, False
        self.stun, self.stun_true = 0, False
        self.cooldown = 0
        self.power = 1
        self.cost = 0
        self.rarity = 1
        self.bp = 3
        self.weaponArt = ""
        self.launchSounds = []
        self.hullBust, self.hullBust_true = 0, False
        # self.lockdown, self.lockdown_true = 0, False
        # optional boost tag, consisting of
        # a <type> tag,     either "damage" or "cooldown"
        # an <amount> tag,  a float, amount to change each time fired
        # a <count> tag,    an int, # of times to do the specified amount '''
        self.boost, self.boost_true = [], False
        '''################### DUPLICATES FOR REVERTING ###################'''
        self.name2 = ""
        self.flavorType2, self.flavorType_true2 = "", False
        self.tip2, self.tip_true2 = "", False
        self.title2 = ""
        self.short2 = ""
        self.desc2 = ""
        self.tooltip2 = ""
        self.ion2, self.ion_true2 = 0, False
        self.damage2, self.damage_true2 = 0, False
        self.sysDamage2, self.sysDamage_true2 = 0, False
        self.persDamage2, self.persDamage_true2 = 0, False
        self.fireChance2, self.fireChance_true2 = 0, False
        self.breachChance2, self.breachChance_true2 = 0, False
        self.stunChance2, self.stunChance_true2 = 0, False
        self.stun2, self.stun_true2 = 0, False
        self.cooldown2 = 0
        self.power2 = 1
        self.cost2 = 0
        self.rarity2 = 1
        self.bp2 = 3
        self.weaponArt2 = ""
        self.launchSounds2 = []
        self.hullBust2, self.hullBust_true2 = 0, False
        # self.lockdown2, self.lockdown_true2 = 0, False
        # optional boost tag, consisting of
        # a <type> tag,     either "damage" or "cooldown"
        # an <amount> tag,  a float, amount to change each time fired
        # a <count> tag,    an int, # of times to do the specified amount '''
        self.boost2, self.boost_true2 = [], False
        # fake stuff
        self.sp, self.image = 9001, "over 9000"
        self.length, self.colors = 9001, [900, 900, 900]

    def revert_weapon(self):
        self.name = self.name2
        self.flavorType, self.flavorType_true = \
            self.flavorType2, self.flavorType_true2
        self.tip, self.tip_true = self.tip2, self.tip_true2
        self.title = self.title2
        self.short = self.short2
        self.desc = self.desc2
        self.tooltip = self.tooltip2
        self.ion, self.ion_true = self.ion2, self.ion_true2
        self.damage, self.damage_true = self.damage2, self.damage_true2
        self.sysDamage, self.sysDamage_true = \
            self.sysDamage2, self.sysDamage_true2
        self.persDamage, self.persDamage_true = \
            self.persDamage2, self.persDamage_true2
        self.fireChance, self.fireChance_true = \
            self.fireChance2, self.fireChance_true2
        self.breachChance, self.breachChance_true = \
            self.breachChance2, self.breachChance_true2
        self.stunChance, self.stunChance_true = \
            self.stunChance2, self.stunChance_true2
        self.stun, self.stun_true = self.stun2, self.stun_true2
        self.cooldown = self.cooldown2
        self.power = self.power2
        self.cost = self.cost2
        self.rarity = self.rarity2
        self.bp = self.bp2
        self.weaponArt = self.weaponArt2
        self.launchSounds.clear()
        for sound in self.launchSounds2:
            self.launchSounds.append(sound)
        self.hullBust, self.hullBust_true = self.hullBust2, self.hullBust_true2
        # self.lockdown, self.lockdown_true = self.lockdown2, self.lockdown_true2
        # optional boost tag, consisting of
        ''' a <type> tag,     either "damage" or "cooldown"
        # an <amount> tag,  a float, amount to change each time fired
        # a <count> tag,    an int, # of times to do the specified amount '''
        self.boost.clear()
        for boost_child in self.boost2:
            self.boost.append(boost_child)
        self.boost_true = self.boost_true2

    def generate_weapon(self):
        pass
        # raise NotImplementedError


class Beam(Weapon2):
    def __init__(self, f):
        super().__init__(f)
        # check for speed_true only at creation
        self.speed, self.speed_true = 0, False
        self.sp = 0
        self.length = 0
        self.colors = []  # r, g, b [int, int, int]
        self.image = ""
        '''################### DUPLICATES FOR REVERTING ###################'''
        # check for speed_true only at creation
        self.speed2, self.speed_true2 = 0, False
        self.sp2 = 0
        self.length2 = 0
        self.colors2 = []  # r, g, b [int, int, int]
        self.image2 = ""

    def revert_weapon(self):
        super().revert_weapon()
        self.speed, self.speed_true = self.speed2, self.speed_true2
        self.sp = self.sp2
        self.length = self.length2
        self.colors.clear()
        for color in self.colors2:
            self.colors.append(color)
        self.image = self.image2

    def generate_weapon(self):
        """ regenerates this weapon in self.file based on all its attributes"""
        self.file.write("<weaponBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>BEAM</type>\n")
        if self.flavorType_true:
            self.file.write("\t<flavorType>" +
                            self.flavorType +
                            "</flavorType>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<tooltip>" + self.tooltip + "</tooltip>\n")
        if self.stun_true:
            # round stun since float. makes for more accurate stun time
            self.file.write("\t<stun>" + str(round(self.stun)) + "</stun>\n")
        if self.damage_true:
            self.file.write("\t<damage>" + str(self.damage) + "</damage>\n")
        if self.sysDamage_true:
            self.file.write(
                "\t<sysDamage>" + str(self.sysDamage) + "</sysDamage>\n")
        if self.persDamage_true:
            self.file.write(
                "\t<persDamage>" + str(self.persDamage) + "</persDamage>\n")
        if self.ion_true:
            self.file.write("\t<ion>" + str(self.ion) + "</ion>\n")
        # round speed since float. makes for more accurate speed
        self.file.write("\t<speed>" +
                        str(round(self.speed)) +
                        "</speed>\n")
        # round length since float. makes for more accurate length
        self.file.write(
            "\t<length>" + str(round(self.length, 1)) + "</length>\n")
        self.file.write("\t<sp>" + str(self.sp) + "</sp>\n")
        if self.fireChance_true:
            self.file.write("\t<fireChance>" +
                            str(self.fireChance) +
                            "</fireChance>\n")
        if self.breachChance_true:
            self.file.write("\t<breachChance>" +
                            str(self.breachChance) +
                            "</breachChance>\n")
        if self.stunChance_true:
            self.file.write("\t<stunChance>" +
                            str(self.stunChance) +
                            "</stunChance>\n")
        if self.hullBust_true:
            self.file.write(
                "\t<hullBust>" + str(self.hullBust) +"</hullBust>\n")
        # since cooldown is a float, needs to round
        if self.cooldown < 10:
            self.file.write("\t<cooldown>" +
                            str(round(self.cooldown, 2)) +
                            "</cooldown>\n")
        else:
            self.file.write("\t<cooldown>" +
                            str(round(self.cooldown, 1)) +
                            "</cooldown>\n")
        self.file.write("\t<color>\n")
        self.file.write("\t\t<r>" + str(self.colors[0]) + "</r>\n")
        self.file.write("\t\t<g>" + str(self.colors[1]) + "</g>\n")
        self.file.write("\t\t<b>" + str(self.colors[2]) + "</b>\n")
        self.file.write("\t</color>\n")
        # round since float
        self.file.write("\t<power>" + str(round(self.power)) + "</power>\n")
        # round cost since float. makes for more accurate prices
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("\t<image>" + self.image + "</image>\n")
        if self.boost_true:
            self.file.write("\t<boost>\n")
            self.file.write("\t\t<type>" + self.boost[0] + "</type>\n")
            self.file.write("\t\t<amount>" + str(round(self.boost[1], 3)) +
                            "</amount>\n")
            self.file.write("\t\t<count>" + str(self.boost[2]) + "</count>\n")
            self.file.write("\t</boost>\n")
        self.file.write("\t<launchSounds>\n")
        for sound in self.launchSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</launchSounds>\n")
        self.file.write("\t<weaponArt>" + self.weaponArt + "</weaponArt>\n")
        self.file.write("</weaponBlueprint>\n")

    # to pierce or not to pierce?
    def ce_piercing(self):
        if (self.sp < 1 and self.ion < 1 and
                not ("BA_BEAM_FIRE_FOCUS" in self.name or
                     "BA_BEAM_BIO_FOCUS" in self.name)):
            self.name += "_PIERCING"
            self.title = "Piercing " + self.title
            if len(self.title) > 27:
                self.title = "Pierce " + self.title2
            self.short = "P " + self.short
            self.desc += " (Rare) Pierces one more shield bubble."
            if self.damage == 0:
                # extra pierce needed for non-hull-damage beams
                self.sp += 2
            else:
                self.sp += 1
            self.cost *= 1.5
            self.weaponArt += "_old"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_green"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_low_energy(self):
        if self.sp > 0 and self.ion < 1:
            self.name += "_LOW_ENERGY"
            self.title = "Low Energy " + self.title
            if len(self.title) > 27:
                self.title = "Low NRG " + self.title2
            self.short = "le " + self.short
            self.desc += " Pierces one less shield bubble."
            self.sp -= 1
            self.cost *= 0.75
            self.weaponArt += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    # support or assault?
    def ce_support_beam(self):
        if self.length > 40:
            self.name += "_SUPPORT_BEAM"
            self.title = "Support " + self.title
            self.short = "Sup " + self.short
            self.desc += " Support: cooldown x0.5 beam range x0.5"
            self.cooldown *= 0.5
            self.length /= 2
            self.cost *= 1.1
            self.weaponArt += "_high_tech"
            self.generate_weapon()
            self.revert_weapon()

    def ce_assault_beam(self):
        if self.power < 4:
            self.name += "_ASSAULT_BEAM"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += " Assault: cooldown x0.75 power cost +1"
            self.cooldown *= 0.75
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_tactical(self):
        if self.damage > 0:
            self.name += "_TACTICAL"
            self.title = "Tactical " + self.title
            if len(self.title) > 27:
                self.title = "Tact. " + self.title2
            self.short = "Ta " + self.short
            self.desc += " Tactical: damage -1 system damage +2"
            self.damage -= 1
            self.sysDamage_true = True
            self.sysDamage += 2
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_brutal(self):
        if self.damage > 0:
            self.name += "_BRUTAL"
            self.title = "Brutal " + self.title
            if len(self.title) > 27:
                self.title = "Brut. " + self.title2
            self.short = "BR " + self.short
            self.desc += " Packs a punch."
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.breachChance_true = True
            self.breachChance += 1
            if self.breachChance > 10:
                self.breachChance = 10
            self.persDamage_true = True
            self.persDamage += 1
            self.stunChance_true = True
            self.stunChance += 1
            if self.stunChance > 10:
                self.stunChance = 10
            self.cost *= 1.3
            self.weaponArt += "_dirty_steel"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_dark"

            self.generate_weapon()
            self.revert_weapon()

    def ce_weaksauce(self):
        if self.damage > 0:
            self.name += "_WEAKSAUCE"
            self.title = "Weaksauce " + self.title
            if len(self.title) > 27:
                self.title = "Weak " + self.title2
            self.short = "weak " + self.short
            self.desc += " Makes your enemy laugh at you."
            self.cooldown *= 1.1
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.1
            self.breachChance -= 1
            if self.breachChance < 0:
                self.breachChance = 0
            self.persDamage -= 1
            self.stunChance -= 1
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    def ce_hull_ripper(self):
        if (self.damage > 0 and self.hullBust < 1 and self.ion < 1 and
                not ("BA_BEAM_ADAPTIVE_1" in self.name or
                     "BA_BEAM_ADAPTIVE_2" in self.name or
                     "BA_BEAM_ADAPTIVE_3" in self.name)):
            self.name += "_HULL_RIPPER"
            self.title = "Hull Ripper " + self.title
            if len(self.title) > 27:
                self.title = "Ripper " + self.title2
            self.short = "HR " + self.short
            self.desc += " Deals double hull damage to systemless rooms."
            self.hullBust_true = True
            self.hullBust = 1
            self.cost *= 1.25
            self.weaponArt += "_green"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_green"

            self.generate_weapon()
            self.revert_weapon()

    def ce_reconfigured(self):
        if self.hullBust > 0:
            self.name += "_RECONFIGURED"
            self.title = "Reconfigured " + self.title
            if len(self.title) > 27:
                self.title = "Reconf. " + self.title2
            self.short = "r " + self.short
            self.desc += \
                " Reconfigured: deals normal damage to systemless rooms"
            self.hullBust_true = False
            self.hullBust = 0
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    def ce_heavy(self):
        if (self.ion < 1 and self.damage == 1 and
                self.hullBust < 1 and self.power < 4):
            self.name += "_HEAVY"
            self.title = "Heavy " + self.title
            self.short = "H " + self.short
            self.desc += " Heavy: damage +1 cooldown x1.5 power cost +1"
            self.damage += 1
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.power += 1
            self.cost *= 1.4
            self.weaponArt += "_old"
            self.generate_weapon()
            self.revert_weapon()

    def ce_light(self):
        if self.ion < 1 and self.damage > 2:
            self.name += "_LIGHT"
            self.title = "Light " + self.title
            self.short = "l " + self.short
            self.desc += " Light: damage -1 cooldown x0.9"
            self.damage -= 1
            # catch for mines
            if self.sysDamage < 0:
                self.sysDamage += 1
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_substandard(self):
        self.name += "_SUBSTANDARD"
        self.title = "Substandard " + self.title
        if len(self.title) > 27:
            self.title = "Subst. " + self.title2
        self.short = "sub " + self.short
        # self.desc += " Overall performance is substandard."
        # this doesn't really say much...
        self.desc += " Substandard: overall bad stats"
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.speed *= 0.9
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 1
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.8
        self.weaponArt += "_slight_desat"
        self.generate_weapon()
        self.revert_weapon()

    def ce_surplus(self):
        self.name += "_SURPLUS"
        self.title = "Surplus " + self.title
        self.short = "sur " + self.short
        self.desc += " Surplus: overall very bad stats"
        self.cooldown *= 1.2
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.2
        self.speed *= 0.8
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 3
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.5
        self.weaponArt += "_heavy_desat"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_quality(self):
        self.name += "_QUALITY"
        self.title = "Quality " + self.title
        self.short = "Q " + self.short
        self.desc += " Quality: overall better stats"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.speed *= 1.1
        self.cost *= 1.25
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_custom(self):
        self.name += "_CUSTOM"
        self.title = "Custom " + self.title
        self.short = "C " + self.short
        self.desc += " Custom (Rare): overall great stats"
        self.cooldown *= 0.8
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.8
        self.speed *= 1.2
        self.fireChance_true = True
        self.fireChance += 1
        if self.fireChance > 10:
            self.fireChance = 10
        self.breachChance_true = True
        self.breachChance += 1
        if self.breachChance > 10:
            self.breachChance = 10
        self.stunChance_true = True
        self.stunChance += 1
        if self.stunChance > 10:
            self.stunChance = 10
        self.cost *= 1.5
        self.weaponArt += "_ht_steel_bright"
        if (self.image == "ba_beam_contact_big" or
                self.image == "ba_beam_contact_pierce"):
            self.image += "_high_tech"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_vintage(self):
        self.name += "_VINTAGE"
        self.title = "Vintage " + self.title
        if len(self.title) > 27:
            self.title = "Vint. " + self.title2
        self.short = "Vin " + self.short
        self.desc += " Vintage: overall bad stats but valuable and rare"
        self.speed *= 0.9
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.cost *= 1.5
        if self.rarity > 0:
            self.rarity += 2
            if self.rarity > 5:
                self.rarity = 5
        self.weaponArt += "_gritty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_antique(self):
        self.name += "_ANTIQUE"
        self.title = "Antique " + self.title
        if len(self.title) > 27:
            self.title = "Anti. " + self.title2
        self.short = "Ant " + self.short
        self.desc += " Antique: overall very bad stats but " \
                     "very valuable and rare"
        self.speed *= 0.7
        self.cooldown *= 1.4
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.4
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        if self.rarity > 0:
            self.rarity += 4
            if self.rarity > 5:
                self.rarity = 5
        self.cost *= 2
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc += " Swag (Rare): good for showing off"
            # self.colors[0] = 255
            self.colors[1] = 180
            self.colors[2] = 0
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_gold"
            self.generate_weapon()
            self.revert_weapon()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Secondhand " + self.title
        if len(self.title) > 27:
            self.title = "Sec. Hand " + self.title2
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_weapon()
        self.revert_weapon()

    # power-only
    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.weaponArt += "_dirty"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_optimized(self):
        if self.power > 2:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            if len(self.title) > 27:
                self.title = "Optim. " + self.title2
            if len(self.title) > 27:
                self.title = "Opt. " + self.title2
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.weaponArt += "_ht_steel"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # cooldown-only
    def ce_outdated(self):
        # every weapon has a cooldown
        self.cooldown *= 1.15
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.15
        self.name += "_OUTDATED"
        # self.desc += (" Drags on with a sub-par reload time.")
        self.desc += " Recharges slightly slower."
        self.title = "Outdated " + self.title
        if len(self.title) > 27:
            self.title = "Outd. " + self.title2
        self.short = "ou " + self.short
        self.cost *= 0.8
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_obsolete(self):
        # every weapon has a cooldown
        self.cooldown *= 1.25
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.25
        self.name += "_OBSOLETE"
        self.desc += " Recharges slower."
        self.title = "Obsolete " + self.title
        if len(self.title) > 27:
            self.title = "Obsol. " + self.title2
        self.short = "ob " + self.short
        self.cost *= 0.6
        self.weaponArt += "_rust"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_upgraded(self):
        # every weapon has a cooldown
        self.cooldown *= 0.85
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.85
        self.name += "_UPGRADED"
        self.desc += " Recharges slightly faster."
        self.title = "Upgraded " + self.title
        if len(self.title) > 27:
            self.title = "Upgr. " + self.title2
        self.short = "UP " + self.short
        self.cost *= 1.2
        self.weaponArt += "_high_tech"

        self.generate_weapon()
        self.revert_weapon()

    def ce_advanced(self):
        # every weapon has a cooldown
        self.cooldown *= 0.75
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.75
        self.name += "_ADVANCED"
        self.desc += " (Rare) Recharges faster."
        self.title = "Advanced " + self.title
        if len(self.title) > 27:
            self.title = "Adv. " + self.title2
        self.short = "AD " + self.short
        self.cost *= 1.4
        self.weaponArt += "_ht_steel_bright"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    # give this a better name
    def ce_widespread(self):
        if self.ion < 1 and self.damage > 0:
            self.name += "_WIDESPREAD"
            self.title = "Wide Sp. " + self.title
            self.short = "wid " + self.short
            self.desc += " Wide Spread: system damage -1"
            self.sysDamage_true = True
            self.sysDamage -= 1
            self.cost *= 0.75
            self.weaponArt += "_slight_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"
            self.colors[0] = 200
            self.colors[1] = 60
            self.colors[2] = 60
            self.generate_weapon()
            self.revert_weapon()

    # give this a better name
    def ce_tightspread(self):
        if self.ion < 1 and self.damage > 0:
            self.name += "_TIGHTSPREAD"
            self.title = "Tight Sp. " + self.title
            self.short = "TIG " + self.short
            self.desc += " Tight Spread: system damage +1"
            self.sysDamage_true = True
            self.sysDamage += 1
            self.cost *= 1.25
            self.weaponArt += "_dirty_steel"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_green"
            self.generate_weapon()
            self.revert_weapon()

    def ce_impacting(self):
        if self.breachChance < 10 and self.stunChance > 0 and self.ion < 1:
            self.name += "_IMPACTING"
            self.title = "Impacting " + self.title
            if len(self.title) > 27:
                self.title = "Impact. " + self.title2
            self.short = "IM " + self.short
            self.desc += " Impact: breach chance +1 stun chance +1"
            # must already have a stun chance, no need to set it
            if self.stunChance < 10:
                self.stunChance += 1
            self.breachChance_true = True
            # since breachChance must already be less than 10 no need to check
            self.breachChance += 1
            self.cost *= 1.1
            self.weaponArt += "_dark"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_incendiary(self):
        if self.fireChance < 7:
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_INCENDIARY"
            self.desc += " A bit more likely to start a fire."
            self.title = "Incendiary " + self.title
            if len(self.title) > 27:
                self.title = "Incend. " + self.title2
            self.short = "IN " + self.short
            self.cost *= 1.2
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_red"
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_plasma(self):
        if self.fireChance < 7:
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 2
            self.name += "_PLASMA"
            self.desc += " (Rare) Imbued with plasma, this weapon's more " \
                         "likely to start a fire."
            self.title = "Plasma " + self.title
            self.short = "PL " + self.short
            self.cost *= 1.3
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_red"
            self.weaponArt += "_red"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_insulated(self):
        if self.ion < 1 and self.fireChance > 1:
            self.fireChance -= 1
            self.name += "_INSULATED"
            self.title = "Insulated " + self.title
            if len(self.title) > 27:
                self.title = "Insul. " + self.title2
            self.short = "in " + self.short
            self.desc += " Insulated: fire chance -1"
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"
            # self.colors[0] = 255
            self.colors[1] = 50
            self.colors[2] = 50
            self.generate_weapon()
            self.revert_weapon()

    def ce_heatshielded(self):
        if self.ion < 1 and self.fireChance > 4:
            self.fireChance -= 3
            self.name += "_HEATSHIELDED"
            self.title = "Heatshielded " + self.title
            if len(self.title) > 27:
                self.title = "Heatsh. " + self.title2
            self.short = "hea " + self.short
            self.desc += " Heatshielded: fire chance -3"
            self.cost *= 0.7
            self.weaponArt += "_heavy_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"
            # self.colors[0] = 255
            self.colors[1] = 100
            self.colors[2] = 100
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # crew-damage only
    def ce_radioactive(self):
        # need to make it true when increasing, but not when decreasing
        self.persDamage_true = True
        self.persDamage += 1
        self.name += "_RADIOACTIVE"
        self.desc += " Radioactive elements make it deadlier to crew."
        self.title = "Radioactive " + self.title
        if len(self.title) > 27:
            self.title = "Rad. " + self.title2
        self.short = "RAD " + self.short
        self.cost *= 1.2
        self.weaponArt += "_yellow"
        if (self.image == "ba_beam_contact_big" or
                self.image == "ba_beam_contact_pierce"):
            self.image += "_yellow"
        self.colors[0] = 126
        self.colors[1] = 117
        self.colors[2] = 82
        self.generate_weapon()
        self.revert_weapon()

    def ce_safe_nonlethal(self):
        # e.g. light scatter lasers?
            # negative persDamage values are not okay since that means
            # crew heal shenanigans since damage is less than 1
        if self.ion < 1 and self.damage < 1 and self.persDamage > 0:
            self.persDamage -= 1
            self.name += "_SAFE_NONLETHAL"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.persDamage == 0:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe(self):
        # clause added to avoid crew heal shenanigans
        if (self.ion < 1 and self.damage > 0 and
                self.persDamage != -self.damage):
            # since damage is at least 1, persDamage tag must be added
            self.persDamage_true = True
            self.persDamage -= 1
            # since damage is at least 1, persDamage will cancel out some crew
            # damage done just by regular damage, so negative values are okay
            self.name += "_SAFE"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.damage == 1:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"
            # self.colors[0] = 255
            self.colors[1] = 50
            self.colors[2] = 50
            self.generate_weapon()
            self.revert_weapon()

    def ce_volatile(self):
        # if fire chance is already 10, then radioactive does the same thing
        if self.fireChance < 10:
            # adds a persDamage tag if one doesn't already exist
            self.persDamage_true = True
            self.persDamage += 1
            # same for fireChance
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_VOLATILE"
            self.title = "Volatile " + self.title
            if len(self.title) > 27:
                self.title = "Volat. " + self.title2
            self.short = "VOL " + self.short
            self.desc += " Releases volatile chemicals on impact."
            self.cost *= 1.3
            self.weaponArt += "_dirty"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_deathly(self):
        if self.persDamage > 0:
            self.persDamage *= 2
            self.name += "_DEATHLY"
            self.title = "Deathly " + self.title
            self.short = "DEA " + self.short
            self.desc += " Deathly (Epic): crew damage x2"
            self.cost *= 1.5
            self.weaponArt += "_dirty_steel"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_dark"
            self.colors[0] = 80
            self.colors[1] = 60
            self.colors[2] = 0
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # beam-only
    def ce_sungazer(self):
        # removed self.sp < 5 requirement (Sungazer Maul pls!)
        if not ("BEAM_FIRE" in self.name or
                "BA_BEAM_FIRE_2" in self.name or
                "BA_BEAM_FIRE_FOCUS" in self.name or
                "BEAM_BIO" in self.name or "BA_BEAM_BIO_2" in self.name or
                "BA_BEAM_BIO_FOCUS" in self.name):
            self.name += "_SUNGAZER"
            self.title = "Sungazer " + self.title
            if len(self.title) > 27:
                self.title = "Sunga. " + self.title2
            self.short = "SUN " + self.short
            self.desc += " Sungazer (Epic): shield piercing +1, fire chance +4"
            # self.colors[0] = 255
            self.colors[1] = 230
            self.colors[2] = 0
            # particle beam catch
            if self.sp == 0 and self.damage < 1:
                self.sp = 2
            else:
                self.sp += 1
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.cost *= 1.5
            self.weaponArt += "_gold"
            self.generate_weapon()
            self.revert_weapon()

    def ce_concentrated(self):
        if (self.length > 10 and
                not ("BEAM_FIRE" in self.name or
                     "BA_BEAM_FIRE_2" in self.name or
                     "BA_BEAM_FIRE_FOCUS" in self.name or
                     "BEAM_BIO" in self.name or "BA_BEAM_BIO_2" in self.name or
                     "BA_BEAM_BIO_FOCUS" in self.name)):
            self.name += "_CONCENTRATED"
            self.title = "Concentrated " + self.title
            if len(self.title) > 27:
                self.title = "Concen. " + self.title2
            self.short = "con " + self.short
            self.desc += " Concentrates its span to pierce through " \
                         "a shield bubble."
            if self.sp == 0 and self.damage < 1:
                self.sp = 2
            else:
                self.sp += 1
            self.length *= 0.2
            self.colors[0] -= 55
            if self.colors[0] < 0:
                self.colors[0] = 0
            self.cost *= 1.1
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_focused(self):
        # removed self.sp < 5 requirement
        if (self.length > 10 and
                not ("BEAM_FIRE" in self.name or
                     "BA_BEAM_FIRE_2" in self.name or
                     "BA_BEAM_FIRE_FOCUS" in self.name or
                     "BEAM_BIO" in self.name or "BA_BEAM_BIO_2" in self.name or
                     "BA_BEAM_BIO_FOCUS" in self.name)):
            self.name += "_FOCUSED"
            self.title = "Focused " + self.title
            if len(self.title) > 27:
                self.title = "Foc. " + self.title2
            self.short = "Foc " + self.short
            self.desc += " (Rare) Focuses its span to pierce through " \
                         "a shield bubble."
            if self.sp == 0 and self.damage < 1:
                self.sp = 2
            else:
                self.sp += 1
            self.length /= 2
            self.colors[0] -= 55
            if self.colors[0] < 0:
                self.colors[0] = 0
            self.cost *= 1.1
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_supercharged(self):
        if not ("BEAM_FIRE" in self.name or
                "BA_BEAM_FIRE_2" in self.name or
                "BA_BEAM_FIRE_FOCUS" in self.name or
                "BEAM_BIO" in self.name or
                "BA_BEAM_BIO_2" in self.name or
                "BA_BEAM_BIO_FOCUS" in self.name):
            self.name += "_SUPERCHARGED"
            self.title = "Supercharged " + self.title
            if len(self.title) > 27:
                self.title = "Supercharg. " + self.title2
            if len(self.title) > 27:
                self.title = "Superch. " + self.title2
            self.short = "SPC " + self.short
            self.desc += " Supercharged: shield piercing +1, power cost +1"
            # particle beam catch
            if self.sp == 0 and self.damage < 1:
                self.sp = 2
            else:
                self.sp += 1
            self.colors[0] -= 35
            if self.colors[0] < 0:
                self.colors[0] = 0
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_unfocused(self):
        if self.length >= 80 and self.power > 2 and self.damage > 1:
            self.name += "_UNFOCUSED"
            self.title = "Unfocused " + self.title
            if len(self.title) > 27:
                self.title = "Unfoc. " + self.title2
            self.short = "Unf " + self.short
            self.desc += " Unfocused: damage -1, beam range x1.2"
            self.damage -= 1
            self.length *= 1.2
            self.colors[0] = 200
            self.colors[1] = 150
            self.colors[2] = 150
            self.cost *= 0.8
            self.weaponArt += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_industrial(self):
        if (self.length > 10 and self.power > 1 and self.damage > 1 and
                not ("BA_BEAM_SCYTHE" in self.name or
                     "BA_BEAM_FLAIL_DAMAGE" in self.name)):
            self.name += "_INDUSTRIAL"
            self.title = "Industrial " + self.title
            if len(self.title) > 27:
                self.title = "Indust. " + self.title2
            self.short = "Ind " + self.short
            self.desc += " Industrial: beam range x1.25 power cost -1 " \
                         "beam speed x0.10 damage -1"
            # self.colors[0] = 255
            self.colors[1] = 50
            self.colors[2] = 0
            self.length *= 1.25
            self.power -= 1
            self.speed *= 0.10
            self.damage -= 1
            self.cost *= 1.1
            self.weaponArt += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_swift(self):
        if self.length > 10 and self.power > 1:
            self.name += "_SWIFT"
            self.title = "Swift " + self.title
            self.short = "SWI " + self.short
            self.desc += " Swift: beam speed x1.5"
            self.speed *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_high_tech"
            self.generate_weapon()
            self.revert_weapon()

    def ce_sluggish(self):
        if self.length > 10 and self.power > 1:
            self.name += "_SLUGGISH"
            self.title = "Sluggish " + self.title
            if len(self.title) > 27:
                self.title = "Slugg. " + self.title2
            self.short = "slu " + self.short
            self.desc += " Sluggish: beam speed x0.5"
            self.speed *= 0.5
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_extended(self):
        if self.length > 10:
            self.name += "_EXTENDED"
            self.title = "Extended " + self.title
            if len(self.title) > 27:
                self.title = "Exten. " + self.title2
            self.short = "EX " + self.short
            self.desc += " Extended beam range."
            self.cost *= 1.15
            self.length *= 1.20
            self.weaponArt += "_ht_steel"
            self.generate_weapon()
            self.revert_weapon()

    # aka _EXPANDED
    def ce_continuous(self):
        if self.length > 10:
            self.name += "_CONTINUOUS"
            self.title = "Continuous " + self.title
            if len(self.title) > 27:
                self.title = "Contin. " + self.title2
            if len(self.title) > 27:
                self.title = "Cont. " + self.title2
            self.short = "CON " + self.short
            self.desc += " Continuous (Rare): Beam Range x1.30"
            self.cost *= 1.2
            self.length *= 1.30
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_ht_steel_bright"
            self.generate_weapon()
            self.revert_weapon()

    def ce_infinite(self):
        if self.length > 10:
            self.name += "_INFINITE"
            self.title = "Infinite " + self.title
            if len(self.title) > 27:
                self.title = "Infin. " + self.title2
            if len(self.title) > 27:
                self.title = "Inf. " + self.title2
            self.short = "INF " + self.short
            self.desc += " Infinite (Epic): Beam Range x1.50"
            self.cost *= 1.5
            self.length *= 1.50
            self.weaponArt += "_ht_steel_bright"
            self.generate_weapon()
            self.revert_weapon()

    def ce_short(self):
        if self.length > 10:
            self.name += "_SHORT"
            self.title = "Short " + self.title
            self.short = "sh " + self.short
            self.desc += " Beam Range x0.80."
            self.cost *= 0.8
            self.length *= 0.75
            self.weaponArt += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_blunt(self):
        if self.length > 10:
            self.name += "_BLUNT"
            self.title = "Blunt " + self.title
            self.short = "bl " + self.short
            self.desc += " Beam Range x0.60."
            self.cost *= 0.67
            self.length *= 0.6
            self.weaponArt += "_rust"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_penetrating_beam(self):
        if self.breachChance < 10 and self.ion < 1:
            self.name += "_PENETRATING_BEAM"
            self.title = "Penetr. " + self.title
            self.short = "PE " + self.short
            self.desc += " Penetrating: breach chance +1"
            self.breachChance += 1
            self.colors[0] -= 55
            if self.colors[0] < 0:
                self.colors[0] = 0
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_breaching_beam(self):
        if self.breachChance < 9 and self.ion < 1:
            self.name += "_BREACHING_BEAM"
            self.title = "Breach. " + self.title
            self.short = "BR " + self.short
            self.desc += " Breaching: breach chance +2"
            self.breachChance += 2
            self.colors[0] -= 105
            if self.colors[0] < 0:
                self.colors[0] = 0
            self.cost *= 1.2
            self.weaponArt += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_stungun(self):
        if 0 < self.stunChance < 8:
            self.name += "_STUNGUN"
            self.title = "Stun " + self.title
            self.short = "ST " + self.short
            self.desc += " Stun: stun chance +3"
            self.stunChance += 3
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shock(self):
        if 0 < self.stunChance < 6 and self.ion > 0:
            self.name += "_SHOCK"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun chance +5"
            self.stunChance += 5
            self.cost *= 1.3
            self.weaponArt += "_yellow"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_regulated(self):
        if self.stunChance > 0:
            self.name += "_REGULATED"
            self.title = "Regulated " + self.title
            if len(self.title) > 27:
                self.title = "Regul. " + self.title2
            self.short = "reg " + self.short
            if 0 < self.stunChance < 3:
                self.desc += " Due to regulations, " \
                             "its ability to stun was removed."
            else:
                self.desc += " Less likely to stun due to regulations."
            self.stunChance -= 2
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            if (self.image == "ba_beam_contact_big" or
                    self.image == "ba_beam_contact_pierce"):
                self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_calibrated_beam(self):
        if self.stun > 4:
            self.name += "_CALIBRATED_BEAM"
            self.title = "Intense " + self.title
            if len(self.title) > 27:
                self.title = "Int. " + self.title2
            self.short = "INT " + self.short
            self.desc += " Intense: stun time x1.25"
            self.stun *= 1.25
            self.cost *= 1.2
            self.weaponArt += "_high_tech_2"
            self.generate_weapon()
            self.revert_weapon()


class Laser(Weapon2):
    def __init__(self, f):
        super().__init__(f)
        self.lockdown, self.lockdown_true = 0, False
        # check for speed_true only at creation
        self.speed, self.speed_true = 0, False
        self.shots = 0
        self.sp = 0
        self.missiles, self.missiles_true = 0, False
        self.hitShipSounds = []
        self.hitShieldSounds = []
        self.missSounds = []
        self.image = ""
        self.explosion, self.explosion_true = "", False
        # unknown if this works with other weapon-types
        self.chargeLevels, self.chargeLevels_true = 1, False
        self.locked, self.locked_true = 1, False
        self.droneTargetable, self.droneTargetable_true = 2, False
        self.droneTargetable_none = False
        '''################### DUPLICATES FOR REVERTING ###################'''
        self.lockdown2, self.lockdown_true2 = 0, False
        # check for speed_true only at creation
        self.speed2, self.speed_true2 = 0, False
        self.shots2 = 0
        self.sp2 = 0
        self.missiles2, self.missiles_true2 = 0, False
        self.hitShipSounds2 = []
        self.hitShieldSounds2 = []
        self.missSounds2 = []
        self.image2 = ""
        self.explosion2, self.explosion_true2 = "", False
        # unknown if this works with other weapon-types
        self.chargeLevels2, self.chargeLevels_true2 = 1, False
        self.locked2, self.locked_true2 = 1, False
        self.droneTargetable2, self.droneTargetable_true2 = 2, False
        self.droneTargetable_none2 = False

    def revert_weapon(self):
        super().revert_weapon()
        self.lockdown, self.lockdown_true = self.lockdown2, self.lockdown_true2
        self.speed, self.speed_true = self.speed2, self.speed_true2
        self.shots = self.shots2
        self.sp = self.sp2
        self.missiles, self.missiles_true = self.missiles2, self.missiles_true2
        self.hitShipSounds.clear()
        for sound in self.hitShipSounds2:
            self.hitShipSounds.append(sound)
        self.hitShieldSounds.clear()
        for sound in self.hitShieldSounds2:
            self.hitShieldSounds.append(sound)
        self.missSounds.clear()
        for sound in self.missSounds2:
            self.missSounds.append(sound)
        self.image = self.image2
        self.explosion, self.explosion_true = \
            self.explosion2, self.explosion_true2
        # unknown if this works with other weapon-types
        self.chargeLevels, self.chargeLevels_true = \
            self.chargeLevels2, self.chargeLevels_true2
        self.locked, self.locked_true = self.locked2, self.locked_true2
        self.droneTargetable = self.droneTargetable2
        self.droneTargetable_true = self.droneTargetable_true2
        self.droneTargetable_none = self.droneTargetable_none2

    def generate_weapon(self):
        """ regenerates this weapon in self.file based on all its attributes"""
        self.file.write("<weaponBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>LASER</type>\n")
        if self.flavorType_true:
            self.file.write(
                "\t<flavorType>" + self.flavorType + "</flavorType>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        if self.droneTargetable_none:
            self.file.write("\t<drone_targetable />\n")
        elif self.droneTargetable_true:
            self.file.write("\t<drone_targetable>" +
                            str(self.droneTargetable) +
                            "</drone_targetable>\n")
        if self.locked_true:
            self.file.write("\t<locked>" + str(self.locked) + "</locked>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<tooltip>" + self.tooltip + "</tooltip>\n")
        if self.stun_true:
            # round stun since float. makes for more accurate stun time
            self.file.write("\t<stun>" + str(round(self.stun)) + "</stun>\n")
        if self.damage_true:
            self.file.write("\t<damage>" + str(self.damage) + "</damage>\n")
        if self.sysDamage_true:
            self.file.write(
                "\t<sysDamage>" + str(self.sysDamage) + "</sysDamage>\n")
        if self.persDamage_true:
            self.file.write(
                "\t<persDamage>" + str(self.persDamage) + "</persDamage>\n")
        if self.ion_true:
            self.file.write("\t<ion>" + str(self.ion) + "</ion>\n")
        # round speed since float. makes for more accurate speed
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        if self.missiles_true:
            self.file.write(
                "\t<missiles>" + str(self.missiles) + "</missiles>\n")
        self.file.write("\t<shots>" + str(self.shots) + "</shots>\n")
        self.file.write("\t<sp>" + str(self.sp) + "</sp>\n")
        if self.fireChance_true:
            self.file.write(
                "\t<fireChance>" + str(self.fireChance) + "</fireChance>\n")
        if self.breachChance_true:
            self.file.write("\t<breachChance>" +
                            str(self.breachChance) +
                            "</breachChance>\n")
        if self.stunChance_true:
            self.file.write("\t<stunChance>" +
                            str(self.stunChance) +
                            "</stunChance>\n")
        if self.lockdown_true:
            self.file.write(
                "\t<lockdown>" + str(self.lockdown) + "</lockdown>\n")
        if self.hullBust_true:
            self.file.write(
                "\t<hullBust>" + str(self.hullBust) + "</hullBust>\n")
        # since cooldown is a float, needs to round
        if self.cooldown < 10:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 2)) +
                            "</cooldown>\n")
        else:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 1)) +
                            "</cooldown>\n")
        # round since float
        self.file.write("\t<power>" + str(round(self.power)) + "</power>\n")
        # round cost since float. makes for more accurate prices
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("\t<image>" + self.image + "</image>\n")
        if self.boost_true:
            self.file.write("\t<boost>\n")
            self.file.write("\t\t<type>" + self.boost[0] + "</type>\n")
            self.file.write("\t\t<amount>" + str(round(self.boost[1], 3)) +
                            "</amount>\n")
            self.file.write("\t\t<count>" + str(self.boost[2]) + "</count>\n")
            self.file.write("\t</boost>\n")
        if self.explosion_true:
            self.file.write(
                "\t<explosion>" + self.explosion + "</explosion>\n")
        if self.chargeLevels_true:
            self.file.write("\t<chargeLevels>" + str(self.chargeLevels) +
                            "</chargeLevels>\n")
        self.file.write("\t<launchSounds>\n")
        for sound in self.launchSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</launchSounds>\n")
        self.file.write("\t<hitShipSounds>\n")
        for sound in self.hitShipSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShipSounds>\n")
        self.file.write("\t<hitShieldSounds>\n")
        for sound in self.hitShieldSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShieldSounds>\n")
        self.file.write("\t<missSounds>\n")
        for sound in self.missSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</missSounds>\n")
        self.file.write("\t<weaponArt>" + self.weaponArt + "</weaponArt>\n")
        self.file.write("</weaponBlueprint>\n")

    # change Laser to Burst
    def _load_burst(self, temp_burst):
        """ Loads all of this Laser's relevant attributes, if applicable,
        into temp_burst.
        
        :param Burst temp_burst:
        :rtype: None 
        """
        # general stuff
        temp_burst.name = self.name
        if self.flavorType_true:
            temp_burst.flavorType_true = True
            temp_burst.flavorType = self.flavorType
        if self.tip_true:
            temp_burst.tip_true = True
            temp_burst.tip = self.tip
        temp_burst.title, temp_burst.title2 = self.title, self.title2
        temp_burst.short = self.short
        temp_burst.desc = self.desc
        temp_burst.tooltip = self.tooltip
        if self.ion_true:
            temp_burst.ion_true = self.ion_true
            temp_burst.ion = self.ion
        if self.damage_true:
            temp_burst.damage_true = True
            temp_burst.damage = self.damage
        if self.sysDamage_true:
            temp_burst.sysDamage_true = True
            temp_burst.sysDamage = self.sysDamage
        if self.persDamage_true:
            temp_burst.persDamage_true = True
            temp_burst.persDamage = self.sysDamage
        if self.fireChance_true:
            temp_burst.fireChance_true = True
            temp_burst.fireChance = self.fireChance
        if self.breachChance_true:
            temp_burst.breachChance_true = True
            temp_burst.breachChance = self.breachChance
        if self.stunChance_true:
            temp_burst.stunChance_true = True
            temp_burst.stunChance = self.stunChance
        if self.stun_true:
            temp_burst.stun_true = True
            temp_burst.stun = self.stun
        temp_burst.cooldown = self.cooldown
        temp_burst.power = self.power
        temp_burst.cost = self.cost
        temp_burst.rarity = self.rarity
        temp_burst.bp = self.bp
        temp_burst.weaponArt = self.weaponArt
        for sound in self.launchSounds:
            temp_burst.launchSounds.append(sound)
        if self.hullBust_true:
            temp_burst.hullBust_true = True
            temp_burst.hullBust = self.hullBust
        if self.lockdown_true:
            temp_burst.lockdown_true = True
            temp_burst.lockdown = self.lockdown
        if self.boost_true:
            temp_burst.boost_true = True
            for b in self.boost:
                temp_burst.boost.append(b)
        # laser specific stuff
        temp_burst.speed = self.speed
        temp_burst.sp = self.sp
        if self.missiles_true:
            temp_burst.missiles_true = True
            temp_burst.missiles = self.missiles
        for sound in self.hitShipSounds:
            temp_burst.hitShipSounds.append(sound)
        for sound in self.hitShieldSounds:
            temp_burst.hitShieldSounds.append(sound)
        for sound in self.missSounds:
            temp_burst.missSounds.append(sound)
        if self.explosion_true:
            temp_burst.explosion_true = True
            temp_burst.explosion = self.explosion
        if self.droneTargetable_none:
            temp_burst.droneTargetable_none = True
        elif self.droneTargetable_true:
            temp_burst.droneTargetable_true = True
            temp_burst.droneTargetable = self.droneTargetable
        if self.chargeLevels_true:
            temp_burst.chargeLevels_true = True
            temp_burst.chargeLevels = self.chargeLevels

    def ce_uncalibrated(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if max_shots < 2:
            burst = Burst(self.file)
            self._load_burst(burst)
            burst.name += "_UNCALIBRATED"
            burst.title = "Uncalib. " + burst.title
            if len(burst.title) > 27:
                burst.title = "Uncal. " + burst.title2
            if len(burst.title) > 27:
                burst.title = "Unc. " + burst.title2
            burst.short = "unc " + burst.short
            burst.desc += " Its uncalibrated sensors make targeting " \
                          "smaller rooms difficult."
            # is +30 correct? is default 17.5 correct?
            burst.radius += 30
            # projectile[i] int, str, str
            burst.projectiles.append([1, "false", self.image])
            burst.cost *= 0.9
            burst.weaponArt += "_slight_desat"

            burst.generate_weapon()

    def ce_unreliable(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if max_shots < 2:
            burst = Burst(self.file)
            self._load_burst(burst)
            burst.name += "_UNRELIABLE"
            burst.title = "Unrel. " + burst.title
            if len(burst.title) > 27:
                burst.title = "Unr. " + burst.title2
            burst.short = "unr " + burst.short
            burst.desc += " Its worn out sensors make targeting unreliable."
            # is +45 correct? is default 17.5 correct?
            burst.radius += 45
            # projectile[i] int, str, str
            burst.projectiles.append([1, "false", self.image])
            burst.cost *= 0.7
            burst.weaponArt += "_dirty"

            burst.generate_weapon()

    def ce_wild(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if max_shots < 2 and self.damage > 0 and self.hullBust < 1:
            burst = Burst(self.file)
            self._load_burst(burst)
            burst.name += "_WILD"
            burst.title = "Wild " + burst.title
            burst.short = "Wi " + burst.short
            burst.desc += " Its sensors couldn't handle the damage increase " \
                          "and broke, making aiming quite difficult."
            burst.damage += 1
            burst.radius += 70
            burst.projectiles.append([1, "false", self.image])
            burst.cost *= 0.7
            burst.weaponArt += "_gritty"

            burst.generate_weapon()

    def ce_suppression(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if max_shots < 2 and self.cooldown < 15:
            burst = Burst(self.file)
            self._load_burst(burst)
            burst.name += "_SUPPRESSION"
            burst.title = "Suppres. " + burst.title
            if len(self.title) > 27:
                self.title = "Supp. " + burst.title2
            burst.short = "Sup " + burst.short
            burst.desc += " Sports a quick cooldown for suppressive fire " \
                          "but is hard to aim."
            burst.cooldown *= 0.70
            if burst.boost_true and burst.boost[0] == "cooldown":
                burst.boost[1] *= 0.70
            burst.radius += 45
            burst.projectiles.append([1, "false", self.image])
            burst.cost *= 0.5
            burst.weaponArt += "_high_tech"

            burst.generate_weapon()

    # to pierce or not to pierce?
    def ce_piercing(self):
        if self.sp < 1 and self.ion < 1 and self.missiles < 1:
            self.name += "_PIERCING"
            self.title = "Piercing " + self.title
            if len(self.title) > 27:
                self.title = "Pierce " + self.title2
            self.short = "P " + self.short
            self.desc += " (Rare) Pierces one more shield bubble."
            self.sp += 1
            self.cost *= 1.5
            self.weaponArt += "_old"
            self.image += "_green"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_low_energy(self):
        if self.sp > 0 and self.ion < 1 and self.missiles < 1:
            self.name += "_LOW_ENERGY"
            self.title = "Low Energy " + self.title
            if len(self.title) > 27:
                self.title = "Low NRG " + self.title2
            self.short = "le " + self.short
            self.desc += " Pierces one less shield bubble."
            self.sp -= 1
            self.cost *= 0.75
            self.weaponArt += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    # support or assault?
    def ce_support_laser(self):
        if self.shots > 2 and self.missiles < 1:
            self.name += "_SUPPORT_LASER"
            self.title = "Support " + self.title
            self.short = "Sup " + self.short
            self.desc += " Support: cooldown x0.6 projectiles -1"
            self.cooldown *= 0.6
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.6
            self.shots -= 1
            self.cost *= 1.1
            self.weaponArt += "_high_tech"

            self.generate_weapon()
            self.revert_weapon()

    def ce_assault_laser(self):
        if self.power < 4 and self.missiles < 1:
            self.name += "_ASSAULT_LASER"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += " Assault: cooldown x0.75 power cost +1"
            self.cooldown *= 0.75
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.75
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    # rip support variation
    def ce_assault_missiles(self):
        if self.missiles > 0 and self.power < 4:
            self.name += "_ASSAULT_MISSILES"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += " Assault: cooldown x0.75 power cost +1"
            self.cooldown *= 0.75
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_stalker(self):
        if self.power < 4:
            self.name += "_STALKER"
            self.title = "Stalking " + self.title
            if len(self.title) > 27:
                self.title = "Stalk. " + self.title2
            self.short = "St " + self.short
            self.desc += " Stalking: " \
                         "cooldown x0.70 projectile speed x0.4 power cost +1"
            self.cooldown *= 0.7
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.7
            self.speed *= 0.4
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_tactical(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if self.damage > 0 and max_shots < 4:
            self.name += "_TACTICAL"
            self.title = "Tactical " + self.title
            if len(self.title) > 27:
                self.title = "Tact. " + self.title2
            self.short = "Ta " + self.short
            self.desc += " Tactical: damage -1 system damage +2"
            self.damage -= 1
            self.sysDamage_true = True
            self.sysDamage += 2
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_brutal(self):
        if self.damage > 0:
            self.name += "_BRUTAL"
            self.title = "Brutal " + self.title
            if len(self.title) > 27:
                self.title = "Brut. " + self.title2
            self.short = "BR " + self.short
            self.desc += " Packs a punch."
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.breachChance_true = True
            self.breachChance += 1
            if self.breachChance > 10:
                self.breachChance = 10
            self.persDamage_true = True
            self.persDamage += 1
            self.stunChance_true = True
            self.stunChance += 1
            if self.stunChance > 10:
                self.stunChance = 10
            self.cost *= 1.3
            self.weaponArt += "_dirty_steel"
            self.image += "_dark"

            self.generate_weapon()
            self.revert_weapon()

    def ce_weaksauce(self):
        if self.damage > 0:
            self.name += "_WEAKSAUCE"
            self.title = "Weaksauce " + self.title
            if len(self.title) > 27:
                self.title = "Weak " + self.title2
            self.short = "weak " + self.short
            self.desc += " Makes your enemy laugh at you."
            self.cooldown *= 1.1
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.1
            self.breachChance -= 1
            if self.breachChance < 0:
                self.breachChance = 0
            self.persDamage -= 1
            self.stunChance -= 1
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    def ce_hull_ripper(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if (self.damage > 0 and self.hullBust < 1 and
                self.ion < 1 and max_shots < 4):
            self.name += "_HULL_RIPPER"
            self.title = "Hull Ripper " + self.title
            if len(self.title) > 27:
                self.title = "Ripper " + self.title2
            self.short = "HR " + self.short
            self.desc += " Deals double hull damage to systemless rooms."
            self.hullBust_true = True
            self.hullBust = 1
            self.cost *= 1.25
            self.weaponArt += "_green"
            self.image += "_green"

            self.generate_weapon()
            self.revert_weapon()

    def ce_reconfigured(self):
        if self.hullBust > 0:
            self.name += "_RECONFIGURED"
            self.title = "Reconfigured " + self.title
            if len(self.title) > 27:
                self.title = "Reconf. " + self.title2
            self.short = "r " + self.short
            self.desc += \
                " Reconfigured: deals normal damage to systemless rooms"
            self.hullBust_true = False
            self.hullBust = 0
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    def ce_repeater(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if (self.ion < 1 and not self.missiles_true and
                max_shots < 2 and self.damage < 4 and
                not ("LASER_CHAINGUN_2" in self.name or
                     "BA_LASER_LIGHT_CHAINGUN" in self.name)):
            self.name += "_REPEATER"
            self.title = "Repeater " + self.title
            if len(self.title) > 27:
                self.title = "Rep. " + self.title2
            self.short = "RE " + self.short
            self.desc += " Its energy coil is optimized to generate " \
                         "another projectile, but needs time."
            self.shots += 1
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.cost *= 1.3
            self.weaponArt += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_repeater_heavy_ion(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if self.ion > 1 and max_shots < 2:
            self.name += "_REPEATER_HEAVY_ION"
            self.title = "Repeater " + self.title
            if len(self.title) > 27:
                self.title = "Rep. " + self.title2
            self.short = "RE " + self.short
            self.desc += " Its energy coil is optimized to generate " \
                         "another projectile, but needs time."
            self.shots += 1
            self.cooldown *= 1.75
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.75
            self.cost *= 1.3
            self.weaponArt += "_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_gatling(self):
        if (self.ion < 1 and self.missiles < 1 and self.shots > 2 and
                not ("LASER_CHAINGUN_2" in self.name or
                     "BA_LASER_LIGHT_CHAINGUN" in self.name)):
            self.name += "_GATLING"
            self.title = "Gatling " + self.title
            if len(self.title) > 27:
                self.title = "Gatl. " + self.title2
            self.short = "GAT " + self.short
            self.desc += " Gatling (Rare): projectiles +2 cooldown x2"
            self.shots += 2
            self.cooldown *= 2
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 2
            self.cost *= 1.4
            self.weaponArt += "_high_tech"
            self.image += "_high_tech"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_starlord(self):
        if (self.ion < 1 and self.missiles < 1 and self.shots > 1 and
                self.damage == 1 and self.hullBust < 1):
            self.name += "_STARLORD"
            self.title = "Starlord " + self.title
            if len(self.title) > 27:
                self.title = "Starl. " + self.title2
            self.short = "STAR " + self.short
            self.desc += " Starlord (Epic): projectiles +1 cooldown x0.9"
            self.shots += 1
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.cost *= 1.5
            self.weaponArt += "_ht_steel_bright"
            self.image += "_high_tech"
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_deathcharge(self):
        # chargeLevels is OK since it would be Heavy Charger
        if self.shots == 1 and self.power < 4 and self.damage > 1:
            self.name += "_DEATHCHARGE"
            self.title = "Deathch. " + self.title
            if len(self.title) > 27:
                self.title = "Death. " + self.title2
            self.short = "Dth " + self.short
            self.desc += " Deathcharge: crew damage +2, power cost +1"
            self.cost *= 1.2
            self.power += 1
            self.persDamage_true = True
            self.persDamage += 2
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_badass(self):
        if (self.ion < 1 and self.missiles < 1 and self.damage > 1 and
                self.hullBust < 1 and "LASER_CHAINGUN_2" not in self.name):
            self.name += "_BADASS"
            self.title = "Badass " + self.title
            self.short = "BAD " + self.short
            self.desc += " Badass (Epic): " \
                         "damage +1, breach chance +1, fire chance +1"
            self.damage += 1
            self.breachChance_true = True
            self.breachChance += 1
            if self.breachChance > 10:
                self.breachChance = 10
            self.fireChance_true = True
            self.fireChance += 1
            if self.fireChance > 10:
                self.fireChance = 10
            self.cost *= 1.5
            self.weaponArt += "_gritty"
            self.image += "_red"
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_massive(self):
        # chargeLevels is OK since it would be Heavy Charger
        if self.shots == 1 and self.damage > 1:
            self.name += "_MASSIVE"
            self.title = "Massive " + self.title
            self.short = "M " + self.short
            self.desc += " Massive: damage +1 cooldown x1.5"
            self.cost *= 1.4
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.damage += 1
            self.weaponArt += "_gritty"
            self.image += "_green"
            self.generate_weapon()
            self.revert_weapon()

    def ce_malfunctioning(self):
        if self.shots > 1:
            self.name += "_MALFUNCTIONING"
            self.title = "Malfunc. " + self.title
            if len(self.title) > 27:
                self.title = "Mlfc. " + self.title2
            self.short = "mal " + self.short
            self.desc += " Unable to fire one of its projectiles due " \
                         "to a malfunction in its energy coil."
            self.shots -= 1
            self.cost *= 0.75
            self.weaponArt += "_dirty"
            self.generate_weapon()
            self.revert_weapon()
        elif self.shots == 1 and self.chargeLevels > 1:
            self.name += "_MALFUNCTIONING"
            self.title = "Malfunc. " + self.title
            if len(self.title) > 27:
                self.title = "Mlfc. " + self.title2
            self.short = "mal " + self.short
            self.desc += " Unable to fire one of its projectiles due " \
                         "to a malfunction in its energy coil."
            self.chargeLevels -= 1
            self.cost *= 0.75
            self.weaponArt += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_damaged(self):
        if self.shots > 2:
            self.name += "_DAMAGED"
            self.title = "Damaged " + self.title
            if len(self.title) > 27:
                self.title = "Dam. " + self.title2
            self.short = "dam " + self.short
            self.desc += " Unable to fire two of its projectiles due " \
                         "to a damaged energy coil."
            self.shots -= 2
            self.cost *= 0.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()
        elif self.shots == 1 and self.chargeLevels > 2:
            self.name += "_DAMAGED"
            self.title = "Damaged " + self.title
            if len(self.title) > 27:
                self.title = "Dam. " + self.title2
            self.short = "dam " + self.short
            self.desc += " Unable to fire two of its projectiles due " \
                         "to a damaged energy coil."
            self.chargeLevels -= 2
            self.cost *= 0.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heavy(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if (self.ion < 1 and self.damage == 1 and self.hullBust < 1 and
                max_shots < 4 and self.power < 4):
            self.name += "_HEAVY"
            self.title = "Heavy " + self.title
            self.short = "H " + self.short
            self.desc += " Heavy: damage +1 cooldown x1.5 power cost +1"
            self.damage += 1
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.power += 1
            self.cost *= 1.4
            self.weaponArt += "_old"
            self.generate_weapon()
            self.revert_weapon()

    def ce_light(self):
        if self.ion < 1 and self.damage > 2:
            self.name += "_LIGHT"
            self.title = "Light " + self.title
            self.short = "l " + self.short
            self.desc += " Light: damage -1 cooldown x0.9"
            self.damage -= 1
            # catch for mines
            if self.sysDamage < 0:
                self.sysDamage += 1
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_substandard(self):
        self.name += "_SUBSTANDARD"
        self.title = "Substandard " + self.title
        if len(self.title) > 27:
            self.title = "Subst. " + self.title2
        self.short = "sub " + self.short
        # self.desc += " Overall performance is substandard."
        # this doesn't really say much...
        self.desc += " Substandard: overall bad stats"
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.speed *= 0.9
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 1
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.8
        self.weaponArt += "_slight_desat"
        self.generate_weapon()
        self.revert_weapon()

    def ce_surplus(self):
        self.name += "_SURPLUS"
        self.title = "Surplus " + self.title
        self.short = "sur " + self.short
        self.desc += " Surplus: overall very bad stats"
        self.cooldown *= 1.2
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.2
        self.speed *= 0.8
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 3
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.5
        self.weaponArt += "_heavy_desat"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_quality(self):
        self.name += "_QUALITY"
        self.title = "Quality " + self.title
        self.short = "Q " + self.short
        self.desc += " Quality: overall better stats"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.speed *= 1.1
        self.cost *= 1.25
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_custom(self):
        self.name += "_CUSTOM"
        self.title = "Custom " + self.title
        self.short = "C " + self.short
        self.desc += " Custom (Rare): overall great stats"
        self.cooldown *= 0.8
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.8
        self.speed *= 1.2
        self.fireChance_true = True
        self.fireChance += 1
        if self.fireChance > 10:
            self.fireChance = 10
        self.breachChance_true = True
        self.breachChance += 1
        if self.breachChance > 10:
            self.breachChance = 10
        self.stunChance_true = True
        self.stunChance += 1
        if self.stunChance > 10:
            self.stunChance = 10
        self.cost *= 1.5
        self.weaponArt += "_ht_steel_bright"
        self.image += "_high_tech"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_vintage(self):
        self.name += "_VINTAGE"
        self.title = "Vintage " + self.title
        if len(self.title) > 27:
            self.title = "Vint. " + self.title2
        self.short = "Vin " + self.short
        self.desc += " Vintage: overall bad stats but valuable and rare"
        self.speed *= 0.9
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.cost *= 1.5
        if self.rarity > 0:
            self.rarity += 2
            if self.rarity > 5:
                self.rarity = 5
        self.weaponArt += "_gritty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_antique(self):
        self.name += "_ANTIQUE"
        self.title = "Antique " + self.title
        if len(self.title) > 27:
            self.title = "Anti. " + self.title2
        self.short = "Ant " + self.short
        self.desc += " Antique: overall very bad stats but " \
                     "very valuable and rare"
        self.speed *= 0.7
        self.cooldown *= 1.4
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.4
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        if self.rarity > 0:
            self.rarity += 4
            if self.rarity > 5:
                self.rarity = 5
        self.cost *= 2
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc += " Swag (Rare): good for showing off"
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_gold"
            self.generate_weapon()
            self.revert_weapon()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Secondhand " + self.title
        if len(self.title) > 27:
            self.title = "Sec. Hand " + self.title2
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_weapon()
        self.revert_weapon()

    # power-only
    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.weaponArt += "_dirty"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_optimized(self):
        if self.power > 2:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            if len(self.title) > 27:
                self.title = "Optim. " + self.title2
            if len(self.title) > 27:
                self.title = "Opt. " + self.title2
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.weaponArt += "_ht_steel"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # cooldown-only
    def ce_outdated(self):
        # every weapon has a cooldown
        self.cooldown *= 1.15
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.15
        self.name += "_OUTDATED"
        # self.desc += (" Drags on with a sub-par reload time.")
        self.desc += " Recharges slightly slower."
        self.title = "Outdated " + self.title
        if len(self.title) > 27:
            self.title = "Outd. " + self.title2
        self.short = "ou " + self.short
        self.cost *= 0.8
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_obsolete(self):
        # every weapon has a cooldown
        self.cooldown *= 1.25
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.25
        self.name += "_OBSOLETE"
        self.desc += " Recharges slower."
        self.title = "Obsolete " + self.title
        if len(self.title) > 27:
            self.title = "Obsol. " + self.title2
        self.short = "ob " + self.short
        self.cost *= 0.6
        self.weaponArt += "_rust"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_upgraded(self):
        # every weapon has a cooldown
        self.cooldown *= 0.85
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.85
        self.name += "_UPGRADED"
        self.desc += " Recharges slightly faster."
        self.title = "Upgraded " + self.title
        if len(self.title) > 27:
            self.title = "Upgr. " + self.title2
        self.short = "UP " + self.short
        self.cost *= 1.2
        self.weaponArt += "_high_tech"

        self.generate_weapon()
        self.revert_weapon()

    def ce_advanced(self):
        # every weapon has a cooldown
        self.cooldown *= 0.75
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.75
        self.name += "_ADVANCED"
        self.desc += " (Rare) Recharges faster."
        self.title = "Advanced " + self.title
        if len(self.title) > 27:
            self.title = "Adv. " + self.title2
        self.short = "AD " + self.short
        self.cost *= 1.4
        self.weaponArt += "_ht_steel_bright"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_quickshot(self):
        self.name += "_QUICKSHOT"
        self.title = "Quickshot " + self.title
        if len(self.title) > 27:
            self.title = "Quick. " + self.title2
        self.short = "QU " + self.short
        self.desc += " Quickshot: cooldown x0.90 projectile speed x2"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.cost *= 1.2
        self.speed *= 2
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    # give this a better name
    def ce_widespread(self):
        if (self.ion < 1 and self.damage > 0 and self.speed > 40 and
                self.sysDamage != -self.damage):
            self.name += "_WIDESPREAD"
            self.title = "Wide Sp. " + self.title
            self.short = "wid " + self.short
            self.desc += " Wide Spread: system damage -1"
            self.sysDamage_true = True
            self.sysDamage -= 1
            self.cost *= 0.75
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    # give this a better name
    def ce_tightspread(self):
        if (self.ion < 1 and self.damage > 0 and self.speed > 40 and
                self.sysDamage != -self.damage):
            self.name += "_TIGHTSPREAD"
            self.title = "Tight Sp. " + self.title
            self.short = "TIG " + self.short
            self.desc += " Tight Spread: system damage +1"
            self.sysDamage_true = True
            self.sysDamage += 1
            self.cost *= 1.25
            self.weaponArt += "_dirty_steel"
            self.image += "_green"

            self.generate_weapon()
            self.revert_weapon()

    def ce_impacting(self):
        if self.breachChance < 10 and self.stunChance > 0 and self.ion < 1:
            self.name += "_IMPACTING"
            self.title = "Impacting " + self.title
            if len(self.title) > 27:
                self.title = "Impact. " + self.title2
            self.short = "IM " + self.short
            self.desc += " Impact: breach chance +1 stun chance +1"
            # must already have a stun chance, no need to set it
            if self.stunChance < 10:
                self.stunChance += 1
            self.breachChance_true = True
            # since breachChance must already be less than 10 no need to check
            self.breachChance += 1
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_penetrating(self):
        if self.ion < 1 and self.breachChance < 10:
            self.name += "_PENETRATING"
            self.title = "Penetr. " + self.title
            self.short = "PE " + self.short
            self.desc += " Penetrating: " \
                         "breach chance +1 projectile speed x1.10"
            self.speed *= 1.1
            # breachChance must be 9 or less
            self.breachChance += 1
            self.breachChance_true = True
            self.cost *= 1.2
            self.weaponArt += "_dirty_steel"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_breaching(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if self.ion < 1 and self.breachChance < 9 and max_shots < 3:
            self.name += "_BREACHING"
            self.title = "Breaching " + self.title
            if len(self.title) > 27:
                self.title = "Breach. " + self.title2
            self.short = "BR " + self.short
            self.desc += " Breaching (Rare): " \
                         "breach chance +2 projectile speed x1.30"
            self.speed *= 1.3
            # breachChance must be 8 or less
            self.breachChance += 2
            self.breachChance_true = True
            self.cost *= 1.4
            self.weaponArt += "_steel"
            self.image += "_dark"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_photon(self):
        max_shots = self.shots
        if self.chargeLevels_true:
            max_shots *= self.chargeLevels
        if self.ion < 1 and max_shots < 3 and self.missiles < 1:
            self.name += "_PHOTON"
            self.title = "Photon " + self.title
            if len(self.title) > 27:
                self.title = "Phot. " + self.title2
            self.short = "Ph " + self.short
            if self.shots == 1:
                self.desc += " Fires a pulse of pure light capable of " \
                             "faster travel speed with increased " \
                             "ignition chance, but is unable to breach."
            else:
                self.desc += " Fires pulses of pure light capable of " \
                             "faster travel speed with increased " \
                             "ignition chance, but are unable to breach."
            self.speed *= 4
            self.breachChance *= 0
            self.fireChance += 2
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowmass(self):
        if self.ion < 1 and self.breachChance > 1:
            self.name += "_LOWMASS"
            self.title = "Low Mass " + self.title
            self.short = "lma " + self.short
            self.desc += " Low Mass: breach chance -2 projectile speed x0.9"
            self.speed *= 0.9
            # breachChance must be at least 2
            self.breachChance -= 2
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # ~~changed req to need two higher breach chance than above
    def ce_lowmomentum(self):
        if self.ion < 1 and self.breachChance > 3:
            self.name += "_LOWMOMENTUM"
            self.title = "Low Momentum " + self.title
            if len(self.title) > 27:
                self.title = "Low Mom. " + self.title2
            self.short = "lmo " + self.short
            self.desc += " Low Momentum: " \
                         "breach chance -4 projectile speed x0.7"
            self.speed *= 0.7
            # breachChance must be at least 4
            self.breachChance -= 4
            self.cost *= 0.6
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # fire
    def ce_incendiary(self):
        if self.fireChance < 7:
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_INCENDIARY"
            self.desc += " A bit more likely to start a fire."
            self.title = "Incendiary " + self.title
            if len(self.title) > 27:
                self.title = "Incend. " + self.title2
            self.short = "IN " + self.short
            self.cost *= 1.2
            self.image += "_red"
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_plasma(self):
        if self.fireChance < 7:
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 2
            self.name += "_PLASMA"
            self.desc += " (Rare) Imbued with plasma, this weapon's more " \
                         "likely to start a fire."
            self.title = "Plasma " + self.title
            self.short = "PL " + self.short
            self.cost *= 1.3
            self.image += "_red"
            self.weaponArt += "_red"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_insulated(self):
        if self.ion < 1 and self.fireChance > 1:
            self.fireChance -= 1
            self.name += "_INSULATED"
            self.title = "Insulated " + self.title
            if len(self.title) > 27:
                self.title = "Insul. " + self.title2
            self.short = "in " + self.short
            self.desc += " Insulated: fire chance -1"
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heatshielded(self):
        if self.ion < 1 and self.fireChance > 4:
            self.fireChance -= 3
            self.name += "_HEATSHIELDED"
            self.title = "Heatshielded " + self.title
            if len(self.title) > 27:
                self.title = "Heatsh. " + self.title2
            self.short = "hea " + self.short
            self.desc += " Heatshielded: fire chance -3"
            self.cost *= 0.7
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # crew-damage only
    def ce_radioactive(self):
        # need to make it true when increasing, but not when decreasing
        self.persDamage_true = True
        self.persDamage += 1
        self.name += "_RADIOACTIVE"
        self.desc += " Radioactive elements make it deadlier to crew."
        self.title = "Radioactive " + self.title
        if len(self.title) > 27:
            self.title = "Rad. " + self.title2
        self.short = "RAD " + self.short
        self.cost *= 1.2
        self.weaponArt += "_yellow"
        self.image += "_yellow"
        self.generate_weapon()
        self.revert_weapon()

    def ce_safe_nonlethal(self):
        # e.g. light scatter lasers?
            # negative persDamage values are not okay since that means
            # crew heal shenanigans since damage is less than 1
        if (self.ion < 1 and self.damage < 1 and self.persDamage > 0 and
                not ("BA_LASER_LIGHT_AUTO" in self.name or
                     "BA_LASER_LIGHT_CHAINGUN" in self.name or
                     "BA_LASER_LIGHT_1" in self.name or
                     "BA_LASER_LIGHT_2" in self.name or
                     "BA_LASER_LIGHT_3" in self.name)):
            self.persDamage -= 1
            self.name += "_SAFE_NONLETHAL"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.persDamage == 0:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe(self):
        # clause added to avoid crew heal shenanigans
        if (self.ion < 1 and self.damage > 0 and
                self.persDamage != -self.damage and
                not ("BA_LASER_LIGHT_AUTO" in self.name or
                     "BA_LASER_LIGHT_CHAINGUN" in self.name or
                     "BA_LASER_LIGHT_1" in self.name or
                     "BA_LASER_LIGHT_2" in self.name or
                     "BA_LASER_LIGHT_3" in self.name)):
            # since damage is at least 1, persDamage tag must be added
            self.persDamage_true = True
            self.persDamage -= 1
            # since damage is at least 1, persDamage will cancel out some crew
            # damage done just by regular damage, so negative values are okay
            self.name += "_SAFE"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.damage == 1:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_volatile(self):
        # if fire chance is already 10, then radioactive does the same thing
        if self.fireChance < 10:
            # adds a persDamage tag if one doesn't already exist
            self.persDamage_true = True
            self.persDamage += 1
            # same for fireChance
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_VOLATILE"
            self.title = "Volatile " + self.title
            if len(self.title) > 27:
                self.title = "Volat. " + self.title2
            self.short = "VOL " + self.short
            self.desc += " Releases volatile chemicals on impact."
            self.cost *= 1.3
            self.weaponArt += "_dirty"
            self.image += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_deathly(self):
        if self.persDamage > 0:
            self.persDamage *= 2
            self.name += "_DEATHLY"
            self.title = "Deathly " + self.title
            self.short = "DEA " + self.short
            self.desc += " Deathly (Epic): crew damage x2"
            self.cost *= 1.5
            self.weaponArt += "_dirty_steel"
            self.image += "_dark"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_pulse(self):
        max_shots = self.shots
        if (self.chargeLevels_true and
                "BA_LASER_CHARGEGUN_HEAVY" not in self.name):
                max_shots *= self.chargeLevels
        if self.damage > 0 and max_shots < 2 and self.sp < 1:
            self.name += "_PULSE"
            self.title = "Pulse " + self.title
            if len(self.title) > 27:
                self.title = "Pul. " + self.title2
            self.short = "PUL " + self.short
            self.desc += " Pulse:  ion damage +1, cooldown x1.5"
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.ion += 1
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heavy_ion(self):
        if self.ion == 1 and self.shots < 4:
            self.name += "_HEAVY_ION"
            self.title = "Heavy " + self.title
            self.short = "H " + self.short
            self.desc += " Heavy: ion damage +1 cooldown x1.7"
            self.cooldown *= 1.7
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.7
            self.ion += 1
            self.cost *= 1.4
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_perfect(self):
        if self.ion == 1 and self.power > 1:
            self.name += "_PERFECT"
            self.title = "Perfect " + self.title
            if len(self.title) > 27:
                self.title = "Perf. " + self.title2
            self.short = "PER " + self.short
            self.desc += " Perfect (Epic): power cost -1, cooldown x0.8"
            self.cooldown *= 0.8
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.8
            self.power -= 1
            self.cost *= 1.5
            self.weaponArt += "_ht_steel_bright"
            self.image += "heavy_desat"
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_overcharged(self):
        if self.shots < 3 and self.power < 4 and self.ion > 1:
            self.ion += 2
            self.power += 1
            self.name += "_OVERCHARGED"
            self.title = "Overcharg. " + self.title
            if len(self.title) > 27:
                self.title = "Overch. " + self.title2
            self.short = "OV " + self.short
            self.desc += " Overcharged: ion damage +1 power cost +1"
            self.cost *= 1.4
            self.weaponArt += "_ht_steel_bright"
            self.image += "_high"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowcharge(self):
        if self.ion > 1:
            self.ion -= 1
            self.name += "_LOWCHARGE"
            self.title = "Low Charge " + self.title
            if len(self.title) > 27:
                self.title = "Low Ch. " + self.title2
            self.short = "lwc " + self.short
            self.desc += " Low Charge: ion damage -1"
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_unstable(self):
        if self.ion > 1:
            self.ion -= 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.name += "_UNSTABLE"
            self.title = "Unstable " + self.title
            if len(self.title) > 27:
                self.title = "Unsta. " + self.title2
            self.short = "Un " + self.short
            self.desc += " Unstable: ion damage -1 system damage +1"
            self.cost *= 0.8
            self.weaponArt += "_purple"
            self.image += "_purple"
            self.generate_weapon()
            self.revert_weapon()

    def ce_flux(self):
        if self.ion > 1:
            self.ion -= 1
            self.stunChance_true = True
            self.stunChance += 3
            if self.stunChance > 10:
                self.stunChance = 10
            self.fireChance_true = True
            self.fireChance += 3
            if self.fireChance > 10:
                self.fireChance = 10
            self.name += "_FLUX"
            self.title = "Flux " + self.title
            self.short = "Fl " + self.short
            self.desc += " Flux: ion damage -1 stun chance +3 fire chance +3"
            self.cost *= 1.1
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    # ~~changed cooldown mult. from 1.6 to 1.5
    def ce_warping(self):
        if self.ion == 1 and self.shots < 3 and self.sp < 1:
            self.sp += 1
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.name += "_WARPING"
            self.title = "Warping " + self.title
            if len(self.title) > 27:
                self.title = "Warp. " + self.title2
            self.short = "Wr " + self.short
            self.desc += " Warps through one shield bubble but takes " \
                         "longer to fire."
            self.cost *= 1.3
            self.weaponArt += "_ht_steel"
            self.image += "_heavy_desat"
            self.generate_weapon()
            self.revert_weapon()

    # ~~changed cooldown mult. from 1.8 to 1.75
    def ce_phasing(self):
        if self.ion == 1 and self.shots < 3 and self.sp < 1:
            self.sp += 3
            self.cooldown *= 1.75
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.75
            self.name += "_PHASING"
            self.title = "Phasing " + self.title
            if len(self.title) > 27:
                self.title = "Phas. " + self.title2
            self.short = "Ph " + self.short
            self.desc += " Phasing (Rare): phases through three " \
                         "shield bubbles cooldown x1.75"
            self.cost *= 1.5
            self.weaponArt += "_ht_steel_bright"
            self.image += "_high_tech"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_untuned(self):
        if self.ion == 1 and self.shots < 3 and self.sp > 4:
            self.sp = 3
            self.name += "_UNTUNED"
            self.title = "Untuned " + self.title
            if len(self.title) > 27:
                self.title = "Untun. " + self.title2
            self.short = "un " + self.short
            self.desc += " Untuned: only phases through three shield bubbles"
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_replicator(self):
        if (self.missiles > 0 and self.cooldown > 8 and
                not ("BA_MISSILES_ASTERIA" in self.name)):
            self.name += "_REPLICATOR"
            self.title = "Replicator " + self.title
            if len(self.title) > 27:
                self.title = "Replic. " + self.title2
            if len(self.title) > 27:
                self.title = "Repl. " + self.title2
            self.short = "RE " + self.short
            self.desc += " (Rare) Given time it can replicate its own ammo."
            # yeah, x2 is too much breh, but how much less???
            self.cooldown *= 1.3
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.3
            self.missiles = 0
            # does the cost justify the benefit?
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_high_tech"
            self.image += "_heavy_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highyield(self):
        if (self.missiles > 0 and self.shots < 2 and
                self.damage > 1 and self.cooldown > 10 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_HIGHYIELD"
            self.title = "High Yield " + self.title
            if len(self.title) > 27:
                self.title = "HighY. " + self.title2
            self.short = "HY " + self.short
            self.desc += " (Rare) Does more damage at the cost of an " \
                         "additional missile."
            self.missiles += 1
            # check for mines
            if self.sysDamage < 0 and self.persDamage < 0:
                self.sysDamage -= 2
                self.persDamage -= 2
            self.damage += 2
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            # mines support these image suffixes, right? Right??
            self.weaponArt += "_steel"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_alpha(self):
        if (self.missiles > 0 and self.shots < 2 and
                self.damage > 1 and self.cooldown > 10 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_ALPHA"
            self.title = "Alpha " + self.title
            self.short = "AL " + self.short
            # gotta come up with an epic description...
            self.desc += " Alpha (Epic): cooldown x0.5, damage +1"
            # check for mines
            if self.sysDamage < 0 and self.persDamage < 0:
                self.sysDamage -= 1
                self.persDamage -= 1
            self.damage += 1
            self.cooldown /= 2
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] /= 2
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_ht_steel_bright"
            self.image += "_ht_steel_bright"
            self.generate_weapon()
            self.revert_weapon()

    def ce_scrambling(self):
        if (self.missiles > 0 and self.damage > 0 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_SCRAMBLING"
            self.title = "Scrambling " + self.title
            if len(self.title) > 27:
                self.title = "Scramble " + self.title2
            if len(self.title) > 27:
                self.title = "Scram. " + self.title2
            self.short = "SC " + self.short
            self.desc += " Scrambles enemy defense drone targeting, " \
                         "masking its trajectory."
            self.droneTargetable_true = False
            self.droneTargetable_none = True
            self.cost *= 1.3
            self.weaponArt += "_ht_steel_bright"
            self.image += "_ht_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_wasteful(self):
        if self.missiles > 0:
            self.name += "_WASTEFUL"
            self.title = "Wasteful " + self.title
            if len(self.title) > 27:
                self.title = "Wast. " + self.title2
            self.short = "was " + self.short
            self.desc += " Needs another missile due to a jammed loader."
            self.missiles += 1
            self.cost *= 0.5
            self.weaponArt += "_dirty"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_frail(self):
        if self.missiles > 0:
            self.name += "_FRAIL"
            self.title = "Frail " + self.title
            self.short = "fr " + self.short
            self.desc += " Frail: shield piercing -3"
            self.sp -= 3
            if self.sp < 0:
                self.sp = 0
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highvelocity(self):
        if self.missiles > 0:
            self.name += "_HIGHVELOCITY"
            self.title = "High Vel. " + self.title
            if len(self.title) > 27:
                self.title = "HighV. " + self.title2
            self.short = "HI " + self.short
            self.desc += " High Velocity: projectile speed x1.5"
            self.speed *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_gritty"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_boosted_missile(self):
        if self.missiles > 0 and self.shots < 3:
            self.name += "_BOOSTED_MISSILE"
            self.title = "Boosted " + self.title
            if len(self.title) > 27:
                self.title = "Boost. " + self.title2
            self.short = "BO " + self.short
            self.desc += " Boosted: projectile speed x2.5"
            self.speed *= 2.5
            self.cost *= 1.3
            self.weaponArt += "_gritty"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowvelocity(self):
        if self.missiles > 0:
            self.name += "_LOW_VELOCITY"
            self.title = "Low Vel. " + self.title
            if len(self.title) > 27:
                self.title = "LowV. " + self.title2
            self.short = "low " + self.short
            self.desc += " Low Velocity: projectile speed x0.6"
            self.speed *= 0.6
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_torpedo(self):
        # self.speed check for mines
        if (self.missiles > 0 and self.damage > 1 and
                self.damage >= 0 and self.cooldown > 10 and
                self.speed > 12 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_TORPEDO"
            self.title = "Torpedo " + self.title
            if len(self.title) > 27:
                self.title = "Torp. " + self.title2
            self.short = "TOR " + self.short
            self.desc += " Torpedo: damage +1, projectile speed x0.5"
            self.speed *= 0.5
            self.damage += 1
            self.cost *= 1.2
            self.weaponArt += "_steel"
            self.image += "_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp(self):
        if (self.missiles > 0 and self.shots < 2 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_EMP"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " EMP: ion damage +3 shield piercing -5"
            self.desc += " Its ion-wrapped missile deals hefty ion damage " \
                         "but is consequently unable to pierce through " \
                         "shields."
            self.ion += 3
            self.ion_true = True
            self.sp -= 5
            if self.sp < 0:
                self.sp = 0
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp_burst(self):
        if (self.missiles > 0 and self.shots > 1 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_EMP_BURST"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " Its ion-coated missiles deal some added " \
                         "ion damage but are consequently unable to " \
                         "pierce through shields."
            self.ion += 1
            self.ion_true = True
            self.sp -= 5
            if self.sp < 0:
                self.sp = 0
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_frag(self):
        if self.missiles > 0 and self.damage > 0:
            self.name += "_FRAG"
            self.title = "Frag " + self.title
            self.short = "Frag " + self.short
            self.desc += " Explodes into fragments upon impact, piercing " \
                         "systems and crew, at the cost of hull damage."
            self.damage -= 1
            self.persDamage_true = True
            self.persDamage += 2
            self.sysDamage_true = True
            self.sysDamage += 2
            self.cost *= 1.30
            self.weaponArt += "_gritty"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shredder(self):
        if (self.missiles > 0 and self.shots < 2 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_SHREDDER"
            self.title = "Shredder " + self.title
            if len(self.title) > 27:
                self.title = "Shred. " + self.title2
            self.short = "SHRE " + self.short
            self.desc += " (Rare) Enlaced spikes deal increased damage " \
                         "to systems and crew."
            self.persDamage_true = True
            self.persDamage += 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.cost *= 1.4
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_dirty_steel"
            self.image += "_dirty_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_caustic(self):
        # why exclude mines??
        if self.missiles > 0 and self.breachChance < 10:
            # makes sure the persDamage tag is there
            self.persDamage_true = True
            self.persDamage += 1
            # makes sure the breach tag is there
            self.breachChance_true = True
            self.breachChance += 1
            self.name += "_CAUSTIC"
            self.title = "Caustic " + self.title
            if len(self.title) > 27:
                self.title = "Caus. " + self.title2
            self.short = "CAU " + self.short
            self.desc += " Corrodes organic and inorganic matter alike."
            self.cost *= 1.2
            self.weaponArt += "_green"
            self.image += "_green"
            self.generate_weapon()
            self.revert_weapon()

    def ce_stungun(self):
        if 0 < self.stunChance < 8:
            self.name += "_STUNGUN"
            self.title = "Stun " + self.title
            self.short = "ST " + self.short
            self.desc += " Stun: stun chance +3"
            self.stunChance += 3
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shock(self):
        if 0 < self.stunChance < 6 and self.ion > 0:
            self.name += "_SHOCK"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun chance +5"
            self.stunChance += 5
            self.cost *= 1.3
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_regulated(self):
        if self.stunChance > 0:
            self.name += "_REGULATED"
            self.title = "Regulated " + self.title
            if len(self.title) > 27:
                self.title = "Regul. " + self.title2
            self.short = "reg " + self.short
            if 0 < self.stunChance < 3:
                self.desc += " Due to regulations, " \
                             "its ability to stun was removed."
            else:
                self.desc += " Less likely to stun due to regulations."
            self.stunChance -= 2
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_concussion(self):
        if self.missiles > 0 and self.ion < 1 and self.stun > 0:
            self.name += "_CONCUSSION"
            self.title = "Concussion " + self.title
            if len(self.title) > 27:
                self.title = "Concuss. " + self.title2
            self.short = "CO " + self.short
            self.desc += " Concussion: stun time x1.5"
            self.stun *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_predictable(self):
        if self.missiles > 0 and 0 < self.stun < 5:
            self.name += "_PREDICTABLE"
            self.title = "Predictable " + self.title
            if len(self.title) > 27:
                self.title = "Predict. " + self.title2
            self.short = "pr " + self.short
            self.desc += " Predictable: cannot stun"
            self.stun = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # having <stun> guarantees stun
    def ce_calibrated(self):
        if self.ion > 0 and self.stun > 4 and self.missiles < 1:
            self.name += "_CALIBRATED"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun time +2"
            self.stun += 2
            self.cost *= 1.2
            self.weaponArt += "_high_tech_2"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()


class Missile(Weapon2):
    def __init__(self, f):
        self.lockdown, self.lockdown_true = 0, False
        super().__init__(f)
        # check for speed_true only at creation
        self.speed, self.speed_true = 0, False
        self.shots = 0
        self.sp = 0
        self.missiles = 1
        self.hitShipSounds = []
        self.hitShieldSounds = []
        self.missSounds = []
        self.image, self.explosion = "", ""
        self.droneTargetable, self.droneTargetable_true = 2, False
        self.droneTargetable_none = False
        '''################### DUPLICATES FOR REVERTING ###################'''
        self.lockdown2, self.lockdown_true2 = 0, False
        # check for speed_true only at creation
        self.speed2, self.speed_true2 = 0, False
        self.shots2 = 0
        self.sp2 = 0
        self.missiles2 = 1
        self.hitShipSounds2 = []
        self.hitShieldSounds2 = []
        self.missSounds2 = []
        self.image2, self.explosion2 = "", ""
        self.droneTargetable2, self.droneTargetable_true2 = 2, False
        self.droneTargetable_none2 = False

    def revert_weapon(self):
        super().revert_weapon()
        self.lockdown, self.lockdown_true = self.lockdown2, self.lockdown_true2
        self.speed, self.speed_true = self.speed2, self.speed_true2
        self.shots = self.shots2
        self.sp = self.sp2
        self.missiles = self.missiles2
        self.hitShipSounds.clear()
        for sound in self.hitShipSounds2:
            self.hitShipSounds.append(sound)
        self.hitShieldSounds.clear()
        for sound in self.hitShieldSounds2:
            self.hitShieldSounds.append(sound)
        self.missSounds.clear()
        for sound in self.missSounds2:
            self.missSounds.append(sound)
        self.image, self.explosion = self.image2, self.explosion2
        self.droneTargetable = self.droneTargetable2
        self.droneTargetable_true = self.droneTargetable_true2
        self.droneTargetable_none = self.droneTargetable_none2

    def generate_weapon(self):
        """ regenerates this weapon in self.file based on all its attributes"""
        self.file.write("<weaponBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>MISSILES</type>\n")
        if self.flavorType_true:
            self.file.write("\t<flavorType>" +
                            self.flavorType +
                            "</flavorType>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        if self.droneTargetable_none:
            self.file.write("\t<drone_targetable />\n")
        elif self.droneTargetable_true:
            self.file.write("\t<drone_targetable>" +
                            str(self.droneTargetable) +
                            "</drone_targetable>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<tooltip>" + self.tooltip + "</tooltip>\n")
        if self.stun_true:
            # round stun since float. makes for more accurate stun time
            self.file.write("\t<stun>" + str(round(self.stun)) + "</stun>\n")
        if self.damage_true:
            self.file.write("\t<damage>" + str(self.damage) + "</damage>\n")
        if self.sysDamage_true:
            self.file.write(
                "\t<sysDamage>" + str(self.sysDamage) + "</sysDamage>\n")
        if self.persDamage_true:
            self.file.write(
                "\t<persDamage>" + str(self.persDamage) + "</persDamage>\n")
        if self.ion_true:
            self.file.write("\t<ion>" + str(self.ion) + "</ion>\n")
        # round speed since float. makes for more accurate speed
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        self.file.write("\t<missiles>" + str(self.missiles) + "</missiles>\n")
        self.file.write("\t<shots>" + str(self.shots) + "</shots>\n")
        self.file.write("\t<sp>" + str(self.sp) + "</sp>\n")
        if self.fireChance_true:
            self.file.write("\t<fireChance>" +
                            str(self.fireChance) +
                            "</fireChance>\n")
        if self.breachChance_true:
            self.file.write("\t<breachChance>" +
                            str(self.breachChance) +
                            "</breachChance>\n")
        if self.stunChance_true:
            self.file.write(
                "\t<stunChance>" + str(self.stunChance) + "</stunChance>\n")
        if self.lockdown_true:
            self.file.write(
                "\t<lockdown>" + str(self.lockdown) + "</lockdown>\n")
        if self.hullBust_true:
            self.file.write(
                "\t<hullBust>" + str(self.hullBust) + "</hullBust>\n")
        # since cooldown is a float, needs to round
        if self.cooldown < 10:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 2)) +
                            "</cooldown>\n")
        else:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 1)) +
                            "</cooldown>\n")
        # round since float
        self.file.write("\t<power>" + str(round(self.power)) + "</power>\n")
        # round cost since float. makes for more accurate prices
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("\t<image>" + self.image + "</image>\n")
        if self.boost_true:
            self.file.write("\t<boost>\n")
            self.file.write("\t\t<type>" + self.boost[0] + "</type>\n")
            self.file.write("\t\t<amount>" + str(round(self.boost[1], 3)) +
                            "</amount>\n")
            self.file.write("\t\t<count>" + str(self.boost[2]) + "</count>\n")
            self.file.write("\t</boost>\n")
        self.file.write("\t<explosion>" + self.explosion + "</explosion>\n")
        self.file.write("\t<launchSounds>\n")
        for sound in self.launchSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</launchSounds>\n")
        self.file.write("\t<hitShipSounds>\n")
        for sound in self.hitShipSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShipSounds>\n")
        self.file.write("\t<hitShieldSounds>\n")
        for sound in self.hitShieldSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShieldSounds>\n")
        self.file.write("\t<missSounds>\n")
        for sound in self.missSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</missSounds>\n")
        self.file.write("\t<weaponArt>" + self.weaponArt + "</weaponArt>\n")
        self.file.write("</weaponBlueprint>\n")

    # rip support variation
    def ce_assault_missiles(self):
        if self.missiles > 0 and self.power < 4:
            self.name += "_ASSAULT_MISSILES"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += " Assault: cooldown x0.75 power cost +1"
            self.cooldown *= 0.75
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_stalker(self):
        if self.power < 4:
            self.name += "_STALKER"
            self.title = "Stalking " + self.title
            if len(self.title) > 27:
                self.title = "Stalk. " + self.title2
            self.short = "St " + self.short
            self.desc += " Stalking: " \
                         "cooldown x0.70 projectile speed x0.4 power cost +1"
            self.cooldown *= 0.7
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.7
            self.speed *= 0.4
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_tactical(self):
        if self.damage > 0 and self.shots < 4:
            self.name += "_TACTICAL"
            self.title = "Tactical " + self.title
            if len(self.title) > 27:
                self.title = "Tact. " + self.title2
            self.short = "Ta " + self.short
            self.desc += " Tactical: damage -1 system damage +2"
            self.damage -= 1
            self.sysDamage_true = True
            self.sysDamage += 2
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_brutal(self):
        if self.damage > 0:
            self.name += "_BRUTAL"
            self.title = "Brutal " + self.title
            if len(self.title) > 27:
                self.title = "Brut. " + self.title2
            self.short = "BR " + self.short
            self.desc += " Packs a punch."
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.breachChance_true = True
            self.breachChance += 1
            if self.breachChance > 10:
                self.breachChance = 10
            self.persDamage_true = True
            self.persDamage += 1
            self.stunChance_true = True
            self.stunChance += 1
            if self.stunChance > 10:
                self.stunChance = 10
            self.cost *= 1.3
            self.weaponArt += "_dirty_steel"
            self.image += "_dark"

            self.generate_weapon()
            self.revert_weapon()

    def ce_weaksauce(self):
        if self.damage > 0:
            self.name += "_WEAKSAUCE"
            self.title = "Weaksauce " + self.title
            if len(self.title) > 27:
                self.title = "Weak " + self.title2
            self.short = "weak " + self.short
            self.desc += " Makes your enemy laugh at you."
            self.cooldown *= 1.1
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.1
            self.breachChance -= 1
            if self.breachChance < 0:
                self.breachChance = 0
            self.persDamage -= 1
            self.stunChance -= 1
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    def ce_hull_ripper(self):
        if (self.damage > 0 and self.hullBust < 1 and
                self.ion < 1 and self.shots < 4):
            self.name += "_HULL_RIPPER"
            self.title = "Hull Ripper " + self.title
            if len(self.title) > 27:
                self.title = "Ripper " + self.title2
            self.short = "HR " + self.short
            self.desc += " Deals double hull damage to systemless rooms."
            self.hullBust_true = True
            self.hullBust = 1
            self.cost *= 1.25
            self.weaponArt += "_green"
            self.image += "_green"

            self.generate_weapon()
            self.revert_weapon()

    def ce_reconfigured(self):
        if self.hullBust > 0:
            self.name += "_RECONFIGURED"
            self.title = "Reconfigured " + self.title
            if len(self.title) > 27:
                self.title = "Reconf. " + self.title2
            self.short = "r " + self.short
            self.desc += \
                " Reconfigured: deals normal damage to systemless rooms"
            self.hullBust_true = False
            self.hullBust = 0
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"

            self.generate_weapon()
            self.revert_weapon()

    def ce_heavy(self):
        if (self.ion < 1 and self.damage == 1 and self.hullBust < 1 and
                self.shots < 4 and self.power < 4):
            self.name += "_HEAVY"
            self.title = "Heavy " + self.title
            self.short = "H " + self.short
            self.desc += " Heavy: damage +1 cooldown x1.5 power cost +1"
            self.damage += 1
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.power += 1
            self.cost *= 1.4
            self.weaponArt += "_old"
            self.generate_weapon()
            self.revert_weapon()

    def ce_light(self):
        if self.ion < 1 and self.damage > 2:
            self.name += "_LIGHT"
            self.title = "Light " + self.title
            self.short = "l " + self.short
            self.desc += " Light: damage -1 cooldown x0.9"
            self.damage -= 1
            # catch for mines
            if self.sysDamage < 0:
                self.sysDamage += 1
            self.cooldown *= 0.9
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.9
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_substandard(self):
        self.name += "_SUBSTANDARD"
        self.title = "Substandard " + self.title
        if len(self.title) > 27:
            self.title = "Subst. " + self.title2
        self.short = "sub " + self.short
        # self.desc += " Overall performance is substandard."
        # this doesn't really say much...
        self.desc += " Substandard: overall bad stats"
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.speed *= 0.9
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 1
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.8
        self.weaponArt += "_slight_desat"
        self.generate_weapon()
        self.revert_weapon()

    def ce_surplus(self):
        self.name += "_SURPLUS"
        self.title = "Surplus " + self.title
        self.short = "sur " + self.short
        self.desc += " Surplus: overall very bad stats"
        self.cooldown *= 1.2
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.2
        # if speed_c False, then speed multiplier is irrelevant
        self.speed *= 0.8
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 3
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.5
        self.weaponArt += "_heavy_desat"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_quality(self):
        self.name += "_QUALITY"
        self.title = "Quality " + self.title
        self.short = "Q " + self.short
        self.desc += " Quality: overall better stats"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.speed *= 1.1
        self.cost *= 1.25
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_custom(self):
        self.name += "_CUSTOM"
        self.title = "Custom " + self.title
        self.short = "C " + self.short
        self.desc += " Custom (Rare): overall great stats"
        self.cooldown *= 0.8
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.8
        self.speed *= 1.2
        self.fireChance_true = True
        self.fireChance += 1
        if self.fireChance > 10:
            self.fireChance = 10
        self.breachChance_true = True
        self.breachChance += 1
        if self.breachChance > 10:
            self.breachChance = 10
        self.stunChance_true = True
        self.stunChance += 1
        if self.stunChance > 10:
            self.stunChance = 10
        self.cost *= 1.5
        self.weaponArt += "_ht_steel_bright"
        self.image += "_high_tech"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_vintage(self):
        self.name += "_VINTAGE"
        self.title = "Vintage " + self.title
        if len(self.title) > 27:
            self.title = "Vint. " + self.title2
        self.short = "Vin " + self.short
        self.desc += " Vintage: overall bad stats but valuable and rare"
        self.speed *= 0.9
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.cost *= 1.5
        if self.rarity > 0:
            self.rarity += 2
            if self.rarity > 5:
                self.rarity = 5
        self.weaponArt += "_gritty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_antique(self):
        self.name += "_ANTIQUE"
        self.title = "Antique " + self.title
        if len(self.title) > 27:
            self.title = "Anti. " + self.title2
        self.short = "Ant " + self.short
        self.desc += " Antique: overall very bad stats but " \
                     "very valuable and rare"
        self.speed *= 0.7
        self.cooldown *= 1.4
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.4
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        if self.rarity > 0:
            self.rarity += 4
            if self.rarity > 5:
                self.rarity = 5
        self.cost *= 2
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc += " Swag (Rare): good for showing off"
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_gold"
            self.generate_weapon()
            self.revert_weapon()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Secondhand " + self.title
        if len(self.title) > 27:
            self.title = "Sec. Hand " + self.title2
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_weapon()
        self.revert_weapon()

    # power-only
    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.weaponArt += "_dirty"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_optimized(self):
        if self.power > 2:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            if len(self.title) > 27:
                self.title = "Optim. " + self.title2
            if len(self.title) > 27:
                self.title = "Opt. " + self.title2
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.weaponArt += "_ht_steel"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # cooldown-only
    def ce_outdated(self):
        # every weapon has a cooldown
        self.cooldown *= 1.15
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.15
        self.name += "_OUTDATED"
        # self.desc += (" Drags on with a sub-par reload time.")
        self.desc += " Recharges slightly slower."
        self.title = "Outdated " + self.title
        if len(self.title) > 27:
            self.title = "Outd. " + self.title2
        self.short = "ou " + self.short
        self.cost *= 0.8
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_obsolete(self):
        # every weapon has a cooldown
        self.cooldown *= 1.25
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.25
        self.name += "_OBSOLETE"
        self.desc += " Recharges slower."
        self.title = "Obsolete " + self.title
        if len(self.title) > 27:
            self.title = "Obsol. " + self.title2
        self.short = "ob " + self.short
        self.cost *= 0.6
        self.weaponArt += "_rust"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_upgraded(self):
        # every weapon has a cooldown
        self.cooldown *= 0.85
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.85
        self.name += "_UPGRADED"
        self.desc += " Recharges slightly faster."
        self.title = "Upgraded " + self.title
        if len(self.title) > 27:
            self.title = "Upgr. " + self.title2
        self.short = "UP " + self.short
        self.cost *= 1.2
        self.weaponArt += "_high_tech"

        self.generate_weapon()
        self.revert_weapon()

    def ce_advanced(self):
        # every weapon has a cooldown
        self.cooldown *= 0.75
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.75
        self.name += "_ADVANCED"
        self.desc += " (Rare) Recharges faster."
        self.title = "Advanced " + self.title
        if len(self.title) > 27:
            self.title = "Adv. " + self.title2
        self.short = "AD " + self.short
        self.cost *= 1.4
        self.weaponArt += "_ht_steel_bright"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_quickshot(self):
        self.name += "_QUICKSHOT"
        self.title = "Quickshot " + self.title
        if len(self.title) > 27:
            self.title = "Quick. " + self.title2
        self.short = "QU " + self.short
        self.desc += " Quickshot: cooldown x0.90 projectile speed x2"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.cost *= 1.2
        self.speed *= 2
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_impacting(self):
        if self.breachChance < 10 and self.stunChance > 0 and self.ion < 1:
            self.name += "_IMPACTING"
            self.title = "Impacting " + self.title
            if len(self.title) > 27:
                self.title = "Impact. " + self.title2
            self.short = "IM " + self.short
            self.desc += " Impact: breach chance +1 stun chance +1"
            # must already have a stun chance, no need to set it
            if self.stunChance < 10:
                self.stunChance += 1
            self.breachChance_true = True
            # since breachChance must already be less than 10 no need to check
            self.breachChance += 1
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_penetrating(self):
        if self.ion < 1 and self.breachChance < 10:
            self.name += "_PENETRATING"
            self.title = "Penetr. " + self.title
            self.short = "PE " + self.short
            self.desc += " Penetrating: " \
                         "breach chance +1 projectile speed x1.10"
            self.speed *= 1.1
            # breachChance must be 9 or less
            self.breachChance += 1
            self.breachChance_true = True
            self.cost *= 1.2
            self.weaponArt += "_dirty_steel"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_breaching(self):
        if self.ion < 1 and self.breachChance < 9 and self.shots < 3:
            self.name += "_BREACHING"
            self.title = "Breaching " + self.title
            if len(self.title) > 27:
                self.title = "Breach. " + self.title2
            self.short = "BR " + self.short
            self.desc += " Breaching (Rare): " \
                         "breach chance +2 projectile speed x1.30"
            self.speed *= 1.3
            # breachChance must be 8 or less
            self.breachChance += 2
            self.breachChance_true = True
            self.cost *= 1.4
            self.weaponArt += "_steel"
            self.image += "_dark"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowmass(self):
        if self.ion < 1 and self.breachChance > 1:
            self.name += "_LOWMASS"
            self.title = "Low Mass " + self.title
            self.short = "lma " + self.short
            self.desc += " Low Mass: breach chance -2 projectile speed x0.9"
            self.speed *= 0.9
            # breachChance must be at least 2
            self.breachChance -= 2
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # ~~changed req to need two higher breach chance than above
    def ce_lowmomentum(self):
        if self.ion < 1 and self.breachChance > 3:
            self.name += "_LOWMOMENTUM"
            self.title = "Low Momentum " + self.title
            if len(self.title) > 27:
                self.title = "Low Mom. " + self.title2
            self.short = "lmo " + self.short
            self.desc += " Low Momentum: " \
                         "breach chance -4 projectile speed x0.7"
            self.speed *= 0.7
            # breachChance must be at least 4
            self.breachChance -= 4
            self.cost *= 0.6
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # fire
    def ce_incendiary(self):
        if self.fireChance < 7:
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_INCENDIARY"
            self.desc += " A bit more likely to start a fire."
            self.title = "Incendiary " + self.title
            if len(self.title) > 27:
                self.title = "Incend. " + self.title2
            self.short = "IN " + self.short
            self.cost *= 1.2
            self.image += "_red"
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_plasma(self):
        if self.fireChance < 7:
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 2
            self.name += "_PLASMA"
            self.desc += " (Rare) Imbued with plasma, this weapon's more " \
                         "likely to start a fire."
            self.title = "Plasma " + self.title
            self.short = "PL " + self.short
            self.cost *= 1.3
            self.image += "_red"
            self.weaponArt += "_red"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_insulated(self):
        if self.ion < 1 and self.fireChance > 1:
            self.fireChance -= 1
            self.name += "_INSULATED"
            self.title = "Insulated " + self.title
            if len(self.title) > 27:
                self.title = "Insul. " + self.title2
            self.short = "in " + self.short
            self.desc += " Insulated: fire chance -1"
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heatshielded(self):
        if self.ion < 1 and self.fireChance > 4:
            self.fireChance -= 3
            self.name += "_HEATSHIELDED"
            self.title = "Heatshielded " + self.title
            if len(self.title) > 27:
                self.title = "Heatsh. " + self.title2
            self.short = "hea " + self.short
            self.desc += " Heatshielded: fire chance -3"
            self.cost *= 0.7
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # crew-damage only
    def ce_radioactive(self):
        # need to make it true when increasing, but not when decreasing
        self.persDamage_true = True
        self.persDamage += 1
        self.name += "_RADIOACTIVE"
        self.desc += " Radioactive elements make it deadlier to crew."
        self.title = "Radioactive " + self.title
        if len(self.title) > 27:
            self.title = "Rad. " + self.title2
        self.short = "RAD " + self.short
        self.cost *= 1.2
        self.weaponArt += "_yellow"
        self.image += "_yellow"
        self.generate_weapon()
        self.revert_weapon()

    def ce_safe_nonlethal(self):
        # e.g. light scatter lasers?
            # negative persDamage values are not okay since that means
            # crew heal shenanigans since damage is less than 1
        if self.ion < 1 and self.damage < 1 and self.persDamage > 0:
            self.persDamage -= 1
            self.name += "_SAFE_NONLETHAL"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.persDamage == 0:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe(self):
        # clause added to avoid crew heal shenanigans
        if (self.ion < 1 and self.damage > 0 and
                self.persDamage != -self.damage):
            # since damage is at least 1, persDamage tag must be added
            self.persDamage_true = True
            self.persDamage -= 1
            # since damage is at least 1, persDamage will cancel out some crew
            # damage done just by regular damage, so negative values are okay
            self.name += "_SAFE"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.damage == 1:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_volatile(self):
        # if fire chance is already 10, then radioactive does the same thing
        if self.fireChance < 10:
            # adds a persDamage tag if one doesn't already exist
            self.persDamage_true = True
            self.persDamage += 1
            # same for fireChance
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_VOLATILE"
            self.title = "Volatile " + self.title
            if len(self.title) > 27:
                self.title = "Volat. " + self.title2
            self.short = "VOL " + self.short
            self.desc += " Releases volatile chemicals on impact."
            self.cost *= 1.3
            self.weaponArt += "_dirty"
            self.image += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_overcharged(self):
        if self.shots < 3 and self.power < 4 and self.ion > 1:
            self.ion += 2
            self.power += 1
            self.name += "_OVERCHARGED"
            self.title = "Overcharg. " + self.title
            if len(self.title) > 27:
                self.title = "Overch. " + self.title2
            self.short = "OV " + self.short
            self.desc += " Overcharged: ion damage +1 power cost +1"
            self.cost *= 1.4
            self.weaponArt += "_ht_steel_bright"
            self.image += "_high"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowcharge(self):
        if self.ion > 1:
            self.ion -= 1
            self.name += "_LOWCHARGE"
            self.title = "Low Charge " + self.title
            if len(self.title) > 27:
                self.title = "Low Ch. " + self.title2
            self.short = "lwc " + self.short
            self.desc += " Low Charge: ion damage -1"
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_unstable(self):
        if self.ion > 1:
            self.ion -= 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.name += "_UNSTABLE"
            self.title = "Unstable " + self.title
            if len(self.title) > 27:
                self.title = "Unsta. " + self.title2
            self.short = "Un " + self.short
            self.desc += " Unstable: ion damage -1 system damage +1"
            self.cost *= 0.8
            self.weaponArt += "_purple"
            self.image += "_purple"
            self.generate_weapon()
            self.revert_weapon()

    def ce_flux(self):
        if self.ion > 1:
            self.ion -= 1
            self.stunChance_true = True
            self.stunChance += 3
            if self.stunChance > 10:
                self.stunChance = 10
            self.fireChance_true = True
            self.fireChance += 3
            if self.fireChance > 10:
                self.fireChance = 10
            self.name += "_FLUX"
            self.title = "Flux " + self.title
            self.short = "Fl " + self.short
            self.desc += " Flux: ion damage -1 stun chance +3 fire chance +3"
            self.cost *= 1.1
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_replicator(self):
        if (self.missiles > 0 and self.cooldown > 8 and
                not ("BA_MISSILES_ASTERIA" in self.name)):
            self.name += "_REPLICATOR"
            self.title = "Replicator " + self.title
            if len(self.title) > 27:
                self.title = "Replic. " + self.title2
            if len(self.title) > 27:
                self.title = "Repl. " + self.title2
            self.short = "RE " + self.short
            self.desc += " (Rare) Given time it can replicate its own ammo."
            # yeah, x2 is too much breh, but how much less???
            self.cooldown *= 1.3
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.3
            self.missiles = 0
            # does the cost justify the benefit?
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_high_tech"
            self.image += "_heavy_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highyield(self):
        if (self.missiles > 0 and self.shots < 2 and
                self.damage > 1 and self.cooldown > 10 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_HIGHYIELD"
            self.title = "High Yield " + self.title
            if len(self.title) > 27:
                self.title = "HighY. " + self.title2
            self.short = "HY " + self.short
            self.desc += " (Rare) Does more damage at the cost of an " \
                         "additional missile."
            self.missiles += 1
            # check for mines
            if self.sysDamage < 0 and self.persDamage < 0:
                self.sysDamage -= 2
                self.persDamage -= 2
            self.damage += 2
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            # mines support these image suffixes, right? Right??
            self.weaponArt += "_steel"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_alpha(self):
        if (self.missiles > 0 and self.shots < 2 and
                self.damage > 1 and self.cooldown > 10 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_ALPHA"
            self.title = "Alpha " + self.title
            self.short = "AL " + self.short
            # gotta come up with an epic description...
            self.desc += " Alpha (Epic): cooldown x0.5, damage +1"
            # check for mines
            if self.sysDamage < 0 and self.persDamage < 0:
                self.sysDamage -= 1
                self.persDamage -= 1
            self.damage += 1
            self.cooldown /= 2
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] /= 2
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_ht_steel_bright"
            self.image += "_ht_steel_bright"
            self.generate_weapon()
            self.revert_weapon()

    def ce_scrambling(self):
        if (self.missiles > 0 and self.damage > 0 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_SCRAMBLING"
            self.title = "Scrambling " + self.title
            if len(self.title) > 27:
                self.title = "Scramble " + self.title2
            if len(self.title) > 27:
                self.title = "Scram. " + self.title2
            self.short = "SC " + self.short
            self.desc += " Scrambles enemy defense drone targeting, " \
                         "masking its trajectory."
            self.droneTargetable_true = False
            self.droneTargetable_none = True
            self.cost *= 1.3
            self.weaponArt += "_ht_steel_bright"
            self.image += "_ht_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_wasteful(self):
        if self.missiles > 0:
            self.name += "_WASTEFUL"
            self.title = "Wasteful " + self.title
            if len(self.title) > 27:
                self.title = "Wast. " + self.title2
            self.short = "was " + self.short
            self.desc += " Needs another missile due to a jammed loader."
            self.missiles += 1
            self.cost *= 0.5
            self.weaponArt += "_dirty"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_frail(self):
        if self.missiles > 0:
            self.name += "_FRAIL"
            self.title = "Frail " + self.title
            self.short = "fr " + self.short
            self.desc += " Frail: shield piercing -3"
            self.sp -= 3
            if self.sp < 0:
                self.sp = 0
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highvelocity(self):
        if self.missiles > 0:
            self.name += "_HIGHVELOCITY"
            self.title = "High Vel. " + self.title
            if len(self.title) > 27:
                self.title = "HighV. " + self.title2
            self.short = "HI " + self.short
            self.desc += " High Velocity: projectile speed x1.5"
            self.speed *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_gritty"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_boosted_missile(self):
        if self.missiles > 0 and self.shots < 3:
            self.name += "_BOOSTED_MISSILE"
            self.title = "Boosted " + self.title
            if len(self.title) > 27:
                self.title = "Boost. " + self.title2
            self.short = "BO " + self.short
            self.desc += " Boosted: projectile speed x2.5"
            self.speed *= 2.5
            self.cost *= 1.3
            self.weaponArt += "_gritty"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowvelocity(self):
        if self.missiles > 0:
            self.name += "_LOW_VELOCITY"
            self.title = "Low Vel. " + self.title
            if len(self.title) > 27:
                self.title = "LowV. " + self.title2
            self.short = "low " + self.short
            self.desc += " Low Velocity: projectile speed x0.6"
            self.speed *= 0.6
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_torpedo(self):
        # self.speed check for mines
        if (self.missiles > 0 and self.damage > 1 and
                self.damage >= 0 and self.cooldown > 10 and
                self.speed > 12 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_TORPEDO"
            self.title = "Torpedo " + self.title
            if len(self.title) > 27:
                self.title = "Torp. " + self.title2
            self.short = "TOR " + self.short
            self.desc += " Torpedo: damage +1, projectile speed x0.5"
            self.speed *= 0.5
            self.damage += 1
            self.cost *= 1.2
            self.weaponArt += "_steel"
            self.image += "_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp(self):
        if (self.missiles > 0 and self.shots < 2 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_EMP"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " EMP: ion damage +3 shield piercing -5"
            self.desc += " Its ion-wrapped missile deals hefty ion damage " \
                         "but is consequently unable to pierce through " \
                         "shields."
            self.ion += 3
            self.ion_true = True
            self.sp -= 5
            if self.sp < 0:
                self.sp = 0
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp_burst(self):
        if (self.missiles > 0 and self.shots > 1 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_EMP_BURST"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " Its ion-coated missiles deal some added " \
                         "ion damage but are consequently unable to " \
                         "pierce through shields."
            self.ion += 1
            self.ion_true = True
            self.sp -= 5
            if self.sp < 0:
                self.sp = 0
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_frag(self):
        if self.missiles > 0 and self.damage > 0:
            self.name += "_FRAG"
            self.title = "Frag " + self.title
            self.short = "Frag " + self.short
            self.desc += " Explodes into fragments upon impact, piercing " \
                         "systems and crew, at the cost of hull damage."
            self.damage -= 1
            self.persDamage_true = True
            self.persDamage += 2
            self.sysDamage_true = True
            self.sysDamage += 2
            self.cost *= 1.30
            self.weaponArt += "_gritty"
            self.image += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shredder(self):
        if (self.missiles > 0 and self.shots < 2 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_SHREDDER"
            self.title = "Shredder " + self.title
            if len(self.title) > 27:
                self.title = "Shred. " + self.title2
            self.short = "SHRE " + self.short
            self.desc += " (Rare) Enlaced spikes deal increased damage " \
                         "to systems and crew."
            self.persDamage_true = True
            self.persDamage += 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.cost *= 1.4
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_dirty_steel"
            self.image += "_dirty_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_caustic(self):
        # why exclude mines??
        if self.missiles > 0 and self.breachChance < 10:
            # makes sure the persDamage tag is there
            self.persDamage_true = True
            self.persDamage += 1
            # makes sure the breach tag is there
            self.breachChance_true = True
            self.breachChance += 1
            self.name += "_CAUSTIC"
            self.title = "Caustic " + self.title
            if len(self.title) > 27:
                self.title = "Caus. " + self.title2
            self.short = "CAU " + self.short
            self.desc += " Corrodes organic and inorganic matter alike."
            self.cost *= 1.2
            self.weaponArt += "_green"
            self.image += "_green"
            self.generate_weapon()
            self.revert_weapon()

    def ce_stungun(self):
        if 0 < self.stunChance < 8:
            self.name += "_STUNGUN"
            self.title = "Stun " + self.title
            self.short = "ST " + self.short
            self.desc += " Stun: stun chance +3"
            self.stunChance += 3
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shock(self):
        if 0 < self.stunChance < 6 and self.ion > 0:
            self.name += "_SHOCK"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun chance +5"
            self.stunChance += 5
            self.cost *= 1.3
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_regulated(self):
        if self.stunChance > 0:
            self.name += "_REGULATED"
            self.title = "Regulated " + self.title
            if len(self.title) > 27:
                self.title = "Regul. " + self.title2
            self.short = "reg " + self.short
            if 0 < self.stunChance < 3:
                self.desc += " Due to regulations, " \
                             "its ability to stun was removed."
            else:
                self.desc += " Less likely to stun due to regulations."
            self.stunChance -= 2
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_concussion(self):
        if self.missiles > 0 and self.ion < 1 and self.stun > 0:
            self.name += "_CONCUSSION"
            self.title = "Concussion " + self.title
            if len(self.title) > 27:
                self.title = "Concuss. " + self.title2
            self.short = "CO " + self.short
            self.desc += " Concussion: stun time x1.5"
            self.stun *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_predictable(self):
        if self.missiles > 0 and 0 < self.stun < 5:
            self.name += "_PREDICTABLE"
            self.title = "Predictable " + self.title
            if len(self.title) > 27:
                self.title = "Predict. " + self.title2
            self.short = "pr " + self.short
            self.desc += " Predictable: cannot stun"
            self.stun = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # having <stun> guarantees stun
    def ce_calibrated(self):
        if self.ion > 0 and self.stun > 4 and self.missiles < 1:
            self.name += "_CALIBRATED"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun time +2"
            self.stun += 2
            self.cost *= 1.2
            self.weaponArt += "_high_tech_2"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()


class Bomb(Weapon2):
    def __init__(self, f):
        super().__init__(f)
        self.lockdown, self.lockdown_true = 0, False
        self.shots = 0
        self.missiles = 1
        self.hitShipSounds = []
        self.image, self.explosion = "", ""
        self.locked = 1
        '''################### DUPLICATES FOR REVERTING ###################'''
        self.lockdown2, self.lockdown_true2 = 0, False
        self.shots2 = 0
        self.missiles2 = 1
        self.hitShipSounds2 = []
        self.image2, self.explosion2 = "", ""
        self.locked2 = 1

    def revert_weapon(self):
        super().revert_weapon()
        self.lockdown, self.lockdown_true = self.lockdown2, self.lockdown_true2
        self.shots = self.shots2
        self.missiles = self.missiles2
        self.hitShipSounds.clear()
        for sound in self.hitShipSounds2:
            self.hitShipSounds.append(sound)
        self.image, self.explosion = self.image2, self.explosion2
        self.locked = self.locked2

    def generate_weapon(self):
        """ regenerates this weapon in self.file based on all its attributes"""
        self.file.write("<weaponBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>BOMB</type>\n")
        if self.flavorType_true:
            self.file.write("\t<flavorType>" +
                            self.flavorType +
                            "</flavorType>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<locked>" + str(self.locked) + "</locked>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<tooltip>" + self.tooltip + "</tooltip>\n")
        if self.stun_true:
            # round stun since float. makes for more accurate stun time
            self.file.write("\t<stun>" + str(round(self.stun)) + "</stun>\n")
        if self.damage_true:
            self.file.write("\t<damage>" + str(self.damage) + "</damage>\n")
        if self.sysDamage_true:
            self.file.write(
                "\t<sysDamage>" + str(self.sysDamage) + "</sysDamage>\n")
        if self.persDamage_true:
            self.file.write(
                "\t<persDamage>" + str(self.persDamage) + "</persDamage>\n")
        if self.ion_true:
            self.file.write("\t<ion>" + str(self.ion) + "</ion>\n")
        self.file.write("\t<missiles>" + str(self.missiles) + "</missiles>\n")
        self.file.write("\t<shots>" + str(self.shots) + "</shots>\n")
        if self.fireChance_true:
            self.file.write(
                "\t<fireChance>" + str(self.fireChance) + "</fireChance>\n")
        if self.breachChance_true:
            self.file.write("\t<breachChance>" +
                            str(self.breachChance) +
                            "</breachChance>\n")
        if self.stunChance_true:
            self.file.write(
                "\t<stunChance>" + str(self.stunChance) + "</stunChance>\n")
        if self.lockdown_true:
            self.file.write(
                "\t<lockdown>" + str(self.lockdown) + "</lockdown>\n")
        if self.hullBust_true:
            self.file.write(
                "\t<hullBust>" + str(self.hullBust) + "</hullBust>\n")
        # since cooldown is a float, needs to round
        if self.cooldown < 10:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 2)) +
                            "</cooldown>\n")
        else:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 1)) +
                            "</cooldown>\n")
        # round since float
        self.file.write("\t<power>" + str(round(self.power)) + "</power>\n")
        # round cost since float. makes for more accurate prices
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("\t<image>" + self.image + "</image>\n")
        if self.boost_true:
            self.file.write("\t<boost>\n")
            self.file.write("\t\t<type>" + self.boost[0] + "</type>\n")
            self.file.write("\t\t<amount>" + str(round(self.boost[1], 3)) +
                            "</amount>\n")
            self.file.write("\t\t<count>" + str(self.boost[2]) + "</count>\n")
            self.file.write("\t</boost>\n")
        self.file.write("\t<explosion>" + self.explosion + "</explosion>\n")
        self.file.write("\t<launchSounds>\n")
        for sound in self.launchSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</launchSounds>\n")
        self.file.write("\t<hitShipSounds>\n")
        for sound in self.hitShipSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShipSounds>\n")
        self.file.write("\t<weaponArt>" + self.weaponArt + "</weaponArt>\n")
        self.file.write("</weaponBlueprint>\n")

    # rip support variation
    def ce_assault_missiles(self):
        if self.missiles > 0 and self.power < 4:
            self.name += "_ASSAULT_MISSILES"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += " Assault: cooldown x0.75 power cost +1"
            self.cooldown *= 0.75
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_substandard(self):
        self.name += "_SUBSTANDARD"
        self.title = "Substandard " + self.title
        if len(self.title) > 27:
            self.title = "Subst. " + self.title2
        self.short = "sub " + self.short
        # self.desc += " Overall performance is substandard."
        # this doesn't really say much...
        self.desc += " Substandard: overall bad stats"
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        # self.speed *= 0.9
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 1
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.8
        self.weaponArt += "_slight_desat"
        self.generate_weapon()
        self.revert_weapon()

    def ce_surplus(self):
        if not ("BA_EFFECTOR_1" in self.name or
                "BA_EFFECTOR_2" in self.name or
                "BA_EFFECTOR_3" in self.name or
                "BA_BOMB_NANO_1" in self.name or
                "BA_BOMB_NANO_2" in self.name or
                "BOMB_HEAL_SYSTEM" in self.name or
                "BOMB_HEAL" in self.name or "BA_BOMB_HEAL_2" in self.name):
            self.name += "_SURPLUS"
            self.title = "Surplus " + self.title
            self.short = "sur " + self.short
            self.desc += " Surplus: overall very bad stats"
            self.cooldown *= 1.2
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.2
            # self.speed *= 0.8
            self.fireChance -= 3
            if self.fireChance < 0:
                self.fireChance = 0
            self.breachChance -= 3
            if self.breachChance < 0:
                self.breachChance = 0
            self.stunChance -= 3
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.5
            self.weaponArt += "_heavy_desat"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_quality(self):
        self.name += "_QUALITY"
        self.title = "Quality " + self.title
        self.short = "Q " + self.short
        self.desc += " Quality: overall better stats"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        # self.speed *= 1.1
        self.cost *= 1.25
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_custom(self):
        if not ("BA_EFFECTOR_1" in self.name or
                "BA_EFFECTOR_2" in self.name or
                "BA_EFFECTOR_3" in self.name or
                "BA_BOMB_NANO_1" in self.name or
                "BA_BOMB_NANO_2" in self.name or
                "BOMB_HEAL_SYSTEM" in self.name or
                "BOMB_HEAL" in self.name or "BA_BOMB_HEAL_2" in self.name):
            self.name += "_CUSTOM"
            self.title = "Custom " + self.title
            self.short = "C " + self.short
            self.desc += " Custom (Rare): overall great stats"
            self.cooldown *= 0.8
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.8
            # self.speed *= 1.2
            self.fireChance_true = True
            self.fireChance += 1
            if self.fireChance > 10:
                self.fireChance = 10
            self.breachChance_true = True
            self.breachChance += 1
            if self.breachChance > 10:
                self.breachChance = 10
            self.stunChance_true = True
            self.stunChance += 1
            if self.stunChance > 10:
                self.stunChance = 10
            self.cost *= 1.5
            self.weaponArt += "_ht_steel_bright"
            self.image += "_high_tech"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_vintage(self):
        self.name += "_VINTAGE"
        self.title = "Vintage " + self.title
        if len(self.title) > 27:
            self.title = "Vint. " + self.title2
        self.short = "Vin " + self.short
        self.desc += " Vintage: overall bad stats but valuable and rare"
        # self.speed *= 0.9
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.cost *= 1.5
        if self.rarity > 0:
            self.rarity += 2
            if self.rarity > 5:
                self.rarity = 5
        self.weaponArt += "_gritty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_antique(self):
        self.name += "_ANTIQUE"
        self.title = "Antique " + self.title
        if len(self.title) > 27:
            self.title = "Anti. " + self.title2
        self.short = "Ant " + self.short
        self.desc += " Antique: overall very bad stats but " \
                     "very valuable and rare"
        # self.speed *= 0.7
        self.cooldown *= 1.4
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.4
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        if self.rarity > 0:
            self.rarity += 4
            if self.rarity > 5:
                self.rarity = 5
        self.cost *= 2
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc += " Swag (Rare): good for showing off"
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_gold"
            self.generate_weapon()
            self.revert_weapon()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Secondhand " + self.title
        if len(self.title) > 27:
            self.title = "Sec. Hand " + self.title2
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_weapon()
        self.revert_weapon()

    # power-only
    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.weaponArt += "_dirty"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_optimized(self):
        if self.power > 2:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            if len(self.title) > 27:
                self.title = "Optim. " + self.title2
            if len(self.title) > 27:
                self.title = "Opt. " + self.title2
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.weaponArt += "_ht_steel"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # cooldown-only
    def ce_outdated(self):
        # every weapon has a cooldown
        self.cooldown *= 1.15
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.15
        self.name += "_OUTDATED"
        # self.desc += (" Drags on with a sub-par reload time.")
        self.desc += " Recharges slightly slower."
        self.title = "Outdated " + self.title
        if len(self.title) > 27:
            self.title = "Outd. " + self.title2
        self.short = "ou " + self.short
        self.cost *= 0.8
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_obsolete(self):
        # every weapon has a cooldown
        self.cooldown *= 1.25
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.25
        self.name += "_OBSOLETE"
        self.desc += " Recharges slower."
        self.title = "Obsolete " + self.title
        if len(self.title) > 27:
            self.title = "Obsol. " + self.title2
        self.short = "ob " + self.short
        self.cost *= 0.6
        self.weaponArt += "_rust"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_upgraded(self):
        # every weapon has a cooldown
        self.cooldown *= 0.85
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.85
        self.name += "_UPGRADED"
        self.desc += " Recharges slightly faster."
        self.title = "Upgraded " + self.title
        if len(self.title) > 27:
            self.title = "Upgr. " + self.title2
        self.short = "UP " + self.short
        self.cost *= 1.2
        self.weaponArt += "_high_tech"

        self.generate_weapon()
        self.revert_weapon()

    def ce_advanced(self):
        # every weapon has a cooldown
        self.cooldown *= 0.75
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.75
        self.name += "_ADVANCED"
        self.desc += " (Rare) Recharges faster."
        self.title = "Advanced " + self.title
        if len(self.title) > 27:
            self.title = "Adv. " + self.title2
        self.short = "AD " + self.short
        self.cost *= 1.4
        self.weaponArt += "_ht_steel_bright"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_impacting(self):
        if self.breachChance < 10 and self.stunChance > 0 and self.ion < 1:
            self.name += "_IMPACTING"
            self.title = "Impacting " + self.title
            if len(self.title) > 27:
                self.title = "Impact. " + self.title2
            self.short = "IM " + self.short
            self.desc += " Impact: breach chance +1 stun chance +1"
            # must already have a stun chance, no need to set it
            if self.stunChance < 10:
                self.stunChance += 1
            self.breachChance_true = True
            # since breachChance must already be less than 10 no need to check
            self.breachChance += 1
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    # fire
    def ce_incendiary(self):
        if (self.fireChance < 7 and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_INCENDIARY"
            self.desc += " A bit more likely to start a fire."
            self.title = "Incendiary " + self.title
            if len(self.title) > 27:
                self.title = "Incend. " + self.title2
            self.short = "IN " + self.short
            self.cost *= 1.2
            self.image += "_red"
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_plasma(self):
        if (self.fireChance < 7 and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 2
            self.name += "_PLASMA"
            self.desc += " (Rare) Imbued with plasma, this weapon's more " \
                         "likely to start a fire."
            self.title = "Plasma " + self.title
            self.short = "PL " + self.short
            self.cost *= 1.3
            self.image += "_red"
            self.weaponArt += "_red"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_insulated(self):
        if (self.ion < 1 and self.fireChance > 1 and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            self.fireChance -= 1
            self.name += "_INSULATED"
            self.title = "Insulated " + self.title
            if len(self.title) > 27:
                self.title = "Insul. " + self.title2
            self.short = "in " + self.short
            self.desc += " Insulated: fire chance -1"
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heatshielded(self):
        if (self.ion < 1 and self.fireChance > 4 and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            self.fireChance -= 3
            self.name += "_HEATSHIELDED"
            self.title = "Heatshielded " + self.title
            if len(self.title) > 27:
                self.title = "Heatsh. " + self.title2
            self.short = "hea " + self.short
            self.desc += " Heatshielded: fire chance -3"
            self.cost *= 0.7
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # crew-damage only
    def ce_radioactive(self):
        if not ("BA_EFFECTOR_1" in self.name or
                "BA_EFFECTOR_2" in self.name or
                "BA_EFFECTOR_3" in self.name or
                "BA_BOMB_NANO_1" in self.name or
                "BA_BOMB_NANO_2" in self.name or
                "BOMB_HEAL_SYSTEM" in self.name or
                "BOMB_HEAL" in self.name or
                "BA_BOMB_HEAL_2" in self.name):
            # need to make it true when increasing, but not when decreasing
            self.persDamage_true = True
            self.persDamage += 1
            self.name += "_RADIOACTIVE"
            self.desc += " Radioactive elements make it deadlier to crew."
            self.title = "Radioactive " + self.title
            if len(self.title) > 27:
                self.title = "Rad. " + self.title2
            self.short = "RAD " + self.short
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe_nonlethal(self):
        # e.g. light scatter lasers?
            # negative persDamage values are not okay since that means
            # crew heal shenanigans since damage is less than 1
        if (self.ion < 1 and self.damage < 1 and self.persDamage > 0 and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            self.persDamage -= 1
            self.name += "_SAFE_NONLETHAL"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.persDamage == 0:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe(self):
        # clause added to avoid crew heal shenanigans
        if (self.ion < 1 and self.damage > 0 and
                self.persDamage != -self.damage and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            # since damage is at least 1, persDamage tag must be added
            self.persDamage_true = True
            self.persDamage -= 1
            # since damage is at least 1, persDamage will cancel out some crew
            # damage done just by regular damage, so negative values are okay
            self.name += "_SAFE"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.damage == 1:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_volatile(self):
        # if fire chance is already 10, then radioactive does the same thing
        if (self.fireChance < 10 and
                not ("BA_EFFECTOR_1" in self.name or
                     "BA_EFFECTOR_2" in self.name or
                     "BA_EFFECTOR_3" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            # adds a persDamage tag if one doesn't already exist
            self.persDamage_true = True
            self.persDamage += 1
            # same for fireChance
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_VOLATILE"
            self.title = "Volatile " + self.title
            if len(self.title) > 27:
                self.title = "Volat. " + self.title2
            self.short = "VOL " + self.short
            self.desc += " Releases volatile chemicals on impact."
            self.cost *= 1.3
            self.weaponArt += "_dirty"
            self.image += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_pulse(self):
        if (self.damage > 0 and self.shots < 2 and
                not ("BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            self.name += "_PULSE"
            self.title = "Pulse " + self.title
            if len(self.title) > 27:
                self.title = "Pul. " + self.title2
            self.short = "PUL " + self.short
            self.desc += " Pulse:  ion damage +1, cooldown x1.5"
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.ion += 1
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_overcharged(self):
        if self.shots < 3 and self.power < 4 and self.ion > 1:
            self.ion += 2
            self.power += 1
            self.name += "_OVERCHARGED"
            self.title = "Overcharg. " + self.title
            if len(self.title) > 27:
                self.title = "Overch. " + self.title2
            self.short = "OV " + self.short
            self.desc += " Overcharged: ion damage +1 power cost +1"
            self.cost *= 1.4
            self.weaponArt += "_ht_steel_bright"
            self.image += "_high"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowcharge(self):
        if self.ion > 1:
            self.ion -= 1
            self.name += "_LOWCHARGE"
            self.title = "Low Charge " + self.title
            if len(self.title) > 27:
                self.title = "Low Ch. " + self.title2
            self.short = "lwc " + self.short
            self.desc += " Low Charge: ion damage -1"
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_unstable(self):
        if self.ion > 1:
            self.ion -= 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.name += "_UNSTABLE"
            self.title = "Unstable " + self.title
            if len(self.title) > 27:
                self.title = "Unsta. " + self.title2
            self.short = "Un " + self.short
            self.desc += " Unstable: ion damage -1 system damage +1"
            self.cost *= 0.8
            self.weaponArt += "_purple"
            self.image += "_purple"
            self.generate_weapon()
            self.revert_weapon()

    def ce_flux(self):
        if self.ion > 1:
            self.ion -= 1
            self.stunChance_true = True
            self.stunChance += 3
            if self.stunChance > 10:
                self.stunChance = 10
            self.fireChance_true = True
            self.fireChance += 3
            if self.fireChance > 10:
                self.fireChance = 10
            self.name += "_FLUX"
            self.title = "Flux " + self.title
            self.short = "Fl " + self.short
            self.desc += " Flux: ion damage -1 stun chance +3 fire chance +3"
            self.cost *= 1.1
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_replicator(self):
        if (self.missiles > 0 and self.cooldown > 8 and
                not ("BA_MISSILES_ASTERIA" in self.name)):
            self.name += "_REPLICATOR"
            self.title = "Replicator " + self.title
            if len(self.title) > 27:
                self.title = "Replic. " + self.title2
            if len(self.title) > 27:
                self.title = "Repl. " + self.title2
            self.short = "RE " + self.short
            self.desc += " (Rare) Given time it can replicate its own ammo."
            # yeah, x2 is too much breh, but how much less???
            self.cooldown *= 1.3
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.3
            self.missiles = 0
            # does the cost justify the benefit?
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_high_tech"
            self.image += "_heavy_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highyield_bomb(self):
        if self.sysDamage > 0 and self.missiles > 0 and self.shots > 2:
            self.name += "_HIGHYIELD_BOMB"
            self.title = "High Yield " + self.title
            if len(self.title) > 27:
                self.title = "HighY. " + self.title2
            self.short = "HY " + self.short
            self.desc += " (Rare) Doubles bomb count at the cost of an " \
                         "additional missile."
            self.missiles += 1
            self.shots *= 2
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.cost *= 1.5
            self.weaponArt += "_steel"
            self.image += "_ht_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_wasteful(self):
        if self.missiles > 0:
            self.name += "_WASTEFUL"
            self.title = "Wasteful " + self.title
            if len(self.title) > 27:
                self.title = "Wast. " + self.title2
            self.short = "was " + self.short
            self.desc += " Needs another missile due to a jammed loader."
            self.missiles += 1
            self.cost *= 0.5
            self.weaponArt += "_dirty"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp_bomb(self):
        if self.missiles > 0 and self.shots < 2:
            self.name += "_EMP_BOMB"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " Its explosives deal a chunk of " \
                         "additional ion damage."
            self.ion += 2
            self.ion_true = True
            self.cost *= 1.3
            self.weaponArt += "_blue"
            self.image += "_blue"
            self.explosion = "explosion_big1_ion"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shredder_bomb(self):
        if (self.missiles > 0 and self.shots < 2 and
                not ("BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            self.name += "_SHREDDER_BOMB"
            self.title = "Shredder " + self.title
            if len(self.title) > 27:
                self.title = "Shred. " + self.title2
            self.short = "SHRE " + self.short
            self.desc += " (Rare) Enlaced spikes deal increased damage " \
                         "to systems and crew."
            self.persDamage_true = True
            self.persDamage += 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.cost *= 1.4
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_dirty_steel"
            self.image += "_dirty_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_caustic_bomb(self):
        if (self.missiles > 0 and self.breachChance < 10 and
                not ("BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL_SYSTEM" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            # makes sure the persDamage tag is there
            self.persDamage_true = True
            self.persDamage += 1
            # makes sure the breach tag is there
            self.breachChance_true = True
            self.breachChance += 1
            self.name += "_CAUSTIC_BOMB"
            self.title = "Caustic " + self.title
            if len(self.title) > 27:
                self.title = "Caus. " + self.title2
            self.short = "CAU " + self.short
            self.desc += " Corrodes organic and inorganic matter alike."
            self.cost *= 1.2
            self.weaponArt += "_green"
            self.image += "_green"
            self.generate_weapon()
            self.revert_weapon()

    def ce_submunition(self):
        if self.sysDamage > 1 and self.persDamage > 1 and self.shots < 2:
            self.name += "_SUBMUNITION"
            self.title = "Submunition " + self.title
            if len(self.title) > 27:
                self.title = "Submun. " + self.title2
            if len(self.title) > 27:
                self.title = "Subm. " + self.title2
            self.short = "Sub " + self.short
            self.desc += " Submunition: crew damage -1; system damage -1; " \
                         "teleports two bombs"
            self.persDamage -= 1
            self.sysDamage -= 1
            self.shots += 1
            self.cost *= 1.2
            self.weaponArt += "_high_tech"
            self.image += "_high_tech"
            self.generate_weapon()
            self.revert_weapon()

    # a cluster cluster bomb lol
    def ce_submunition_cluster(self):
        if self.shots > 2:
            self.name += "_SUBMUNITION_CLUSTER"
            self.title = "Submunition " + self.title
            if len(self.title) > 27:
                self.title = "Submun. " + self.title2
            if len(self.title) > 27:
                self.title = "Subm. " + self.title2
            self.short = "Sub " + self.short
            self.desc += " Submunition: bombs +1"
            self.shots += 1
            self.cost *= 1.4
            self.weaponArt += "_high_tech"
            self.image += "_high_tech"
            self.generate_weapon()
            self.revert_weapon()

    def ce_stungun(self):
        if 0 < self.stunChance < 8:
            self.name += "_STUNGUN"
            self.title = "Stun " + self.title
            self.short = "ST " + self.short
            self.desc += " Stun: stun chance +3"
            self.stunChance += 3
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shock(self):
        if 0 < self.stunChance < 6 and self.ion > 0:
            self.name += "_SHOCK"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun chance +5"
            self.stunChance += 5
            self.cost *= 1.3
            self.weaponArt += "_yellow"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_regulated(self):
        if self.stunChance > 0:
            self.name += "_REGULATED"
            self.title = "Regulated " + self.title
            if len(self.title) > 27:
                self.title = "Regul. " + self.title2
            self.short = "reg " + self.short
            if 0 < self.stunChance < 3:
                self.desc += " Due to regulations, " \
                             "its ability to stun was removed."
            else:
                self.desc += " Less likely to stun due to regulations."
            self.stunChance -= 2
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_concussion(self):
        if self.missiles > 0 and self.ion < 1 and self.stun > 0:
            self.name += "_CONCUSSION"
            self.title = "Concussion " + self.title
            if len(self.title) > 27:
                self.title = "Concuss. " + self.title2
            self.short = "CO " + self.short
            self.desc += " Concussion: stun time x1.5"
            self.stun *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_dark"
            self.image += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_predictable(self):
        if (self.missiles > 0 and 0 < self.stun < 5 and
                not ("BOMB_HEAL_SYSTEM" in self.name or
                     "BA_BOMB_NANO_1" in self.name or
                     "BA_BOMB_NANO_2" in self.name or
                     "BOMB_HEAL" in self.name or
                     "BA_BOMB_HEAL_2" in self.name)):
            self.name += "_PREDICTABLE"
            self.title = "Predictable " + self.title
            if len(self.title) > 27:
                self.title = "Predict. " + self.title2
            self.short = "pr " + self.short
            self.desc += " Predictable: cannot stun"
            self.stun = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            self.image += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # having <stun> guarantees stun
    def ce_calibrated(self):
        if self.ion > 0 and self.stun > 4:
            self.name += "_CALIBRATED"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun time +2"
            self.stun += 2
            self.cost *= 1.2
            self.weaponArt += "_high_tech_2"
            self.image += "_yellow"
            self.generate_weapon()
            self.revert_weapon()


class Burst(Weapon2):
    def __init__(self, f):
        super().__init__(f)
        self.lockdown, self.lockdown_true = 0, False
        self.shots = 1
        # check for speed_true only at creation
        self.speed, self.speed_true = 0, False
        # self.projectiles contains lists of length 3, indicating projectiles
        ''' each projectile has an int "count" value, a str "fake" value 
        ("false" or "true") and a str "image" value which is the weapon's 
        image, equivalent to other weapon-type's self.image attribute.'''
        self.projectiles = []
        self.radius = 17.5
        self.spin, self.spin_true = 720, False
        self.sp = 0
        self.missiles, self.missiles_true = 0, False
        self.hitShipSounds = []
        self.hitShieldSounds = []
        self.missSounds = []
        self.explosion, self.explosion_true = "", False
        self.droneTargetable, self.droneTargetable_true = 2, False
        self.droneTargetable_none = False
        self.chargeLevels, self.chargeLevels_true = 1, False
        '''################### DUPLICATES FOR REVERTING ###################'''
        self.lockdown2, self.lockdown_true2 = 0, False
        # check for speed_true only at creation
        self.shots2 = 1
        self.speed2, self.speed_true2 = 0, False
        self.projectiles2 = []
        self.radius2 = 17.5
        self.spin2, self.spin_true2 = 720, False
        self.sp2 = 0
        self.missiles2, self.missiles_true2 = 0, False
        self.hitShipSounds2 = []
        self.hitShieldSounds2 = []
        self.missSounds2 = []
        self.explosion2, self.explosion_true2 = "", False
        self.droneTargetable2, self.droneTargetable_true2 = 2, False
        self.droneTargetable_none2 = False
        self.chargeLevels2, self.chargeLevels_true2 = 1, False

    def revert_weapon(self):
        super().revert_weapon()
        self.lockdown, self.lockdown_true = self.lockdown2, self.lockdown_true2
        self.shots = self.shots2
        self.speed, self.speed_true = self.speed2, self.speed_true2
        self.projectiles.clear()
        for projectile in self.projectiles2:
            proj_stuff = []
            for proj_var in projectile:
                proj_stuff.append(proj_var)
            self.projectiles.append(proj_stuff)
        self.radius = self.radius2
        self.spin, self.spin_true = self.spin2, self.spin_true2
        self.sp = self.sp2
        self.missiles, self.missiles_true = self.missiles2, self.missiles_true2
        self.hitShipSounds.clear()
        for sound in self.hitShipSounds2:
            self.hitShipSounds.append(sound)
        self.hitShieldSounds.clear()
        for sound in self.hitShieldSounds2:
            self.hitShieldSounds.append(sound)
        self.missSounds.clear()
        for sound in self.missSounds2:
            self.missSounds.append(sound)
        self.explosion, self.explosion_true = \
            self.explosion2, self.explosion_true2
        self.droneTargetable = self.droneTargetable2
        self.droneTargetable_true = self.droneTargetable_true2
        self.droneTargetable_none = self.droneTargetable_none2
        self.chargeLevels, self.chargeLevels_true = \
            self.chargeLevels2, self.chargeLevels_true2

    def generate_weapon(self):
        """ regenerates this weapon in self.file based on all its attributes"""
        ''' tags that must be there (name isn't a tag)
        type, title, short, desc, tooltip, cooldown, power, cost, rarity,
        weaponArt, launchSounds, hitShipSounds '''
        self.file.write("<weaponBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>BURST</type>\n")
        if self.flavorType_true:
            self.file.write("\t<flavorType>" +
                            self.flavorType +
                            "</flavorType>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        if self.droneTargetable_none:
            self.file.write("\t<drone_targetable />\n")
        elif self.droneTargetable_true:
            self.file.write("\t<drone_targetable>" +
                            str(self.droneTargetable) +
                            "</drone_targetable>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<tooltip>" + self.tooltip + "</tooltip>\n")
        # round radius since float. makes for more accurate radius
        self.file.write("\t<radius>" + str(round(self.radius)) + "</radius>\n")
        if self.stun_true:
            # round stun since float. makes for more accurate stun time
            self.file.write("\t<stun>" + str(round(self.stun)) + "</stun>\n")
        if self.damage_true:
            self.file.write("\t<damage>" + str(self.damage) + "</damage>\n")
        if self.sysDamage_true:
            self.file.write(
                "\t<sysDamage>" + str(self.sysDamage) + "</sysDamage>\n")
        if self.persDamage_true:
            self.file.write(
                "\t<persDamage>" + str(self.persDamage) + "</persDamage>\n")
        if self.ion_true:
            self.file.write("\t<ion>" + str(self.ion) + "</ion>\n")
        self.file.write("\t<shots>" + str(self.shots) + "</shots>\n")
        # round speed since float. makes for more accurate speed
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        if self.missiles_true:
            self.file.write(
                "\t<missiles>" + str(self.missiles) + "</missiles>\n")
        self.file.write("\t<sp>" + str(self.sp) + "</sp>\n")
        if self.spin_true:
            self.file.write(
                "\t<spin>" + str(round(self.spin, 1)) + "</spin>\n")
        if self.fireChance_true:
            self.file.write(
                "\t<fireChance>" + str(self.fireChance) + "</fireChance>\n")
        if self.breachChance_true:
            self.file.write("\t<breachChance>" +
                            str(self.breachChance) +
                            "</breachChance>\n")
        if self.stunChance_true:
            self.file.write(
                "\t<stunChance>" + str(self.stunChance) + "</stunChance>\n")
        if self.lockdown_true:
            self.file.write(
                "\t<lockdown>" + str(self.lockdown) + "</lockdown>\n")
        if self.hullBust_true:
            self.file.write(
                "\t<hullBust>" + str(self.hullBust) + "</hullBust>\n")
        # since cooldown is a float, needs to round
        if self.cooldown < 10:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 2)) +
                            "</cooldown>\n")
        else:
            self.file.write("\t<cooldown>" + str(round(self.cooldown, 1)) +
                            "</cooldown>\n")
        # round since float
        self.file.write("\t<power>" + str(round(self.power)) + "</power>\n")
        # round cost since float. makes for more accurate prices
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        # default value, if for some reason the source is missing a <bp> tag
        # change if default value is changed
        if self.bp == 3:
            self.file.write("\t<bp>3</bp>\n")
        else:
            self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("\t<projectiles>\n")
        for i in range(len(self.projectiles)):
            self.file.write("\t\t<projectile count=\"" +
                            str(self.projectiles[i][0]) + "\" fake=\"" +
                            self.projectiles[i][1] + "\">" +
                            self.projectiles[i][2] + "</projectile>\n")
        self.file.write("\t</projectiles>\n")
        if self.boost_true:
            self.file.write("\t<boost>\n")
            self.file.write("\t\t<type>" + self.boost[0] + "</type>\n")
            self.file.write("\t\t<amount>" + str(round(self.boost[1], 3)) +
                            "</amount>\n")
            self.file.write("\t\t<count>" + str(self.boost[2]) + "</count>\n")
            self.file.write("\t</boost>\n")
        if self.explosion_true:
            self.file.write(
                "\t<explosion>" + self.explosion + "</explosion>\n")
        if self.chargeLevels_true:
            self.file.write("\t<chargeLevels>" + str(self.chargeLevels) +
                            "</chargeLevels>\n")
        self.file.write("\t<launchSounds>\n")
        for sound in self.launchSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</launchSounds>\n")
        self.file.write("\t<hitShipSounds>\n")
        for sound in self.hitShipSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShipSounds>\n")
        self.file.write("\t<hitShieldSounds>\n")
        for sound in self.hitShieldSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</hitShieldSounds>\n")
        self.file.write("\t<missSounds>\n")
        for sound in self.missSounds:
            self.file.write("\t\t<sound>" + sound + "</sound>\n")
        self.file.write("\t</missSounds>\n")
        self.file.write("\t<weaponArt>" + self.weaponArt + "</weaponArt>\n")
        self.file.write("</weaponBlueprint>\n")

    # rip support variation
    def ce_assault_missiles(self):
        if self.missiles > 0 and self.power < 4:
            self.name += "_ASSAULT_MISSILES"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += " Assault: cooldown x0.75 power cost +1"
            self.cooldown *= 0.75
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"

            self.generate_weapon()
            self.revert_weapon()

    def ce_stalker(self):
        if self.power < 4:
            self.name += "_STALKER"
            self.title = "Stalking " + self.title
            if len(self.title) > 27:
                self.title = "Stalk. " + self.title2
            self.short = "St " + self.short
            self.desc += " Stalking: " \
                         "cooldown x0.70 projectile speed x0.4 power cost +1"
            self.cooldown *= 0.7
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.7
            self.speed *= 0.4
            self.power += 1
            self.cost *= 1.1
            self.weaponArt += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heavy(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if (self.ion < 1 and self.damage == 1 and self.hullBust < 1 and
                num_shots < 4 and self.power < 4 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_HEAVY"
            self.title = "Heavy " + self.title
            self.short = "H " + self.short
            self.desc += " Heavy: damage +1 cooldown x1.5 power cost +1"
            self.damage += 1
            self.cooldown *= 1.5
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.5
            self.power += 1
            self.cost *= 1.4
            self.weaponArt += "_old"
            self.generate_weapon()
            self.revert_weapon()

    def ce_substandard(self):
        self.name += "_SUBSTANDARD"
        self.title = "Substandard " + self.title
        if len(self.title) > 27:
            self.title = "Subst. " + self.title2
        self.short = "sub " + self.short
        # self.desc += " Overall performance is substandard."
        # this doesn't really say much...
        self.desc += " Substandard: overall bad stats"
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.speed *= 0.9
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.stunChance -= 1
        if self.stunChance < 0:
            self.stunChance = 0
        self.cost *= 0.8
        self.weaponArt += "_slight_desat"
        self.generate_weapon()
        self.revert_weapon()

    def ce_surplus(self):
        if not ("BA_STUNGUN_1" in self.name or "BA_STUNGUN_2" in self.name):
            self.name += "_SURPLUS"
            self.title = "Surplus " + self.title
            self.short = "sur " + self.short
            self.desc += " Surplus: overall very bad stats"
            self.cooldown *= 1.2
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.2
            self.speed *= 0.8
            self.fireChance -= 3
            if self.fireChance < 0:
                self.fireChance = 0
            self.breachChance -= 3
            if self.breachChance < 0:
                self.breachChance = 0
            self.stunChance -= 3
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.5
            self.weaponArt += "_heavy_desat"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_quality(self):
        self.name += "_QUALITY"
        self.title = "Quality " + self.title
        self.short = "Q " + self.short
        self.desc += " Quality: overall better stats"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.speed *= 1.1
        self.cost *= 1.25
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_custom(self):
        if not ("BA_STUNGUN_1" in self.name or "BA_STUNGUN_2" in self.name):
            self.name += "_CUSTOM"
            self.title = "Custom " + self.title
            self.short = "C " + self.short
            self.desc += " Custom (Rare): overall great stats"
            self.cooldown *= 0.8
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.8
            self.speed *= 1.2
            self.fireChance_true = True
            self.fireChance += 1
            if self.fireChance > 10:
                self.fireChance = 10
            self.breachChance_true = True
            self.breachChance += 1
            if self.breachChance > 10:
                self.breachChance = 10
            self.stunChance_true = True
            self.stunChance += 1
            if self.stunChance > 10:
                self.stunChance = 10
            self.cost *= 1.5
            self.weaponArt += "_ht_steel_bright"
            for projectile in self.projectiles:
                projectile[2] += "_high_tech"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_vintage(self):
        self.name += "_VINTAGE"
        self.title = "Vintage " + self.title
        if len(self.title) > 27:
            self.title = "Vint. " + self.title2
        self.short = "Vin " + self.short
        self.desc += " Vintage: overall bad stats but valuable and rare"
        self.speed *= 0.9
        self.cooldown *= 1.1
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.1
        self.fireChance -= 1
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 1
        if self.breachChance < 0:
            self.breachChance = 0
        self.cost *= 1.5
        if self.rarity > 0:
            self.rarity += 2
            if self.rarity > 5:
                self.rarity = 5
        self.weaponArt += "_gritty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_antique(self):
        self.name += "_ANTIQUE"
        self.title = "Antique " + self.title
        if len(self.title) > 27:
            self.title = "Anti. " + self.title2
        self.short = "Ant " + self.short
        self.desc += " Antique: overall very bad stats but " \
                     "very valuable and rare"
        self.speed *= 0.7
        self.cooldown *= 1.4
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.4
        self.fireChance -= 3
        if self.fireChance < 0:
            self.fireChance = 0
        self.breachChance -= 3
        if self.breachChance < 0:
            self.breachChance = 0
        if self.rarity > 0:
            self.rarity += 4
            if self.rarity > 5:
                self.rarity = 5
        self.cost *= 2
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc += " Swag (Rare): good for showing off"
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_gold"
            self.generate_weapon()
            self.revert_weapon()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Secondhand " + self.title
        if len(self.title) > 27:
            self.title = "Sec. Hand " + self.title2
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_weapon()
        self.revert_weapon()

    # power-only
    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.weaponArt += "_dirty"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_optimized(self):
        if self.power > 2:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            if len(self.title) > 27:
                self.title = "Optim. " + self.title2
            if len(self.title) > 27:
                self.title = "Opt. " + self.title2
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.weaponArt += "_ht_steel"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # cooldown-only
    def ce_outdated(self):
        # every weapon has a cooldown
        self.cooldown *= 1.15
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.15
        self.name += "_OUTDATED"
        # self.desc += (" Drags on with a sub-par reload time.")
        self.desc += " Recharges slightly slower."
        self.title = "Outdated " + self.title
        if len(self.title) > 27:
            self.title = "Outd. " + self.title2
        self.short = "ou " + self.short
        self.cost *= 0.8
        self.weaponArt += "_dirty"
        self.generate_weapon()
        self.revert_weapon()

    def ce_obsolete(self):
        # every weapon has a cooldown
        self.cooldown *= 1.25
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 1.25
        self.name += "_OBSOLETE"
        self.desc += " Recharges slower."
        self.title = "Obsolete " + self.title
        if len(self.title) > 27:
            self.title = "Obsol. " + self.title2
        self.short = "ob " + self.short
        self.cost *= 0.6
        self.weaponArt += "_rust"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_upgraded(self):
        # every weapon has a cooldown
        self.cooldown *= 0.85
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.85
        self.name += "_UPGRADED"
        self.desc += " Recharges slightly faster."
        self.title = "Upgraded " + self.title
        if len(self.title) > 27:
            self.title = "Upgr. " + self.title2
        self.short = "UP " + self.short
        self.cost *= 1.2
        self.weaponArt += "_high_tech"

        self.generate_weapon()
        self.revert_weapon()

    def ce_advanced(self):
        # every weapon has a cooldown
        self.cooldown *= 0.75
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.75
        self.name += "_ADVANCED"
        self.desc += " (Rare) Recharges faster."
        self.title = "Advanced " + self.title
        if len(self.title) > 27:
            self.title = "Adv. " + self.title2
        self.short = "AD " + self.short
        self.cost *= 1.4
        self.weaponArt += "_ht_steel_bright"
        if self.rarity > 0:
            self.rarity += 1
            if self.rarity > 5:
                self.rarity = 5
        self.generate_weapon()
        self.revert_weapon()

    def ce_quickshot(self):
        self.name += "_QUICKSHOT"
        self.title = "Quickshot " + self.title
        if len(self.title) > 27:
            self.title = "Quick. " + self.title2
        self.short = "QU " + self.short
        self.desc += " Quickshot: cooldown x0.90 projectile speed x2"
        self.cooldown *= 0.9
        if self.boost_true and self.boost[0] == "cooldown":
            self.boost[1] *= 0.9
        self.cost *= 1.2
        self.speed *= 2
        self.weaponArt += "_high_tech"
        self.generate_weapon()
        self.revert_weapon()

    def ce_widespread_flak(self):
        if self.ion < 1 and self.stun < 5 and self.radius > 10:
            self.name += "_WIDESPREAD_FLAK"
            self.title = "Wide Sp. " + self.title
            self.short = "wid " + self.short
            self.desc += " Wide Spread: targeting radius x1.25"
            self.radius *= 1.25
            self.cost *= 0.75
            self.weaponArt += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_tightspread_flak(self):
        if self.ion < 1 and self.stun < 5 and self.radius > 10:
            self.name += "_TIGHTSPREAD_FLAK"
            self.title = "Tight Sp. " + self.title
            self.short = "TIG " + self.short
            self.desc += " Tight Spread: targeting radius x0.75"
            self.radius *= 0.75
            self.cost *= 1.25
            self.weaponArt += "_dirty_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_impacting(self):
        if self.breachChance < 10 and self.stunChance > 0 and self.ion < 1:
            self.name += "_IMPACTING"
            self.title = "Impacting " + self.title
            if len(self.title) > 27:
                self.title = "Impact. " + self.title2
            self.short = "IM " + self.short
            self.desc += " Impact: breach chance +1 stun chance +1"
            # must already have a stun chance, no need to set it
            if self.stunChance < 10:
                self.stunChance += 1
            self.breachChance_true = True
            # since breachChance must already be less than 10 no need to check
            self.breachChance += 1
            self.cost *= 1.1
            for projectile in self.projectiles:
                projectile[2] += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    # stungun shouldn't be in here, right? Right?? RIGHT???
    def ce_penetrating(self):
        if (self.ion < 1 and self.breachChance < 10 and
                "BA_STUNGUN_1" not in self.name and
                "BA_STUNGUN_2" not in self.name):
            self.name += "_PENETRATING"
            self.title = "Penetr. " + self.title
            self.short = "PE " + self.short
            self.desc += " Penetrating: " \
                         "breach chance +1 projectile speed x1.10"
            self.speed *= 1.1
            # breachChance must be 9 or less
            self.breachChance += 1
            self.breachChance_true = True
            self.cost *= 1.2
            self.weaponArt += "_dirty_steel"
            for projectile in self.projectiles:
                projectile[2] += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_breaching(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if self.ion < 1 and self.breachChance < 9 and num_shots < 3:
            self.name += "_BREACHING"
            self.title = "Breaching " + self.title
            if len(self.title) > 27:
                self.title = "Breach. " + self.title2
            self.short = "BR " + self.short
            self.desc += " Breaching (Rare): " \
                         "breach chance +2 projectile speed x1.30"
            self.speed *= 1.3
            # breachChance must be 8 or less
            self.breachChance += 2
            self.breachChance_true = True
            self.cost *= 1.4
            self.weaponArt += "_steel"
            for projectile in self.projectiles:
                projectile[2] += "_dark"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # fire
    def ce_incendiary(self):
        if (self.fireChance < 7 and
                not ("BA_PLASMA_1" in self.name or
                     "BA_PLASMA_2" in self.name or
                     "BA_STUNGUN_1" in self.name or
                     "BA_STUNGUN_2" in self.name)):
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_INCENDIARY"
            self.desc += " A bit more likely to start a fire."
            self.title = "Incendiary " + self.title
            if len(self.title) > 27:
                self.title = "Incend. " + self.title2
            self.short = "IN " + self.short
            self.cost *= 1.2
            for projectile in self.projectiles:
                projectile[2] += "_red"
            self.weaponArt += "_rust"
            self.generate_weapon()
            self.revert_weapon()

    def ce_plasma(self):
        if (self.fireChance < 7 and
                not ("BA_PLASMA_1" in self.name or
                     "BA_PLASMA_2" in self.name or
                     "BA_STUNGUN_1" in self.name or
                     "BA_STUNGUN_2" in self.name)):
            # adds a fire chance tag if one doesn't already exist
            self.fireChance_true = True
            self.fireChance += 2
            self.name += "_PLASMA"
            self.desc += " (Rare) Imbued with plasma, this weapon's more " \
                         "likely to start a fire."
            self.title = "Plasma " + self.title
            self.short = "PL " + self.short
            self.cost *= 1.3
            for projectile in self.projectiles:
                projectile[2] += "_red"
            self.weaponArt += "_red"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_fusion_plasma(self):
        if "BA_PLASMA_1" in self.name or "BA_PLASMA_2" in self.name:
            self.name += "_FUSION_PLASMA"
            self.title = "Fusion " + self.title
            if len(self.title) > 27:
                self.title = "Fus. " + self.title2
            # changed from FU because, well you know...
            self.short = "FUS " + self.short
            self.desc += " Fusion: fire chance +3"
            # fireChance tag is already there
            self.fireChance += 3
            if self.fireChance > 10:
                self.fireChance = 10
            self.cost *= 1.3
            self.weaponArt += "_red"
            # change the image
            for projectile in self.projectiles:
                projectile[2] += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_insulated(self):
        if self.ion < 1 and self.fireChance > 1:
            self.fireChance -= 1
            self.name += "_INSULATED"
            self.title = "Insulated " + self.title
            if len(self.title) > 27:
                self.title = "Insul. " + self.title2
            self.short = "in " + self.short
            self.desc += " Insulated: fire chance -1"
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heatshielded(self):
        if self.ion < 1 and self.fireChance > 4:
            self.fireChance -= 3
            self.name += "_HEATSHIELDED"
            self.title = "Heat Shielded " + self.title
            if len(self.title) > 27:
                self.title = "H. Shield " + self.title2
            if len(self.title) > 27:
                self.title = "Heat Sh. " + self.title2
            self.short = "hea " + self.short
            self.desc += " Heatshielded: fire chance -3"
            self.cost *= 0.7
            self.weaponArt += "_heavy_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    # crew-damage only
    def ce_radioactive(self):
        if not ("BA_STUNGUN_1" in self.name or "BA_STUNGUN_2" in self.name):
            # need to make it true when increasing, but not when decreasing
            self.persDamage_true = True
            self.persDamage += 1
            self.name += "_RADIOACTIVE"
            self.desc += " Radioactive elements make it deadlier to crew."
            self.title = "Radioactive " + self.title
            if len(self.title) > 27:
                self.title = "Rad. " + self.title2
            self.short = "RAD " + self.short
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            for projectile in self.projectiles:
                projectile[2] += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe_nonlethal(self):
        # e.g. light scatter lasers?
            # negative persDamage values are not okay since that means
            # crew heal shenanigans since damage is less than 1
        if (self.ion < 1 and self.damage < 1 and self.persDamage > 0 and
                not ("BA_STUNGUN_1" in self.name or
                     "BA_STUNGUN_2" in self.name)):
            self.persDamage -= 1
            self.name += "_SAFE_NONLETHAL"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.persDamage == 0:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_safe(self):
        # clause added to avoid crew heal shenanigans
        if (self.ion < 1 and self.damage > 0 and
                self.persDamage != -self.damage and
                not ("BA_STUNGUN_1" in self.name or
                     "BA_STUNGUN_2" in self.name)):
            # since damage is at least 1, persDamage tag must be added
            self.persDamage_true = True
            self.persDamage -= 1
            # since damage is at least 1, persDamage will cancel out some crew
            # damage done just by regular damage, so negative values are okay
            self.name += "_SAFE"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            if self.damage == 1:
                self.desc += " Unable to damage crew due to regulations."
            else:
                self.desc += " Less able to damage crew due to regulations."
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_volatile(self):
        # if fire chance is already 10, then radioactive does the same thing
        if (self.fireChance < 10 and
                not ("BA_STUNGUN_1" in self.name or
                     "BA_STUNGUN_2" in self.name)):
            # adds a persDamage tag if one doesn't already exist
            self.persDamage_true = True
            self.persDamage += 1
            # same for fireChance
            self.fireChance_true = True
            self.fireChance += 1
            self.name += "_VOLATILE"
            self.title = "Volatile " + self.title
            if len(self.title) > 27:
                self.title = "Volat. " + self.title2
            self.short = "VOL " + self.short
            self.desc += " Releases volatile chemicals on impact."
            self.cost *= 1.3
            self.weaponArt += "_dirty"
            for projectile in self.projectiles:
                projectile[2] += "_red"
            self.generate_weapon()
            self.revert_weapon()

    def ce_heavy_ion(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if self.ion == 1 and num_shots < 4:
            self.name += "_HEAVY_ION"
            self.title = "Heavy " + self.title
            self.short = "H " + self.short
            self.desc += " Heavy: ion damage +1 cooldown x1.7"
            self.cooldown *= 1.7
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.7
            self.ion += 1
            self.cost *= 1.4
            self.weaponArt += "_blue"
            for projectile in self.projectiles:
                projectile[2] += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_perfect(self):
        if self.ion == 1 and self.power > 1:
            self.name += "_PERFECT"
            self.title = "Perfect " + self.title
            if len(self.title) > 27:
                self.title = "Perf. " + self.title2
            self.short = "PER " + self.short
            self.desc += " Perfect (Epic): power cost -1, cooldown x0.8"
            self.cooldown *= 0.8
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 0.8
            self.power -= 1
            self.cost *= 1.5
            self.weaponArt += "_ht_steel_bright"
            for projectile in self.projectiles:
                projectile[2] += "heavy_desat"
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.generate_weapon()
            self.revert_weapon()

    def ce_replicator(self):
        if (self.missiles > 0 and self.cooldown > 8 and
                not ("BA_MISSILES_ASTERIA" in self.name)):
            self.name += "_REPLICATOR"
            self.title = "Replicator " + self.title
            if len(self.title) > 27:
                self.title = "Replic. " + self.title2
            if len(self.title) > 27:
                self.title = "Repl. " + self.title2
            self.short = "RE " + self.short
            self.desc += " (Rare) Given time it can replicate its own ammo."
            # yeah, x2 is too much breh, but how much less???
            self.cooldown *= 1.3
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] *= 1.3
            self.missiles = 0
            # does the cost justify the benefit?
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_high_tech"
            for projectile in self.projectiles:
                projectile[2] += "_heavy_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highyield(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if (self.missiles > 0 and num_shots < 2 and
                self.damage > 1 and self.cooldown > 10 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_HIGHYIELD"
            self.title = "High Yield " + self.title
            if len(self.title) > 27:
                self.title = "HighY. " + self.title2
            self.short = "HY " + self.short
            self.desc += " (Rare) Does more damage at the cost of an " \
                         "additional missile."
            self.missiles += 1
            # check for mines
            if self.sysDamage < 0 and self.persDamage < 0:
                self.sysDamage -= 2
                self.persDamage -= 2
            self.damage += 2
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            # mines support these image suffixes, right? Right??
            self.weaponArt += "_steel"
            for projectile in self.projectiles:
                projectile[2] += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_alpha(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if (self.missiles > 0 and num_shots < 2 and
                self.damage > 1 and self.cooldown > 10 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_ALPHA"
            self.title = "Alpha " + self.title
            self.short = "AL " + self.short
            # gotta come up with an epic description...
            self.desc += " Alpha (Epic): cooldown x0.5, damage +1"
            # check for mines
            if self.sysDamage < 0 and self.persDamage < 0:
                self.sysDamage -= 1
                self.persDamage -= 1
            self.damage += 1
            self.cooldown /= 2
            if self.boost_true and self.boost[0] == "cooldown":
                self.boost[1] /= 2
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity += 4
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_ht_steel_bright"
            for projectile in self.projectiles:
                projectile[2] += "_ht_steel_bright"
            self.generate_weapon()
            self.revert_weapon()

    def ce_wasteful(self):
        if self.missiles > 0:
            self.name += "_WASTEFUL"
            self.title = "Wasteful " + self.title
            if len(self.title) > 27:
                self.title = "Wast. " + self.title2
            self.short = "was " + self.short
            self.desc += " Needs another missile due to a jammed loader."
            self.missiles += 1
            self.cost *= 0.5
            self.weaponArt += "_dirty"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_frail(self):
        if self.missiles > 0:
            self.name += "_FRAIL"
            self.title = "Frail " + self.title
            self.short = "fr " + self.short
            self.desc += " Frail: shield piercing -3"
            self.sp -= 3
            if self.sp < 0:
                self.sp = 0
            self.cost *= 0.75
            self.weaponArt += "_heavy_desat"
            for projectile in self.projectiles:
                projectile[2] += "_dirty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_highvelocity(self):
        if self.missiles > 0:
            self.name += "_HIGHVELOCITY"
            self.title = "High Vel. " + self.title
            if len(self.title) > 27:
                self.title = "HighV. " + self.title2
            self.short = "HI " + self.short
            self.desc += " High Velocity: projectile speed x1.5"
            self.speed *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_gritty"
            for projectile in self.projectiles:
                projectile[2] += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_boosted_missile(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if self.missiles > 0 and num_shots < 3:
            self.name += "_BOOSTED_MISSILE"
            self.title = "Boosted " + self.title
            if len(self.title) > 27:
                self.title = "Boost. " + self.title2
            self.short = "BO " + self.short
            self.desc += " Boosted: projectile speed x2.5"
            self.speed *= 2.5
            self.cost *= 1.3
            self.weaponArt += "_gritty"
            for projectile in self.projectiles:
                projectile[2] += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_lowvelocity(self):
        if self.missiles > 0:
            self.name += "_LOW_VELOCITY"
            self.title = "Low Vel. " + self.title
            if len(self.title) > 27:
                self.title = "LowV. " + self.title2
            self.short = "low " + self.short
            self.desc += " Low Velocity: projectile speed x0.6"
            self.speed *= 0.6
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_torpedo(self):
        # self.speed check for mines
        if (self.missiles > 0 and self.damage > 1 and
                self.damage >= 0 and self.cooldown > 10 and
                self.speed > 12 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_TORPEDO"
            self.title = "Torpedo " + self.title
            if len(self.title) > 27:
                self.title = "Torp. " + self.title2
            self.short = "TOR " + self.short
            self.desc += " Torpedo: damage +1, projectile speed x0.5"
            self.speed *= 0.5
            self.damage += 1
            self.cost *= 1.2
            self.weaponArt += "_steel"
            for projectile in self.projectiles:
                projectile[2] += "_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if (self.missiles > 0 and num_shots < 2 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_EMP"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " EMP: ion damage +3 shield piercing -5"
            self.desc += " Its ion-wrapped missile deals hefty ion damage " \
                         "but is consequently unable to pierce through " \
                         "shields."
            self.ion += 3
            self.ion_true = True
            self.sp -= 5
            if self.sp < 0:
                self.sp = 0
            self.cost *= 1.3
            self.weaponArt += "_blue"
            for projectile in self.projectiles:
                projectile[2] += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_emp_burst(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if (self.missiles > 0 and num_shots > 1 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_EMP_BURST"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " Its ion-coated missiles deal some added " \
                         "ion damage but are consequently unable to " \
                         "pierce through shields."
            self.ion += 1
            self.ion_true = True
            self.sp -= 5
            if self.sp < 0:
                self.sp = 0
            self.cost *= 1.3
            self.weaponArt += "_blue"
            for projectile in self.projectiles:
                projectile[2] += "_blue"
            self.generate_weapon()
            self.revert_weapon()

    def ce_frag(self):
        if self.missiles > 0 and self.damage > 0:
            self.name += "_FRAG"
            self.title = "Frag " + self.title
            self.short = "Frag " + self.short
            self.desc += " Explodes into fragments upon impact, piercing " \
                         "systems and crew, at the cost of hull damage."
            self.damage -= 1
            self.persDamage_true = True
            self.persDamage += 2
            self.sysDamage_true = True
            self.sysDamage += 2
            self.cost *= 1.30
            self.weaponArt += "_gritty"
            for projectile in self.projectiles:
                projectile[2] += "_gritty"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shredder(self):
        num_shots = 0
        # [int, str, str]
        for projectile in self.projectiles:
            if projectile[1] == "false":
                num_shots += projectile[0]
                # num_shots is # of real projectiles
        if self.chargeLevels_true:
            # if num_shots > 1, you have charge flak shenanigans
            num_shots *= self.chargeLevels
        num_shots *= self.shots
        if (self.missiles > 0 and num_shots < 2 and
                not ("BA_SHOTGUN_MISSILES" in self.name)):
            self.name += "_SHREDDER"
            self.title = "Shredder " + self.title
            if len(self.title) > 27:
                self.title = "Shred. " + self.title2
            self.short = "SHRE " + self.short
            self.desc += " (Rare) Enlaced spikes deal increased damage " \
                         "to systems and crew."
            self.persDamage_true = True
            self.persDamage += 1
            self.sysDamage_true = True
            self.sysDamage += 1
            self.cost *= 1.4
            if self.rarity > 0:
                self.rarity += 1
                if self.rarity > 5:
                    self.rarity = 5
            self.weaponArt += "_dirty_steel"
            for projectile in self.projectiles:
                projectile[2] += "_dirty_steel"
            self.generate_weapon()
            self.revert_weapon()

    def ce_caustic(self):
        # why exclude mines??
        if self.missiles > 0 and self.breachChance < 10:
            # makes sure the persDamage tag is there
            self.persDamage_true = True
            self.persDamage += 1
            # makes sure the breach tag is there
            self.breachChance_true = True
            self.breachChance += 1
            self.name += "_CAUSTIC"
            self.title = "Caustic " + self.title
            if len(self.title) > 27:
                self.title = "Caus. " + self.title2
            self.short = "CAU " + self.short
            self.desc += " Corrodes organic and inorganic matter alike."
            self.cost *= 1.2
            self.weaponArt += "_green"
            for projectile in self.projectiles:
                projectile[2] += "_green"
            self.generate_weapon()
            self.revert_weapon()

    def ce_stungun(self):
        if 0 < self.stunChance < 8:
            self.name += "_STUNGUN"
            self.title = "Stun " + self.title
            self.short = "ST " + self.short
            self.desc += " Stun: stun chance +3"
            self.stunChance += 3
            self.cost *= 1.2
            self.weaponArt += "_yellow"
            for projectile in self.projectiles:
                projectile[2] += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_shock(self):
        if 0 < self.stunChance < 6 and self.ion > 0:
            self.name += "_SHOCK"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun chance +5"
            self.stunChance += 5
            self.cost *= 1.3
            self.weaponArt += "_yellow"
            for projectile in self.projectiles:
                projectile[2] += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_regulated(self):
        if self.stunChance > 0:
            self.name += "_REGULATED"
            self.title = "Regulated " + self.title
            if len(self.title) > 27:
                self.title = "Regul. " + self.title2
            self.short = "reg " + self.short
            if 0 < self.stunChance < 3:
                self.desc += " Due to regulations, " \
                             "its ability to stun was removed."
            else:
                self.desc += " Less likely to stun due to regulations."
            self.stunChance -= 2
            if self.stunChance < 0:
                self.stunChance = 0
            self.cost *= 0.9
            self.weaponArt += "_slight_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    def ce_concussion(self):
        if self.missiles > 0 and self.ion < 1 and self.stun > 0:
            self.name += "_CONCUSSION"
            self.title = "Concussion " + self.title
            if len(self.title) > 27:
                self.title = "Concuss. " + self.title2
            self.short = "CO " + self.short
            self.desc += " Concussion: stun time x1.5"
            self.stun *= 1.5
            self.cost *= 1.1
            self.weaponArt += "_dark"
            for projectile in self.projectiles:
                projectile[2] += "_dark"
            self.generate_weapon()
            self.revert_weapon()

    def ce_predictable(self):
        if self.missiles > 0 and 0 < self.stun < 5:
            self.name += "_PREDICTABLE"
            self.title = "Predictable " + self.title
            if len(self.title) > 27:
                self.title = "Predict. " + self.title2
            self.short = "pr " + self.short
            self.desc += " Predictable: cannot stun"
            self.stun = 0
            self.cost *= 0.8
            self.weaponArt += "_slight_desat"
            for projectile in self.projectiles:
                projectile[2] += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()

    # having <stun> guarantees stun
    def ce_calibrated(self):
        if self.ion > 0 and self.stun > 4 and self.missiles < 1:
            self.name += "_CALIBRATED"
            self.title = "Shock " + self.title
            self.short = "SH " + self.short
            self.desc += " Shock: stun time +2"
            self.stun += 2
            self.cost *= 1.2
            self.weaponArt += "_high_tech_2"
            for projectile in self.projectiles:
                projectile[2] += "_yellow"
            self.generate_weapon()
            self.revert_weapon()

    def ce_calibrated_stungun(self):
        if self.stun > 4 and self.missiles < 1:
            self.name += "_CALIBRATED_STUNGUN"
            self.title = "Intense " + self.title
            if len(self.title) > 27:
                self.title = "Int. " + self.title2
            self.short = "INT " + self.short
            self.desc += " Intense: stun time x1.25"
            self.stun *= 1.25
            self.cost *= 1.2
            self.weaponArt += "_high_tech_2"
            self.generate_weapon()
            self.revert_weapon()

    def ce_predictable_stungun(self):
        if self.stun > 4 and self.missiles < 1:
            self.name += "_PREDICTABLE_STUNGUN"
            self.title = "Predictable " + self.title
            if len(self.title) > 27:
                self.title = "Predict. " + self.title2
            if len(self.title) > 27:
                self.title = "Pred. " + self.title2
            self.short = "pr " + self.short
            self.desc += " Predictable: stun time -2"
            self.stun -= 2
            self.cost *= 0.7
            self.weaponArt += "_slight_desat"
            self.generate_weapon()
            self.revert_weapon()


class Drone:
    def __init__(self, f):
        # the file to write this Drone or any of its modified versions to
        self.file = f
        # name of this droneBlueprint
        self.name, self.name2 = "", ""
        # all drones can have this, but can be left out
        self.tip, self.tip_true = "", False
        self.tip2, self.tip_true2 = "", False
        # title displayed in UI box.
        self.title, self.title2 = "", ""
        # shorter version of title. cannot be too long.
        self.short, self.short2 = "", ""
        # displayed in UI box and tooltip.
        self.desc, self.desc2 = "", ""
        # power requirement. can be set to values less than 1.
        self.power, self.power2 = 1, 1
        # cost in stores. sell value is floor(cost/2)
        self.cost, self.cost2 = 0, 0
        # unimplemented build point functionality. needed?
        self.bp, self.bp2 = 3, 3
        # rarity in loot pool, 1-5, where 5 is "rarest". 0 is unobtainable
        self.rarity, self.rarity2 = 0, 0

    def revert_drone(self):
        # how to implement this for weaponBlueprint?
        self.name = self.name2
        self.tip, self.tip_true = self.tip2, self.tip_true2
        self.title = self.title2
        self.short = self.short2
        self.desc = self.desc2
        self.power = self.power2
        self.cost = self.cost2
        self.bp = self.bp2
        self.rarity = self.rarity2

    def generate_drone(self):
        # this function encompasses writing this Drone based on its attributes
        # but first we need to get its attributes!
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>" + "self.dtype" + "</type>\n")
        # if self.dtype == "BOARDER" or self.dtype == "BATTLE":
        #    self.file.write("\t<locked>" + str(self.locked) + "</locked>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        # if self.dtype == "DEFENSE":
        #    self.file.write("\t<level>" + str(self.level) + "</level>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        # if self.dtype == "DEFENSE" or self.dtype == "COMBAT":
        #    self.file.write("\t<cooldown>" + str(round(self.cooldown)) +
        #                    "</cooldown>\n")
        # if self.dtype == "DEFENSE" or self.dtype == "COMBAT":
        #    self.file.write("\t<dodge>" + str(round(self.dodge)) +
        #                    "</dodge>\n")
        # if self.dtype != "REPAIR" and self.dtype != "BATTLE":
        #    self.file.write("\t<speed>" + str(round(self.speed)) +
        #                    "</speed>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        # if self.dtype == "SHIP_REPAIR" or self.dtype == "DEFENSE" or \
        #        self.dtype == "COMBAT":
        #    self.file.write("\t<droneImage>" + self.droneImage +
        #                    "</droneImage>\n")
        # if self.dtype == "SHIP_REPAIR":
        #    self.file.write("\t<image>" + self.image + "</image>\n")
        # if self.dtype == "DEFENSE" or self.dtype == "COMBAT":
        #    self.file.write("\t<weaponBlueprint>" + self.weaponBlueprint +
        #                    "</weaponBlueprint>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")


class DefenseDrone(Drone):
    def __init__(self, f):
        super().__init__(f)
        # only for dtype DEFENSE. what do the levels mean??
        self.level, self.level2 = 0, 0
        # only for anti-drones
        self.target, self.target_true = "", False
        self.target2, self.target_true2 = "", False
        # dtype DEFENSE cooldown between shots, might be different from weapon
        self.cooldown, self.cooldown2 = 1, 1
        # dtypes COMBAT and DEFENSE weaponry used
        self.weaponBlueprint, self.weaponBlueprint2 = "", ""
        self.weapon = Weapon2(self.file)
        # dtype DEFENSE visual change
        self.speed, self.speed2 = 1, 1
        # drone evade chance
        # resistance against stray projectiles or asteroids
        self.dodge, self.dodge2 = 0, 0
        # refers to set of images found in ship\drones
        self.droneImage, self.droneImage2 = "", ""

    def revert_drone(self):
        super().revert_drone()
        self.level = self.level2
        self.target, self.target_true = self.target2, self.target_true2
        self.cooldown = self.cooldown2
        self.weaponBlueprint = self.weaponBlueprint2
        self.weapon.revert_weapon()
        self.speed = self.speed2
        self.dodge = self.dodge2
        self.droneImage = self.droneImage2

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>DEFENSE</type>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        if self.target_true:
            self.file.write("\t<target>" + self.target + "</target>\n")
        self.file.write("\t<level>" + str(self.level) + "</level>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write(
            "\t<cooldown>" + str(round(self.cooldown)) + "</cooldown>\n")
        self.file.write("\t<dodge>" + str(round(self.dodge)) + "</dodge>\n")
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<droneImage>" + self.droneImage + "</droneImage>\n")
        self.file.write("\t<weaponBlueprint>" +
                        self.weaponBlueprint +
                        "</weaponBlueprint>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")
        if self.weaponBlueprint != self.weaponBlueprint2:
            self.weapon.generate_weapon()

    def ce_simple(self):
        self.name += "_SIMPLE"
        self.title = "Simple " + self.title
        self.short = "sim " + self.short
        self.desc += " Simple: reload time x1.15"
        self.cooldown *= 1.15
        self.cost *= 0.9
        self.droneImage = "slight_desat_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_unresponsive(self):
        self.name += "_UNRESPONSIVE"
        self.title = "Unresponsive " + self.title
        if len(self.title) > 27:
            self.title = "Unrespons. " + self.title2
        if len(self.title) > 27:
            self.title = "Unrespon. " + self.title2
        if len(self.title) > 27:
            self.title = "Unresp. " + self.title2
        self.short = "un " + self.short
        self.desc += " Unresponsive: reload time x1.25"
        self.cooldown *= 1.25
        self.cost *= 0.8
        if 0 < self.rarity < 5:
            self.rarity += 1
        self.droneImage = "heavy_desat_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_active(self):
        self.name += "_ACTIVE"
        self.title = "Active " + self.title
        self.short = "ACT " + self.short
        self.desc += " Active: reload time x0.85"
        self.cooldown *= 0.85
        self.cost *= 1.1
        self.droneImage = "high_tech_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_frantic(self):
        self.name += "_FRANTIC"
        self.title = "Frantic " + self.title
        self.short = "FR " + self.short
        self.desc += " Frantic (Rare): reload time x0.75"
        self.cooldown *= 0.75
        self.cost *= 1.2
        if 0 < self.rarity < 5:
            self.rarity += 1
        self.droneImage = "ht_steel_bright_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_sentient(self):
        if (self.level == 1 and
                "ANTI_DRONE" not in self.name and
                "DE_ANTI_DRONE_2" not in self.name and
                "DE_ANTI_DRONE_EFFECTOR" not in self.name and
                "DE_ANTI_DRONE_MISSILES" not in self.name and
                "DE_ANTI_DRONE_LASER_HEAVY" not in self.name):
            self.name += "_SENTIENT"
            self.title = "Sentient " + self.title
            self.short = "SEN " + self.short
            self.desc += \
                " Sentient (Epic): targets all projectiles, " \
                "reload time x0.75, evade +3"
            self.level += 1
            self.cooldown *= 0.75
            self.dodge += 3
            if self.dodge > 10:
                self.dodge = 10
            self.cost *= 1.5
            if 0 < self.rarity < 5:
                self.rarity = 5
            self.droneImage = "ht_steel_bright_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    # aka dumb
    def ce_basic(self):
        if (self.level == 2 and
                "ANTI_DRONE" not in self.name and
                "DE_ANTI_DRONE_2" not in self.name and
                "DE_ANTI_DRONE_EFFECTOR" not in self.name and
                "DE_ANTI_DRONE_MISSILES" not in self.name and
                "DE_ANTI_DRONE_LASER_HEAVY" not in self.name):
            self.name += "_BASIC"
            self.title = "Basic " + self.title
            self.short = "bas " + self.short
            self.desc += " Basic: can only target missiles"
            self.level -= 1
            self.cost *= 0.8
            self.droneImage = "slight_desat_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_smart(self):
        if (self.level == 1 and
                "ANTI_DRONE" not in self.name and
                "DE_ANTI_DRONE_2" not in self.name and
                "DE_ANTI_DRONE_EFFECTOR" not in self.name and
                "DE_ANTI_DRONE_MISSILES" not in self.name and
                "DE_ANTI_DRONE_LASER_HEAVY" not in self.name):
            self.name += "_SMART"
            self.title = "Smart " + self.title
            self.short = "SMA " + self.short
            self.desc += " Smart: targets all projectiles"
            self.level += 1
            self.cost *= 1.3
            self.droneImage = "high_tech_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    # not just defense drone
    def ce_highvelocity(self):
        if "DE_ANTI_DRONE_EFFECTOR" not in self.name:
            self.name += "_HIGHVELOCITY"
            self.title = "High Vel. " + self.title
            self.short = "HV " + self.short
            self.desc += " High Velocity: projectile speed x1.25"
            self.weaponBlueprint += "_HIGHVELOCITY_DRONE_WEAPON"
            self.weapon.name += "_HIGHVELOCITY_DRONE_WEAPON"

            self.weapon.speed *= 1.25
            self.weapon.image += "_high_tech"

            self.cost *= 1.1
            self.droneImage = "gritty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_lowvelocity(self):
        if "DE_ANTI_DRONE_EFFECTOR" not in self.name:
            self.name += "_LOWVELOCITY"
            self.title = "Low Vel. " + self.title
            self.short = "low " + self.short
            self.desc += " Low Velocity: projectile speed x0.75"
            self.weaponBlueprint += "_LOWVELOCITY_DRONE_WEAPON"
            self.weapon.name += "_LOWVELOCITY_DRONE_WEAPON"

            self.weapon.speed *= 0.75
            self.weapon.image += "_slight_desat"

            self.cost *= 0.9
            self.droneImage = "slight_desat_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc = " Swag: good for showing off"
            if self.rarity > 0:
                self.rarity = 5
            self.cost *= 1.5
            self.droneImage = "gold_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Sec. Hand " + self.title
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_drone()
        self.revert_drone()

    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "dirty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_optimized(self):
        if self.power > 1:
            self.name += "_OPTIMIZED"
            self.title = "Optim. " + self.title
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "ht_steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_autonomous(self):
        if self.power < 3:
            self.name += "_AUTONOMOUS"
            self.title = "Autonomous " + self.title
            self.short = "A " + self.short
            self.desc += " Autonomous (Epic): requires no power"
            self.power = 0
            self.cost *= 1.5
            if 0 < self.rarity < 5:
                self.rarity = 5
            self.droneImage = "ht_steel_bright_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_fast(self):
        self.name += "_FAST"
        self.title = "Fast " + self.title
        self.short = "F " + self.short
        self.desc += " Fast: movement speed x1.05"
        self.speed *= 1.05
        self.cost *= 1.1
        self.droneImage = "high_tech_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_boosted(self):
        self.name += "_BOOSTED"
        self.title = "Boosted " + self.title
        self.short = "B " + self.short
        self.desc += " Boosted: movement speed x1.1; evade +1"
        self.speed *= 1.1
        if self.dodge < 10:
            self.dodge += 1
        self.cost *= 1.2
        self.droneImage = "ht_steel_bright_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_more_dodge(self):
        if self.dodge < 9:
            self.name += "_MORE_DODGE"
            self.title = "Low Profile " + self.title
            self.short = "LoP " + self.short
            self.desc += " Low Profile: evade +2"
            self.dodge += 2
            self.cost *= 1.1
            self.droneImage = "steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_even_more_dodge(self):
        if self.dodge < 8:
            self.name += "_EVEN_MORE_DODGE"
            self.title = "Camo " + self.title
            self.short = "CA " + self.short
            self.desc += " Camouflaged: evade +5"
            self.dodge += 5
            if self.dodge > 10:
                self.dodge = 10
            self.cost *= 1.3
            self.droneImage = "dirty_steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_less_dodge(self):
        if self.dodge > 0:
            self.name += "_LESS_DODGE"
            self.title = "Obvious " + self.title
            self.short = "obv " + self.short
            self.desc += " Obvious: evade -4"
            self.dodge -= 4
            if self.dodge < 0:
                self.dodge = 0
            self.cost *= 0.9
            self.droneImage = "dirty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_slow(self):
        self.name += "_SLOW"
        self.title = "Slow " + self.title
        self.short = "s " + self.short
        self.desc += " Slow: movement speed x0.9"
        self.speed *= 0.9
        self.cost *= 0.9
        self.droneImage = "slight_desat_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_boosterless(self):
        self.name += "_BOOSTERLESS"
        self.title = "Boosterless " + self.title
        self.short = "b " + self.short
        self.desc += " Boosterless: movement speed x0.8; evade -1"
        self.speed *= 0.8
        if self.dodge > 0:
            self.dodge -= 1
        self.cost *= 0.8
        self.droneImage = "heavy_desat_" + self.droneImage
        self.generate_drone()
        self.revert_drone()


class CombatDrone(Drone):
    def __init__(self, f):
        super().__init__(f)
        # does nothing for dtype COMBAT
        self.cooldown, self.cooldown2 = 1, 1
        # dtypes COMBAT and DEFENSE weaponry used
        self.weaponBlueprint, self.weaponBlueprint2 = "", ""
        self.weapon = Weapon2(self.file)
        # dtype COMBAT attack speed
        self.speed, self.speed2 = 1, 1
        # drone evade chance, for combat drones resistance against anti-drones
        # resistance against stray projectiles or asteroids
        self.dodge, self.dodge2 = 0, 0
        # refers to set of images found in ship\drones
        self.droneImage, self.droneImage2 = "", ""

    def revert_drone(self):
        super().revert_drone()
        self.cooldown = self.cooldown2
        self.weaponBlueprint = self.weaponBlueprint2
        self.weapon.revert_weapon()
        self.speed = self.speed2
        self.dodge = self.dodge2
        self.droneImage = self.droneImage2

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>COMBAT</type>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write(
            "\t<cooldown>" + str(round(self.cooldown)) + "</cooldown>\n")
        self.file.write("\t<dodge>" + str(round(self.dodge)) + "</dodge>\n")
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<droneImage>" + self.droneImage + "</droneImage>\n")
        self.file.write("\t<weaponBlueprint>" +
                        self.weaponBlueprint +
                        "</weaponBlueprint>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")
        if self.weaponBlueprint != self.weaponBlueprint2:
            self.weapon.generate_weapon()

    # combat drone only
    def ce_tactical(self):
        if (self.dodge < 10 and
                ("DE_DRONE_HEAVY_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_1" in self.name or
                 "DE_DRONE_HEAVY_2" in self.name or
                 "COMBAT_1" in self.name or "COMBAT_2" in self.name or
                 "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2_ENEMY" in self.name or
                 "DE_DRONE_BEAM_FOCUS" in self.name or
                 "DE_DRONE_STEALTH_BEAM_1" in self.name or
                 "DE_DRONE_STEALTH_BEAM_2" in self.name or
                 "DE_DRONE_MISSILES_1" in self.name or
                 "DE_DRONE_MISSILES_2" in self.name or
                 "DE_DRONE_MISSILES_3" in self.name or
                 "DE_DRONE_MISSILES_BARRAGE" in self.name)):
            self.name += "_TACTICAL"
            self.title = "Tactical " + self.title
            self.short = "Ta " + self.short
            self.desc += \
                "  Tactical: system damage +1; evade +1; hull damage -1"
            self.weaponBlueprint += "_TACTICAL_DRONE_WEAPON"
            self.weapon.name += "_TACTICAL_DRONE_WEAPON"

            self.weapon.sysDamage_true = True
            self.weapon.sysDamage += 1
            self.weapon.damage_true = True
            self.weapon.damage -= 1

            self.dodge += 1
            self.cost *= 1.1
            self.droneImage = "gritty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_assault(self):
        if self.power < 4 and self.dodge < 9:
            self.name += "_ASSAULT"
            self.title = "Assault " + self.title
            if len(self.title) > 27:
                self.title = "Aslt. " + self.title2
            self.short = "As " + self.short
            self.desc += \
                " Assault: movement speed x1.1; evade +1; power cost +1"
            self.speed *= 1.1
            self.dodge += 2
            self.power += 1
            self.cost *= 1.3
            self.droneImage = "gritty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_brutal(self):
        if ("DE_DRONE_HULL_1" in self.name or "DE_DRONE_HULL_2" in self.name or
            "DE_DRONE_HULL_1_ENEMY" in self.name or
            "DE_DRONE_HULL_2_ENEMY" in self.name or
            "COMBAT_FIRE" in self.name or "DE_DRONE_FIRE" in self.name or
            "DE_DRONE_LIGHT_MISSILE_STUN" in self.name or
            "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
            "DE_DRONE_LIGHT_MISSILE" in self.name or
            "DE_DRONE_LIGHT_1" in self.name or
            "DE_DRONE_LIGHT_2" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name or
            "DE_DRONE_LIGHT_SCATTER" in self.name or
            "DE_DRONE_HEAVY_SCATTER" in self.name or
            "DE_DRONE_HEAVY_1" in self.name or
            "DE_DRONE_HEAVY_2" in self.name or
            "COMBAT_1" in self.name or "COMBAT_2" in self.name or
            "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2_ENEMY" in self.name or
            "DE_DRONE_BEAM_FOCUS" in self.name or
            "DE_DRONE_STEALTH_BEAM_1" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name or
            "DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
                "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_BRUTAL"
            self.title = "Brutal " + self.title
            self.short = "BR " + self.short
            self.desc += " Packs a punch."
            self.weaponBlueprint += "_BRUTAL_DRONE_WEAPON"
            self.weapon.name += "_BRUTAL_DRONE_WEAPON"

            self.weapon.breachChance_true = True
            self.weapon.breachChance += 1
            if self.weapon.breachChance > 10:
                self.weapon.breachChance = 10
            self.weapon.persDamage_true = True
            self.weapon.persDamage += 1
            self.weapon.stunChance_true = True
            self.weapon.stunChance += 1
            if self.weapon.stunChance > 10:
                self.weapon.stunChance = 10

            self.speed *= 1.05
            self.cost *= 1.3
            self.droneImage = "dark_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_flux(self):
        if ("DE_DRONE_ION_1" in self.name or
            "DE_DRONE_ION_2" in self.name or
            "DE_DRONE_ION_2_ENEMY" in self.name or
            "DE_DRONE_ION_3" in self.name or
                "DE_DRONE_ION_PIERCE" in self.name):
            self.name += "_FLUX"
            self.title = "Flux " + self.title
            self.short = "FL " + self.short
            self.desc += " Flux: stun chance +3; fire chance +3"
            self.weaponBlueprint += "_FLUX_DRONE_WEAPON"
            self.weapon.name += "_FLUX_DRONE_WEAPON"

            self.weapon.stunChance_true = True
            self.weapon.stunChance += 3
            self.weapon.fireChance_true = True
            self.weapon.fireChance += 3
            self.weapon.image += "_yellow"

            self.cost *= 1.2
            self.droneImage = "yellow_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_warping(self):
        if ("DE_DRONE_ION_1" in self.name or
            "DE_DRONE_ION_2" in self.name or
            "DE_DRONE_ION_2_ENEMY" in self.name or
            "DE_DRONE_ION_3" in self.name):
            self.name += "_WARPING"
            self.title = "Warping " + self.title
            if len(self.title) > 27:
                self.title = "Warp. " + self.title2
            self.short = "Wa " + self.short
            self.desc += \
                " Warping: projectiles phase through one shield bubble; " \
                "movement speed x0.6; evade -3"
            self.weaponBlueprint += "_WARPING_DRONE_WEAPON"
            self.weapon.name += "_WARPING_DRONE_WEAPON"

            self.weapon.sp += 1
            self.weapon.image += "_heavy_desat"

            self.speed *= 0.6
            self.dodge -= 3
            if self.dodge < 0:
                self.dodge = 0
            self.cost *= 1.3
            self.droneImage = "ht_steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_phasing(self):
        if ("DE_DRONE_ION_1" in self.name or
            "DE_DRONE_ION_2" in self.name or
            "DE_DRONE_ION_2_ENEMY" in self.name or
                "DE_DRONE_ION_3" in self.name):
            self.name += "_PHASING"
            self.title = "Phasing " + self.title
            self.short = "Ph " + self.short
            self.desc += \
                " Phasing (Rare): projectiles phase through three shield " \
                "bubbles; movement speed x0.6; evade -3"
            self.weaponBlueprint += "_PHASING_DRONE_WEAPON"
            self.weapon.name += "_PHASING_DRONE_WEAPON"

            self.weapon.sp += 3
            self.weapon.image += "_high_tech"

            self.speed *= 0.6
            self.dodge -= 3
            if self.dodge < 0:
                self.dodge = 0
            self.cost *= 1.5
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "ht_steel_bright_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_perfect(self):
        if ("DE_DRONE_ION_1" in self.name or
            "DE_DRONE_ION_2" in self.name or
            "DE_DRONE_ION_2_ENEMY" in self.name or
            "DE_DRONE_ION_3" in self.name or
                "DE_DRONE_ION_PIERCE" in self.name):
            self.name += "_PERFECT"
            self.title = "Perfect " + self.title
            self.short = "PER " + self.short
            self.desc += \
                " Perfect (Epic): movement speed x1.1; evade +2; power cost -1"
            self.speed *= 1.1
            self.dodge += 2
            if self.dodge > 10:
                self.dodge = 10
            self.power -= 1
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity = 5
            self.droneImage = "ht_steel_bright_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_sungazer(self):
        if ("DE_DRONE_BEAM_HULL" in self.name or
            "COMBAT_BEAM" in self.name or
            "COMBAT_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2_ENEMY" in self.name or
            "DE_DRONE_STEALTH_BEAM_1" in self.name or
                "DE_DRONE_STEALTH_BEAM_2" in self.name):
            self.name += "_SUNGAZER"
            self.title = "Sungazer " + self.title
            self.short = "SUN " + self.short
            self.desc += \
                " Sungazer (Epic): shield piercing +1; fire chance +3, " \
                "movement speed x1.05"
            self.weaponBlueprint += "_SUNGAZER_DRONE_WEAPON"
            self.weapon.name += "_SUNGAZER_DRONE_WEAPON"

            self.weapon.sp += 1
            self.weapon.fireChance_true = True
            self.weapon.fireChance += 3
            if self.weapon.fireChance > 10:
                self.weapon.fireChance = 10
            self.weapon.colors[0] = 255
            self.weapon.colors[1] = 230
            self.weapon.colors[2] = 0

            self.speed *= 1.05
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity = 5
            self.droneImage = "gold_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_torpedo(self):
        if ("DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
                "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_TORPEDO"
            self.title = "Torpedo " + self.title
            self.short = "To " + self.short
            self.desc += \
                " Torpedo: damage +1; projectile speed x0.5; " \
                "movement speed x0.5; evade -3"
            self.weaponBlueprint += "_TORPEDO_DRONE_WEAPON"
            self.weapon.name += "_TORPEDO_DRONE_WEAPON"

            self.weapon.damage_true = True
            self.weapon.damage += 1
            self.weapon.speed *= 0.5
            self.weapon.image += "_steel"

            self.speed *= 0.5
            self.dodge -= 3
            if self.dodge < 0:
                self.dodge = 0
            self.cost *= 1.1
            self.droneImage = "steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_emp(self):
        if ("DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
                "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_EMP"
            self.title = "EMP " + self.title
            self.short = "EMP " + self.short
            self.desc += " EMP: ion damage +1; shield piercing -5"
            self.weaponBlueprint += "_EMP_DRONE_WEAPON"
            self.weapon.name += "_EMP_DRONE_WEAPON"

            self.weapon.ion_true = True
            self.weapon.ion += 1
            self.weapon.sp -= 5
            if self.weapon.sp < 0:
                self.weapon.sp = 0
            self.weapon.image += "_blue"

            self.cost *= 1.1
            self.droneImage = "blue_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_frag(self):
        if ("DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
                "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_FRAG"
            self.title = "Frag " + self.title
            self.short = "Frag " + self.short
            self.desc += \
                " Shrapnel: system damage +1; crew damage +1; hull damage -1"
            self.weaponBlueprint += "_FRAG_DRONE_WEAPON"
            self.weapon.name += "_FRAG_DRONE_WEAPON"

            self.weapon.damage -= 1
            self.weapon.sysDamage_true = True
            self.weapon.sysDamage += 1
            self.weapon.persDamage_true = True
            self.weapon.persDamage += 1
            self.weapon.image += "_gritty"

            self.cost *= 1.1
            self.droneImage = "gritty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_shredder(self):
        if ("DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
            "DE_DRONE_MISSILES_BARRAGE" in self.name or
            "DE_DRONE_LIGHT_MISSILE" in self.name or
            "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
                "DE_DRONE_LIGHT_MISSILE_STUN" in self.name):
            self.name += "_SHREDDER"
            self.title = "Shredder " + self.title
            self.short = "Shre " + self.short
            self.desc += " Shredder (Rare): system damage +1; crew damage +1"
            self.weaponBlueprint += "_SHREDDER_DRONE_WEAPON"
            self.weapon.name += "_SHREDDER_DRONE_WEAPON"

            self.weapon.sysDamage_true = True
            self.weapon.sysDamage += 1
            self.weapon.persDamage_true = True
            self.weapon.persDamage += 1
            self.weapon.image += "_dirty_steel"

            self.cost *= 1.4
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "dirty_steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_deathly(self):
        if ("DE_DRONE_LIGHT_1" in self.name or
            "DE_DRONE_LIGHT_2" in self.name or
            "DE_DRONE_LIGHT_SCATTER" in self.name or
            "DE_DRONE_LIGHT_MISSILE" in self.name or
            "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
                "DE_DRONE_LIGHT_MISSILE_STUN" in self.name):
            self.name += "_DEATHLY"
            self.title = "Deathly " + self.title
            self.short = "DEA " + self.short
            self.desc += \
                " Deathly (Epic): crew damage x2; movement speed x1.1; evade +3"
            self.weaponBlueprint += "_DEATHLY_DRONE_WEAPON"
            self.weapon.name += "_DEATHLY_DRONE_WEAPON"

            self.weapon.persDamage *= 2
            self.weapon.image += "_dark"

            self.speed *= 1.1
            self.dodge += 3
            if self.dodge > 10:
                self.dodge = 10
            self.cost *= 1.5
            if self.rarity > 0:
                self.rarity = 5
            self.droneImage = "dark_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_hull_ripper(self):
        if ("DE_DRONE_HEAVY_SCATTER" in self.name or
            "DE_DRONE_HEAVY_1" in self.name or
            "DE_DRONE_HEAVY_2" in self.name or
            "COMBAT_1" in self.name or "COMBAT_2" in self.name or
            "COMBAT_BEAM" in self.name or
            "COMBAT_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2_ENEMY" in self.name or
            "DE_DRONE_BEAM_FOCUS" in self.name or
            "DE_DRONE_STEALTH_BEAM_1" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name or
            "DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3," in self.name or
                "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_HULL_RIPPER"
            self.title = "Ripper " + self.title
            self.short = "HR " + self.short
            self.desc += " (Rare) Deals double hull damage " \
                         "to systemless rooms."
            self.weaponBlueprint += "_HULL_RIPPER_DRONE_WEAPON"
            self.weapon.name += "_HULL_RIPPER_DRONE_WEAPON"

            self.weapon.hullBust_true = True
            self.weapon.hullBust = 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_green"

            self.cost *= 1.3
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "old_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_widespread(self):
        if ("DE_DRONE_HULL_1" in self.name or
            "DE_DRONE_HULL_2" in self.name or
            "DE_DRONE_HULL_1_ENEMY" in self.name or
            "DE_DRONE_HULL_2_ENEMY" in self.name or
            "DE_DRONE_HEAVY_SCATTER" in self.name or
            "DE_DRONE_HEAVY_1" in self.name or
            "DE_DRONE_HEAVY_2" in self.name or
            "COMBAT_1" in self.name or
            "COMBAT_2" in self.name or
            "COMBAT_BEAM" in self.name or
            "COMBAT_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2_ENEMY" in self.name or
            "DE_DRONE_BEAM_FOCUS" in self.name or
            "DE_DRONE_STEALTH_BEAM_1" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name or
            "DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
            "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_WIDESPREAD"
            self.title = "Wide Spr. " + self.title
            self.short = "wi " + self.short
            self.desc += " Wide Spread: system damage -1"
            self.weaponBlueprint += "_WIDESPREAD_DRONE_WEAPON"
            self.weapon.name += "_WIDESPREAD_DRONE_WEAPON"

            self.weapon.sysDamage_true = True
            self.weapon.sysDamage -= 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_slight_desat"

            self.cost *= 0.8
            self.droneImage = "slight_desat_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_tightspread(self):
        if (self.speed < 15 and
                ("DE_DRONE_HULL_1" in self.name or
                 "DE_DRONE_HULL_2" in self.name or
                 "DE_DRONE_HULL_1_ENEMY" in self.name or
                 "DE_DRONE_HULL_2_ENEMY" in self.name or
                 "DE_DRONE_HEAVY_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_1" in self.name or
                 "DE_DRONE_HEAVY_2" in self.name or
                 "COMBAT_1" in self.name or
                 "COMBAT_2" in self.name or
                 "COMBAT_BEAM" in self.name or
                 "COMBAT_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2_ENEMY" in self.name or
                 "DE_DRONE_BEAM_FOCUS" in self.name or
                 "DE_DRONE_STEALTH_BEAM_1" in self.name or
                 "DE_DRONE_STEALTH_BEAM_2" in self.name or
                 "DE_DRONE_MISSILES_1" in self.name or
                 "DE_DRONE_MISSILES_2" in self.name or
                 "DE_DRONE_MISSILES_3" in self.name or
                 "DE_DRONE_MISSILES_BARRAGE" in self.name)):
            self.name += "_TIGHTSPREAD"
            self.title = "Tight Spr. " + self.title
            self.short = "TIG " + self.short
            self.desc += " Tight Spread: system damage +1"
            self.weaponBlueprint += "_TIGHTSPREAD_DRONE_WEAPON"
            self.weapon.name += "_TIGHTSPREAD_DRONE_WEAPON"

            self.weapon.sysDamage_true = True
            self.weapon.sysDamage += 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_green"

            self.cost *= 1.2
            self.droneImage = "gritty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_incendiary(self):
        if (self.weapon.fireChance < 10 and
                ("DE_DRONE_HULL_1" in self.name or
                 "DE_DRONE_HULL_2" in self.name or
                 "DE_DRONE_HULL_1_ENEMY" in self.name or
                 "DE_DRONE_HULL_2_ENEMY" in self.name or
                 "COMBAT_FIRE" in self.name or
                 "DE_DRONE_FIRE" in self.name or
                 "DE_DRONE_LIGHT_MISSILE_STUN" in self.name or
                 "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
                 "DE_DRONE_LIGHT_MISSILE" in self.name or
                 "DE_DRONE_LIGHT_1" in self.name or
                 "DE_DRONE_LIGHT_2" in self.name or
                 "DE_DRONE_LIGHT_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_1" in self.name or
                 "DE_DRONE_HEAVY_2" in self.name or
                 "COMBAT_1" in self.name or "COMBAT_2" in self.name or
                 "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2_ENEMY" in self.name or
                 "DE_DRONE_BEAM_FOCUS" in self.name or
                 "DE_DRONE_STEALTH_BEAM_1" in self.name or
                 "DE_DRONE_STEALTH_BEAM_2" in self.name or
                 "DE_DRONE_MISSILES_1" in self.name or
                 "DE_DRONE_MISSILES_2" in self.name or
                 "DE_DRONE_MISSILES_3" in self.name or
                 "DE_DRONE_MISSILES_BARRAGE" in self.name)):
            self.name += "_INCENDIARY"
            self.title = "Incend. " + self.title
            self.short = "IN " + self.short
            self.desc += " Incendiary: fire chance +2"
            self.weaponBlueprint += "_INCENDIARY_DRONE_WEAPON"
            self.weapon.name += "_INCENDIARY_DRONE_WEAPON"

            self.weapon.fireChance_true = True
            self.weapon.fireChance += 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_red"

            self.cost *= 1.2
            self.droneImage = "red_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_radioactive(self):
        if ("DE_DRONE_HULL_1" in self.name or "DE_DRONE_HULL_2" in self.name or
            "DE_DRONE_HULL_1_ENEMY" in self.name or
            "DE_DRONE_HULL_2_ENEMY" in self.name or
            "COMBAT_FIRE" in self.name or "DE_DRONE_FIRE" in self.name or
            "DE_DRONE_LIGHT_MISSILE_STUN" in self.name or
            "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
            "DE_DRONE_LIGHT_MISSILE" in self.name or
            "DE_DRONE_LIGHT_1" in self.name or
            "DE_DRONE_LIGHT_2" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name or
            "DE_DRONE_LIGHT_SCATTER" in self.name or
            "DE_DRONE_HEAVY_SCATTER" in self.name or
            "DE_DRONE_HEAVY_1" in self.name or
            "DE_DRONE_HEAVY_2" in self.name or
            "COMBAT_1" in self.name or "COMBAT_2" in self.name or
            "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2_ENEMY" in self.name or
            "DE_DRONE_BEAM_FOCUS" in self.name or
            "DE_DRONE_STEALTH_BEAM_1" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name or
            "DE_DRONE_MISSILES_1" in self.name or
            "DE_DRONE_MISSILES_2" in self.name or
            "DE_DRONE_MISSILES_3" in self.name or
            "DE_DRONE_MISSILES_BARRAGE" in self.name):
            self.name += "_RADIOACTIVE"
            self.title = "Rad. " + self.title
            self.short = "RAD " + self.short
            self.desc += " Radioactive: crew damage +1"
            self.weaponBlueprint += "_RADIOACTIVE_DRONE_WEAPON"
            self.weapon.name += "_RADIOACTIVE_DRONE_WEAPON"

            self.weapon.persDamage_true = True
            self.weapon.persDamage += 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_green"

            self.cost *= 1.2
            self.droneImage = "yellow_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_volatile(self):
        if (self.weapon.fireChance < 10 and
                ("DE_DRONE_HULL_1" in self.name or
                 "DE_DRONE_HULL_2" in self.name or
                 "DE_DRONE_HULL_1_ENEMY" in self.name or
                 "DE_DRONE_HULL_2_ENEMY" in self.name or
                 "COMBAT_FIRE" in self.name or
                 "DE_DRONE_FIRE" in self.name or
                 "DE_DRONE_LIGHT_MISSILE_STUN" in self.name or
                 "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
                 "DE_DRONE_LIGHT_MISSILE" in self.name or
                 "DE_DRONE_LIGHT_1" in self.name or
                 "DE_DRONE_LIGHT_2" in self.name or
                 "DE_DRONE_LIGHT_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_1" in self.name or
                 "DE_DRONE_HEAVY_2" in self.name or
                 "COMBAT_1" in self.name or "COMBAT_2" in self.name or
                 "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2_ENEMY" in self.name or
                 "DE_DRONE_BEAM_FOCUS" in self.name or
                 "DE_DRONE_STEALTH_BEAM_1" in self.name or
                 "DE_DRONE_STEALTH_BEAM_2" in self.name or
                 "DE_DRONE_MISSILES_1" in self.name or
                 "DE_DRONE_MISSILES_2" in self.name or
                 "DE_DRONE_MISSILES_3" in self.name or
                 "DE_DRONE_MISSILES_BARRAGE" in self.name)):
            self.name += "_VOLATILE"
            self.title = "Volat. " + self.title
            self.short = "VOL " + self.short
            self.desc += " Volatile: fire chance +1, crew damage +1"
            self.weaponBlueprint += "_VOLATILE_DRONE_WEAPON"
            self.weapon.name += "_VOLATILE_DRONE_WEAPON"

            self.weapon.fireChance_true = True
            self.weapon.fireChance += 1
            self.weapon.persDamage_true = True
            self.weapon.persDamage += 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_red"

            self.cost *= 1.3
            self.droneImage = "dirty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_safe(self):
        if ((self.weapon.damage > 0 or self.weapon.persDamage > 0) and
                self.weapon.persDamage != -self.weapon.damage and
                ("DE_DRONE_HULL_1" in self.name or
                 "DE_DRONE_HULL_2" in self.name or
                 "DE_DRONE_HULL_1_ENEMY" in self.name or
                 "DE_DRONE_HULL_2_ENEMY" in self.name or
                 "DE_DRONE_LIGHT_MISSILE_STUN" in self.name or
                 "DE_DRONE_LIGHT_MISSILE_FIRE" in self.name or
                 "DE_DRONE_LIGHT_1" in self.name or
                 "DE_DRONE_LIGHT_2" in self.name or
                 "DE_DRONE_LIGHT_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_SCATTER" in self.name or
                 "DE_DRONE_HEAVY_1" in self.name or
                 "DE_DRONE_HEAVY_2" in self.name or
                 "COMBAT_1" in self.name or "COMBAT_2" in self.name or
                 "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2" in self.name or
                 "DE_DRONE_BEAM_2_ENEMY" in self.name or
                 "DE_DRONE_BEAM_FOCUS" in self.name or
                 "DE_DRONE_STEALTH_BEAM_1" in self.name or
                 "DE_DRONE_STEALTH_BEAM_2" in self.name or
                 "DE_DRONE_MISSILES_1" in self.name or
                 "DE_DRONE_MISSILES_2" in self.name or
                 "DE_DRONE_MISSILES_3" in self.name or
                 "DE_DRONE_MISSILES_BARRAGE" in self.name)):
            self.name += "_SAFE"
            self.title = "Safe " + self.title
            self.short = "saf " + self.short
            self.desc += " Safe: crew damage -1"
            self.weaponBlueprint += "_SAFE_DRONE_WEAPON"
            self.weapon.name += "_SAFE_DRONE_WEAPON"

            self.weapon.persDamage_true = True
            self.weapon.persDamage -= 1
            if type(self.weapon) is not Beam:
                self.weapon.image += "_slight_desat"
            else:
                self.weapon.colors[0] = 255
                self.weapon.colors[1] = 50
                self.weapon.colors[2] = 50

            self.cost *= 0.9
            self.droneImage = "slight_desat_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_focus(self):
        if ("DE_DRONE_BEAM_HULL" in self.name or
            "COMBAT_BEAM" in self.name or "COMBAT_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2" in self.name or
            "DE_DRONE_BEAM_2_ENEMY" in self.name or
            "DE_DRONE_STEALTH_BEAM_1" in self.name or
            "DE_DRONE_STEALTH_BEAM_2" in self.name):
            self.name += "_FOCUS"
            self.title = "Focus " + self.title
            self.short = "FOC " + self.short
            self.desc += " Focus (Rare): shield piercing +1"
            self.weaponBlueprint += "_FOCUSED_DRONE_WEAPON"
            self.weapon.name += "_FOCUSED_DRONE_WEAPON"

            self.weapon.sp += 1
            self.weapon.length *= 0.5
            self.weapon.colors[0] -= 55
            if self.weapon.colors[0] < 0:
                self.weapon.colors[0] = 0

            self.cost *= 1.3
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "rust_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_sentient(self):
        self.name += "_SENTIENT"
        self.title = "Sentient " + self.title
        self.short = "SEN " + self.short
        self.desc += " Sentient (Epic): movement speed x1.15, evade +3"
        self.speed *= 1.15
        self.dodge += 3
        if self.dodge > 10:
            self.dodge = 10
        self.cost *= 1.5
        if 0 < self.rarity < 5:
            self.rarity = 5
        self.droneImage = "ht_steel_bright_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    # not just combat drone
    def ce_highvelocity(self):
        if not ("DE_DRONE_BEAM_HULL" in self.name or
                "COMBAT_FIRE" in self.name or
                "DE_DRONE_FIRE" in self.name or
                "COMBAT_BEAM" in self.name or
                "COMBAT_BEAM_2" in self.name or
                "DE_DRONE_BEAM_2" in self.name or
                "DE_DRONE_BEAM_2_ENEMY" in self.name or
                "DE_DRONE_BEAM_FOCUS" in self.name or
                "DE_DRONE_STEALTH_BEAM_1" in self.name or
                "DE_DRONE_STEALTH_BEAM_2" in self.name):
            self.name += "_HIGHVELOCITY"
            self.title = "High Vel. " + self.title
            self.short = "HV " + self.short
            self.desc += " High Velocity: projectile speed x1.25"
            self.weaponBlueprint += "_HIGHVELOCITY_DRONE_WEAPON"
            self.weapon.name += "_HIGHVELOCITY_DRONE_WEAPON"

            self.weapon.speed *= 1.25
            self.weapon.image += "_high_tech"

            self.cost *= 1.1
            self.droneImage = "gritty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_lowvelocity(self):
        if not ("DE_DRONE_BEAM_HULL" in self.name or
                "COMBAT_FIRE" in self.name or
                "DE_DRONE_FIRE" in self.name or
                "COMBAT_BEAM" in self.name or
                "COMBAT_BEAM_2" in self.name or
                "DE_DRONE_BEAM_2" in self.name or
                "DE_DRONE_BEAM_2_ENEMY" in self.name or
                "DE_DRONE_BEAM_FOCUS" in self.name or
                "DE_DRONE_STEALTH_BEAM_1" in self.name or
                "DE_DRONE_STEALTH_BEAM_2" in self.name):
            self.name += "_LOWVELOCITY"
            self.title = "Low Vel. " + self.title
            self.short = "low " + self.short
            self.desc += " Low Velocity: projectile speed x0.75"
            self.weaponBlueprint += "_LOWVELOCITY_DRONE_WEAPON"
            self.weapon.name += "_LOWVELOCITY_DRONE_WEAPON"

            self.weapon.speed *= 0.75
            self.weapon.image += "_slight_desat"

            self.cost *= 0.9
            self.droneImage = "slight_desat_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_swag(self):
        if self.power > 2:
            self.name += "_SWAG"
            self.title = "Swag " + self.title
            self.short = "S " + self.short
            self.desc = " Swag: good for showing off"
            if self.rarity > 0:
                self.rarity = 5
            self.cost *= 1.5
            self.droneImage = "gold_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_second_hand(self):
        self.name += "_SECOND_HAND"
        self.title = "Sec. Hand " + self.title
        self.short = "Sec " + self.short
        self.desc += " Second Hand: as good as a new one, but cheaper"
        self.cost *= 0.75
        self.generate_drone()
        self.revert_drone()

    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "dirty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_optimized(self):
        if self.power > 1:
            self.name += "_OPTIMIZED"
            self.title = "Optim. " + self.title
            self.short = "O " + self.short
            self.desc += " (Rare) Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            if 0 < self.rarity < 5:
                self.rarity += 1
            self.droneImage = "ht_steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_autonomous(self):
        if self.power < 3:
            self.name += "_AUTONOMOUS"
            self.title = "Autonomous " + self.title
            self.short = "A " + self.short
            self.desc += " Autonomous (Epic): requires no power"
            self.power = 0
            self.cost *= 1.5
            if 0 < self.rarity < 5:
                self.rarity = 5
            self.droneImage = "ht_steel_bright_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_fast(self):
        self.name += "_FAST"
        self.title = "Fast " + self.title
        self.short = "F " + self.short
        self.desc += " Fast: movement speed x1.05"
        self.speed *= 1.05
        self.cost *= 1.1
        self.droneImage = "high_tech_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_boosted(self):
        self.name += "_BOOSTED"
        self.title = "Boosted " + self.title
        self.short = "B " + self.short
        self.desc += " Boosted (Rare): movement speed x1.1; evade +1"
        self.speed *= 1.1
        if self.dodge < 10:
            self.dodge += 1
        self.cost *= 1.2
        if 0 < self.rarity < 5:
            self.rarity += 1
        self.droneImage = "ht_steel_bright_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_more_dodge(self):
        if self.dodge < 9:
            self.name += "_MORE_DODGE"
            self.title = "Low Profile " + self.title
            self.short = "LoP " + self.short
            self.desc += " Low Profile: evade +2"
            self.dodge += 2
            self.cost *= 1.1
            self.droneImage = "steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_even_more_dodge(self):
        if self.dodge < 8:
            self.name += "_EVEN_MORE_DODGE"
            self.title = "Camo " + self.title
            self.short = "CA " + self.short
            self.desc += " Camouflaged: evade +5"
            self.dodge += 5
            if self.dodge > 10:
                self.dodge = 10
            self.cost *= 1.3
            self.droneImage = "dirty_steel_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_less_dodge(self):
        if self.dodge > 0:
            self.name += "_LESS_DODGE"
            self.title = "Obvious " + self.title
            self.short = "obv " + self.short
            self.desc += " Obvious: evade -4"
            self.dodge -= 4
            if self.dodge < 0:
                self.dodge = 0
            self.cost *= 0.9
            self.droneImage = "dirty_" + self.droneImage
            self.generate_drone()
            self.revert_drone()

    def ce_slow(self):
        self.name += "_SLOW"
        self.title = "Slow " + self.title
        self.short = "s " + self.short
        self.desc += " Slow: movement speed x0.9"
        self.speed *= 0.9
        self.cost *= 0.9
        self.droneImage = "slight_desat_" + self.droneImage
        self.generate_drone()
        self.revert_drone()

    def ce_boosterless(self):
        self.name += "_BOOSTERLESS"
        self.title = "Boosterless " + self.title
        self.short = "b " + self.short
        self.desc += " Boosterless: movement speed x0.8; evade -1"
        self.speed *= 0.8
        if self.dodge > 0:
            self.dodge -= 1
        self.cost *= 0.8
        if 0 < self.rarity < 5:
            self.rarity += 1
        self.droneImage = "heavy_desat_" + self.droneImage
        self.generate_drone()
        self.revert_drone()


class BattleDrone(Drone):
    def __init__(self, f):
        super().__init__(f)
        # not sure what this is for.
        self.locked, self.locked2 = 1, 1

    def revert_drone(self):
        super().revert_drone()
        self.locked = self.locked2

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>BATTLE</type>\n")
        self.file.write("\t<locked>" + str(self.locked) + "</locked>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")

    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.generate_drone()
            self.revert_drone()

    def ce_optimized(self):
        if self.power > 1:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            self.short = "O " + self.short
            self.desc += " Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.generate_drone()
            self.revert_drone()

    def ce_autonomous(self):
        if self.power < 3:
            self.name += "_AUTONOMOUS"
            self.title = "Autonomous " + self.title
            self.short = "A " + self.short
            self.desc += " Autonomous (Epic): requires no power"
            self.power = 0
            if 0 < self.rarity < 5:
                self.rarity = 5
            self.cost *= 1.5
            self.generate_drone()
            self.revert_drone()

    def ce_standard_internal_1(self):
        self.name += "_STANDARD_INTERNAL_1"
        self.generate_drone()
        self.revert_drone()

    def ce_standard_internal_2(self):
        self.name += "_STANDARD_INTERNAL_2"
        self.generate_drone()
        self.revert_drone()

    def ce_standard_internal_3(self):
        self.name += "_STANDARD_INTERNAL_3"
        self.generate_drone()
        self.revert_drone()


class RepairDrone(Drone):
    def __init__(self, f):
        super().__init__(f)

    def revert_drone(self):
        super().revert_drone()

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>REPAIR</type>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")

    def ce_faulty(self):
        if self.power < 4:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.generate_drone()
            self.revert_drone()

    def ce_optimized(self):
        if self.power > 1:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            self.short = "O " + self.short
            self.desc += " Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.generate_drone()
            self.revert_drone()

    def ce_autonomous(self):
        if self.power < 3:
            self.name += "_AUTONOMOUS"
            self.title = "Autonomous " + self.title
            self.short = "A " + self.short
            self.desc += " Autonomous (Epic): requires no power"
            self.power = 0
            if 0 < self.rarity < 5:
                self.rarity = 5
            self.cost *= 1.5
            self.generate_drone()
            self.revert_drone()

    def ce_standard_internal_1(self):
        self.name += "_STANDARD_INTERNAL_1"
        self.generate_drone()
        self.revert_drone()

    def ce_standard_internal_2(self):
        self.name += "_STANDARD_INTERNAL_2"
        self.generate_drone()
        self.revert_drone()

    def ce_standard_internal_3(self):
        self.name += "_STANDARD_INTERNAL_3"
        self.generate_drone()
        self.revert_drone()


# Might not have bp??
class BoarderDrone(Drone):
    def __init__(self, f):
        super().__init__(f)
        # dtype BOARDER time-to-impact speed
        self.speed, self.speed2 = 1, 1
        # not sure what this is for.
        self.locked, self.locked2 = 1, 1

    def revert_drone(self):
        super().revert_drone()
        self.speed = self.speed2
        self.locked = self.locked2

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>BOARDER</type>\n")
        self.file.write("\t<locked>" + str(self.locked) + "</locked>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")

    def ce_faulty(self):
        if self.power < 4 and "BOARDER_ION" not in self.name:
            self.name += "_FAULTY"
            self.title = "Faulty " + self.title
            self.short = "f " + self.short
            self.desc += " Needs more power due to faulty power couplers."
            self.power += 1
            self.cost *= 0.6
            self.generate_drone()
            self.revert_drone()

    def ce_optimized(self):
        if self.power > 1 and "BOARDER_ION" not in self.name:
            self.name += "_OPTIMIZED"
            self.title = "Optimized " + self.title
            self.short = "O " + self.short
            self.desc += " Optimized to require less power."
            self.power -= 1
            self.cost *= 1.4
            self.generate_drone()
            self.revert_drone()

    def ce_autonomous(self):
        if self.power < 3 and "BOARDER_ION" not in self.name:
            self.name += "_AUTONOMOUS"
            self.title = "Autonomous " + self.title
            self.short = "A " + self.short
            self.desc += " Autonomous (Epic): requires no power"
            self.power = 0
            if 0 < self.rarity < 5:
                self.rarity = 5
            self.cost *= 1.5
            self.generate_drone()
            self.revert_drone()

    def ce_fast(self):
        if "BOARDER_ION" not in self.name:
            self.name += "_FAST"
            self.title = "Fast " + self.title
            self.short = "F " + self.short
            self.desc += " Fast: launch speed x2"
            self.speed *= 2
            self.cost *= 1.1
            self.generate_drone()
            self.revert_drone()

    def ce_boosted(self):
        if "BOARDER_ION" not in self.name:
            self.name += "_BOOSTED"
            self.title = "Boosted " + self.title
            self.short = "B " + self.short
            self.desc += " Boosted: launch speed x3"
            self.speed *= 3
            self.cost *= 1.2
            self.generate_drone()
            self.revert_drone()

    def ce_slow(self):
        if "BOARDER_ION" not in self.name:
            self.name += "_SLOW"
            self.title = "Slow " + self.title
            self.short = "s " + self.short
            self.desc += " Slow: launch speed x0.5"
            self.speed *= 0.5
            self.cost *= 0.8
            self.generate_drone()
            self.revert_drone()

    def ce_standard_internal_1(self):
        if "BOARDER_ION" not in self.name:
            self.name += "_STANDARD_INTERNAL_1"
            self.generate_drone()
            self.revert_drone()

    def ce_standard_internal_2(self):
        if "BOARDER_ION" not in self.name:
            self.name += "_STANDARD_INTERNAL_2"
            self.generate_drone()
            self.revert_drone()

    def ce_standard_internal_3(self):
        if "BOARDER_ION" not in self.name:
            self.name += "_STANDARD_INTERNAL_3"
            self.generate_drone()
            self.revert_drone()


class ShipRepairDrone(Drone):
    def __init__(self, f):
        super().__init__(f)
        # does nothing for dtype SHIP_REPAIR
        self.cooldown, self.cooldown2 = 1, 1
        # dtype SHIP_REPAIR something.. move speed?
        self.speed, self.speed2 = 1, 1
        # something to do with dtype SHIP_REPAIR. but what??
        self.image, self.image2 = "", ""
        # refers to set of images found in ship\drones
        self.droneImage, self.droneImage2 = "", ""

    def revert_drone(self):
        super().revert_drone()
        self.cooldown = self.cooldown2
        self.speed = self.speed2
        self.image = self.image2
        self.droneImage = self.droneImage2

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>SHIP_REPAIR</type>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<droneImage>" + self.droneImage + "</droneImage>\n")
        self.file.write("\t<image>" + self.image + "</image>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")

class ShieldDrone(Drone):
    def __init__(self, f):
        super().__init__(f)
        self.level, self.level2 = 1, 1
        # cooldown matters
        self.cooldown, self.cooldown2 = 1, 1
        self.dodge, self.dodge2 = 1, 1
        # speed is just visual
        self.speed, self.speed2 = 1, 1

    def revert_drone(self):
        super().revert_drone()
        self.level = self.level2
        self.cooldown = self.cooldown2
        self.dodge = self.dodge2
        self.speed = self.speed2

    def generate_drone(self):
        self.file.write("<droneBlueprint name=\"" + self.name + "\">\n")
        self.file.write("\t<type>SHIELD</type>\n")
        if self.tip_true:
            self.file.write("\t<tip>" + self.tip + "</tip>\n")
        self.file.write("\t<level>" + str(self.level) + "</level>\n")
        self.file.write("\t<title>" + self.title + "</title>\n")
        self.file.write("\t<short>" + self.short + "</short>\n")
        self.file.write("\t<desc>" + self.desc + "</desc>\n")
        self.file.write("\t<power>" + str(self.power) + "</power>\n")
        self.file.write(
            "\t<cooldown>" + str(round(self.cooldown)) + "</cooldown>\n")
        self.file.write("\t<dodge>" + str(round(self.dodge)) + "</dodge>\n")
        self.file.write("\t<speed>" + str(round(self.speed)) + "</speed>\n")
        self.file.write("\t<cost>" + str(round(self.cost)) + "</cost>\n")
        self.file.write("\t<bp>" + str(self.bp) + "</bp>\n")
        self.file.write("\t<rarity>" + str(self.rarity) + "</rarity>\n")
        self.file.write("</droneBlueprint>\n")
