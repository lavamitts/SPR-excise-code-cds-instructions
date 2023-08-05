# Generates HTML includes for condition dialogs for SPR

This generates:

- an HTML include per excise code
- a YAML file that associates the codes with the HTML fragments

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python -m venv venv/`

  `source venv/bin/activate`

- Install necessary Python modules via `pip install -r requirements.txt`

## Usage

### To process:
`python process.py`
