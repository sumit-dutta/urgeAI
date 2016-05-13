import RuleRepository.ruleRepository as rp


def computeScore(record, rules, scores, preference, bodyPart):
    score = 0
    for attr in rules[preference][bodyPart]:
        print attr
        if attr in record.keys() and record["Type"] in scores[bodyPart].keys() and record[attr] in scores[bodyPart][record["Type"]].keys():
            score = score + scores[bodyPart][record["Type"]][record[attr]]
            print attr, score

    return score


def computeAccentuateScores(record, userPrefs, rules = rp.rules, scores = rp.scores):

    score  = 0
    if userPrefs["accentuate"]["arms"]:
         score = score + computeScore(record, rules, scores, "accentuate", "arms")
    if userPrefs["accentuate"]["bust"]:
         score = score + computeScore(record, rules, scores, "accentuate", "bust")
    if userPrefs["accentuate"]["legs"]:
         score = score + computeScore(record, rules, scores, "accentuate", "legs")
    if userPrefs["accentuate"]["waist"]:
         score = score + computeScore(record, rules, scores, "accentuate", "waist")

    return score





