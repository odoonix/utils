# Odoonix Toolbox: Empowering Developers and Administrators

Introducing the Odoonix Toolbox – the ultimate solution designed to empower both developers and administrators in the dynamic world of Odoo. Whether you're a developer looking to create and customize powerful Odoo modules or an administrator tasked with maintaining robust server environments, Odoonix is here to elevate your efficiency and capabilities.

For Developers:

Harness the full potential of Odoo with a suite of developer-centric tools tailored to streamline your workflow. The Odoonix Toolbox offers:

- **Module Creation Wizards**: Simplify the process of building new Odoo modules with intuitive wizards and templates.
- **Code Optimization Tools**: Enhance your code quality with automated linting, debugging, and performance optimization features.
- **Integrated Version Control**: Seamlessly manage your code versions and collaborate with team members using built-in version control systems.
- **Comprehensive Documentation**: Access a rich library of guides, best practices, and API references to support your development journey.

For Administrators:

Keep your systems running like a well-oiled machine with a powerful set of administration tools. The Odoonix Toolbox provides:

- **Server Monitoring**: Real-time dashboards to monitor server health, resource usage, and performance metrics.
- **Automated Backups**: Ensure data integrity with automated backup schedules and restore options.
- **Security Management**: Protect your environment with advanced security features, including vulnerability scans and patch management.
- **Easy Deployment**: Simplify the deployment process with tools for managing updates, rollbacks, and configurations.

With Odoonix, experience a seamless integration of development and administrative tasks, all in one comprehensive toolbox. Elevate your Odoo game and achieve new levels of productivity and reliability.

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

