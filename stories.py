# World news of Wednesday 25 November 2026, checked against the outlets named.
# Each story: (region, label, headline, detail, big number, source)
# Labels: OFFICIAL = stated by a government/statistics body or official result,
#         REPORTED = reported by the outlet from named sources,
#         CLAIM    = one party's statement, not confirmed by the other side.

DAY = "WEDNESDAY 25 NOVEMBER 2026"

LEADS = [
    ("ASIA", "OFFICIAL", "CHINA DOCKS SHENZHOU-24 WITH FIRST PAKISTANI ASTRONAUT",
     "Launched 00:18 UTC from Jiuquan, docked at Tiangong 03:56 UTC. "
     "Muhammad Zeeshan Ali is the first foreign astronaut on China's station.",
     "03:56 UTC", "Reuters", "rocket"),
    ("AMERICAS", "OFFICIAL", "U.S. PROPOSES NEW TARIFFS ON 14 TRADING PARTNERS",
     "Headline rates of 20% to 40% after a Section 301 excess-capacity probe: "
     "China, EU, Japan, India, South Korea and nine more. Open for comment.",
     "14", "Reuters", "tariff"),
    ("ASIA", "OFFICIAL", "ASIAN CHIP STOCKS PLUNGE: SEOUL'S KOSPI LOSES 6.16%",
     "Kospi closed at 4,697.51. Samsung -9.87%, SK hynix -11.05%. "
     "Tokyo's Nikkei fell 2.78% to 57,011.62.",
     "-6.16%", "AP", "chart"),
]

CARDS = [
    ("MIDEAST", "CLAIM", "Iran's IRGC: two tankers hit mines, burn in Hormuz",
     "2 tankers", "Reuters", "ship"),
    ("OCEANIA", "OFFICIAL", "Australia and Solomon Islands sign treaty in Canberra: no foreign bases",
     "TREATY", "Reuters", "pen"),
    ("AMERICAS", "OFFICIAL", "Colombia: all Cartagena supermarket hostages freed, one gunman killed",
     "17 hours", "AP", "door"),
    ("MIDEAST", "CLAIM", "Houthis say they hit Saudi Ras Tanura refinery; Saudis: 4 drones downed",
     "4 drones", "Reuters", "flame"),
    ("MIDEAST", "REPORTED", "Gaza: Israeli strike kills Hamas security chief, his wife and two children",
     "4 dead", "Reuters", "blast"),
    ("OCEANIA", "OFFICIAL", "Australia inflation jumps to 4.9%, highest since 2023",
     "4.9%", "ABS", "up"),
    ("EUROPE", "OFFICIAL", "EU Parliament votes 367-268 to reopen nature laws",
     "367-268", "Politico", "vote"),
    ("EUROPE", "OFFICIAL", "EU court: Commission must set a date for banning caged farming",
     "RULING", "Euronews", "gavel"),
    ("AFRICA", "OFFICIAL", "DR Congo: UN troops evacuate 10 Ebola workers trapped by fighting",
     "5,867 dead", "Reuters", "cross"),
    ("EUROPE", "OFFICIAL", "Champions League: Lille 2-1 Bayern, Paris 2-2 Roma, Brugge 0-3 Liverpool",
     "2-1", "UEFA", "ball"),
]

BRIEFS = [
    ("AFRICA", "REPORTED", "Nigeria: gunmen kill at least 30 in Niger state villages", "Reuters"),
    ("AFRICA", "OFFICIAL", "Egypt: 21 die as fuel truck overturns and burns", "Reuters"),
    ("AFRICA", "REPORTED", "Sudan: rights group says RSF drones killed 19 civilians", "Reuters"),
    ("AFRICA", "OFFICIAL", "Senegal MPs vote 128-9 against president's budget move", "Reuters"),
    ("AFRICA", "OFFICIAL", "Kenya: cult leader Mackenzie convicted of child cruelty", "Reuters"),
    ("AFRICA", "OFFICIAL", "Nigeria seizes $227m of meth, arrests five Mexicans", "Reuters"),
    ("AFRICA", "OFFICIAL", "Morocco opens $2.2bn defence-industry drive", "Reuters"),
    ("AFRICA", "REPORTED", "Libya's LNA vows to retaliate against Ukraine", "AP"),
    ("ASIA", "REPORTED", "Bangladesh: garment workers clash with police on pay", "Reuters"),
    ("ASIA", "OFFICIAL", "India: Hasina's return is separate from extradition", "Reuters"),
    ("ASIA", "OFFICIAL", "India approves $1.2bn building-equipment plan", "Reuters"),
    ("ASIA", "OFFICIAL", "India rejects U.S. excess-capacity finding", "Reuters"),
    ("EUROPE", "OFFICIAL", "Merz: Russia 'wants more than Ukraine'", "Reuters"),
    ("EUROPE", "OFFICIAL", "EU Parliament backs shield for world courts, 438-168", "EP"),
    ("EUROPE", "OFFICIAL", "Pope Leo XIV laments COP31's failure to agree", "AP"),
    ("EUROPE", "OFFICIAL", "EU Parliament extends anti-VAT-fraud rules to 2030", "Bloomberg"),
]

# Stories deliberately left out because they belong to another day.
DATE_CHECK = [
    "Houthi strike on Riyadh tower: 24 Nov",
    "Huawei guilty verdict in U.S.: 24 Nov",
    "Real Madrid 5-1 PSV: 24 Nov",
    "Cartagena siege began: 24 Nov",
]

REGION_COLORS = {
    "ASIA": (200, 60, 50),
    "MIDEAST": (214, 130, 30),
    "EUROPE": (40, 90, 170),
    "AFRICA": (30, 130, 80),
    "AMERICAS": (120, 60, 150),
    "OCEANIA": (0, 140, 150),
}
