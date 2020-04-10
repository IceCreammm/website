data_cols = [
    "Country",
    "Study Pop Size (N)",
    "Paper Title",
    "Peer-Reviewed? (As of 2 April 2020)",
    "Study length (days)",
    "Overall study population or subgroup?",
    "Subgroup",
    "Median Age",
    "Hypertension",
    "Diabetes",
    "Cardiovascular Disease (incl. CAD)",
    "Chronic obstructive lung (COPD)",
    "Fever (temperature ≥37·3°C)",
    "Cough",
    "Fatigue",
    "Diarrhoea",
    "White Blood Cell Count (10^9/L) - Median",
    "Lymphocyte Count (10^9/L) - Median",
    "Platelet Count (10^9/L) - Median",
    "C-Reactive Protein (mg/L)",
    "Uses Kaletra (lopinavir–ritonavir)",
    "Uses Arbidol (umifenovir)",
    "Corticosteroid (including Glucocorticoid, Methylprednisolone)",
    "Invasive mechanical ventilation",
    "ARDS",
    "Hospital admission (%)",
    "Discharged (%)",
    "Mortality",
    "Projected Mortality (accounting for patients not currently discharged)"
]

all_options = {
    'Comorbidities': [
        "Hypertension",
        "Diabetes",
        "Cardiovascular Disease (incl. CAD)",
        "Chronic obstructive lung (COPD)"
    ],
    'Symptoms': [
        "Fever (temperature ≥37·3°C)",
        "Cough",
        "Fatigue",
        "Diarrhoea",
    ],
    'Treatment': ["Invasive mechanical ventilation"],
}


states = {
    'US':'US','Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'American Samoa': 'AS',
    'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT',
    'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Guam': 'GU', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI',
    'Minnesota': 'MN', 'Missouri': 'MO', 'Northern Mariana Islands': 'MP',
    'Mississippi': 'MS', 'Montana': 'MT', 'National': 'NA', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI',
    'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Virginia': 'VA', 'Virgin Islands': 'VI', 'Vermont': 'VT',
    'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV', 'Wyoming': 'WY'
    }

# colors that align with inferno
colors =[
            '#000004',
            '#4a0c6b',
            '#a52c60',
            '#ed6925',
            '#f7d31d'
        ]
