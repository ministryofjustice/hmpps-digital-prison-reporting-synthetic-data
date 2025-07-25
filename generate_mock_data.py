import random
from faker import Faker
import pandas as pd
from pathlib import Path

fake = Faker("en_GB")

# Directory where CSV files will be saved
DATA_DIR = Path("data")

# Real establishment list
ESTABLISHMENTS = {
    "ACI": "Altcourse", "ASI": "Ashfield", "AGI": "Askham Grange", "AYI": "Aylesbury", "BFI": "Bedford",
    "BAI": "Belmarsh", "BWI": "Berwyn", "BMI": "Birmingham", "BSI": "Brinsford", "BLI": "Bristol",
    "BXI": "Brixton", "BZI": "Bronzefield", "BCI": "Buckley Hall", "BNI": "Bullingdon", "BRI": "Bure",
    "CFI": "Cardiff", "CWI": "Channings Wood", "CDI": "Chelmsford", "CLI": "Coldingley", "CKI": "Cookham Wood",
    "DAI": "Dartmoor", "DTI": "Deerbolt", "DNI": "Doncaster", "DGI": "Dovegate", "DWI": "Downview",
    "DHI": "Drake Hall", "DMI": "Durham", "ESI": "East Sutton Park", "EWI": "Eastwood Park", "EYI": "Elmley",
    "EEI": "Erlestoke", "EXI": "Exeter", "FSI": "Featherstone", "FMI": "Feltham", "FYI": "Feltham A",
    "FWI": "Five Wells", "FDI": "Ford", "FBI": "Forest Bank", "FEI": "Fosse Way", "FHI": "Foston Hall",
    "FKI": "Frankland", "FNI": "Full Sutton", "GHI": "Garth", "GTI": "Gartree", "GNI": "Grendon",
    "GMI": "Guys Marsh", "HDI": "Hatfield", "HVI": "Haverigg", "HEI": "Hewell", "HOI": "High Down",
    "HPI": "Highpoint", "HII": "Hindley", "HBI": "Hollesley Bay", "HHI": "Holme House", "HLI": "Hull",
    "HMI": "Humber", "HCI": "Huntercombe", "ISI": "Isis", "IWI": "Isle of Wight", "KMI": "Kirkham",
    "KVI": "Kirklevington Grange", "LFI": "Lancaster Farms", "LEI": "Leeds", "LCI": "Leicester", "LWI": "Lewes",
    "LYI": "Leyhill", "LII": "Lincoln", "LHI": "Lindholme", "LTI": "Littlehey", "LPI": "Liverpool",
    "LLI": "Long Lartin", "LNI": "Low Newton", "LGI": "Lowdham Grange", "MSI": "Maidstone", "MRI": "Manchester",
    "MDI": "Moorland", "MHI": "Morton Hall", "NHI": "New Hall", "NSI": "North Sea Camp", "NLI": "Northumberland",
    "NWI": "Norwich", "NMI": "Nottingham", "OWI": "Oakwood", "ONI": "Onley", "PRI": "Parc",
    "PVI": "Pentonville", "PFI": "Peterborough (Female)", "PBI": "Peterborough (Male)", "PDI": "Portland",
    "UPI": "Prescoed", "PNI": "Preston", "RNI": "Ranby", "RSI": "Risley", "RCI": "Rochester", "RHI": "Rye Hill",
    "SDI": "Send", "SPI": "Spring Hill", "SFI": "Stafford", "EHI": "Standford Hill", "SKI": "Stocken",
    "SHI": "Stoke Heath", "STI": "Styal", "SUI": "Sudbury", "SLI": "Swaleside", "SWI": "Swansea",
    "SNI": "Swinfen Hall", "TSI": "Thameside", "MTI": "The Mount", "VEI": "The Verne", "TCI": "Thorn Cross",
    "UKI": "Usk", "WDI": "Wakefield", "WWI": "Wandsworth", "WII": "Warren Hill", "WLI": "Wayland",
    "WEI": "Wealstun", "WNI": "Werrington", "WYI": "Wetherby", "WTI": "Whatton", "WRI": "Whitemoor",
    "WCI": "Winchester", "WHI": "Woodhill", "WSI": "Wormwood Scrubs", "WMI": "Wymott",

    # Additional Probation Offices, Courts, etc:
    "693103": "Kingston & Richmond Probation Office",
    "696575": "BOURNEMOUTH Probation Centre",
    "701109": "Wallsend Probation Office",
    "703230": "DORSET CLOSE Probation Office",
    "705109": "Enfield Probation Office",
    "705670": "Oxford City Probation Office",
    "706931": "Plymouth Probation Centre",
    "714662": "Sittingbourne Probation Office",
    "721844": "NELSON Probation Office",
    "724559": "Woolwich Probation Office",
    "724648": "Sheerness Probation Office",
    "727642": "NORTHAMPTONSHIRE OFFICES",
    "735096": "Bexleyheath Probation Office",
    "739917": "LINCOLN Probation Office",
    "754134": "WESTON-SUPER-MARE Probation Centre",
    "754990": "Littlehampton Probation Office",
    "761287": "MAGISTRATES COURT",
    "770452": "LEELAND HOUSE",
    "776185": "High Wycombe Probation Office",
    "778998": "West Bromwich Probation Office",
    "781940": "Croydon Probation Office",
    "795760": "DTTO NOTTINGHILL GATE",
    "796120": "Erdington Probation Centre",
    "AAAAA1": "AA Mike H Crown Court",
    "AAAMH1": "AAAMH1 Court Mike H2 Test2",
    "AAAMH2": "AAA Mike H Testing",
    "AAAMH3": "AAAMH1 Court Mike H2 Test2 - Building tr",
    "AAAMH5": "AAAMH1 Court Mike H2 Test2 - 22",
    "ABDALE": "Abbey Dale Court, London",
    "ABDRCT": "Aberdare County Court",
    "ABDRMC": "Aberdare Mc",
    "ABDRYC": "Aberdare Youth Court",
    "ABDSUM": "Aberdeen Sheriff's Court (ABDSHF)",
    "ABGVMC": "Abergavenny Magistrates Court",
    "ABRYCT": "Aberystwyth County Court",
    "ABRYMC": "Aberystwyth Magistrates Court",
    "ABRYYC": "Aberystwyth Youth Court",
    "ABTYMC": "Abertillery Mc",
    "ABWLEY": "Abraham Cowley Unit",
    "ACCRCT": "Accrington County Court",
    "ACCRMC": "Accrington (Hyndburn) Magistrates Court",
    "ACCRYC": "Accrington (Hyndburn) Youth Court",
    "ACTNCC": "Acton Crown Court",
    "ACTNMC": "Acton Mc",
    "ACTNYC": "Acton Youth Court",
    "AKI": "Acklington (HMP)",
    "ALDRCT": "Aldershot and Farnham County Court",
    "ALDRMC": "Aldershot (Nort East Hampshire) Magistrates",
    "ALI": "Albany (HMP)",
    "ALLSHF": "Alloa Sheriff's Court",
    "ALNWMC": "Alnwick Mc",
    "ALNWYC": "Alnwick Youth Court",
    "ALPHA": "Alpha Hospital",
    "ALPHHO": "Alpha Hospitals Sheffield",
    "ALTNMC": "Alton Mc",
    "ALTNYC": "Alton Youth Court",
    "ALTRCT": "Altrincham County Court",
    "AMERCC": "Amersham Crown Court",
    "AMERSH": "Amersham General",
    "AMMNMC": "Ammanford Mc",
    "AMMNYC": "Ammanford Youth Court",
    "AMRSMC": "Amersham Mc",
    "AMRSYC": "Amersham Youth Court",
    "ANDVMC": "Andover Mc",
    "ANDVYC": "Andover Youth Court",
    "ANI": "Aldington (HMP)",
    "ANTCC1": "Antrim Crown Court",
    "ANTMC1": "Antrim Magistrates Court",
    "ARDEN": "Arden Leigh MSU",
    "ARNOLD": "Arnold Lodge",
    "ASHEHO": "Ashen Hill/Southview",
    "ASHFCT": "Ashford County Court",
    "ASHFMC": "Ashford Mc",
    "ASHTMC": "Tameside (Ashton under Lyne) Magistrates",
    "ASHTYC": "Tameside (Ashton under Lyne) Youth Court",
    "ASHWTH": "Ashworth Hospital",
    "ASP001": "North Somerset Courthouse Probation",
    "ASP002": "Bath Probation Centre",
    "ASP003": "Knowle Park, Bristol Probation Centre",
    "ASP004": "Bristol Probation Centre",
    "ASP005": "North Bristol Probation Centre",
    "ASP006": "Weston-super-Mare Probation Centre",
    "ASP007": "Bristol Probation Centre",
    "ASP008": "Bristol Crown Court Liaison Office",
    "ASP009": "Taunton Probation Centre",
    "ASP010": "Wells Probation Centre",
    "ASP011": "Yeovil Probation Centre",
    "ASP012": "Bridgwater Probation Centre",
    "ASP013": "Taunton Crown Court Liaison Unit",
    "ASP015": "Bath Prolific Offender Unit",
    "ASP016": "New Bridewell Prolific Offender Unit",
    "ASP017": "Staple Hill Police St. Prolific Off Unit",
    "ASP019": "Taunton Police Station Prolific Off Unit",
    "GLDFCC": "Guildford Crown Court",
    "SNARCC": "Snaresbrook Crown Court",
    "PLYMCC": "Plymouth Crown Court",
    "TRURCC": "Truro Crown Court",
    "EXETCC": "Exeter Crown Court",
    "COACD": "Court Of Appeal Criminal Division",
    "PLYMMC": "Plymouth Magistrates Court",
    "HGHBMC": "Highbury Corner Magistrates Court",
}
# List of special unknown locations
SPECIAL_LOCATIONS = {
    "UNKNWN": "UNKNOWN LOCATION",
    "NULL": None,
    "OUT": "OUTSIDE",
}


def generate_establishment_establishment_csv():
    path = DATA_DIR / "establishment_establishment.csv"
    data = [{"establishment_id": est_id, "name": name} for est_id, name in ESTABLISHMENTS.items()]
    pd.DataFrame(data).to_csv(path, index=False)
    print(f"✅ Generated {path} with {len(data)} establishments.")


def generate_establishment_living_unit_csv():
    path = DATA_DIR / "establishment_living_unit.csv"
    data = []

    codes = set()
    unit_id = 1

    for est_id in ESTABLISHMENTS.keys():
        for _ in range(random.randint(1, 3)):  # Each establishment has 1-3 units
            while True:
                code = f"{fake.bothify(text='??###').upper()}"
                if code not in codes:
                    codes.add(code)
                    break
            data.append({
                "id": unit_id,
                "code": code,
                "establishment_id": est_id,
                "name": f"{est_id}-{code}"
            })
            unit_id += 1

    pd.DataFrame(data).to_csv(path, index=False)
    print(f"✅ Generated {path} with {len(data)} living units.")


def generate_prisoner_prisoner_csv():
    path = DATA_DIR / "prisoner_prisoner.csv"
    living_units_df = pd.read_csv(DATA_DIR / "establishment_living_unit.csv")
    codes = living_units_df["code"].tolist()

    data = []
    prisoner_ids = []

    for _ in range(1000):
        prisoner_id = random.randint(1100000, 1200000)
        prisoner_ids.append(prisoner_id)
        number = f"G{random.randint(1000, 9999)}{random.choice(['UD', 'UN', 'UF'])}"
        firstname = fake.first_name().upper().replace("'", "").replace("-", "")
        lastname = fake.last_name().upper().replace("'", "").replace("-", "")
        living_unit_reference = random.choice(codes)

        data.append({
            "id": prisoner_id,
            "number": number,
            "firstname": firstname,
            "lastname": lastname,
            "living_unit_reference": living_unit_reference
        })

    pd.DataFrame(data).to_csv(path, index=False)
    print(f"✅ Generated {path} with 100 prisoners.")
    return prisoner_ids


def generate_movement_movement_csv(prisoner_ids):
    path = DATA_DIR / "movement_movement.csv"
    data = []

    movement_type_abbr = ["ADM", "TAP", "TRN", "REL", "CRT"]
    REASONS = {
        "ADM": ["Initial Admission", "Immigration Admission"],
        "TAP": ["Temporary Transfer", "Outside Hospital Attendance"],
        "TRN": ["Normal Transfer", "Medical Transfer", "Category Change"],
        "REL": ["Release on License", "Release to Immigration", "End of Sentence"],
        "CRT": ["Court Appearance", "Remand Hearing"]
    }

    all_location_codes = list(ESTABLISHMENTS.keys())
    all_location_names = ESTABLISHMENTS.copy()

    for prisoner_id in prisoner_ids:
        num_movements = random.randint(1, 4)
        for i in range(1, num_movements + 1):
            movement_id = f"{prisoner_id}.{i}"
            dt = fake.date_time_between(start_date="-10y", end_date="now")
            date_str = dt.strftime("%Y-%m-%d 00:00:00")
            time_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            direction = random.choice(["IN", "OUT"])
            type_abbr = random.choice(movement_type_abbr)

            # Origin can be a special location (10% chance)
            if random.random() < 0.10:
                origin_code = random.choice(list(SPECIAL_LOCATIONS.keys()))
                origin_name = SPECIAL_LOCATIONS[origin_code]
            else:
                origin_code = random.choice(all_location_codes)
                origin_name = all_location_names[origin_code]

            # Destination must be different from origin
            while True:
                if random.random() < 0.10:
                    destination_code = random.choice(list(SPECIAL_LOCATIONS.keys()))
                    destination_name = SPECIAL_LOCATIONS[destination_code]
                else:
                    destination_code = random.choice(all_location_codes)
                    destination_name = all_location_names[destination_code]
                if destination_code != origin_code:
                    break

            reason = random.choice(REASONS.get(type_abbr, ["Other"]))

            data.append({
                "id": movement_id,
                "prisoner": prisoner_id,
                "date": date_str,
                "time": time_str,
                "direction": direction,
                "type": type_abbr,
                "origin_code": origin_code,
                "origin": origin_name,
                "destination_code": destination_code,
                "destination": destination_name,
                "reason": reason
            })

    pd.DataFrame(data).to_csv(path, index=False)
    print(f"✅ Generated {path} with {len(data)} movements.")


if __name__ == "__main__":
    import os
    print("🔧 Script started")
    print(f"Working directory: {os.getcwd()}")
    DATA_DIR.mkdir(exist_ok=True)
    print(f"📁 Data directory: {DATA_DIR.resolve()}")

    generate_establishment_establishment_csv()
    generate_establishment_living_unit_csv()
    prisoner_ids = generate_prisoner_prisoner_csv()
    generate_movement_movement_csv(prisoner_ids)

    print("🎉 All synthetic data files generated successfully.")