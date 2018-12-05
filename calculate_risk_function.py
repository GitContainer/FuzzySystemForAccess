import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def calculate_risk(new_time,new_location,kindofinfo):
    time = ctrl.Antecedent(np.arange(0, 11, 1), 'time')
    location = ctrl.Antecedent(np.arange(0, 11, 1), 'location')
    kindinfo = ctrl.Antecedent(np.arange(0, 11, 1), 'kindinfo')

    risk = ctrl.Consequent(np.arange(0, 11, 1), 'risk')

    time['poor'] = fuzz.trimf(time.universe, [0, 0, 5])
    time['medium'] = fuzz.trimf(time.universe, [0, 5, 10])
    time['good'] = fuzz.trimf(time.universe, [5, 10, 10])

    location['poor'] = fuzz.trimf(location.universe, [0, 0, 5])
    location['average'] = fuzz.trimf(location.universe, [0, 5, 10])
    location['good'] = fuzz.trimf(location.universe, [5, 10, 10])

    kindinfo['critical'] = fuzz.trimf(kindinfo.universe, [0, 0, 5])
    kindinfo['med'] = fuzz.trimf(kindinfo.universe, [0, 5, 10])
    kindinfo['basic'] = fuzz.trimf(kindinfo.universe, [5, 10, 10])

    risk['low'] = fuzz.trimf(risk.universe, [0, 0, 5])
    risk['medium'] = fuzz.trimf(risk.universe, [0, 5, 10])
    risk['high'] = fuzz.trimf(risk.universe, [5, 10, 10])

    rule1 = ctrl.Rule(kindinfo['basic'], risk['low'])
    rule2 = ctrl.Rule(kindinfo['med'], risk['medium'])
    rule3 = ctrl.Rule(kindinfo['critical'], risk['high'])
    rule4 = ctrl.Rule(location['poor'], risk['high'])
    rule5 = ctrl.Rule(location['average'], risk['medium'])
    rule6 = ctrl.Rule(location['good'], risk['low'])
    rule7 = ctrl.Rule(time['poor'], risk['high'])
    rule8 = ctrl.Rule(time['medium'], risk['medium'])
    rule9 = ctrl.Rule(time['good'], risk['low'])

    rule11 = ctrl.Rule(kindinfo['critical'] & location['poor'], risk['high'])
    rule12 = ctrl.Rule(kindinfo['critical'] & location['average'], risk['high'])
    rule13 = ctrl.Rule(kindinfo['critical'] & location['good'], risk['high'])
    rule14 = ctrl.Rule(kindinfo['critical'] & time['poor'], risk['high'])
    rule15 = ctrl.Rule(kindinfo['critical'] & time['medium'], risk['high'])
    rule16 = ctrl.Rule(kindinfo['critical'] & time['good'], risk['high'])

    rule17 = ctrl.Rule(kindinfo['critical'] | location['poor'], risk['high'])
    rule18 = ctrl.Rule(kindinfo['critical'] | location['average'], risk['high'])
    rule19 = ctrl.Rule(kindinfo['critical'] | location['good'], risk['high'])
    rule20 = ctrl.Rule(kindinfo['critical'] | time['poor'], risk['high'])
    rule21 = ctrl.Rule(kindinfo['critical'] | time['medium'], risk['high'])
    rule22 = ctrl.Rule(kindinfo['critical'] | time['good'], risk['high'])

    rule23 = ctrl.Rule(kindinfo['critical'] | location['poor'] | time['poor'], risk['high'])
    rule24 = ctrl.Rule(kindinfo['critical'] | location['average'] | time['medium'], risk['high'])
    rule25 = ctrl.Rule(kindinfo['critical'] | location['good'] | time['good'], risk['high'])
    rule26 = ctrl.Rule(kindinfo['critical'] | time['poor'] | location['poor'], risk['high'])
    rule27 = ctrl.Rule(kindinfo['critical'] | time['poor'] | location['average'], risk['high'])
    rule28 = ctrl.Rule(kindinfo['critical'] | time['poor'] | location['good'], risk['high'])

    rule29 = ctrl.Rule(kindinfo['critical'] & location['poor'] & time['poor'], risk['high'])
    rule30 = ctrl.Rule(kindinfo['critical'] & location['average'] & time['medium'], risk['high'])
    rule31 = ctrl.Rule(kindinfo['critical'] & location['good'] & time['good'], risk['high'])
    rule32 = ctrl.Rule(kindinfo['critical'] & time['poor'] & location['poor'], risk['high'])
    rule33 = ctrl.Rule(kindinfo['critical'] & time['poor'] & location['average'], risk['high'])
    rule34 = ctrl.Rule(kindinfo['critical'] & time['poor'] & location['good'], risk['high'])

    # next

    rule36 = ctrl.Rule(kindinfo['med'] & location['poor'], risk['medium'])
    rule37 = ctrl.Rule(kindinfo['med'] & location['average'], risk['medium'])
    rule38 = ctrl.Rule(kindinfo['med'] & location['good'], risk['medium'])
    rule39 = ctrl.Rule(kindinfo['med'] & time['poor'], risk['medium'])
    rule40 = ctrl.Rule(kindinfo['med'] & time['medium'], risk['medium'])
    rule41 = ctrl.Rule(kindinfo['med'] & time['good'], risk['medium'])

    rule42 = ctrl.Rule(kindinfo['med'] | location['poor'], risk['medium'])
    rule43 = ctrl.Rule(kindinfo['med'] | location['average'], risk['medium'])
    rule44 = ctrl.Rule(kindinfo['med'] | location['good'], risk['medium'])
    rule45 = ctrl.Rule(kindinfo['med'] | time['poor'], risk['medium'])
    rule46 = ctrl.Rule(kindinfo['med'] | time['medium'], risk['medium'])
    rule47 = ctrl.Rule(kindinfo['med'] | time['good'], risk['medium'])

    rule48 = ctrl.Rule(kindinfo['med'] | location['poor'] | time['poor'], risk['medium'])
    rule49 = ctrl.Rule(kindinfo['med'] | location['average'] | time['medium'], risk['medium'])
    rule50 = ctrl.Rule(kindinfo['med'] | location['good'] | time['good'], risk['medium'])
    rule51 = ctrl.Rule(kindinfo['med'] | time['poor'] | location['poor'], risk['medium'])
    rule52 = ctrl.Rule(kindinfo['med'] | time['poor'] | location['average'], risk['medium'])
    rule53 = ctrl.Rule(kindinfo['med'] | time['poor'] | location['good'], risk['medium'])

    rule54 = ctrl.Rule(kindinfo['med'] & location['poor'] & time['poor'], risk['medium'])
    rule55 = ctrl.Rule(kindinfo['med'] & location['average'] & time['medium'], risk['medium'])
    rule56 = ctrl.Rule(kindinfo['med'] & location['good'] & time['good'], risk['medium'])
    rule57 = ctrl.Rule(kindinfo['med'] & time['poor'] & location['poor'], risk['medium'])
    rule58 = ctrl.Rule(kindinfo['med'] & time['poor'] & location['average'], risk['medium'])
    rule59 = ctrl.Rule(kindinfo['med'] & time['poor'] & location['good'], risk['medium'])

    # next2

    rule60 = ctrl.Rule(kindinfo['basic'] & location['poor'], risk['low'])
    rule61 = ctrl.Rule(kindinfo['basic'] & location['average'], risk['low'])
    rule62 = ctrl.Rule(kindinfo['basic'] & location['good'], risk['low'])
    rule63 = ctrl.Rule(kindinfo['basic'] & time['poor'], risk['low'])
    rule64 = ctrl.Rule(kindinfo['basic'] & time['medium'], risk['low'])
    rule65 = ctrl.Rule(kindinfo['basic'] & time['good'], risk['low'])

    rule66 = ctrl.Rule(kindinfo['basic'] | location['poor'], risk['low'])
    rule67 = ctrl.Rule(kindinfo['basic'] | location['average'], risk['low'])
    rule68 = ctrl.Rule(kindinfo['basic'] | location['good'], risk['low'])
    rule69 = ctrl.Rule(kindinfo['basic'] | time['poor'], risk['low'])
    rule70 = ctrl.Rule(kindinfo['basic'] | time['medium'], risk['low'])
    rule71 = ctrl.Rule(kindinfo['basic'] | time['good'], risk['low'])

    rule72 = ctrl.Rule(kindinfo['basic'] | location['poor'] | time['poor'], risk['low'])
    rule73 = ctrl.Rule(kindinfo['basic'] | location['average'] | time['medium'], risk['low'])
    rule74 = ctrl.Rule(kindinfo['basic'] | location['good'] | time['good'], risk['low'])
    rule75 = ctrl.Rule(kindinfo['basic'] | time['poor'] | location['poor'], risk['low'])
    rule76 = ctrl.Rule(kindinfo['basic'] | time['poor'] | location['average'], risk['low'])
    rule77 = ctrl.Rule(kindinfo['basic'] | time['poor'] | location['good'], risk['low'])

    rule78 = ctrl.Rule(kindinfo['basic'] & location['poor'] & time['poor'], risk['low'])
    rule79 = ctrl.Rule(kindinfo['basic'] & location['average'] & time['medium'], risk['low'])
    rule80 = ctrl.Rule(kindinfo['basic'] & location['good'] & time['good'], risk['low'])
    rule81 = ctrl.Rule(kindinfo['basic'] & time['poor'] & location['poor'], risk['low'])
    rule82 = ctrl.Rule(kindinfo['basic'] & time['poor'] & location['average'], risk['low'])
    rule83 = ctrl.Rule(kindinfo['basic'] & time['poor'] & location['good'], risk['low'])

    # next3

    rule84 = ctrl.Rule(kindinfo['critical'] | location['poor'] & time['poor'], risk['high'])
    rule85 = ctrl.Rule(kindinfo['critical'] | location['average'] & time['medium'], risk['high'])
    rule86 = ctrl.Rule(kindinfo['critical'] | location['good'] & time['good'], risk['high'])
    rule87 = ctrl.Rule(kindinfo['critical'] | time['poor'] & location['poor'], risk['high'])
    rule88 = ctrl.Rule(kindinfo['critical'] | time['poor'] & location['average'], risk['high'])
    rule89 = ctrl.Rule(kindinfo['critical'] | time['poor'] & location['good'], risk['high'])

    rule90 = ctrl.Rule(kindinfo['critical'] & location['poor'] | time['poor'], risk['high'])
    rule91 = ctrl.Rule(kindinfo['critical'] & location['average'] | time['medium'], risk['high'])
    rule92 = ctrl.Rule(kindinfo['critical'] & location['good'] | time['good'], risk['high'])
    rule93 = ctrl.Rule(kindinfo['critical'] & time['poor'] | location['poor'], risk['high'])
    rule94 = ctrl.Rule(kindinfo['critical'] & time['poor'] | location['average'], risk['high'])
    rule95 = ctrl.Rule(kindinfo['critical'] & time['poor'] | location['good'], risk['high'])

    rule96 = ctrl.Rule(kindinfo['med'] | location['poor'] & time['poor'], risk['medium'])
    rule97 = ctrl.Rule(kindinfo['med'] | location['average'] & time['medium'], risk['medium'])
    rule98 = ctrl.Rule(kindinfo['med'] | location['good'] & time['good'], risk['medium'])
    rule99 = ctrl.Rule(kindinfo['med'] | time['poor'] & location['poor'], risk['medium'])
    rule100 = ctrl.Rule(kindinfo['med'] | time['poor'] & location['average'], risk['medium'])
    rule110 = ctrl.Rule(kindinfo['med'] | time['poor'] & location['good'], risk['medium'])

    rule111 = ctrl.Rule(kindinfo['med'] & location['poor'] | time['poor'], risk['medium'])
    rule112 = ctrl.Rule(kindinfo['med'] & location['average'] | time['medium'], risk['medium'])
    rule113 = ctrl.Rule(kindinfo['med'] & location['good'] | time['good'], risk['medium'])
    rule114 = ctrl.Rule(kindinfo['med'] & time['poor'] | location['poor'], risk['medium'])
    rule115 = ctrl.Rule(kindinfo['med'] & time['poor'] | location['average'], risk['medium'])
    rule116 = ctrl.Rule(kindinfo['med'] & time['poor'] | location['good'], risk['medium'])

    rule117 = ctrl.Rule(kindinfo['basic'] | location['poor'] & time['poor'], risk['low'])
    rule118 = ctrl.Rule(kindinfo['basic'] | location['average'] & time['medium'], risk['low'])
    rule119 = ctrl.Rule(kindinfo['basic'] | location['good'] & time['good'], risk['low'])
    rule120 = ctrl.Rule(kindinfo['basic'] | time['poor'] & location['poor'], risk['low'])
    rule121 = ctrl.Rule(kindinfo['basic'] | time['poor'] & location['average'], risk['low'])
    rule122 = ctrl.Rule(kindinfo['basic'] | time['poor'] & location['good'], risk['low'])

    rule123 = ctrl.Rule(kindinfo['basic'] & location['poor'] | time['poor'], risk['low'])
    rule124 = ctrl.Rule(kindinfo['basic'] & location['average'] | time['medium'], risk['low'])
    rule125 = ctrl.Rule(kindinfo['basic'] & location['good'] | time['good'], risk['low'])
    rule126 = ctrl.Rule(kindinfo['basic'] & time['poor'] | location['poor'], risk['low'])
    rule127 = ctrl.Rule(kindinfo['basic'] & time['poor'] | location['average'], risk['low'])
    rule128 = ctrl.Rule(kindinfo['basic'] & time['poor'] | location['good'], risk['low'])

    # FOR AND
    # location['poor'] & time['good'] & kindinfo['basic'], risk['low'])
    # location['poor'] & time['good'] & kindinfo['medium'], risk['low'])
    # location['poor'] & time['good'] & kindinfo['critical'], risk['low'])

    # location['average'] & time['good'] & kindinfo['basic'], risk['low'])
    # location['average'] & time['good'] & kindinfo['medium'], risk['medium'])
    # location['average'] & time['good'] & kindinfo['critical'], risk['low'])

    # location['good'] & time['good'] & kindinfo['basic'], risk['low'])
    # location['good'] & time['good'] & kindinfo['medium'], risk['low'])
    # location['good'] & time['good'] & kindinfo['critical'], risk['low'])

    # location['poor'] & time['poor'] & kindinfo['basic'], risk['low'])
    # location['poor'] & time['poor'] & kindinfo['medium'], risk['low'])
    # location['poor'] & time['poor'] & kindinfo['critical'], risk['high'])

    # location['poor'] & time['medium'] & kindinfo['basic'], risk['low'])
    # location['poor'] & time['medium'] & kindinfo['medium'], risk['low'])
    # location['poor'] & time['medium'] & kindinfo['critical'], risk['low'])

    # FOR OR

    # location['poor'] | time['good'] | kindinfo['basic'], risk['low'])
    # location['poor'] | time['good'] | kindinfo['medium'], risk['low'])
    # location['poor'] | time['good'] | kindinfo['critical'], risk['low'])

    # location['average'] | time['good'] | kindinfo['basic'], risk['low'])
    # location['average'] | time['good'] | kindinfo['medium'], risk['low'])
    # location['average'] | time['good'] | kindinfo['critical'], risk['low'])

    # location['good'] | time['good'] | kindinfo['basic'], risk['low'])
    # location['good'] | time['good'] | kindinfo['medium'], risk['low'])
    # location['good'] | time['good'] | kindinfo['critical'], risk['low'])

    # location['poor'] | time['poor'] | kindinfo['basic'], risk['low'])
    # location['poor'] | time['poor'] | kindinfo['medium'], risk['low'])
    # location['poor'] | time['poor'] | kindinfo['critical'], risk['low'])

    # location['poor'] | time['medium'] | kindinfo['basic'], risk['low'])
    # location['poor'] | time['medium'] | kindinfo['medium'], risk['low'])
    # location['poor'] | time['medium'] | kindinfo['critical'], risk['low'])

    # location['poor'] | time['poor'], risk['low']
    # location['poor'] | time['medium'], risk['low']
    # location['poor'] | time['good'], risk['low']
    # location['average'] | time['poor'], risk['low']
    # location['average'] | time['medium'], risk['low']
    # location['average'] | time['good'], risk['low']
    # location['good'] | time['poor'], risk['low']
    # location['good'] | time['medium'], risk['low']
    # location['good'] | time['good'], risk['low']

    # kindinfo['basic'] | time['poor'], risk['low']
    # kindinfo['basic'] | time['medium'], risk['low']
    # kindinfo['basic'] | time['good'], risk['low']
    # kindinfo['med'] | time['poor'], risk['low']
    # kindinfo['med'] | time['medium'], risk['low']
    # kindinfo['med'] | time['good'], risk['low']
    # kindinfo['critical'] | time['poor'], risk['low']
    # kindinfo['critical'] | time['medium'], risk['low']
    # kindinfo['critical'] | time['good'], risk['low']
    #
    # location['poor'] | kindinfo['basic'], risk['low']
    # location['poor'] | kindinfo['med'], risk['low']
    # location['poor'] | kindinfo['critical'], risk['low']
    # location['average'] | kindinfo['basic'], risk['low']
    # location['average'] | kindinfo['med'], risk['low']
    # location['average'] | kindinfo['critical'], risk['low']
    # location['good'] | kindinfo['basic'], risk['low']
    # location['good'] | kindinfo['med'], risk['low']
    # location['good'] | kindinfo['critical'], risk['low']
    #

    # location['poor'] & time['poor'], risk['low']
    # location['poor'] & time['medium'], risk['low']
    # location['poor'] & time['good'], risk['low']
    # location['average'] & time['poor'], risk['low']
    # location['average'] & time['medium'], risk['low']
    # location['average'] & time['good'], risk['low']
    # location['good'] & time['poor'], risk['low']
    # location['good'] & time['medium'], risk['low']
    # location['good'] & time['good'], risk['low']

    # kindinfo['basic'] & time['poor'], risk['low']
    # kindinfo['basic'] & time['medium'], risk['low']
    # kindinfo['basic'] & time['good'], risk['low']
    # kindinfo['med'] & time['poor'], risk['low']
    # kindinfo['med'] & time['medium'], risk['low']
    # kindinfo['med'] & time['good'], risk['low']
    # kindinfo['critical'] & time['poor'], risk['low']
    # kindinfo['critical'] & time['medium'], risk['low']
    # kindinfo['critical'] & time['good'], risk['low']

    # location['poor'] & kindinfo['basic'], risk['low']
    # location['poor'] & kindinfo['med'], risk['low']
    # location['poor'] & kindinfo['critical'], risk['low']
    # location['average'] & kindinfo['basic'], risk['low']
    # location['average'] & kindinfo['med'], risk['low']
    # location['average'] & kindinfo['critical'], risk['low']
    # location['good'] & kindinfo['basic'], risk['low']
    # location['good'] & kindinfo['med'], risk['low']
    # location['good'] & kindinfo['critical'], risk['low']



    # risk_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule31,rule32,rule33,rule34,rule36,rule37,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64,rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74,rule75,rule76,rule77,rule78,rule79,rule80,rule81,rule82,rule83,rule84,rule85,rule86,rule87,rule88,rule89,rule90,rule91,rule92,rule93,rule94,rule95,rule96,rule97,rule98,rule99,rule100,rule110,rule111,rule112,rule113,rule114,rule115,rule116,rule117,rule118,rule119,rule120,rule121,rule122,rule123,rule124,rule125,rule126,rule127,rule128])
    risk_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    calculated_risk = ctrl.ControlSystemSimulation(risk_ctrl)

    calculated_risk.input['time'] = new_time
    calculated_risk.input['location'] = new_location
    calculated_risk.input['kindinfo'] = kindofinfo

    # Crunch the numbers
    calculated_risk.compute()

    # print(calculated_risk.output['risk'])

    return calculated_risk.output['risk']
    # risk.view(sim=calculated_risk)
