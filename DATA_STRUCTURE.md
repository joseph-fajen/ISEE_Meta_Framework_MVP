# ISEE Framework Data Structure

This document explains the data structure used by the ISEE framework and how to set it up correctly.

## Directory Structure

The ISEE framework uses the following directory structure for data storage:

```
ISEE_Meta_Framework/
├── data/
│   ├── output/    # For storing generated outputs
│   ├── state/     # For storing application states
│   └── config/    # For storing configuration files
```

## Setting Up the Data Structure

Create the data directory structure using the following command:

```bash
mkdir -p data/output data/state data/config
```

## Data Storage Overview

### Output Files (`data/output/`)

This directory stores the formatted outputs from the ISEE framework, including:

- Markdown files containing synthesized ideas
- JSON files with structured idea data
- Other output formats as configured

Example files:
- `urban_transportation.md` - Ideas for improving urban transportation
- `education_innovation.md` - Ideas for education system redesign
- `sustainable_energy.md` - Ideas for transitioning to sustainable energy

### State Files (`data/state/`)

This directory stores application state files that capture the complete state of an ISEE session, including:

- Combinations
- Results
- Evaluations
- Synthesized ideas

These files allow you to save your progress and resume work later, or to analyze the results using the Result Viewer.

Example files:
- `urban_transportation.json` - State from urban transportation session
- `education_innovation.json` - State from education innovation session
- `combined_session.json` - State from a session combining multiple domains

### Configuration Files (`data/config/`)

This directory stores configuration files for the ISEE framework, including:

- Custom instruction templates
- Domain definitions
- Evaluation criteria
- Model configurations

Example files:
- `custom_templates.json` - User-defined instruction templates
- `industry_domains.json` - Domain definitions for specific industries
- `evaluation_criteria.json` - Custom evaluation criteria

## Working with Data Files

### Loading Configuration

```bash
python main.py --config data/config/my_config.json --query "How might we..."
```

### Saving and Loading State

```bash
# Save state
python main.py --query "How might we..." --save-state "data/state/my_session.json"

# Load state
python main.py --load-state "data/state/my_session.json"
```

### Viewing Results

```bash
# View results interactively
python result_viewer.py --state "data/state/my_session.json" --interactive

# Export results to a specific file
python main.py --load-state "data/state/my_session.json" --output-file "data/output/my_results.md"
```

## Best Practices

1. **Use meaningful names** for state and output files to easily identify sessions
2. **Create separate directories** under `data/output/` for related projects
3. **Version your configurations** in `data/config/` with dates or version numbers
4. **Back up your state files** regularly to prevent data loss
5. **Use the Result Viewer** to explore and analyze your results in depth
