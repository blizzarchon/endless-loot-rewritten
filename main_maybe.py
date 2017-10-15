"""
Created on Apr 12, 2017

@author: BAJ
"""
from xml.etree import ElementTree
from EL_Rewrite_2.new_classes import Beam, Laser, Missile, Bomb, Burst, \
    DefenseDrone, CombatDrone, BoarderDrone, \
    BattleDrone, RepairDrone, ShipRepairDrone, ShieldDrone
import tkinter
from tkinter.filedialog import askopenfilename



ENEMY_WEAPONS = False
# when True, player prefixed weapons cannot be created, only enemy
# when False, enemy prefixed weapons cannot be created, only player
DRONE_CREATION = False
# when True, regular prefixed weapons cannot be created, only drones
# and their weapons (if they have one)
# when False, drones cannot be created
ENEMY_DRONES = False
# when True, player drones shouldn't be able to be created, duplicate drone
# weps won't happen since enemy drone weapons also have "ENEMY" in them
# when False, enemy shouldn't be able to be created
BLUE_R_PROMPT = "- blueprints-type file containing all generated " \
                "blueprints either player or enemy\n"
AUTO_R_PROMPT = "- autoBlueprints-type file containing " \
                "existing blueprintLists\n"
AUTO_W_PROMPT = "- new file to write to matching autoBlueprint " \
                "type (autoBlueprints|dlcBlueprints-type file)\n"

prefix_read_prompt = "Enter the name of the file to READ from if it's " \
                     "in this directory, otherwise, enter its full path:\n"
prefix_write_prompt = "Enter the name of the file to WRITE to. " \
                      "Unless otherwise specified, " \
                      "if it doesn't exist, it will be created:\n"

def _into_lists(blueTree, autoTree, bar):
    """ Stores prefixed weapons in tree into bar depending on if their base
    versions of themselves are in the blueprintLists in autoTree.

    NOTE: replace "mod:" and "mod-append:" with an empty string, unless
    you have a way to make it recognized as well-formed XML

    :param Element blueTree: root element of tree containing info on all
                             tags in the blueprints.xml.append-type file
    :param Element autoTree: root element of tree containing info on all
                             tags in the autoBlueprints.xml-type file
    :param File bar: some file to write stuff in
    :rtype: None, since nothing to return; this function writes into the
            given file, bar.
    """
    for autoChild in autoTree:
        # e.g. a <blueprintList>, or a <mod:findName type="blueprintList">
        if (autoChild.tag == 'blueprintList' or
                (autoChild.tag == 'findName' and
                    autoChild.attrib['type'] == 'blueprintList')):
            possible_wep_names, possible_drone_names = [], []
            for blueChild in blueTree:
                # e.g. a <weaponBlueprint>, or a <droneBlueprint>
                if blueChild.tag == 'weaponBlueprint':
                    for autoChildName in autoChild:
                        # go through each <name> tag to see if
                        # the base weapon is in the list
                        if autoChildName.text in blueChild.attrib['name']:
                            # the weapon is in fact inside the blueprintList
                            if "DRONE_WEAPON" in blueChild.attrib['name']:
                                # without this, these weapons go into the lists
                                continue
                            if "ENEMY" in autoChildName.text:
                                # ENEMY must be in blueChild
                                possible_wep_names.append(
                                    blueChild.attrib['name'])
                                break
                            elif "ENEMY" not in blueChild.attrib['name']:
                                # ENEMY can't be in autoChildName.text
                                possible_wep_names.append(
                                    blueChild.attrib['name'])
                                break
                    else:
                        # the weaponBlueprint is not in the blueprintList
                        continue
                elif blueChild.tag == 'droneBlueprint':
                    for autoChildName in autoChild:
                        if autoChildName.text in blueChild.attrib['name']:
                            # problem: what if autoChildName.text is a weapon?
                            if "ENEMY" in autoChildName.text:
                                possible_drone_names.append(
                                    blueChild.attrib['name'])
                                break
                            elif "ENEMY" not in blueChild.attrib['name']:
                                possible_drone_names.append(
                                    blueChild.attrib['name'])
                                break
                        else:
                            continue
            # write into a designated file, all the names to add
            if autoChild.attrib['name'] == "DLC_ITEMS":
                if len(possible_wep_names) > 0:
                    bar.write("<mod:findName type=\"blueprintList\" "
                              "name=\"{}\">\n".format(autoChild.attrib['name']))
                    for name in possible_wep_names:
                        bar.write("\t<mod-append:name>{}</mod-append:name>\n".format(name))
                    # bar.write("</mod:findName>\n")
                    # bar.write("\n")
                if len(possible_drone_names) > 0:
                    # bar.write("<mod:findName type=\"blueprintList\" "
                    #          "name=\"{}\">\n".format(autoChild.attrib['name']))
                    for name in possible_drone_names:
                        bar.write(
                            "\t<mod-append:name>{}</mod-append:name>\n".format(
                                name))
                    bar.write("</mod:findName>\n")
                    bar.write("\n")
            else:
                if len(possible_wep_names) > 0:
                    bar.write("<mod:findName type=\"blueprintList\" "
                              "name=\"{}\">\n".format(autoChild.attrib['name']))
                    for name in possible_wep_names:
                        bar.write(
                            "\t<mod-append:name>{}</mod-append:name>\n".format(
                                name))
                    bar.write("</mod:findName>\n")
                    bar.write("\n")
                elif len(possible_drone_names) > 0:
                    bar.write("<mod:findName type=\"blueprintList\" "
                              "name=\"{}\">\n".format(autoChild.attrib['name']))
                    for name in possible_drone_names:
                        bar.write(
                            "\t<mod-append:name>{}</mod-append:name>\n".format(
                                name))
                    bar.write("</mod:findName>\n")
                    bar.write("\n")


def to_the_auto_lists(blue=''):
    """ Selects the files to use via user entry from standard input.

    This function is required to always catch an invalid file to read from.
    """
    try:
        if blue == '':
            print(BLUE_R_PROMPT)
            tkinter.Tk().withdraw()
            blues_file = askopenfilename()
        else:
            blues_file = blue
        with open(blues_file, 'r') as blues_to_read:
            # file to read from's contents stored in ElementTree
            blues_tree = ElementTree.parse(blues_to_read)
            blues_root = blues_tree.getroot()

            try:
                print(AUTO_R_PROMPT)
                # tkinter.Tk().withdraw()
                autos_file = askopenfilename()
                with open(autos_file, 'r') as autos_to_read:
                    autos_tree = ElementTree.parse(autos_to_read)
                    autos_root = autos_tree.getroot()

                    auto_lists_write = input(AUTO_W_PROMPT)
                    with open(auto_lists_write, 'w') as writing_file:
                        _into_lists(blues_root, autos_root, writing_file)

                        return blues_file
            except FileNotFoundError:
                print("If you're trying to quit, end the program, "
                      "not the dialog.")
                to_the_auto_lists(blues_file)
    except FileNotFoundError:
        print("If you're trying to quit, end the program, not the dialog.")
        to_the_auto_lists()


def write_beam_prefixes(beam):
    """ Writes prefixed variations of beam in beam's file.

    :param Beam beam: 
    :rtype: None 
    """
    if ((beam.rarity > 0 and not ENEMY_WEAPONS) or
        (ENEMY_WEAPONS and "_ENEMY" in beam.name and
            "ENEMY_OLD" not in beam.name and
            "BA_ARTILLERY" not in beam.name and
            "DRONE" not in beam.name)):
        beam.ce_piercing()
        beam.ce_low_energy()
        beam.ce_support_beam()
        beam.ce_assault_beam()
        beam.ce_tactical()
        beam.ce_brutal()
        beam.ce_weaksauce()
        beam.ce_hull_ripper()
        beam.ce_reconfigured()
        beam.ce_heavy()
        beam.ce_light()
        beam.ce_substandard()
        beam.ce_surplus()
        beam.ce_quality()
        beam.ce_custom()
        beam.ce_vintage()
        beam.ce_antique()
        beam.ce_swag()
        beam.ce_second_hand()
        beam.ce_faulty()
        beam.ce_optimized()
        beam.ce_outdated()
        beam.ce_obsolete()
        beam.ce_upgraded()
        beam.ce_advanced()
        beam.ce_widespread()
        beam.ce_tightspread()
        beam.ce_impacting()
        beam.ce_incendiary()
        beam.ce_plasma()
        beam.ce_insulated()
        beam.ce_heatshielded()
        beam.ce_radioactive()
        beam.ce_safe_nonlethal()
        beam.ce_safe()
        beam.ce_volatile()
        beam.ce_deathly()
        beam.ce_sungazer()
        beam.ce_concentrated()
        beam.ce_focused()
        beam.ce_supercharged()
        beam.ce_unfocused()
        beam.ce_industrial()
        beam.ce_swift()
        beam.ce_sluggish()
        beam.ce_extended()
        beam.ce_continuous()
        beam.ce_infinite()
        beam.ce_short()
        beam.ce_blunt()
        beam.ce_penetrating_beam()
        beam.ce_breaching_beam()
        beam.ce_stungun()
        beam.ce_shock()
        beam.ce_regulated()
        beam.ce_calibrated_beam()


def write_laser_prefixes(laser):
    """ Writes prefixed variations of laser in laser's file.

    :param Laser laser: 
    :rtype: None 
    """
    if ((laser.rarity > 0 and not ENEMY_WEAPONS) or
        (ENEMY_WEAPONS and "_ENEMY" in laser.name and
            "ENEMY_OLD" not in laser.name and
            "BA_ARTILLERY" not in laser.name and
            "DRONE" not in laser.name)):
        laser.ce_uncalibrated()
        laser.ce_unreliable()
        laser.ce_wild()
        laser.ce_suppression()
        laser.ce_piercing()
        laser.ce_low_energy()
        laser.ce_support_laser()
        laser.ce_assault_laser()
        laser.ce_assault_missiles()
        laser.ce_stalker()
        laser.ce_tactical()
        laser.ce_brutal()
        laser.ce_weaksauce()
        laser.ce_hull_ripper()
        laser.ce_reconfigured()
        laser.ce_repeater()
        laser.ce_repeater_heavy_ion()
        laser.ce_gatling()
        laser.ce_starlord()
        laser.ce_deathcharge()
        laser.ce_badass()
        laser.ce_massive()
        laser.ce_malfunctioning()
        laser.ce_damaged()
        laser.ce_heavy()
        laser.ce_light()
        laser.ce_substandard()
        laser.ce_surplus()
        laser.ce_quality()
        laser.ce_custom()
        laser.ce_vintage()
        laser.ce_antique()
        laser.ce_swag()
        laser.ce_second_hand()
        laser.ce_faulty()
        laser.ce_optimized()
        laser.ce_outdated()
        laser.ce_obsolete()
        laser.ce_upgraded()
        laser.ce_advanced()
        laser.ce_quickshot()
        laser.ce_widespread()
        laser.ce_tightspread()
        laser.ce_impacting()
        laser.ce_penetrating()
        laser.ce_breaching()
        laser.ce_photon()
        laser.ce_lowmass()
        laser.ce_lowmomentum()
        laser.ce_incendiary()
        laser.ce_plasma()
        laser.ce_insulated()
        laser.ce_heatshielded()
        laser.ce_radioactive()
        laser.ce_safe_nonlethal()
        laser.ce_safe()
        laser.ce_volatile()
        laser.ce_deathly()
        laser.ce_pulse()
        laser.ce_heavy_ion()
        laser.ce_perfect()
        laser.ce_overcharged()
        laser.ce_lowcharge()
        laser.ce_unstable()
        laser.ce_flux()
        laser.ce_warping()
        laser.ce_phasing()
        laser.ce_untuned()
        laser.ce_replicator()
        laser.ce_highyield()
        laser.ce_alpha()
        laser.ce_scrambling()
        laser.ce_wasteful()
        laser.ce_frail()
        laser.ce_highvelocity()
        laser.ce_boosted_missile()
        laser.ce_lowvelocity()
        laser.ce_torpedo()
        laser.ce_emp()
        laser.ce_emp_burst()
        laser.ce_frag()
        laser.ce_shredder()
        laser.ce_caustic()
        laser.ce_stungun()
        laser.ce_shock()
        laser.ce_regulated()
        laser.ce_concussion()
        laser.ce_predictable()
        laser.ce_calibrated()


def write_missile_prefixes(missile):
    """ Writes prefixed variations of missile in missile's file.

    :param Missile missile: 
    :rtype: None 
    """
    if ((missile.rarity > 0 and not ENEMY_WEAPONS) or
        (ENEMY_WEAPONS and "_ENEMY" in missile.name and
            "ENEMY_OLD" not in missile.name and
            "BA_ARTILLERY" not in missile.name and
            "DRONE" not in missile.name)):
        missile.ce_assault_missiles()
        missile.ce_stalker()
        missile.ce_tactical()
        missile.ce_brutal()
        missile.ce_weaksauce()
        missile.ce_hull_ripper()
        missile.ce_reconfigured()
        missile.ce_heavy()
        missile.ce_light()
        missile.ce_substandard()
        missile.ce_surplus()
        missile.ce_quality()
        missile.ce_custom()
        missile.ce_vintage()
        missile.ce_antique()
        missile.ce_swag()
        missile.ce_second_hand()
        missile.ce_faulty()
        missile.ce_optimized()
        missile.ce_outdated()
        missile.ce_obsolete()
        missile.ce_upgraded()
        missile.ce_advanced()
        missile.ce_quickshot()
        missile.ce_impacting()
        missile.ce_penetrating()
        missile.ce_breaching()
        missile.ce_lowmass()
        missile.ce_lowmomentum()
        missile.ce_incendiary()
        missile.ce_plasma()
        missile.ce_insulated()
        missile.ce_heatshielded()
        missile.ce_radioactive()
        missile.ce_safe_nonlethal()
        missile.ce_safe()
        missile.ce_volatile()
        missile.ce_overcharged()
        missile.ce_lowcharge()
        missile.ce_unstable()
        missile.ce_flux()
        missile.ce_replicator()
        missile.ce_highyield()
        missile.ce_alpha()
        missile.ce_scrambling()
        missile.ce_wasteful()
        missile.ce_frail()
        missile.ce_highvelocity()
        missile.ce_boosted_missile()
        missile.ce_lowvelocity()
        missile.ce_torpedo()
        missile.ce_emp()
        missile.ce_emp_burst()
        missile.ce_frag()
        missile.ce_shredder()
        missile.ce_caustic()
        missile.ce_stungun()
        missile.ce_shock()
        missile.ce_regulated()
        missile.ce_concussion()
        missile.ce_predictable()
        missile.ce_calibrated()


def write_bomb_prefixes(bomb):
    """ Writes prefixed variations of bomb in bomb's file.

    :param Bomb bomb: 
    :rtype: None 
    """
    if ((bomb.rarity > 0 and not ENEMY_WEAPONS) or
        (ENEMY_WEAPONS and "_ENEMY" in bomb.name and
            "ENEMY_OLD" not in bomb.name and
            "BA_ARTILLERY" not in bomb.name and
            "DRONE" not in bomb.name)):
        bomb.ce_assault_missiles()
        bomb.ce_substandard()
        bomb.ce_surplus()
        bomb.ce_quality()
        bomb.ce_custom()
        bomb.ce_vintage()
        bomb.ce_antique()
        bomb.ce_swag()
        bomb.ce_second_hand()
        bomb.ce_faulty()
        bomb.ce_optimized()
        bomb.ce_outdated()
        bomb.ce_obsolete()
        bomb.ce_upgraded()
        bomb.ce_advanced()
        bomb.ce_impacting()
        bomb.ce_incendiary()
        bomb.ce_plasma()
        bomb.ce_insulated()
        bomb.ce_heatshielded()
        bomb.ce_radioactive()
        bomb.ce_safe_nonlethal()
        bomb.ce_safe()
        bomb.ce_volatile()
        bomb.ce_pulse()
        bomb.ce_overcharged()
        bomb.ce_lowcharge()
        bomb.ce_unstable()
        bomb.ce_flux()
        bomb.ce_replicator()
        bomb.ce_highyield_bomb()
        bomb.ce_wasteful()
        bomb.ce_emp_bomb()
        bomb.ce_shredder_bomb()
        bomb.ce_caustic_bomb()
        bomb.ce_submunition()
        bomb.ce_submunition_cluster()
        bomb.ce_stungun()
        bomb.ce_shock()
        bomb.ce_regulated()
        bomb.ce_concussion()
        bomb.ce_predictable()
        bomb.ce_calibrated()


def write_burst_prefixes(burst):
    """ Writes prefixed variations of burst in burst's file.

    :param Burst burst: 
    :rtype: None 
    """
    if ((burst.rarity > 0 and not ENEMY_WEAPONS) or
        (ENEMY_WEAPONS and "_ENEMY" in burst.name and
            "ENEMY_OLD" not in burst.name and
            "BA_ARTILLERY" not in burst.name and
            "DRONE" not in burst.name)):
        burst.ce_assault_missiles()
        burst.ce_stalker()
        burst.ce_heavy()
        burst.ce_substandard()
        burst.ce_surplus()
        burst.ce_quality()
        burst.ce_custom()
        burst.ce_vintage()
        burst.ce_antique()
        burst.ce_swag()
        burst.ce_second_hand()
        burst.ce_faulty()
        burst.ce_optimized()
        burst.ce_outdated()
        burst.ce_obsolete()
        burst.ce_upgraded()
        burst.ce_advanced()
        burst.ce_quickshot()
        burst.ce_widespread_flak()
        burst.ce_tightspread_flak()
        burst.ce_impacting()
        burst.ce_penetrating()
        burst.ce_breaching()
        burst.ce_incendiary()
        burst.ce_plasma()
        burst.ce_fusion_plasma()
        burst.ce_insulated()
        burst.ce_heatshielded()
        burst.ce_radioactive()
        burst.ce_safe_nonlethal()
        burst.ce_safe()
        burst.ce_volatile()
        burst.ce_heavy_ion()
        burst.ce_perfect()
        burst.ce_replicator()
        burst.ce_highyield()
        burst.ce_alpha()
        burst.ce_wasteful()
        burst.ce_frail()
        burst.ce_highvelocity()
        burst.ce_boosted_missile()
        burst.ce_lowvelocity()
        burst.ce_torpedo()
        burst.ce_emp()
        burst.ce_emp_burst()
        burst.ce_frag()
        burst.ce_shredder()
        burst.ce_caustic()
        burst.ce_shock()
        burst.ce_regulated()
        burst.ce_concussion()
        burst.ce_predictable()
        burst.ce_calibrated()
        burst.ce_calibrated_stungun()
        burst.ce_predictable_stungun()


def defense_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param DefenseDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        drone.ce_simple()
        drone.ce_unresponsive()
        drone.ce_active()
        drone.ce_frantic()
        drone.ce_sentient()
        drone.ce_basic()
        drone.ce_smart()
        drone.ce_highvelocity()
        drone.ce_lowvelocity()
        drone.ce_swag()
        drone.ce_second_hand()
        drone.ce_faulty()
        drone.ce_optimized()
        drone.ce_autonomous()
        drone.ce_fast()
        drone.ce_boosted()
        drone.ce_more_dodge()
        drone.ce_even_more_dodge()
        drone.ce_less_dodge()
        drone.ce_slow()
        drone.ce_boosterless()


def combat_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param CombatDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        drone.ce_tactical()
        drone.ce_assault()
        drone.ce_brutal()
        drone.ce_flux()
        drone.ce_warping()
        drone.ce_phasing()
        drone.ce_perfect()
        drone.ce_sungazer()
        drone.ce_torpedo()
        drone.ce_emp()
        drone.ce_frag()
        drone.ce_shredder()
        drone.ce_deathly()
        drone.ce_hull_ripper()
        drone.ce_widespread()
        drone.ce_tightspread()
        drone.ce_incendiary()
        drone.ce_radioactive()
        drone.ce_volatile()
        drone.ce_safe()
        drone.ce_focus()
        drone.ce_sentient()
        drone.ce_highvelocity()
        drone.ce_lowvelocity()
        drone.ce_swag()
        drone.ce_second_hand()
        drone.ce_faulty()
        drone.ce_optimized()
        drone.ce_autonomous()
        drone.ce_fast()
        drone.ce_boosted()
        drone.ce_more_dodge()
        drone.ce_even_more_dodge()
        drone.ce_less_dodge()
        drone.ce_slow()
        drone.ce_boosterless()


def battle_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param BattleDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        drone.ce_faulty()
        drone.ce_optimized()
        drone.ce_autonomous()
        drone.ce_standard_internal_1()
        drone.ce_standard_internal_2()
        drone.ce_standard_internal_3()


def repair_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param RepairDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        drone.ce_faulty()
        drone.ce_optimized()
        drone.ce_autonomous()
        drone.ce_standard_internal_1()
        drone.ce_standard_internal_2()
        drone.ce_standard_internal_3()


def boarder_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param BoarderDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        drone.ce_faulty()
        drone.ce_optimized()
        drone.ce_autonomous()
        drone.ce_fast()
        drone.ce_boosted()
        drone.ce_slow()
        drone.ce_standard_internal_1()
        drone.ce_standard_internal_2()
        drone.ce_standard_internal_3()


def ship_repair_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param ShipRepairDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        # nothing yet... different colors maybe?
        # there are already types which make it change its speed
        pass


def shield_drone_prefixes(drone):
    """ Writes prefixed variations of drone in drone's file.

    :param ShieldDrone drone:
    :rtype: None
    """
    if ((drone.rarity > 0 and not ENEMY_DRONES) or
        (ENEMY_DRONES and "_ENEMY" in drone.name)):
        # nothing yet...
        pass


def _nmpc_store_weapons(node, filewrite):
    """ Returns the weapon indicated by node after storing it
        into its respective class.

    :param Element node:
    :param File filewrite:
    :rtype: Beam|Laser|Missile|Bomb|Burst
    """
    weapon_type = ''
    for bob in node:
        if bob.tag == 'type':
            weapon_type = bob.text
            break
    if weapon_type == 'BEAM':
        beam = Beam(filewrite)
        beam.name, beam.name2 = \
            node.attrib['name'], node.attrib['name']
        for sub in node:
            if sub.tag == 'flavorType':
                beam.flavorType, beam.flavorType2 = sub.text, sub.text
                beam.flavorType_true = False
                beam.flavorType_true2 = False
            elif sub.tag == 'tip':
                beam.tip, beam.tip2 = sub.text, sub.text
                beam.tip_true = True
                beam.tip_true2 = True
            elif sub.tag == 'title':
                beam.title, beam.title2 = sub.text, sub.text
            elif sub.tag == 'short':
                beam.short, beam.short2 = sub.text, sub.text
            elif sub.tag == 'desc':
                beam.desc, beam.desc2 = sub.text, sub.text
            elif sub.tag == 'tooltip':
                beam.tooltip, beam.tooltip2 = sub.text, sub.text
            elif sub.tag == 'ion':
                beam.ion, beam.ion2 = int(sub.text), int(sub.text)
                beam.ion_true, beam.ion_true2 = True, True
            elif sub.tag == 'damage':
                beam.damage, beam.damage2 = \
                    int(sub.text), int(sub.text)
                beam.damage_true = True
                beam.damage_true2 = True
            elif sub.tag == 'sysDamage':
                beam.sysDamage, beam.sysDamage2 = \
                    int(sub.text), int(sub.text)
                beam.sysDamage_true = True
                beam.sysDamage_true2 = True
            elif sub.tag == 'persDamage':
                beam.persDamage, beam.persDamage2 = \
                    int(sub.text), int(sub.text)
                beam.persDamage_true = True
                beam.persDamage_true2 = True
            elif sub.tag == 'fireChance':
                beam.fireChance, beam.fireChance2 = \
                    int(sub.text), int(sub.text)
                beam.fireChance_true = True
                beam.fireChance_true2 = True
            elif sub.tag == 'breachChance':
                beam.breachChance, beam.breachChance2 = \
                    int(sub.text), int(sub.text)
                beam.breachChance_true = True
                beam.breachChance_true2 = True
            elif sub.tag == 'stunChance':
                beam.stunChance, beam.stunChance2 = \
                    int(sub.text), int(sub.text)
                beam.stunChance_true = True
                beam.stunChance_true2 = True
            elif sub.tag == 'stun':
                beam.stun, beam.stun2 = \
                    float(sub.text), float(sub.text)
                beam.stun_true, beam.stun_true2 = True, True
            elif sub.tag == 'cooldown':
                beam.cooldown, beam.cooldown2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'power':
                beam.power, beam.power2 = int(sub.text), int(sub.text)
            elif sub.tag == 'cost':
                beam.cost, beam.cost2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'rarity':
                beam.rarity, beam.rarity2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'bp':
                beam.bp, beam.bp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'weaponArt':
                beam.weaponArt, beam.weaponArt2 = sub.text, sub.text
            elif sub.tag == 'launchSounds':
                for sound in sub:
                    beam.launchSounds.append(sound.text)
                    beam.launchSounds2.append(sound.text)
            elif sub.tag == 'hullBust':
                beam.hullBust, beam.hullBust2 = \
                    int(sub.text), int(sub.text)
                beam.hullBust_true, beam.hullBust_true2 = True, True
            # elif sub.tag == 'lockdown':
            #    beam.lockdown, beam.lockdown2 = \
            #        int(sub.text), int(sub.text)
            #    beam.lockdown_true = True
            #    beam.lockdown_true2 = True
            elif sub.tag == 'boost':
                beam.boost_true = True
                beam.boost_true2 = True
                for sub_boost in sub:
                    if sub_boost.tag == 'type':
                        beam.boost.append(sub_boost.text)
                        beam.boost2.append(sub_boost.text)
                    elif sub_boost.tag == 'amount':
                        beam.boost.append(float(sub_boost.text))
                        beam.boost2.append(float(sub_boost.text))
                    elif sub_boost.tag == 'count':
                        beam.boost.append(int(sub_boost.text))
                        beam.boost2.append(int(sub_boost.text))
            # specific to BEAM
            elif sub.tag == 'speed':
                beam.speed, beam.speed2 = \
                    float(sub.text), float(sub.text)
                beam.speed_true = True
                beam.speed_true2 = True
            elif sub.tag == 'sp':
                beam.sp, beam.sp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'image':
                beam.image, beam.image2 = sub.text, sub.text
            elif sub.tag == 'color':
                for color in sub:
                    beam.colors.append(int(color.text))
                    beam.colors2.append(int(color.text))
            elif sub.tag == 'length':
                beam.length = float(sub.text)
                beam.length2 = float(sub.text)
        # default speeds
        if not beam.speed_true:
            # is this 5 or 8?
            beam.speed = 5
            beam.speed2 = 5
        # default beam colors, right?
        if len(beam.colors) == 0:
            beam.colors.extend([255, 0, 0])
            beam.colors2.extend([255, 0, 0])
        return beam
    elif weapon_type == 'LASER':
        laser = Laser(filewrite)
        laser.name, laser.name2 = \
            node.attrib['name'], node.attrib['name']
        for sub in node:
            if sub.tag == 'flavorType':
                laser.flavorType, laser.flavorType2 = \
                    sub.text, sub.text
                laser.flavorType_true = False
                laser.flavorType_true2 = False
            elif sub.tag == 'tip':
                laser.tip, laser.tip2 = sub.text, sub.text
                laser.tip_true = True
                laser.tip_true2 = True
            elif sub.tag == 'title':
                laser.title, laser.title2 = sub.text, sub.text
            elif sub.tag == 'short':
                laser.short, laser.short2 = sub.text, sub.text
            elif sub.tag == 'desc':
                laser.desc, laser.desc2 = sub.text, sub.text
            elif sub.tag == 'tooltip':
                laser.tooltip, laser.tooltip2 = sub.text, sub.text
            elif sub.tag == 'ion':
                laser.ion, laser.ion2 = int(sub.text), int(sub.text)
                laser.ion_true, laser.ion_true2 = True, True
            elif sub.tag == 'damage':
                laser.damage, laser.damage2 = \
                    int(sub.text), int(sub.text)
                laser.damage_true = True
                laser.damage_true2 = True
            elif sub.tag == 'sysDamage':
                laser.sysDamage, laser.sysDamage2 = \
                    int(sub.text), int(sub.text)
                laser.sysDamage_true = True
                laser.sysDamage_true2 = True
            elif sub.tag == 'persDamage':
                laser.persDamage, laser.persDamage2 = \
                    int(sub.text), int(sub.text)
                laser.persDamage_true = True
                laser.persDamage_true2 = True
            elif sub.tag == 'fireChance':
                laser.fireChance, laser.fireChance2 = \
                    int(sub.text), int(sub.text)
                laser.fireChance_true = True
                laser.fireChance_true2 = True
            elif sub.tag == 'breachChance':
                laser.breachChance, laser.breachChance2 = \
                    int(sub.text), int(sub.text)
                laser.breachChance_true = True
                laser.breachChance_true2 = True
            elif sub.tag == 'stunChance':
                laser.stunChance, laser.stunChance2 = \
                    int(sub.text), int(sub.text)
                laser.stunChance_true = True
                laser.stunChance_true2 = True
            elif sub.tag == 'stun':
                laser.stun, laser.stun2 = \
                    float(sub.text), float(sub.text)
                laser.stun_true, laser.stun_true2 = True, True
            elif sub.tag == 'cooldown':
                laser.cooldown, laser.cooldown2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'power':
                laser.power, laser.power2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'cost':
                laser.cost, laser.cost2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'rarity':
                laser.rarity, laser.rarity2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'bp':
                laser.bp, laser.bp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'weaponArt':
                laser.weaponArt, laser.weaponArt2 = sub.text, sub.text
            elif sub.tag == 'launchSounds':
                for sound in sub:
                    laser.launchSounds.append(sound.text)
                    laser.launchSounds2.append(sound.text)
            elif sub.tag == 'hullBust':
                laser.hullBust, laser.hullBust2 = \
                    int(sub.text), int(sub.text)
                laser.hullBust_true, laser.hullBust_true2 = True, True
            elif sub.tag == 'lockdown':
                laser.lockdown, laser.lockdown2 = \
                    int(sub.text), int(sub.text)
                laser.lockdown_true = True
                laser.lockdown_true2 = True
            elif sub.tag == 'boost':
                laser.boost_true = True
                laser.boost_true2 = True
                for sub_boost in sub:
                    if sub_boost.tag == 'type':
                        laser.boost.append(sub_boost.text)
                        laser.boost2.append(sub_boost.text)
                    elif sub_boost.tag == 'amount':
                        laser.boost.append(float(sub_boost.text))
                        laser.boost2.append(float(sub_boost.text))
                    elif sub_boost.tag == 'count':
                        laser.boost.append(int(sub_boost.text))
                        laser.boost2.append(int(sub_boost.text))
            # specific to LASER
            elif sub.tag == 'speed':
                laser.speed, laser.speed2 = \
                    float(sub.text), float(sub.text)
                laser.speed_true = True
                laser.speed_true2 = True
            elif sub.tag == 'sp':
                laser.sp, laser.sp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'image':
                laser.image, laser.image2 = sub.text, sub.text
            elif sub.tag == 'explosion':
                laser.explosion_true = True
                laser.explosion_true2 = True
                laser.explosion, laser.explosion2 = sub.text, sub.text
            elif sub.tag == 'shots':
                laser.shots, laser.shots2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'missiles':
                laser.missiles, laser.missiles2 = \
                    int(sub.text), int(sub.text)
                laser.missiles_true = True
                laser.missiles_true2 = True
            elif sub.tag == 'hitShipSounds':
                for sound in sub:
                    laser.hitShipSounds.append(sound.text)
                    laser.hitShipSounds2.append(sound.text)
            elif sub.tag == 'hitShieldSounds':
                for sound in sub:
                    laser.hitShieldSounds.append(sound.text)
                    laser.hitShieldSounds2.append(sound.text)
            elif sub.tag == 'missSounds':
                for sound in sub:
                    laser.missSounds.append(sound.text)
                    laser.missSounds2.append(sound.text)
            elif sub.tag == 'locked':
                laser.locked_true = True
                laser.locked_true2 = True
                laser.locked, laser.locked2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'chargeLevels':
                laser.chargeLevels_true = True
                laser.chargeLevels_true2 = True
                laser.chargeLevels, laser.chargeLevels2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'drone_targetable' and sub.text is None:
                laser.droneTargetable_none = True
                laser.droneTargetable_none2 = True
            elif sub.tag == 'drone_targetable':
                laser.droneTargetable = int(sub.text)
                laser.droneTargetable2 = int(sub.text)
                laser.droneTargetable_true = True
                laser.droneTargetable_true2 = True
        # default speeds
        if not laser.speed_true:
            laser.speed = 60
            laser.speed2 = 60
        return laser
    elif weapon_type == 'MISSILES':
        missile = Missile(filewrite)
        missile.name, missile.name2 = \
            node.attrib['name'], node.attrib['name']
        for sub in node:
            if sub.tag == 'flavorType':
                missile.flavorType, missile.flavorType2 = \
                    sub.text, sub.text
                missile.flavorType_true = False
                missile.flavorType_true2 = False
            elif sub.tag == 'tip':
                missile.tip, missile.tip2 = sub.text, sub.text
                missile.tip_true = True
                missile.tip_true2 = True
            elif sub.tag == 'title':
                missile.title, missile.title2 = sub.text, sub.text
            elif sub.tag == 'short':
                missile.short, missile.short2 = sub.text, sub.text
            elif sub.tag == 'desc':
                missile.desc, missile.desc2 = sub.text, sub.text
            elif sub.tag == 'tooltip':
                missile.tooltip, missile.tooltip2 = sub.text, sub.text
            elif sub.tag == 'ion':
                missile.ion, missile.ion2 = int(sub.text), int(sub.text)
                missile.ion_true, missile.ion_true2 = True, True
            elif sub.tag == 'damage':
                missile.damage, missile.damage2 = \
                    int(sub.text), int(sub.text)
                missile.damage_true = True
                missile.damage_true2 = True
            elif sub.tag == 'sysDamage':
                missile.sysDamage, missile.sysDamage2 = \
                    int(sub.text), int(sub.text)
                missile.sysDamage_true = True
                missile.sysDamage_true2 = True
            elif sub.tag == 'persDamage':
                missile.persDamage, missile.persDamage2 = \
                    int(sub.text), int(sub.text)
                missile.persDamage_true = True
                missile.persDamage_true2 = True
            elif sub.tag == 'fireChance':
                missile.fireChance, missile.fireChance2 = \
                    int(sub.text), int(sub.text)
                missile.fireChance_true = True
                missile.fireChance_true2 = True
            elif sub.tag == 'breachChance':
                missile.breachChance, missile.breachChance2 = \
                    int(sub.text), int(sub.text)
                missile.breachChance_true = True
                missile.breachChance_true2 = True
            elif sub.tag == 'stunChance':
                missile.stunChance, missile.stunChance2 = \
                    int(sub.text), int(sub.text)
                missile.stunChance_true = True
                missile.stunChance_true2 = True
            elif sub.tag == 'stun':
                missile.stun, missile.stun2 = \
                    float(sub.text), float(sub.text)
                missile.stun_true, missile.stun_true2 = True, True
            elif sub.tag == 'cooldown':
                missile.cooldown, missile.cooldown2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'power':
                missile.power, missile.power2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'cost':
                missile.cost, missile.cost2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'rarity':
                missile.rarity, missile.rarity2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'bp':
                missile.bp, missile.bp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'weaponArt':
                missile.weaponArt, missile.weaponArt2 = sub.text, sub.text
            elif sub.tag == 'launchSounds':
                for sound in sub:
                    missile.launchSounds.append(sound.text)
                    missile.launchSounds2.append(sound.text)
            elif sub.tag == 'hullBust':
                missile.hullBust, missile.hullBust2 = \
                    int(sub.text), int(sub.text)
                missile.hullBust_true, missile.hullBust_true2 = True, True
            elif sub.tag == 'lockdown':
                missile.lockdown, missile.lockdown2 = \
                    int(sub.text), int(sub.text)
                missile.lockdown_true = True
                missile.lockdown_true2 = True
            elif sub.tag == 'boost':
                missile.boost_true = True
                missile.boost_true2 = True
                for sub_boost in sub:
                    if sub_boost.tag == 'type':
                        missile.boost.append(sub_boost.text)
                        missile.boost2.append(sub_boost.text)
                    elif sub_boost.tag == 'amount':
                        missile.boost.append(float(sub_boost.text))
                        missile.boost2.append(float(sub_boost.text))
                    elif sub_boost.tag == 'count':
                        missile.boost.append(int(sub_boost.text))
                        missile.boost2.append(int(sub_boost.text))
            # specific to MISSILES
            elif sub.tag == 'speed':
                missile.speed, missile.speed2 = \
                    float(sub.text), float(sub.text)
                missile.speed_true = True
                missile.speed_true2 = True
            elif sub.tag == 'shots':
                missile.shots = int(sub.text)
                missile.shots2 = int(sub.text)
            elif sub.tag == 'sp':
                missile.sp, missile.sp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'missiles':
                missile.missiles = int(sub.text)
                missile.missiles2 = int(sub.text)
            elif sub.tag == 'image':
                missile.image, missile.image2 = sub.text, sub.text
            elif sub.tag == 'explosion':
                missile.explosion_true = True
                missile.explosion_true2 = True
                missile.explosion, missile.explosion2 = sub.text, sub.text
            elif sub.tag == 'hitShipSounds':
                for sound in sub:
                    missile.hitShipSounds.append(sound.text)
                    missile.hitShipSounds2.append(sound.text)
            elif sub.tag == 'hitShieldSounds':
                for sound in sub:
                    missile.hitShieldSounds.append(sound.text)
                    missile.hitShieldSounds2.append(sound.text)
            elif sub.tag == 'missSounds':
                for sound in sub:
                    missile.missSounds.append(sound.text)
                    missile.missSounds2.append(sound.text)
            elif sub.tag == 'drone_targetable' and sub.text is None:
                missile.droneTargetable_none = True
                missile.droneTargetable_none2 = True
            elif sub.tag == 'drone_targetable':
                missile.droneTargetable = int(sub.text)
                missile.droneTargetable2 = int(sub.text)
                missile.droneTargetable_true = True
                missile.droneTargetable_true2 = True
        # default speeds
        if not missile.speed_true:
            missile.speed = 35
            missile.speed2 = 35
        return missile
    elif weapon_type == 'BOMB':
        bomb = Bomb(filewrite)
        bomb.name, bomb.name2 = \
            node.attrib['name'], node.attrib['name']
        for sub in node:
            if sub.tag == 'flavorType':
                bomb.flavorType, bomb.flavorType2 = \
                    sub.text, sub.text
                bomb.flavorType_true = False
                bomb.flavorType_true2 = False
            elif sub.tag == 'tip':
                bomb.tip, bomb.tip2 = sub.text, sub.text
                bomb.tip_true = True
                bomb.tip_true2 = True
            elif sub.tag == 'title':
                bomb.title, bomb.title2 = sub.text, sub.text
            elif sub.tag == 'short':
                bomb.short, bomb.short2 = sub.text, sub.text
            elif sub.tag == 'desc':
                bomb.desc, bomb.desc2 = sub.text, sub.text
            elif sub.tag == 'tooltip':
                bomb.tooltip, bomb.tooltip2 = sub.text, sub.text
            elif sub.tag == 'ion':
                bomb.ion, bomb.ion2 = int(sub.text), int(sub.text)
                bomb.ion_true, bomb.ion_true2 = True, True
            elif sub.tag == 'damage':
                bomb.damage, bomb.damage2 = \
                    int(sub.text), int(sub.text)
                bomb.damage_true = True
                bomb.damage_true2 = True
            elif sub.tag == 'sysDamage':
                bomb.sysDamage, bomb.sysDamage2 = \
                    int(sub.text), int(sub.text)
                bomb.sysDamage_true = True
                bomb.sysDamage_true2 = True
            elif sub.tag == 'persDamage':
                bomb.persDamage, bomb.persDamage2 = \
                    int(sub.text), int(sub.text)
                bomb.persDamage_true = True
                bomb.persDamage_true2 = True
            elif sub.tag == 'fireChance':
                bomb.fireChance, bomb.fireChance2 = \
                    int(sub.text), int(sub.text)
                bomb.fireChance_true = True
                bomb.fireChance_true2 = True
            elif sub.tag == 'breachChance':
                bomb.breachChance, bomb.breachChance2 = \
                    int(sub.text), int(sub.text)
                bomb.breachChance_true = True
                bomb.breachChance_true2 = True
            elif sub.tag == 'stunChance':
                bomb.stunChance, bomb.stunChance2 = \
                    int(sub.text), int(sub.text)
                bomb.stunChance_true = True
                bomb.stunChance_true2 = True
            elif sub.tag == 'stun':
                bomb.stun, bomb.stun2 = \
                    float(sub.text), float(sub.text)
                bomb.stun_true, bomb.stun_true2 = True, True
            elif sub.tag == 'cooldown':
                bomb.cooldown, bomb.cooldown2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'power':
                bomb.power, bomb.power2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'cost':
                bomb.cost, bomb.cost2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'rarity':
                bomb.rarity, bomb.rarity2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'bp':
                bomb.bp, bomb.bp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'weaponArt':
                bomb.weaponArt, bomb.weaponArt2 = sub.text, sub.text
            elif sub.tag == 'launchSounds':
                for sound in sub:
                    bomb.launchSounds.append(sound.text)
                    bomb.launchSounds2.append(sound.text)
            elif sub.tag == 'hullBust':
                bomb.hullBust, bomb.hullBust2 = \
                    int(sub.text), int(sub.text)
                bomb.hullBust_true, bomb.hullBust_true2 = True, True
            elif sub.tag == 'lockdown':
                bomb.lockdown, bomb.lockdown2 = \
                    int(sub.text), int(sub.text)
                bomb.lockdown_true = True
                bomb.lockdown_true2 = True
            elif sub.tag == 'boost':
                bomb.boost_true = True
                bomb.boost_true2 = True
                for sub_boost in sub:
                    if sub_boost.tag == 'type':
                        bomb.boost.append(sub_boost.text)
                        bomb.boost2.append(sub_boost.text)
                    elif sub_boost.tag == 'amount':
                        bomb.boost.append(float(sub_boost.text))
                        bomb.boost2.append(float(sub_boost.text))
                    elif sub_boost.tag == 'count':
                        bomb.boost.append(int(sub_boost.text))
                        bomb.boost2.append(int(sub_boost.text))
            # specific to BOMB
            elif sub.tag == 'shots':
                bomb.shots, bomb.shots2 = int(sub.text), int(sub.text)
            elif sub.tag == 'missiles':
                bomb.missiles, bomb.missiles2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'hitShipSounds':
                for sound in sub:
                    bomb.hitShipSounds.append(sound.text)
                    bomb.hitShipSounds2.append(sound.text)
            elif sub.tag == 'image':
                bomb.image, bomb.image2 = sub.text, sub.text
            elif sub.tag == 'explosion':
                bomb.explosion, bomb.explosion2 = sub.text, sub.text
            elif sub.tag == 'locked':
                bomb.locked, bomb.locked2 = sub.text, sub.text
        return bomb
    elif weapon_type == 'BURST':
        burst = Burst(filewrite)
        burst.name, burst.name2 = \
            node.attrib['name'], node.attrib['name']
        for sub in node:
            if sub.tag == 'flavorType':
                burst.flavorType, burst.flavorType2 = \
                    sub.text, sub.text
                burst.flavorType_true = False
                burst.flavorType_true2 = False
            elif sub.tag == 'tip':
                burst.tip, burst.tip2 = sub.text, sub.text
                burst.tip_true = True
                burst.tip_true2 = True
            elif sub.tag == 'title':
                burst.title, burst.title2 = sub.text, sub.text
            elif sub.tag == 'short':
                burst.short, burst.short2 = sub.text, sub.text
            elif sub.tag == 'desc':
                burst.desc, burst.desc2 = sub.text, sub.text
            elif sub.tag == 'tooltip':
                burst.tooltip, burst.tooltip2 = sub.text, sub.text
            elif sub.tag == 'ion':
                burst.ion, burst.ion2 = int(sub.text), int(sub.text)
                burst.ion_true, burst.ion_true2 = True, True
            elif sub.tag == 'damage':
                burst.damage, burst.damage2 = \
                    int(sub.text), int(sub.text)
                burst.damage_true = True
                burst.damage_true2 = True
            elif sub.tag == 'sysDamage':
                burst.sysDamage, burst.sysDamage2 = \
                    int(sub.text), int(sub.text)
                burst.sysDamage_true = True
                burst.sysDamage_true2 = True
            elif sub.tag == 'persDamage':
                burst.persDamage, burst.persDamage2 = \
                    int(sub.text), int(sub.text)
                burst.persDamage_true = True
                burst.persDamage_true2 = True
            elif sub.tag == 'shots':
                burst.shots, burst.shots2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'fireChance':
                burst.fireChance, burst.fireChance2 = \
                    int(sub.text), int(sub.text)
                burst.fireChance_true = True
                burst.fireChance_true2 = True
            elif sub.tag == 'breachChance':
                burst.breachChance, burst.breachChance2 = \
                    int(sub.text), int(sub.text)
                burst.breachChance_true = True
                burst.breachChance_true2 = True
            elif sub.tag == 'stunChance':
                burst.stunChance, burst.stunChance2 = \
                    int(sub.text), int(sub.text)
                burst.stunChance_true = True
                burst.stunChance_true2 = True
            elif sub.tag == 'stun':
                burst.stun, burst.stun2 = \
                    float(sub.text), float(sub.text)
                burst.stun_true, burst.stun_true2 = True, True
            elif sub.tag == 'cooldown':
                burst.cooldown, burst.cooldown2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'power':
                burst.power, burst.power2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'cost':
                burst.cost, burst.cost2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'rarity':
                burst.rarity, burst.rarity2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'bp':
                burst.bp, burst.bp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'weaponArt':
                burst.weaponArt, burst.weaponArt2 = sub.text, sub.text
            elif sub.tag == 'launchSounds':
                for sound in sub:
                    burst.launchSounds.append(sound.text)
                    burst.launchSounds2.append(sound.text)
            elif sub.tag == 'hullBust':
                burst.hullBust, burst.hullBust2 = \
                    int(sub.text), int(sub.text)
                burst.hullBust_true, burst.hullBust_true2 = True, True
            elif sub.tag == 'lockdown':
                burst.lockdown, burst.lockdown2 = \
                    int(sub.text), int(sub.text)
                burst.lockdown_true = True
                burst.lockdown_true2 = True
            elif sub.tag == 'boost':
                burst.boost_true = True
                burst.boost_true2 = True
                for sub_boost in sub:
                    if sub_boost.tag == 'type':
                        burst.boost.append(sub_boost.text)
                        burst.boost2.append(sub_boost.text)
                    elif sub_boost.tag == 'amount':
                        burst.boost.append(float(sub_boost.text))
                        burst.boost2.append(float(sub_boost.text))
                    elif sub_boost.tag == 'count':
                        burst.boost.append(int(sub_boost.text))
                        burst.boost2.append(int(sub_boost.text))
            # specific to BURST
            elif sub.tag == 'speed':
                burst.speed_true = True
                burst.speed_true2 = True
                burst.speed, burst.speed2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'projectiles':
                for projectile in sub:
                    burst.projectiles.append(
                        [int(projectile.attrib['count']),
                         projectile.attrib['fake'],
                         projectile.text])
                    burst.projectiles2.append(
                        [int(projectile.attrib['count']),
                         projectile.attrib['fake'],
                         projectile.text])
            elif sub.tag == 'radius':
                burst.radius, burst.radius2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'spin':
                burst.spin_true, burst.spin_true2 = True, True
                burst.spin, burst.spin2 = \
                    float(sub.text), float(sub.text)
            elif sub.tag == 'sp':
                burst.sp, burst.sp2 = int(sub.text), int(sub.text)
            elif sub.tag == 'missiles':
                burst.missiles_true = True
                burst.missiles_true2 = True
                burst.missiles, burst.missiles2 = \
                    int(sub.text), int(sub.text)
            elif sub.tag == 'hitShipSounds':
                for sound in sub:
                    burst.hitShipSounds.append(sound.text)
                    burst.hitShipSounds2.append(sound.text)
            elif sub.tag == 'hitShieldSounds':
                for sound in sub:
                    burst.hitShieldSounds.append(sound.text)
                    burst.hitShieldSounds2.append(sound.text)
            elif sub.tag == 'missSounds':
                for sound in sub:
                    burst.missSounds.append(sound.text)
                    burst.missSounds2.append(sound.text)
            elif sub.tag == 'explosion':
                burst.explosion_true = True
                burst.explosion_true2 = True
                burst.explosion, burst.explosion2 = sub.text, sub.text
            elif sub.tag == 'drone_targetable' and sub.text is None:
                burst.droneTargetable_none = True
                burst.droneTargetable_none2 = True
            elif sub.tag == 'drone_targetable':
                burst.droneTargetable = int(sub.text)
                burst.droneTargetable2 = int(sub.text)
                burst.droneTargetable_true = True
                burst.droneTargetable_true2 = True
            elif sub.tag == 'chargeLevels':
                burst.chargeLevels_true = True
                burst.chargeLevels_true2 = True
                burst.chargeLevels, burst.chargeLevels2 = \
                    int(sub.text), int(sub.text)
        if not burst.speed_true:
            burst.speed = 35
            burst.speed2 = 35
        return burst
    else:
        raise ValueError("{}'s type tag doesn't have a proper "
                         "weapon type!".format(node.attrib['name']))


def new_main_prefix_creation(rootElement, file_to_write):
    """ Stores each weapon using the weaponBlueprint tags in the tree 
        rootElement refers to and writes modified variations specified by
        write_prefixes in file_to_write.

        :param Element rootElement: the root of a tree containing info
                                    on an xml file
        :param File file_to_write: the file to which to write 
                                   the modified weapons into
        :rtype: None 
        """
    # XML Parser is the way to go! no need to worry about comments!
    for child in rootElement:
        if child.tag == 'weaponBlueprint' and not DRONE_CREATION:
            # writing weapon modifiers
            weapon = _nmpc_store_weapons(child, file_to_write)
            if type(weapon) is Beam:
                write_beam_prefixes(weapon)
            elif type(weapon) is Laser:
                write_laser_prefixes(weapon)
            elif type(weapon) is Missile:
                write_missile_prefixes(weapon)
            elif type(weapon) is Bomb:
                write_bomb_prefixes(weapon)
            elif type(weapon) is Burst:
                write_burst_prefixes(weapon)
        elif child.tag == 'droneBlueprint' and DRONE_CREATION:
            # writing drone modifiers, and drone weapon modifiers
            drone_type = ''
            for joe in child:
                if joe.tag == 'type':
                    drone_type = joe.text
                    break
            if drone_type == 'DEFENSE':
                drone = DefenseDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                    # Defense Drone only
                    elif dr.tag == 'level':
                        drone.level, drone.level2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'target':
                        drone.target, drone.target_true = dr.text, True
                        drone.target2, drone.target_true2 = dr.text, True
                    elif dr.tag == 'cooldown':
                        drone.cooldown, drone.cooldown2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'dodge':
                        drone.dodge, drone.dodge2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'speed':
                        drone.speed, drone.speed2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'droneImage':
                        drone.droneImage, drone.droneImage2 = dr.text, dr.text
                    elif dr.tag == 'weaponBlueprint':
                        drone.weaponBlueprint, drone.weaponBlueprint2 = \
                            dr.text, dr.text
                        # is this a good link?
                        for blueprint in rootElement:
                            if blueprint.attrib['name'] == drone.weaponBlueprint:
                                drone.weapon = _nmpc_store_weapons(
                                    blueprint, file_to_write)
                                break
                defense_prefixes(drone)
            elif drone_type == 'COMBAT':
                drone = CombatDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                    # Combat Drone only
                    elif dr.tag == 'cooldown':
                        drone.cooldown, drone.cooldown2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'weaponBlueprint':
                        drone.weaponBlueprint, drone.weaponBlueprint2 = \
                            dr.text, dr.text
                        # is this a good link?
                        for blueprint in rootElement:
                            if blueprint.attrib['name'] == drone.weaponBlueprint:
                                drone.weapon = _nmpc_store_weapons(
                                    blueprint, file_to_write)
                                break
                    elif dr.tag == 'speed':
                        drone.speed, drone.speed2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'dodge':
                        drone.dodge, drone.dodge2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'droneImage':
                        drone.droneImage, drone.droneImage2 = dr.text, dr.text
                combat_prefixes(drone)
            elif drone_type == 'BATTLE':
                drone = BattleDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                    # Battle Drone only
                    elif dr.tag == 'locked':
                        drone.locked, drone.locked2 = \
                            int(dr.text), int(dr.text)
                battle_prefixes(drone)
            elif drone_type == 'REPAIR':
                drone = RepairDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                repair_prefixes(drone)
            elif drone_type == 'BOARDER':
                drone = BoarderDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                    # Boarder Drone only
                    elif dr.tag == 'locked':
                        drone.locked, drone.locked2 = \
                            int(dr.text), int(dr.text)
                    elif dr.tag == 'speed':
                        drone.speed, drone.speed2 = \
                            float(dr.text), float(dr.text)
                boarder_prefixes(drone)
            elif drone_type == 'SHIP_REPAIR':
                drone = ShipRepairDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                    # Ship Repair Drone only
                    elif dr.tag == 'cooldown':
                        drone.cooldown, drone.cooldown2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'speed':
                        drone.speed, drone.speed2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'image':
                        drone.image, drone.image2 = dr.text, dr.text
                    elif dr.tag == 'droneImage':
                        drone.droneImage, drone.droneImage2 = dr.text, dr.text
                ship_repair_prefixes(drone)
            elif drone_type == 'SHIELD':
                drone = ShieldDrone(file_to_write)
                drone.name, drone.name2 = \
                    child.attrib['name'], child.attrib['name']
                for dr in child:
                    if dr.tag == 'tip':
                        drone.tip, drone.tip_true = dr.text, True
                        drone.tip2, drone.tip_true2 = dr.text, True
                    elif dr.tag == 'title':
                        drone.title, drone.title2 = dr.text, dr.text
                    elif dr.tag == 'short':
                        drone.short, drone.short2 = dr.text, dr.text
                    elif dr.tag == 'desc':
                        drone.desc, drone.desc2 = dr.text, dr.text
                    elif dr.tag == 'power':
                        drone.power, drone.power2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cost':
                        drone.cost, drone.cost2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'bp':
                        drone.bp, drone.bp2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'rarity':
                        drone.rarity, drone.rarity2 = \
                            int(dr.text), int(dr.text)
                    # Shield Drone only
                    elif dr.tag == 'level':
                        drone.level, drone.level2 = int(dr.text), int(dr.text)
                    elif dr.tag == 'cooldown':
                        drone.cooldown, drone.cooldown2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'dodge':
                        drone.dodge, drone.dodge2 = \
                            float(dr.text), float(dr.text)
                    elif dr.tag == 'speed':
                        drone.speed, drone.speed2 = \
                            float(dr.text), float(dr.text)
                shield_drone_prefixes(drone)
            else:
                raise ValueError("{}'s type tag doesn't have a proper "
                                 "drone type!".format(child.attrib['name']))


def enter_files(write_style):
    """ Selects the files to use via user entry from standard input.
    
    This function is required to always catch an invalid file to read from.

    :param str write_style: a setting of how to open a file to write to for
    """
    try:
        print(prefix_read_prompt)
        tkinter.Tk().withdraw()
        entered_reading_file = askopenfilename()
        with open(entered_reading_file, 'r') as reading_file:
            # file to read from's contents stored in ElementTree
            tree = ElementTree.parse(reading_file)
            root = tree.getroot()

            # briefly tells you what the current setting is,
            # but do not rely on these to tell you what the settings do
            if write_style == 'r' or write_style == 'rb':
                print("ERROR: File to write to is set as READ not WRITE.")
            elif write_style == 'r+':
                print("File to write to is set as OVERWRITE. "
                      "Will only write to if file exists.")
            elif write_style == 'w' or write_style == 'w+':
                print("File to write to's current contents "
                      "will be deleted if it exists.")
            elif write_style == 'a' or write_style == 'a+':
                print("File to write to is set as APPEND.")
            elif write_style == "wb":
                print("Binary file writing has been specified.")
                print("If file exists its contents will be deleted.")
            elif write_style == 'r+b':
                print("Binary file writing has been specified.")
                print("File to write to is set as OVERWRITE. "
                      "Will only write to if file exists.")
            else:
                print("WARNING: Current setting WILL cause an error!")

            entered_writing_file = input(prefix_write_prompt)
            with open(entered_writing_file,
                      write_style) as writing_file:
                # main_prefix_creation(reading_file, writing_file)
                new_main_prefix_creation(root, writing_file)
    except FileNotFoundError:
        print("If you're trying to quit, end the program, not the dialog.")
        enter_files(write_style)


def main_prefix_player():
    global DRONE_CREATION
    print("Player Weapons: blueprints.xml.append")
    enter_files('w')
    DRONE_CREATION = True
    print("Player Drones: blueprints.xml.append")
    enter_files('a')
    DRONE_CREATION = False
    print("Player Weapons: dlcBlueprints.xml.append")
    enter_files('w')
    DRONE_CREATION = True
    print("Player Drones: dlcBlueprints.xml.append")
    enter_files('a')


def main_prefix_enemy():
    global DRONE_CREATION
    global ENEMY_WEAPONS
    global ENEMY_DRONES
    # ENEMY right now only exists in blueprints.xml.append
    DRONE_CREATION, ENEMY_WEAPONS = False, True
    print("Enemy Weapons: blueprints.xml.append")
    enter_files('w')
    DRONE_CREATION, ENEMY_DRONES = True, True
    print("Enemy Drones: blueprints.xml.append")
    enter_files('a')


def main_auto_player():
    print("Player Everything: autoBlueprints.xml")
    blueprint = to_the_auto_lists()
    print("Player Everything: dlcBlueprints.xml")
    to_the_auto_lists(blueprint)
    print("Player Everything: dlcBlueprintsOverwrite.xml")
    to_the_auto_lists(blueprint)


def main_auto_enemy():
    print("Enemy Everything: autoBlueprints.xml")
    blueprint = to_the_auto_lists()
    print("Enemy Everything: dlcBlueprints.xml")
    to_the_auto_lists(blueprint)
    print("Enemy Everything: dlcBlueprintsOverwrite.xml")
    to_the_auto_lists(blueprint)


if __name__ == '__main__':
    print("***Rewritten Endless Loot Generator***\n"
          "NOTE: the source file to READ from must be proper XML, with one "
          "root tag, not how FTL's original blueprint files lack a root tag.\n"
          "XML malformed in other ways may make this break.\n")
    prefixes_or_autos = input("Enter 'p' for prefixes access, "
                              "'a' for autoBlueprints access, "
                              "or 'all' for accessing everything.\n")
    if prefixes_or_autos == 'p':
        # all constants false by default
        player_or_enemy = input("Enter 'p' for Player blueprints access, "
                                "'e' for Enemy blueprints access, "
                                "or 'b' for accessing both.\n")
        if player_or_enemy == 'p':
            main_prefix_player()
        elif player_or_enemy == 'e':
            main_prefix_enemy()
        elif player_or_enemy == 'b':
            main_prefix_player()
            main_prefix_enemy()
        else:
            raise ValueError("Must enter p, e, or b -- Restart.")

    elif prefixes_or_autos == 'a':
        player_or_enemy = input("Enter 'p' for Player autoBlueprints access, "
                                "'e' for Enemy autoBlueprints access, "
                                "or 'b' for accessing both.\n")
        if player_or_enemy == 'p':
            main_auto_player()
        elif player_or_enemy == 'e':
            main_auto_enemy()
        elif player_or_enemy == 'b':
            main_auto_player()
            main_auto_enemy()
        else:
            raise ValueError("Must enter either p, e, or b -- Restart.")
    elif prefixes_or_autos == 'all':
        main_prefix_player()
        main_prefix_enemy()
        main_auto_player()
        main_auto_enemy()
    else:
        raise ValueError("Must enter either p, a, or all -- Restart.")
