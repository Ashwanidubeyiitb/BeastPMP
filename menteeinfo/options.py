OPTIONS = [
    ('placement', 'Placement'),
    ('grad', 'Grad Mentoring'),
]

PLACEMENT_FIELDS = [
    ('it_software', 'IT/Software'),
    ('analytics', 'Analytics'),
    ('consultancy', 'Consultancy'),
    ('finance', 'Finance'),
    ('management', 'Management'),
    ('core', 'Core'),
    ('other', 'Other')
]

HIGHERSTUDIES_FIELDS = [
    ('management', 'Management'),
    ('core', 'Core')
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
        ('Aerospace', 'Aerospace'),
('Aerodynamics', 'Aerodynamics'),
('Aerospace structures', 'Aerospace structures'),
('Dynamics and controls', 'Dynamics and controls'),
('Aerospace Propulsion', 'Aerospace Propulsion'),
],

'cse': [
('Computer Science', 'Computer Science'),
('Research', 'Research'),
],

'ee': [
('Electrical', 'Electrical'),
('Power systems', 'Power systems'),
('Control systems', 'Control systems'),
('Communication systems and signal processing', 'Communication systems and signal processing'),
('Design engineering', 'Design engineering'),
('Microelectronics and nanotechnology', 'Microelectronics and nanotechnology'),
('Semiconductors', 'Semiconductors'),
],

'mech': [
('Mechanical', 'Mechanical'),
('Thermal and Fluid engineering', 'Thermal and Fluid engineering'),
('Manufacturing engineering', 'Manufacturing engineering'),
('Design and optimization (CAD, FEA)', 'Design and optimization (CAD, FEA)'),
('Automotive and Aerospace', 'Automotive and Aerospace'),
('Mechatronics', 'Mechatronics'),
],

'chem': [
('Chemistry', 'Chemistry'),
('Pharmaceutical', 'Pharmaceutical'),
('Computational Chemistry', 'Computational Chemistry'),
('Cosmetics and Paint industry', 'Cosmetics and Paint industry'),
('Coal, Oil and Gas', 'Coal, Oil and Gas'),
],

'biosci': [
('Biosciences', 'Biosciences'),
('Biomechanics', 'Biomechanics'),
('Immunology and Drug Discovery', 'Immunology and Drug Discovery'),
('Research (Molecular/Cell biology)', 'Research (Molecular/Cell biology)'),
('Genetics and Genomics', 'Genetics and Genomics'),
],

'che': [
('Chemical', 'Chemical'),
('Transport phenomena', 'Transport phenomena'),
('Thermodynamics', 'Thermodynamics'),
('Nanotechnology', 'Nanotechnology'),
('Polymer science', 'Polymer science'),
('Process design and analysis', 'Process design and analysis'),
],

'ieor': [
('IEOR', 'IEOR'),
('Optimization models', 'Optimization models'),
('Stochastic models', 'Stochastic models'),
('Game theory', 'Game theory'),
('Simulation models', 'Simulation models'),
('Supply chain analysis', 'Supply chain analysis'),
],

'metallurgy': [
('Metallurgy', 'Metallurgy'),
('Metallurgical Thermodynamics and Kinetics', 'Metallurgical Thermodynamics and Kinetics'),
('Phase Transformations & Heat Treatment of Materials', 'Phase Transformations & Heat Treatment of Materials'),
('Welding & Manufacturing', 'Welding & Manufacturing'),
('Material Science Characteristics', 'Material Science Characteristics'),
('Surface Engineering', 'Surface Engineering'),
('Iron & Steel', 'Iron & Steel'),
],

'engphy': [
('EP', 'EP'),
('High Energy Physics', 'High Energy Physics'),
('Condensed Matter Physics', 'Condensed Matter Physics'),
('Soft Matter Physics', 'Soft Matter Physics'),
('Optics & Photonics', 'Optics & Photonics'),
('Astronomy, Cosmology & Gravity', 'Astronomy, Cosmology & Gravity'),
],

'envsci': [
('Environmental', 'Environmental'),
('Air Quality Management and Pollution Control', 'Air Quality Management and Pollution Control'),
('Environmental System Modelling', 'Environmental System Modelling'),
('Solid and Hazardous Waste Management', 'Solid and Hazardous Waste Management'),
('Water and Wastewater Treatment Reuse and Management', 'Water and Wastewater Treatment Reuse and Management'),
],

'energy': [
('Energy', 'Energy'),
('Renewable energy', 'Renewable energy'),
('Batteries', 'Batteries'),
('EV', 'EV'),
('Electrical grid', 'Electrical grid'),
('Energy policy', 'Energy policy'),
],

'math': [
('Mathematics', 'Mathematics'),
('Research', 'Research'),
],

'civil': [
('Civil', 'Civil'),
('Construction Technology and Management', 'Construction Technology and Management'),
('Structural Engineering', 'Structural Engineering'),
('Disaster Resilience and Risk Management', 'Disaster Resilience and Risk Management'),
('Transport engineering', 'Transport engineering'),
('Urban planning', 'Urban planning'),
],

'earthsci': [
('Earth Sciences', 'Earth Sciences'),
('Oceanography and Hydrology', 'Oceanography and Hydrology'),
('Remote sensing and GIS', 'Remote sensing and GIS'),
('Geology', 'Geology'),
('Climatology', 'Climatology'),
],

'rural': [
('Rural', 'Rural'),
('Technology for Rural Areas', 'Technology for Rural Areas'),
],

'design': [
('Design', 'Design'),
],

'other': [
('Other (If not mentioned above)', 'Other (If not mentioned above)'),
]
}