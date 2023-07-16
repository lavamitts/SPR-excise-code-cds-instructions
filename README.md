# Generates HTML includes for condition dialogs for SPR

This generates:

- an HTML include per excise code
- a YAML file that associates the codes with the HTML fragments

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`

  `source venv/bin/activate`

- Install necessary Python modules via `pip3 install -r requirements.txt`

## Usage

### To parse an existing electronic Tariff file:
`python3 process.py`
