import cdsapi

c = cdsapi.Client()

c.retrieve(
    'projections-cmip5-monthly-single-levels',
    {
        'variable':'2m_temperature',
        'model':'gfdl_cm3',
        'experiment':[
            'rcp_2_6','rcp_8_5'
        ],
        'ensemble_member':'r1i1p1',
        'period':[
            '203101-203512','209601-210012'
        ],
        'format':'zip'
    },
    'download.zip')
