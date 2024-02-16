import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-field-service",
    description="Meta package for open-synergy-ssi-field-service Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_field_service',
        'odoo14-addon-ssi_field_service_work_log',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
