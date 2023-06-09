OPTIONS = [
    ('placement', 'Placement'),
    ('gradmentoring', 'Grad Mentoring'),
]

PLACEMENT_FIELDS = [
    ('it_software', 'IT/Software'),
    ('analytics', 'Analytics'),
    ('consultancy', 'Consultancy'),
    ('finance', 'Finance'),
    ('management', 'Management'),
    ('core', 'Core'),
]

HIGHERSTUDIES_FIELDS = [
    ('management', 'Management'),
    ('core', 'Core'),
]

DEGREE_CHOICES =[
    ('btech', 'B.Tech'),
    ('bs', 'B.S'),
    ('dual_degree', 'Dual Degree'),
    ('mtech', 'M.Tech'),
    ('msc', 'M.Sc'),
    ('phd', 'PhD'),
    ('other_degree', 'Other Degree'),
]

BRANCH_CHOICES = [
    ('aero', 'Aerospace Engineering'),
    ('cse', 'Computer Science Engineering'),
    ('ee', 'Electrical Engineering'),
    ('mech', 'Mechanical Engineering'),
    ('chem', 'Chemistry'),
    ('biosci', 'Biosciences & Bioengineering'),
    ('che', 'Chemical Engineering'),
    ('ieor', 'Industrial Engineering and Operations Research'),
    ('metallurgy', 'Metallurgical Engineering and Material Science'),
    ('engphy', 'Engineering Physics'),
    ('envsci', 'Environmental Science & Engineering'),
    ('energy', 'Energy Science & Engineering'),
    ('math', 'Mathematics'),
    ('civil', 'Civil Engineering'),
    ('earthsci', 'Earth Sciences and Resource engineering'),
    ('rural', 'Technology for Rural Areas'),
    ('design', 'Design'),
    ('other', 'Other (If not mentioned above)'),
]

BRANCH_SUBDIVISION_CHOICES = {
    'aero': [
        ('aero', 'Aerospace'),
        ('aerodynamics', 'Aerodynamics'),
        ('aerostructures', 'Aerospace structures'),
        ('dynamics', 'Dynamics and controls'),
        ('propulsion', 'Aerospace Propulsion'),
    ],
    'cse': [
        ('cse', 'Computer Science'),
        ('research', 'Research'),
    ],
    'ee': [
        ('ee', 'Electrical'),
        ('power', 'Power systems'),
        ('control', 'Control systems'),
        ('communication', 'Communication systems and signal processing'),
        ('design', 'Design engineering'),
        ('microelectronics', 'Microelectronics and nanotechnology'),
        ('semiconductors', 'Semiconductors'),
    ],
    'mech': [
        ('mech', 'Mechanical'),
        ('thermal', 'Thermal and Fluid engineering'),
        ('manufacturing', 'Manufacturing engineering'),
        ('design', 'Design and optimization (CAD, FEA)'),
        ('autoaero', 'Automotive and Aerospace'),
        ('mechatronics', 'Mechatronics'),
    ],
    'chem': [
        ('chem', 'Chemistry'),
        ('pharmaceutical', 'Pharmaceutical'),
        ('computational', 'Computational Chemistry'),
        ('cosmetics', 'Cosmetics and Paint industry'),
        ('coal', 'Coal, Oil and Gas'),
    ],
    'biosci': [
        ('biosci', 'Biosciences'),
        ('biomechanics', 'Biomechanics'),
        ('immunology', 'Immunology and Drug Discovery'),
        ('research', 'Research (Molecular/Cell biology)'),
        ('genetics', 'Genetics and Genomics'),
    ],
    'che': [
        ('che', 'Chemical'),
        ('transport', 'Transport phenomena'),
        ('thermo', 'Thermodynamics'),
        ('nanotech', 'Nanotechnology'),
        ('polymer', 'Polymer science'),
        ('process', 'Process design and analysis'),
    ],
    'ieor': [
        ('ieor', 'IEOR'),
        ('optimization', 'Optimization models'),
        ('stochastic', 'Stochastic models'),
        ('game', 'Game theory'),
        ('simulation', 'Simulation models'),
        ('supplychain', 'Supply chain analysis'),
    ],
    'metallurgy': [
        ('metallurgy', 'Metallurgy'),
        ('thermodynamics', 'Metallurgical Thermodynamics and Kinetics'),
        ('phase', 'Phase Transformations & Heat Treatment of Materials'),
        ('welding', 'Welding & Manufacturing'),
        ('characteristics', 'Material Science Characteristics'),
        ('surface', 'Surface Engineering'),
        ('ironsteel', 'Iron & Steel'),
    ],
    'engphy': [
        ('engphy', 'EP'),
        ('highenergy', 'High Energy Physics'),
        ('condensed', 'Condensed Matter Physics'),
        ('softmatter', 'Soft Matter Physics'),
        ('optics', 'Optics & Photonics'),
        ('astronomy', 'Astronomy, Cosmology & Gravity'),
    ],
    'envsci': [
        ('envsci', 'Environmental'),
        ('air', 'Air Quality Management and Pollution Control'),
        ('modeling', 'Environmental System Modelling'),
        ('waste', 'Solid and Hazardous Waste Management'),
        ('water', 'Water and Wastewater Treatment Reuse and Management'),
    ],
    'energy': [
        ('energy', 'Energy'),
        ('renewable', 'Renewable energy'),
        ('batteries', 'Batteries'),
        ('ev', 'EV'),
        ('grid', 'Electrical grid'),
        ('policy', 'Energy policy'),
    ],
    'math': [
        ('math', 'Mathematics'),
        ('research', 'Research'),
    ],
    'civil': [
        ('civil', 'Civil'),
        ('construction', 'Construction Technology and Management'),
        ('structural', 'Structural Engineering'),
        ('disaster', 'Disaster Resilience and Risk Management'),
        ('transport', 'Transport engineering'),
        ('urban', 'Urban planning'),
    ],
    'earthsci': [
        ('earthsci', 'Earth Sciences'),
        ('oceanography', 'Oceanography and Hydrology'),
        ('remote', 'Remote sensing and GIS'),
        ('geology', 'Geology'),
        ('climatology', 'Climatology'),
    ],
    'rural': [
        ('rural', 'Rural'),
        ('technology', 'Technology for Rural Areas'),
    ],
    'design': [
        ('design', 'Design'),
    ],
    'other': [
        ('other', 'Other (If not mentioned above)'),
    ],
}

