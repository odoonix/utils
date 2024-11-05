# Odoo Utils

Some utilities to manage odoos

Following extensions are required:

## How use odoo utils?

Create a folder named "odoo18"

    mkdir "Odoo-18"
    cd "Odoo-18"

Clone odoo-utill

    git clone git@github.com:odoonix/utils.git

Make the main file executable:

    chmod +X odoo-utils/main.py

### Development environment

To prepaire development environment:

    odoo-utils/main.py dev init --vscode --repo --python


### To update repos

For Update Run command

    odoo-utils/main.py dev update

### To launch

Activate your venv using this command if not activated: "source .venv/bin/activate"

With this, a Python environment will be created for you and all the required Odoo libraries will be installed in it

The launch file of the vscode program is created automatically and makes the necessary settings for communication between odoo and postgres

Finally, vscode will open automatically and you just need to press the "F5" key to install Odoo locally on your system.

To see ODOO environment, go to your browser and view the address: "localhost:8069"

