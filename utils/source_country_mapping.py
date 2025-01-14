import pycountry

source_country_dict = {
    "Stgnews": "United States",
    "Zimbabwe Mail": "Zimbabwe",
    "4-Traders": "Unknown",
    "Planet": "Unknown",
    "The Chronicle": "United Kingdom",
    "International Business Times Au": "Australia",
    "Abovethelaw": "United States",
    "Midhudsonnews": "United States",
    "Talking Biz News": "United States",
    "Thereporter": "Unknown",
    "Timesheraldonline": "United States",
    "Post": "Unknown",
    "Seeking Alpha": "United States",
    "Executivegov": "United States",
    "Calgary": "Canada",
    "Mymotherlode": "United States",
    "Thebusinessjournal": "United States",
    "Business Travel News": "United States",
    "Finanznachrichten": "Germany",
    "Mail": "United Kingdom",
    "Suffolktimes": "United States",
    "Castanet": "Canada",
    "Koreaherald": "South Korea",
    "Kvia": "United States",
    "Financial Post Canada Business News": "Canada",
    "Lowell Sun": "United States",
    "Bostonherald": "United States",
    "Slashdot": "United States",
    "Chicago Tribune": "United States",
    "Appolicious": "United States",
    "Pharmpro": "United States",
    "Abc Money": "United Kingdom",
    "Journalrecord": "United States",
    "The Age": "Australia",
    "Brisbane Times": "Australia",
    "Watoday": "Australia",
    "Orovillemr": "United States",
    "Chicoer": "United States",
    "Insights Success": "United States",
    "Dailybulletin": "United States",
    "Dailybreeze": "United States",
    "Press-Telegram": "United States",
    "Sgvtribune": "United States",
    "Pasadenastarnews": "United States",
    "Sbsun": "United States",
    "Whittierdailynews": "United States",
    "Ocregister": "United States",
    "Redlandsdailyfacts": "United States",
    "Americansongwriter": "United States",
    "Hitfix": "United States",
    "Centralpennbusiness": "United States",
    "Thetrucker": "United States",
    "Torontosun": "Canada",
    "Keyt": "United States",
    "Ksro": "United States",
    "Vox": "United States",
    "Dvidshub": "United States",
    "Dailycamera": "United States",
    "The Guardian": "United Kingdom",
    "Washingtonian": "United States",
    "The New York Times": "United States",
    "247Wallst": "United States",
    "Essentially Sports": "India",
    "Cagesideseats": "United States",
    "Investingcom Stock Market Quotes Financial News": "United States",
    "Globalgrind": "United States",
    "The Jamaica Star": "Jamaica",
    "Polygon": "United States",
    "Independent": "United Kingdom",
    "Cincyjungle": "United States",
    "Awfulannouncing": "United States",
    "Kionrightnow": "United States",
    "Webwire": "United States",
    "Thepoke": "United Kingdom",
    "Tmz": "United States",
    "Lep": "Unknown",
    "Newscaststudio": "United States",
    "Abc News": "United States",
    "Americanbankingnews": "United States",
    "Google News Sports Gb": "United Kingdom",
    "Businesstoday": "India",
    "Etfdailynews": "United States",
    "Sundayworld": "Ireland",
    "Artsbeat": "United States",
    "Vegasinc": "United States",
    "Interaksyon": "Philippines",
    "Nme": "United Kingdom",
    "The Hindu": "India",
    "Nesn": "United States",
    "Canyon-News": "United States",
    "Headlineplanet": "United States",
    "Slashgear": "United States",
    "Thewrap": "United States",
    "Pocket-Lint": "United Kingdom",
    "Hollywoodlife": "United States",
    "Theroot": "United States",
    "Monstersandcritics": "United States",
    "Wrestlingnewssource": "United States",
    "Samoa News": "Samoa",
    "Nbc": "United States",
    "The Roar Sports Writers Blog": "Australia",
    "Paradisepost": "United States",
    "Mercurynews": "United States",
    "Montereyherald": "United States",
    "Dailydemocrat": "United States",
    "Santacruzsentinel": "United States",
    "Marinij": "United States",
    "Eurasiareview": "United States",
    "En": "Unknown",
    "Whkp": "United States",
    "Suntimes": "United States",
    "Ktvz": "United States",
    "Nz Herald": "New Zealand",
    "Newswise": "United States",
    "Bulawayo24 News": "Zimbabwe",
    "Thisdaylive": "Nigeria",
    "Valleyadvocate": "United States",
    "Localnews8": "United States",
    "Avclub": "United States",
    "Covnews": "United States",
    "Aurorasentinel": "United States",
    "Chipchick": "United States",
    "Ctvbc": "Canada",
    "Kyma": "United States",
    "Wvmetronews": "United States",
    "Mauinow": "United States",
    "Wtvq": "United States",
    "Interlakespectator": "Canada",
    "Times-Standard": "United States",
    "Lythamstannesexpress": "United Kingdom",
    "Fox21Online": "United States",
    "Pakistan Today": "Pakistan",
    "Live Science The Most Interesting Articles": "United States",
    "Winnipegsun": "Canada",
    "Twincities": "United States",
    "Reporterherald": "United States",
    "Greeleytribune": "United States",
    "Dailynews": "United States",
    "Ukiahdailyjournal": "United States",
    "Fortmorgantimes": "United States",
    "Presstelegram": "United States",
    "Journal-Advocate": "United States",
    "Latimes": "United States",
    "Globalmontreal": "Canada",
    "Deccanchronicle": "India",
    "Fox News - Video": "United States",
    "Thenewamerican": "United States",
    "Winklertimes": "Canada",
    "Sports": "Unknown",
    "Euroweeklynews": "Spain",
    "Theinquirer": "United Kingdom",
    "The Sydney Morning Herald": "Australia",
    "Brisbanetimes": "Australia",
    "Pcworld": "United States",
    "Alternet": "United States",
    "Tribune": "Unknown",
    "Physorg - News And Articles On Science And Technology": "United States",
    "Advanced Science News": "Germany",
    "Haiti Libre": "Haiti",
    "Wnyc": "United States",
    "Thefilmstage": "United States",
    "Metro": "United Kingdom",
    "Highland Radio": "Ireland",
    "Businessdayonline": "Nigeria",
    "Greece": "Greece",
    "Orissadiary": "India",
    "India": "India",
    "Google News Science Us": "United States",
    "Counterpunch": "United States",
    "Ghanabusinessnews": "Ghana",
    "Cornwallseawaynews": "Canada",
    "Federalnewsradio": "United States",
    "Nation News": "Barbados",
    "Science Aaas": "United States",
    "Thisislondon": "United Kingdom",
    "Cwn Sports": "Unknown",
    "Insidesport": "India",
    "Sporting News": "United States",
    "Kesq": "United States",
    "Larrybrownsports": "United States",
    "Sfist": "United States",
    "The Sports News": "Unknown",
    "Google News Sports Us": "United States",
    "Dailynorseman": "United States",
    "Sportspac12": "United States",
    "Wwd": "United States",
    "Bleacher Report": "United States",
    "Thesudburystar": "Canada",
    "Thesportsbank": "United States",
    "Thedailyrecord": "United Kingdom",
    "Thejournal": "United Kingdom",
    "Jta": "United States",
    "Winnipeg": "Canada",
    "Betanews": "United States",
    "Altonaecho": "Canada",
    "Rdmag": "United States",
    "Sheffieldtelegraph": "United Kingdom",
    "Dewsburyreporter": "United Kingdom",
    "Blackpoolgazette": "United Kingdom",
    "Yorkshirepost": "United Kingdom",
    "The Verge": "United States",
    "Neworleanscitybusiness": "United States",
    "Abc Au": "Australia",
    "Google News Sports In": "India",
    "Eastcountymagazine": "United States",
    "Manchester Evening News": "United Kingdom",
    "Rep-Am": "United States",
    "World In Sport": "United Kingdom",
    "Sthelensreporter": "United Kingdom",
    "Krdo": "United States",
    "Medcitynews": "United States",
    "Google News Business Us": "United States",
    "Lacombeglobe": "Canada",
    "Cyprus-Mail": "Cyprus",
    "Google News World In": "India",
    "Journal": "Unknown",
    "Zee Business": "India",
    "Bandt": "Australia",
    "Heyuguys": "United Kingdom",
    "Thyblackman": "United States",
    "Politicsie": "Ireland",
    "Theborneopost": "Malaysia",
    "Bearsdenherald": "United Kingdom",
    "Stnonline": "United States",
    "Kaieteur News": "Guyana",
    "Photos": "Unknown",
    "Kuenselonline": "Bhutan",
    "Ilkestonadvertiser": "United Kingdom",
    "Zenit": "Vatican City",
    "Dailymail": "United Kingdom",
    "Arabnews": "Saudi Arabia",
    "Timesrecord": "United States",
    "Bernews": "Bermuda",
    "Siliconvalley": "United States",
    "Guardian": "Unknown",
    "Fortune": "United States",
    "Google News Health Au": "Australia",
    "Antiwar": "United States",
    "620Wtmj": "United States",
    "Mirror": "United Kingdom",
    "Myedmondsnews": "United States",
    "Srilankaguardian": "Sri Lanka",
    "Yalibnan": "Lebanon",
    "The Star Online": "Malaysia",
    "Barbados Today": "Barbados",
    "Daily Record": "United Kingdom",
    "Theage": "Australia",
    "Fox News - Health": "United States",
    "Scoop": "New Zealand",
    "Bigislandvideonews": "United States",
    "Times Of Malta": "Malta",
    "News24": "South Africa",
    "Nationalreview": "United States",
    "Arabamericannews": "United States",
    "Mrzine": "United States",
    "Mybroadband": "South Africa",
    "Cbssports": "United States",
    "Toledoblade": "United States",
    "Steelersdepot": "United States",
    "Mailonsunday": "United Kingdom",
    "Wide World Of Sports": "Australia",
    "Sbnation": "United States",
    "Bleedinggreennation": "United States",
    "Edinburghnews": "United Kingdom",
    "Complete Sports Nigeria": "Nigeria",
    "Bahamas Press": "Bahamas",
    "Bloomberg Latest And Live Business": "United States",
    "Dnaindia": "India",
    "Cnbc": "United States",
    "Housingwire": "United States",
    "Channelnews": "Australia",
    "Eastbayexpress": "United States",
    "Edsonleader": "Canada",
    "Todaystmj4": "United States",
    "Dailyherald": "United States",
    "Japantoday": "Japan",
    "Forsythnews": "United States",
    "Business": "Unknown",
    "Science20": "United States",
    "Webpronews": "United States",
    "Gizmodo": "United States",
    "Argophilia": "Unknown",
    "Starcasm": "United States",
    "Engadget": "United States",
    "Yardbarker": "United States",
    "Calgaryherald": "Canada",
    "Hiphopwired": "United States",
    "Worldscreen": "United States",
    "Franchise Sports": "United States",
    "Lulegacy": "Unknown",
    "The Independent - Travel": "United Kingdom",
    "Nyasa Times": "Malawi",
    "Business Line": "India",
    "Business Standard": "India",
    "Dinningtontoday": "United Kingdom",
    "Thecaucus": "United States",
    "Wral": "United States",
    "Arktimes": "United States",
    "Gaytoday": "United States",
    "Fwweekly": "United States",
    "Thestreet": "United States",
    "Onlineopinion": "Australia",
    "Thenewcivilrightsmovement": "United States",
    "Rafu": "United States",
    "Upiasia": "United States",
    "Google News Health Ca": "Canada",
    "Upi": "United States",
    "Abc6": "United States",
    "Chadrad": "United States",
    "Cknw": "Canada",
    "Pulse": "Unknown",
    "Feeds": "Unknown",
    "Wtop": "United States",
    "Libn": "United States",
    "Donegal Daily": "Ireland",
    "M": "Unknown",
    "Zdnet": "United States",
    "Carmanvalleyleader": "Canada",
    "Dailycaller": "United States",
    "Ns": "Unknown",
    "Physorg": "United States",
    "Inthenews": "United Kingdom",
    "London Evening Standard": "United Kingdom",
    "Ryeandbattleobserver": "United Kingdom",
    "Daily Times": "United States",
    "Kbc": "Kenya",
    "Espn": "United States",
    "Google News Sports Ca": "Canada",
    "Shelterislandreporter": "United States",
    "Defensedaily": "United States",
    "Jalopnik": "United States",
    "Sociable": "Unknown",
    "Starherald": "United States",
    "Digitaltrends": "United States",
    "Digitalfacility": "Unknown",
    "Landlinemag": "United States",
    "Thescotsman": "United Kingdom",
    "Wgmd": "United States",
    "Thewhig": "Canada",
    "Axcessnews": "United States",
    "Chicagoreader": "United States",
    "Haylingtoday": "United Kingdom",
    "Bbc News - World": "United Kingdom",
    "Wgil": "United States",
    "Music Business Worldwide": "United Kingdom",
    "Business World": "Philippines",
    "Zazoom": "United States",
    "Louthleader": "United Kingdom",
    "Securityinfowatch": "United States",
    "Iot Business News": "Unknown",
    "Lankabusinessonline": "Sri Lanka",
    "Gamereactor": "Denmark",
    "Marketingvox": "United States",
    "Lvrj": "United States",
    "Wfir960": "United States",
    "Google News Technology Gb": "United Kingdom",
    "Wavenewspapers": "United States",
    "Radioink": "United States",
    "Dailyiowan": "United States",
    "Informationnigeria": "Nigeria",
    "Techcrunch": "United States",
    "Nextbigfuture": "United States",
    "Chattanoogan": "United States",
    "Extratv": "United States",
    "Businessmole": "United Kingdom",
    "Edmontonjournal": "Canada",
    "Post-Gazette": "United States",
    "Mycentraloregon": "United States",
    "Ottawacitizen": "Canada",
    "Chelsearecord": "United States",
    "Google News World Us": "United States",
    "Boston": "United States",
    "Gainesvilletimes": "United States",
    "Google News Science Gb": "United Kingdom",
    "Ips News Agency": "Italy",
    "Sportsration Nigeria Soccer World Sports": "Nigeria",
    "Jewishtimes": "United States",
    "Catholicnews": "United States",
    "Queerty": "United States",
    "Express Star": "United Kingdom",
    "Hellomagazine": "United Kingdom",
    "B-Townblog": "United States",
    "Itnewsafrica": "South Africa",
}


def add_country_column(df, column_name):
    df["country"] = df[column_name].map(source_country_dict)

    return df


def add_country_code_column(df, column_name):
    def get_country_code(x):
        try:
            country = pycountry.countries.get(name=x)  # get by country name
            if country:
                return country.alpha_2
            else:
                return None
        except LookupError:
            return None

    df["country_code"] = df[column_name].apply(get_country_code)
    return df
