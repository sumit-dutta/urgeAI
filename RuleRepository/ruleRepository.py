####################################################Rules###################################

rules = {"accentuate":
            {
                "arms" : ["Sleeves","Neck"],
                "bust" : ["Neck","Type"],
                "legs" : ["Type", "Fit", "Length"],
                "waist" : ["Type"]

            }
        }



####################################################Scores######################################


scores = {
          "arms":{},
          "bust":{},
          "legs": {},
          "waist": {}
          }



##############arms#####################
scores["arms"] = dict.fromkeys(
                    ['tops','tees','dresses','kurtas','shirts'],{
                    'half sleeves': .4,
                    'sleeveless': 1,
                    'cap sleeves': .8,
                    'puff sleeves': .8,
                    'flutter sleeves': .6,
                    '3/4 sleeves': .2,
                    'halter neck': .6,
                    'tube': .8
                    } )


###############bust################

scores["bust"] = dict.fromkeys(
        ['tops','tees','dresses','shirts'],{
            'v neck': .8,
            'spaghetti': 1,
            'sweetheart neck': 1,
            'tube': .8,
            'asymmetric': 1,
            'halter neck': .8,
            'boat neck': .4,
            'henley': .6,
            'square collar': .6,
            'polo': .6,

        })


scores["bust"].update(dict.fromkeys(
        ['kurtas'],{
            'sweetheart neck': .8,
            'v neck': 1
        }))


####################legs#################

scores["legs"] =  dict.fromkeys(
        ['bottomwear'],{
            'jeggings': .8,
            'shorts': .8
        })

scores["legs"].update( dict.fromkeys(
        ['jeans'],{
            'skinny fit': 1,
            'slim fit': 1
        }))

scores["legs"].update( dict.fromkeys(
        ['skirts'],{
            'pencil': 1,
            'mini': 1
        }))


############waist################

scores["waist"] = dict.fromkeys(
        ['dresses', 'kurtas'],{
            'peplums': 1,
            'bodycon': 1,
            'empire waist': .8,
            'wrap': .6,
            'maxi': .6,
            'fit and flare': 1,
            'bandage': .8,
            'skater': .4,
            'anarkali': 1
        })

