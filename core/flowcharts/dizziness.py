# Instantiate a multiple choice question
from question import MultipleChoice, QuestionBool, QuestionFloat

# Import common assessment forms
from assessments.fever import assessFever
from assessments.constitutionalSymptoms import assessConstitutionalSymptoms
from assessments.pain import assessPain


# Questions
ongoingDizziness = QuestionBool(prompt='Upplever du yrsel just nu?', lang='sv')

suddenDizziness = QuestionBool(prompt='Kom yrseln plötsligt?', lang='sv')

qSevereDizziness = MultipleChoice(
    prompt='Ibland kan yrsel vara så kraftig att man inte klarar av några vardagliga sysslor.\nVad av följande stämmer in på dig?', 
    choices=[
        'Svårt att gå utan att hålla sig i väggarna pga yrsel', 
        'Kan ej äta pga yrsel', 
        'Kan ej dricka pga yrsel'
    ], 
    none_prompt='Inget av ovanstående', none_option=True, 
    variant='multi-select', lang='sv')

potentiallySeriousDizzinessSymptoms = MultipleChoice(
    prompt='Upplever du eller har du upplevt något av följande symptom tillsammans med yrseln?',
    choices=[
        'Bröstsmärta',
        'Oregelbunden puls',
        'Öronvärk',
        'Huvudvärk',
    ],
    none_prompt='Inget av ovanstående',
    lang='sv',
    variant = 'multi-select')

pSD = potentiallySeriousDizzinessSymptoms

potentiallyModeratelySeriouesDizzinessSymptoms = MultipleChoice(
    prompt='Vilka av följande symptom har du besvärats av under perioden du har haft yrsel?',
    choices=[
        'Kraftlöshet',
        'Balanssvårigheter',
        'Koordinationssvårigheter',
        'Talsvårigheter',
        'Sväljsvårigheter',
    ],
    none_prompt='Inget av ovanstående',
    lang='sv',
    variant='multi-select')

pMSD = potentiallyModeratelySeriouesDizzinessSymptoms

certainMovementTriggers = QuestionBool(
    prompt='Kommer yrseln endast vid vissa rörelser?',
    lang='sv')

otherDizzinessFeatures = MultipleChoice(
    prompt='Stämmer något av följande in på dig?',
    choices=[
        'Yrseln har kommit och gått under flera dagar',
        'Yrseln har pågått i flera dagar',
        'Gradvis försämrad hörsel under flera dagar',
    ],
    none_prompt='Inget av ovanstående',
    lang='sv',
    variant='multi-select')

oDF = otherDizzinessFeatures

benignDizzinessSymptoms = MultipleChoice(
    prompt='Stämmer något av följande in på dig',
    choices=[
        'Yrseln har endast kommit vid enstaka tillfällen',
        'Yrseln kommer endast i samband med snabb uppresning',
        'Yrseln uppstod efter en gungig sjöfärd',
    ],
    lang='sv',
    none_prompt='Inget av ovanstående',
    variant='multi-select')

bDS = benignDizzinessSymptoms

potentiallyModeratelySeriouesDizzinessSymptomsNotOngoing = QuestionBool(
    prompt='Har alla symptom gått över?',
    lang='sv')

pMSD_notOngoing = potentiallyModeratelySeriouesDizzinessSymptomsNotOngoing

lastEpisodeThisWeek = QuestionBool(
    prompt='Har du besvärats av yrsel under den senaste veckan?',
    lang='sv')

def odf_subtree(lang):
    oDF.ask(lang)
    if any(a.idx in [0] for a in oDF.answer):
        bDS.ask(lang)
        if any(a.idx in [0] for a in bDS.answer):
            return f"RGS Vardag närmaste dygnet"
        else:
            return f"RGS Avvakta"
    else:
        return f"RGS Vardag närmaste dygnet"

def qSevereDizziness_subtree(lang):
    qSevereDizziness.ask(lang)
    if any(a.idx == 0 for a in qSevereDizziness.answer):
        aConstitutionalSymptoms = assessConstitutionalSymptoms(lang)
        if aConstitutionalSymptoms.value <= 1:
            pSD.ask(lang)
            if any(a.idx in [1,2] for a in pSD.answer):
                return f"RGS Omgående: Symptom från bröstet"
            elif any(a.idx in [3] for a in pSD.answer):
                return f"RGS Omgående: Öronbesvär och yrsel",
            elif any(a.idx in [4] for a in pSD.answer) and suddenDizziness.answer == True:
                return f"RGS Omgående: Plötslig yrsel och huvudvärk",
            else:
                pMSD.ask(lang)
                if any(a.idx in [0] for a in pMSD.answer):
                    certainMovementTriggers.ask(lang)
                    if certainMovementTriggers.answer == True:
                        return f"RGS Närmaste dygnet: Lägesberoende yrsel"
                    else:
                        return odf_subtree(lang)
                else:
                    pMSD_notOngoing.ask(lang)
                    if pMSD_notOngoing.answer == True:
                        return f"RGS Omgående: Bortfallssymptom, balansproblem eller förvirring"
                    else:
                        return f"RGS Skyndsamt: Bortfallssymptom, balansproblem eller förvirring som gått över"
        else:
            return f"RGS Omgående: Yrsel och allmänpåverkan"
    else:
        return f"RGS Omgående: Kraftig yrsel"
    
def assessDizziness(lang='sv'):
    
    ongoingDizziness.ask(lang)
    if ongoingDizziness.answer == True:
        suddenDizziness.ask(lang)
        return qSevereDizziness_subtree(lang)
    
    else:
        lastEpisodeThisWeek.ask(lang)
        if lastEpisodeThisWeek.answer == True:
            return qSevereDizziness_subtree(lang)
        elif lastEpisodeThisWeek.answer == False:
            certainMovementTriggers.ask(lang)
            if certainMovementTriggers.answer == True:
                return f"RGS Närmaste dygnet: Lägesberoende yrsel"
            else:
                return odf_subtree(lang)