# Python UUIDv7 Generator

A zero dependency, dead simple version 7 UUID generator.

## Usage

Just copy the `generator.py` file (or the contents) to your project.

```python
from uuid7 import uuid7
import uuid

rand_uuid: uuid.UUID = uuid7()
print(rand_uuid)
```

## Running the tests locally

### Prerequisites

- Python 3.8+
- `pip`

### Setup

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Install the package in editable mode to allow importing from tests or external scripts:

```bash
pip install -e .
```

### Running Tests

Tests are written using `pytest`. Run tests from the project root:

```bash
pytest tests/
```


## License

WTFPL

