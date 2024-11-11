from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):

    for code, name in COUNTRIES.items():
            if name == country_name:
                return code
            
            elif country_name == 'Korea, Rep.':
                return 'kp'            
            elif country_name == 'Türkiye':
                return 'tr'
            elif country_name == 'Iran, Islamic Rep.':
                return 'ir'
            elif country_name == 'Egypt, Arab Rep.':
                return 'eg'
            elif country_name == 'Hong Kong SAR, China':
                return 'hk'
            elif country_name == 'Qatar':
                return 'qa'
            elif country_name == 'Slovak Republic':
                return 'sk'
            elif country_name == 'Tanzania':
                return 'tz'
            elif country_name == 'Côte d\'Ivoire':
                return 'ci'
            elif country_name == 'Congo, Dem. Rep.':
                return 'cd'
            elif country_name == 'Libya':
                return 'ly'
            elif country_name == 'Macao SAR, China':
                return 'mo'
            elif country_name == 'Bolivia':
                return 'bo'
            elif country_name == 'Trinidad and Tobago':
                return 'tt'
            elif country_name == 'West Bank and Gaza':
                return 'ps'
            elif country_name == 'Moldova':
                return 'md'
            elif country_name == 'Lao PDR':
                return 'la'
            elif country_name == 'Congo, Rep.':
                return 'cg'
            elif country_name == 'North Macedonia':
                return 'mk'
            elif country_name == 'Bahamas, The':
                return 'bs'
            elif country_name == 'Kyrgyz Republic':
                return 'kg'
            elif country_name == 'Channel Islands':
                return 'je'
            elif country_name == 'Kosovo':
                return 'xk'
            elif country_name == 'New Caledonia':
                return 'nc'
            elif country_name == 'Isle of Man':
                return 'im'
            elif country_name == 'Bermuda':
                return 'bm'
            elif country_name == 'Cayman Islands':
                return 'ky'
            elif country_name == 'Barbados':
                return 'bb'
            elif country_name == 'French Polynesia':
                return 'pf'
            elif country_name == 'Fiji':
                return 'fj'
            elif country_name == 'Eswatini':
                return 'sz'
            elif country_name == 'Virgin Islands (U.S.)':
                return 'vi'
            elif country_name == 'Faroe Islands':
                return 'fo'
            elif country_name == 'Aruba':
                return 'aw'
            elif country_name == 'Curaçao':
                return 'cw'
            elif country_name == 'Cabo Verde':
                return 'cv'
            elif country_name == 'St. Lucia':
                return 'lc'
            elif country_name == 'Gambia, The':
                return 'gm'
            elif country_name == 'Antigua and Barbuda':
                return 'ag'
            elif country_name == 'Solomon Islands':
                return 'sb'
            elif country_name == 'Sint Maarten (Dutch part)':
                return 'sx'
            elif country_name == 'Turks and Caicos Islands':
                return 'tc'
            elif country_name == 'Comoros':
                return 'km'
            elif country_name == 'Grenada':
                return 'gd'
            elif country_name == 'Vanuatu':
                return 'vu'
            elif country_name == 'St. Kitts and Nevis':
                return 'kn'
            elif country_name == 'St. Vincent and the Grenadines':
                return 'vc'
            elif country_name == 'Samoa':
                return 'ws'
            elif country_name == 'American Samoa':
                return 'as'
            elif country_name == 'Dominica':
                return 'dm'
            elif country_name == 'St. Martin (French part)':
                return 'mf'
            elif country_name == 'São Tomé and Principe':
                return 'st'
            elif country_name == 'Tonga':
                return 'to'
            elif country_name == 'Micronesia, Fed. Sts.':
                return 'fm'
            elif country_name == 'Marshall Islands':
                return 'mh'
            elif country_name == 'Kiribati':
                return 'ki'
            elif country_name == 'Palau':
                return 'pw'
            elif country_name == 'Nauru':
                return 'nr'
            elif country_name == 'Tuvalu':
                return 'tv'
            elif country_name == 'East Asia & Pacific':
                return 'eap'
            elif country_name == 'Europe & Central Asia':
                return 'eca'
            elif country_name == 'Latin America & Caribbean':
                return 'lac'
            elif country_name == 'Sub-Saharan Africa':
                return 'ssa'