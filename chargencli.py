"""
"Fair" Character Generator, CLI edition

Representation of minorities in the media (or lack thereof)
is a real and serious problem.
This site is a tool for writers who would rather be a part of the solution than the problem.

usage:
    chargencli -h | --help | --version
    chargencli [--countrymode=<countrymode>]

options:
  -h --help              Show this screen.
  --version              Show the version.
  --countrymode=<countrymode> either US or worldwide

"""

import random
from docopt import docopt
from os import system

arguments = docopt(__doc__, options_first=True, version='1.0.0')


def get_worldwide_statistics():
    traits = [
        ("Sex", generate_from_distribution(
            [("Female", 100),
             ("Male", 101)])),
        ("Country", generate_from_distribution(
            [("China", 1374390000),
             ("India", 1283230000),
             ("United States", 322673000),
             ("Indonesia", 258705000),
             ("Brazil", 205506000),
             ("Pakistan", 192540254),
             ("Nigeria", 186988000),
             ("Bangladesh", 159736000),
             ("Russia", 146504980),
             ("Japan", 126880000),
             ("Mexico", 122273500),
             ("Philippines", 102677200),
             ("Ethiopia", 92206005),
             ("Vietnam", 91700000),
             ("Egypt", 90251100),
             ("Democratic Republic of the Congo", 85026000),
             ("Germany", 81292400),
             ("Iran", 78947900),
             ("Turkey", 77695904),
             ("France", 67286000),
             ("United Kingdom", 65572409),
             ("Thailand", 65226008),
             ("Italy", 60685487),
             ("Tanzania", 55155000),
             ("South Africa", 54956900),
             ("Myanmar", 54363000),
             ("South Korea", 51529338),
             ("Colombia", 48488900),
             ("Kenya", 47251000),
             ("Spain", 46423064),
             ("Argentina", 43590400),
             ("Ukraine", 42789472),
             ("Algeria", 40400000),
             ("Sudan", 39598700),
             ("Poland", 38484000),
             ("Iraq", 36575000),
             ("Canada", 35985751),
             ("Uganda", 34856813),
             ("Morocco", 33337529),
             ("Saudi Arabia", 32248200),
             ("Peru", 31488700),
             ("Venezuela", 31028700),
             ("Uzbekistan", 31022500),
             ("Malaysia", 30832500),
             ("Nepal", 28431500),
             ("Afghanistan", 27101365),
             ("Ghana", 27043093),
             ("Mozambique", 26423700),
             ("Yemen", 25956000),
             ("North Korea", 25281000),
             ("Angola", 24383301),
             ("Australia", 23973700),
             ("Cameroon", 23924000),
             ("Syria", 23580189),
             ("Taiwan", 23476640),
             ("Ivory Coast", 22671331),
             ("Madagascar", 22434363),
             ("Sri Lanka", 20966000),
             ("Niger", 20715000),
             ("Romania", 19861000),
             ("Burkina Faso", 18450494),
             ("Chile", 18191900),
             ("Mali", 18135000),
             ("Kazakhstan", 17651300),
             ("Netherlands", 16984000),
             ("Malawi", 16832910),
             ("Ecuador", 16278844),
             ("Guatemala", 16176133),
             ("Zimbabwe", 15967000),
             ("Zambia", 15933883),
             ("Cambodia", 15626444),
             ("Chad", 14497000),
             ("Senegal", 14354690),
             ("Guinea", 12947000),
             ("South Sudan", 11892934),
             ("Rwanda", 11553188),
             ("Belgium", 11291746),
             ("Cuba", 11238317),
             ("Somalia", 11079000),
             ("Haiti", 11078033),
             ("Bolivia", 10985059),
             ("Tunisia", 10982754),
             ("Greece", 10846979),
             ("Benin", 10653654),
             ("Czech Republic", 10541466),
             ("Portugal", 10374822),
             ("Burundi", 10114505),
             ("Dominican Republic", 10075045),
             ("Hungary", 9849000),
             ("Sweden", 9845155),
             ("Azerbaijan", 9687300),
             ("Belarus", 9494200),
             ("United Arab Emirates", 9267000),
             ("Austria", 8662588),
             ("Honduras", 8576532),
             ("Israel", 8462000),
             ("Tajikistan", 8352000),
             ("Switzerland", 8306200),
             ("Papua New Guinea", 8083700),
             ("Hong Kong (China)", 7298600),
             ("Bulgaria", 7202198),
             ("Togo", 7143000),
             ("Serbia", 7114393),
             ("Paraguay", 6854536),
             ("Jordan", 6675000),
             ("Sierra Leone", 6592000),
             ("El Salvador", 6520675),
             ("Laos", 6472400),
             ("Libya", 6330000),
             ("Nicaragua", 6198154),
             ("Kyrgyzstan", 5975000),
             ("Denmark", 5699220),
             ("Singapore", 5535000),
             ("Finland", 5497302),
             ("Slovakia", 5424058),
             ("Eritrea", 5352000),
             ("Norway", 5214890),
             ("Central African Republic", 4998000),
             ("Costa Rica", 4832234),
             ("Turkmenistan", 4751120),
             ("Republic of the Congo", 4741000),
             ("Palestine", 4682467),
             ("New Zealand", 4653440),
             ("Ireland", 4635400),
             ("Liberia", 4615000),
             ("Oman", 4337151),
             ("Croatia", 4225316),
             ("Kuwait", 4183658),
             ("Lebanon", 4168000),
             ("Puntland (Somalia)", 3900000),
             ("Bosnia and Herzegovina", 3791622),
             ("Panama", 3764166),
             ("Georgia", 3729500),
             ("Mauritania", 3718678),
             ("Moldova", 3555200),
             ("Somaliland", 3500000),
             ("Uruguay", 3480222),
             ("Puerto Rico (U.S.)", 3474182),
             ("Mongolia", 3063000),
             ("Armenia", 3004000),
             ("Albania", 2893005),
             ("Lithuania", 2890679),
             ("Jamaica", 2723246),
             ("Qatar", 2421000),
             ("Namibia", 2324400),
             ("Botswana", 2141206),
             ("Slovenia", 2069366),
             ("Macedonia", 2069172),
             ("Latvia", 1972100),
             ("Lesotho", 1894194),
             ("The Gambia", 1882450),
             ("Kosovo", 1836978),
             ("Gabon", 1802278),
             ("Guinea-Bissau", 1547777),
             ("Bahrain", 1404900),
             ("Trinidad and Tobago", 1349667),
             ("Estonia", 1313271),
             ("Mauritius", 1262879),
             ("Equatorial Guinea", 1222442),
             ("East Timor", 1167242),
             ("Swaziland", 1132657),
             ("Djibouti", 900000),
             ("Fiji", 867000),
             ("Cyprus", 847000),
             ("Reunion (France)", 844994),
             ("Comoros", 806153),
             ("Bhutan", 769430),
             ("Guyana", 746900),
             ("Macau (China)", 643100),
             ("Solomon Islands", 642000),
             ("Montenegro", 621810),
             ("Luxembourg", 562958),
             ("Suriname", 534189),
             ("Cape Verde", 531239),
             ("Western Sahara", 510713),
             ("Transnistria", 505153),
             ("Malta", 445426),
             ("Brunei", 411900),
             ("Guadeloupe (France)", 403750),
             ("The Bahamas", 393000),
             ("Martinique (France)", 381326),
             ("Belize", 368310),
             ("Maldives", 341256),
             ("Iceland", 331310),
             ("Northern Cyprus", 294396),
             ("Barbados", 285000),
             ("Vanuatu", 277500),
             ("New Caledonia (France)", 268767),
             ("French Polynesia (France)", 268270),
             ("Abkhazia", 240705),
             ("French Guiana (France)", 239648),
             ("Mayotte (France)", 212645),
             ("Samoa", 187820),
             ("Sao Tome and Principe", 187356),
             ("Saint Lucia", 186000),
             ("Guam (U.S.)", 184200),
             ("Curacao (Netherlands)", 154843),
             ("Nagorno-Karabakh Republic", 148900),
             ("Kiribati", 113400),
             ("Saint Vincent and the Grenadines", 109991),
             ("Aruba (Netherlands)", 107394),
             ("United States Virgin Islands (U.S.)", 106000),
             ("Grenada", 103328),
             ("Tonga", 103252),
             ("Federated States of Micronesia", 102800),
             ("Jersey (UK)", 100800),
             ("Seychelles", 91400),
             ("Antigua and Barbuda", 86295),
             ("Isle of Man (UK)", 84497),
             ("Andorra", 76949),
             ("Dominica", 71293),
             ("Guernsey (UK)", 65150),
             ("Bermuda (UK)", 61954),
             ("Cayman Islands (UK)", 58238),
             ("American Samoa (U.S.)", 57100),
             ("Northern Mariana Islands (U.S.)", 56940),
             ("Greenland (Denmark)", 56114),
             ("Marshall Islands", 54880),
             ("South Ossetia", 51547),
             ("Faroe Islands (Denmark)", 49179),
             ("Sint Maarten (Netherlands)", 38247),
             ("Saint Kitts and Nevis", 46204),
             ("Monaco", 37800),
             ("Liechtenstein", 37370),
             ("Saint-Martin (France)", 36522),
             ("Gibraltar (UK)", 33140),
             ("San Marino", 32968),
             ("Turks and Caicos Islands (UK)", 31458),
             ("Aland Islands (Finland)", 28875),
             ("British Virgin Islands (UK)", 28514),
             ("Cook Islands", 19100),
             ("Palau", 17950),
             ("Bonaire (Netherlands)", 17408),
             ("Anguilla (UK)", 13452),
             ("Wallis and Futuna (France)", 11750),
             ("Tuvalu", 10640),
             ("Nauru", 10084),
             ("Saint Barthelemy (France)", 9269),
             ("Saint Pierre and Miquelon (France)", 6069),
             ("Montserrat (UK)", 4922),
             ("Saint Helena Ascension and Tristan da Cunha (UK)", 4255),
             ("Sint Eustatius (Netherlands)", 4020),
             ("Falkland Islands (UK)", 2563),
             ("Svalbard and Jan Mayen (Norway)", 2562),
             ("Norfolk Island (Australia)", 2302),
             ("Christmas Island (Australia)", 2072),
             ("Saba (Netherlands)", 1991),
             ("Niue", 1470),
             ("Tokelau (NZ)", 1411),
             ("Vatican City", 839),
             ("Cocos (Keeling) Islands (Australia)", 550),
             ("French Southern and Antarctic Lands (France)", 140),
             ("Pitcairn Islands (UK)", 56)])),
        ("Sexual Orientation", generate_from_distribution(
            [("Bisexual", 18),
             ("Homosexual", 17),
             ("Asexual", 21),
             ("Heterosexual", 944)])),
        ("Gender Identity", generate_from_distribution(
            [("Transgender", 3),
             ("Cisgender", 997)])),
        ("Vision", generate_from_distribution(
            [("Functional", 960),
             ("Impaired", 35),
             ("Blind", 5)])),
        ("Hearing", generate_from_distribution(
            [("Functional", 95),
             ("Deaf", 5)])),
        ("Handedness", generate_from_distribution(
            [("Right-handed", 89),
             ("Left-handed", 10),
             ("Ambidextrous", 1)]))]
    return traits


def get_usa_statistics():
    traits = [
        ("Sex", generate_from_distribution(
            [("Female", 100),
             ("Male", 97)])),
        ("Race", generate_from_distribution(
            [("White", 637),
             ("Black", 122),
             ("Asian", 47),
             ("Hispanic/Latino", 164),
             ("Native American", 7),
             ("Native Hawaiian", 2),
             ("Mixed race", 19),
             ("Other (Too small to categorize)", 2)])),
        ("Sexual Orientation", generate_from_distribution(
            [("Bisexual", 18),
             ("Homosexual", 17),
             ("Asexual", 21),
             ("Heterosexual", 944)])),
        ("Gender Identity", generate_from_distribution(
            [("Transgender", 3),
             ("Cisgender", 997)])),
        ("Body Size", generate_from_distribution(
            [("Underweight", 18),
             ("Healthy weight", 299),
             ("Overweight", 333),
             ("Obese", 287),
             ("Severely obese", 63)])),
        ("Vision", generate_from_distribution(
            [("Functional", 979),
             ("Impaired", 21)])),
        ("Hearing", generate_from_distribution(
            [("Functional", 98),
             ("Deaf", 2)])),
        ("Handedness", generate_from_distribution(
            [("Right-handed", 89),
             ("Left-handed", 10),
             ("Ambidextrous", 1)]))]
    return traits


def generate_from_distribution(distribution):
    total_sum = sum(value for trait, value in distribution)
    x = random.randrange(total_sum)
    index = 0
    partial_sum = distribution[0][1]
    while partial_sum <= x:
        index += 1
        partial_sum += distribution[index][1]
    return distribution[index][0]


if __name__ == '__main__':

    if arguments["--countrymode"] is None:
        region = "worldwide"
    else:
        region = arguments["--countrymode"].lower()

    if region == 'worldwide':
        traits = get_worldwide_statistics()
    else:  # region == 'usa':
        traits = get_usa_statistics()
    print(f"For the region of: {region.upper()}")
    for attrib, value in traits:
        print(f"{attrib} -> {value}")
    os.system('pause')
